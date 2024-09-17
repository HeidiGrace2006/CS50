function validateForm(event) {
    var username = document.forms["RegistrationForm"]["username"].value;
    var password = document.forms["RegistrationForm"]["password"].value;

    if (username == "") {
        alert("Please enter your username");
        event.preventDefault();
        return false;
    }

    if (password == "") {
        alert("Please enter your password");
        event.preventDefault();
        return false;
    }

    return true;
}

document.addEventListener("DOMContentLoaded", function() {
    document.forms["RegistrationForm"].addEventListener("submit", validateForm);
});
