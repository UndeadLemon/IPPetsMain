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
@app.route("/login_processing", methods = ["POST"])
def login_processing():
    data = {
        'username':request.form['username']
    }
    userdata = User.get_one(data)
    
    if not userdata:
        flash("Invalid Email/Password")
        return redirect('/login')
    if not bcrypt.check_password_hash(userdata.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/login')

    session['user_id'] = userdata.id
    
    return redirect("/user_page")

@app.route("/registration_processing", methods = ["POST"])
def registration_processing():
    is_valid = User.validate_user(request.form)
    if request.form['password'] != request.form['confirm_password']:
        flash("Passwords do not match!")
        is_valid = False
    if is_valid == False:
        return redirect('/login')
    data ={}

    data['username'] = request.form['username']

    data['password'] = bcrypt.generate_password_hash(request.form['password'])
    print(data)
    print(User.create(data))
    
    return redirect('/user_page')

@app.route("/user_page")
def user_page():

    return render_template("user_page.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
