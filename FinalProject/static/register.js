async function checkUsername() {
    const username = document.getElementById('username').value;
    const usernameError = document.getElementById('username-error');

    if (username) {
        try {
            const response = await fetch(`/check-username?username=${username}`);
            const data = await response.json();

            if (data.exists) {
                usernameError.textContent = 'Username is already in use';
                return false;
            } else {
                usernameError.textContent = '';
                return true;
            }
        } catch (error) {
            console.error('Error checking username:', error);
            return false;
        }
    }
    return true;
}

async function validateForm(event) {
    event.preventDefault();

    var username = document.forms["RegistrationForm"]["username"].value;
    var password = document.forms["RegistrationForm"]["password"].value;
    var confirmation = document.forms["RegistrationForm"]["confirmation"].value;

    if (username == "") {
        alert("Please enter a username");
        return false;
    }

    const isUsernameValid = await checkUsername();
    if (!isUsernameValid) {
        alert("Username is already in use");
        return false;
    }

    if (password == "") {
        alert("Please enter a password");
        return false;
    }

    if (confirmation == "") {
        alert("Please re-type the password");
        return false;
    }

    if (password != confirmation) {
        alert("Passwords must match");
        return false;
    }

    document.forms["RegistrationForm"].submit();
    return true;
}

document.addEventListener("DOMContentLoaded", function() {
    document.forms["RegistrationForm"].addEventListener("submit", validateForm);
    document.getElementById('username').addEventListener("blur", checkUsername);
});
