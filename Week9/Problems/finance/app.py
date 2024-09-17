from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # AS creates an alias that only lasts for the query
    # GROUP BY combines rows with the same values (for example.. if multiple transactions were made for the same symbol).
    stocks = db.execute("SELECT symbol, SUM(shares) AS total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0",
                        user_id=session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = :user_id",
                      user_id=session["user_id"])[0]["cash"]

    total = 0
    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["price"] = quote["price"]
        stock["value"] = quote["price"] * stock["total_shares"]
        total += stock["value"]

    return render_template("index.html", stocks=stocks, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        if not symbol:
            return apology("You didn't enter a symbol :(", 400)
        if not shares:
            return apology("You didn't enter any shares :(", 400)
        if not shares.isdigit() or int(shares) <= 0:
            return apology("Invalid number of shares", 400)

        quote = lookup(symbol)
        if quote is None:
            return apology("Invalid symbol", 400)
        price = quote["price"]
        purchase_cost = int(shares) * price

        cash = db.execute("SELECT cash FROM users WHERE id = :user_id",
                          user_id=session["user_id"])[0]["cash"]
        if purchase_cost > cash:
            return apology("Insufficient funds", 400)

        # Update user's cash .. user_id is from the user id of the current session
        db.execute("UPDATE users SET cash = cash - :purchase_cost WHERE id = :user_id",
                   purchase_cost=purchase_cost, user_id=session["user_id"])

        # Add purchase to history
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
                   user_id=session["user_id"], symbol=symbol, shares=shares, price=price)

        flash(f"Purchased {shares} shares of {symbol} for {usd(purchase_cost)}!")
        return redirect("/")
    else:
        return render_template("buy.html", symbol="", shares="")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT * FROM transactions WHERE user_id = :user_id ORDER BY created_at DESC", user_id=session["user_id"])
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        if not quote:
            return apology("Invalid symbol", 400)
        return render_template("quote.html", quote=quote)
    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            return apology("You must enter a username!", 400)

        password = request.form.get("password")
        if not password:
            return apology("You must enter a password!", 400)

        confirmation = request.form.get("confirmation")
        if not confirmation:
            return apology("You must confirm your password!", 400)
        if password != confirmation:
            return apology("Password and confirmation must match!", 400)

        usernames = [row['username'] for row in db.execute("SELECT username FROM users")]
        if username in usernames:
            return apology("Username already in use.", 400)

        hash = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)
        return redirect("/")
    else:
        return render_template("register.html")
    
@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    stocks = db.execute("SELECT symbol, SUM(shares) AS total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0",
                        user_id=session["user_id"])
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = int(request.form.get("shares"))
        if not shares or shares <= 0:
            return apology("Invalid number of shares")

        for stock in stocks:
            if stock["symbol"] == symbol:
                if shares > stock["total_shares"]:
                    return apology("You do not own that many shares")
            quote = lookup(symbol)
            price = quote["price"]
            sale_price = price * shares

            db.execute("UPDATE users SET cash = cash + :sale_price WHERE id = :user_id",
                       sale_price=sale_price, user_id=session["user_id"])
            db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                       session["user_id"], symbol, -shares, price)

            flash(f"Sold {shares} shares of {stock['symbol']} for {usd(sale_price)}!")
            return redirect("/")
    else:
        return render_template("sell.html", stocks=stocks)
