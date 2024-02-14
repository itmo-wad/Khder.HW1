from flask import Flask, render_template, url_for, redirect
import datetime


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('get_profile'), 301)


@app.route('/profile')
def get_profile():
    account = {"email" : "khder96ju@gmail.com", "address": "ST Petersburg, Lensoveta 23"
    , "hobbies": "football, basketball, reading books",
     "job" : "technical support", "skill" : "HTML, CSS and Java Script"}
    Github = "https://github.com/KhderAbdo"
    Lab1deadline = datetime.datetime.strptime('2024/02/16 18:40', "%Y/%m/%d %H:%M")
    Lab1time_before_deadline = Lab1deadline - datetime.datetime.now().replace(microsecond=0)
    data = {"name" : "Khder", "Github" : Github
        , "Lab1deadline" : Lab1deadline, "Lab1time_before_deadline" : Lab1time_before_deadline,
            "owner" : "Khder Abdo", "version" : "1.0.0.1","account":account
            }
    return render_template("index.html", data=data)
