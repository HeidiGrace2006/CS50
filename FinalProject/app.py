from flask import Flask, flash, redirect, render_template, request, session, jsonify, url_for, abort
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from cs50 import SQL
import os
import json

app = Flask(__name__)

app.secret_key = os.urandom(24)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///FinalProject.db")

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def index():
    user_id = session.get("user_id")
    logged_in = user_id is not None

    with open('static/stories_data/stories.json') as f:
        stories_data = json.load(f)

    user_stories_data = {}
    if logged_in:
        user_stories = db.execute(
            "SELECT title, choices_made, current_segment FROM user_stories WHERE user_id = ?", user_id)

        for user_story in user_stories:
            title = user_story['title']
            choices_made = user_story['choices_made']
            current_segment = user_story['current_segment']

            total_choices = next(
                (story['choices'] for story in stories_data if story["title"] == title), 0)

            percent_complete = (choices_made / int(total_choices)) * 100 if choices_made > 0 and int(total_choices) > 0 else 0
            print("index, segment" + str(current_segment))
            user_stories_data[title] = {
                "title": title,
                "percent_complete": percent_complete,
                "current_segment": current_segment
            }

            print()
            print()
            print("index, total " + total_choices)
            print("index, made " + str(choices_made))
            print("index, data " + str(user_stories_data[title]))
            print("index, percent " + str(percent_complete))

    return render_template("index.html", stories_data=stories_data, user_stories_data=user_stories_data, logged_in=logged_in)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        hash = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)
        flash("Account successfully created!")
        return redirect("/login")
    return render_template("register.html")

@app.route("/check-username")
def check_username():
    username = request.args.get("username")
    result = db.execute("SELECT 1 FROM users WHERE username = ?", username)
    exists = len(result) > 0
    return jsonify({"exists": exists})

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.clear()

        username = request.form.get("username")
        password = request.form.get("password")

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return "Invalid username or password"

        session["user_id"] = rows[0]["user_id"]
        return redirect("/")
    return render_template("login.html")

@app.route("/story/<title>/<string:segment_number>", methods=["GET", "POST"])
@login_required
def story_segments(title, segment_number):
    with open('static/stories_data/stories.json') as f:
        stories_data = json.load(f)

    story_data = next((story for story in stories_data if story['title'].replace(" ", "-").lower() == title.lower()), None)
    if not story_data:
        abort(404, description="Story not found")

    segment = next((seg for seg in story_data['content'] if seg['id'] == f"{segment_number}"), None)
    if not segment:
        abort(404, description="Segment not found")

    user_id = session.get("user_id")

    db.execute('''
        INSERT INTO user_stories (user_id, title, current_segment)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id, title)
        DO UPDATE SET current_segment = excluded.current_segment
    ''', user_id, story_data['title'], segment_number)

    if request.method == "POST":
        progress = db.execute("SELECT choices_made FROM user_stories WHERE user_id = ? AND title = ?", user_id, story_data['title'])
        if int(segment_number[0]) > progress[0]['choices_made'] < int(story_data['choices']):
            db.execute('''
                UPDATE user_stories
                SET choices_made = choices_made + 1
                WHERE user_id = ? AND title = ?
            ''', user_id, story_data['title'])
            print()
            print()
            print("segment, segment " + str(segment_number[0]))
            print("segment, total " + str(story_data['choices']))
            print("segment, made " + str(progress[0]['choices_made']))
    return render_template("story_segments.html", story_data=story_data, segment=segment)

@app.route("/story/<title>/restart")
@login_required
def restart_story(title):
    with open('static/stories_data/stories.json') as f:
        stories_data = json.load(f)

    story_data = next((story for story in stories_data if story['title'].replace(" ", "-").lower() == title.lower()), None)
    if not story_data:
        abort(404, description="Story not found")

    user_id = session.get("user_id")

    db.execute('''
        UPDATE user_stories
        SET choices_made = 0, current_segment = "1.1"
        WHERE user_id = ? AND title = ?
        ''', user_id, story_data['title'])
    return redirect(url_for('story_segments', title=title, segment_number="1.1"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
