from ip_pets import app, bcrypt
from ip_pets.models.pet import Pet
from ip_pets.models.SQL import SQL
from flask import render_template,redirect,request,session,flash

@app.route("/this_ip_pet")
def this_ip_pet():
    data = {
        'id':1
        }
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    pet = Pet.get_one(data)
    return render_template('index.html', pet=pet,ip=ip)

