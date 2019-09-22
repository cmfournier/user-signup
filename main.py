from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True
    
@app.route("/")
def index():
    return render_template('signup_form.html', title="Signup Form")


@app.route("/signup", methods=['POST'])
def signup():

    username = request.form['username']
    password = request.form['password']
    pw_match = request.form['pw_match']
    email = request.form['email']

    username_error = ''
    password_error = ''
    pw_match_error = ''
    email_error = ''

    at_count = email.count('@')
    dot_count = email.count('.')
    

#verify required fields aren't empty
    if len(username) == 0:
        username_error = "That's not a valid username"

    if len(password) == 0:
        password_error = "That's not a valid password"
        password = ''

    if len(pw_match) == 0:
        pw_match_error = "Passwords don't match"
        password = ''
        pw_match = ''

#verify passwords match each other
    if password != pw_match:
        pw_match_error = "Passwords don't match"
        password = ''
        pw_match = ''

#verify username is valid
    if len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters"
        username = ''
        password = ''
        pw_match = ''

    if ' ' in username:
        username_error = "No spaces allowed in username"
        password = ''
        pw_match = ''

#verify password is valid
    if len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters"
        password = ''
        pw_match = ''

    if ' ' in password:
        password_error = "No spaces allowed in password"
        password = ''
        pw_match = ''

#verify email if one was entered
    if len(email) > 0:

        if ' ' in email:
            email_error = "No spaces in email"   
            password = ''
            pw_match = ''
        
        if len(email) < 3 or len(email) > 20:
            email_error = "Email must be between 3 and 20 characters"
            password = ''
            pw_match = ''

        for i in email:
            if at_count > 1:            
                email_error = "Not a valid email address"
                password = ''
                pw_match = ''

        for i in email:
            if dot_count > 1:
                email_error = "Not a valid email address"
                password = ''
                pw_match = ''

#redirect user to Welcome page if required conditions are satisfied
    if not username_error and not password_error and not pw_match_error and not email_error:
        username = request.form['username']
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup_form.html', title="Signup Form",
            username=username, username_error=username_error,
            password=password, password_error=password_error,
            pw_match=pw_match, pw_match_error=pw_match_error, 
            email=email, email_error=email_error)

@app.route("/welcome")
def validated():
    username = request.args.get('username')
    return render_template("welcome.html", title="Welcome", name=username)

app.run()
