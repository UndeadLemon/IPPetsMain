from ip_pets import app, bcrypt
from ip_pets.models.pet import Pet
from ip_pets.models.SQL import SQL
from flask import render_template,redirect,request,session,flash

@app.route("/this_ip_pet")
def this_ip_pet():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']

    data= {
        'pet_ip':ip
    }
    pet = Pet.get_one(data)
    if not pet:
        Pet.initialize_pet(data)
    timer = pet.last_fed_at
    
    return render_template('index.html',timer=timer, pet=pet,ip=ip)

