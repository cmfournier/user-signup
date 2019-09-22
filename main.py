from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

#def valid_user():
    
@app.route("/")
def index():
    return render_template('base.html')



username_error = ''
password_error = ''
match_error = ''


@app.route("/welcome")
def validated():
    username = request.args.get('username')
    return render_template("welcome.html", name=username)

app.run()
