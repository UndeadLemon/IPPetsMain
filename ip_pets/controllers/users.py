from math import floor
from ip_pets import app, bcrypt
from ip_pets.models.user import User
from ip_pets.models.SQL import SQL
from datetime import datetime
from flask import render_template,redirect,request,session,flash


@app.route("/")
def redirect_pets():
    return render_template("landing_page.html")
@app.route("/project_info")
def project_info():
    
    return render_template("info_page.html")

@app.route("/support_dev")
def support_dev():

    return render_template("support.html")

@app.route("/suggestions")
def suggestions():

    return render_template("suggestions.html")

@app.route("/changelog")
def changelog():

    return render_template("changelog.html")
@app.route("/login")
def login():

    return render_template("login.html")

