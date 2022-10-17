from ip_pets import app, bcrypt
from ip_pets.models.pet import Pet
from ip_pets.models.SQL import SQL
from flask import render_template,redirect,request,session,flash

@app.route("/")
def redirect_pets():
    return redirect("/this_ip_pet")
@app.route("/this_ip_pet")
def this_ip_pet():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = str(request.environ['REMOTE_ADDR'])
    else:
        ip = str(request.environ['HTTP_X_FORWARDED_FOR'])

    data = {
        'pet_ip':ip
    }
    print("Checking IP...")
    if not Pet.check_ip(data):
        print ("Nope, no pet at this IP! Initializing...")
        Pet.initialize_pet(data)
        print ("Initialized")
        pet = Pet.get_one(data)
    else:
        pet = Pet.get_one(data)
    timer = pet.last_fed_at
    
    return render_template('index.html',timer=timer, pet=pet,ip=ip)

