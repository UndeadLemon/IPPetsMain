from math import floor
from ip_pets import app, bcrypt
from ip_pets.models.pet import Pet
from ip_pets.models.SQL import SQL
from datetime import datetime
from flask import render_template,redirect,request,session,flash


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
    
    if pet.process_update() == True:
        return redirect('/')
    print(pet.last_fed_at)
    time_difference = datetime.now() - pet.last_fed_at
    timer = floor(time_difference.seconds/3600)
    
    # d = datetime.strptime(pet.last_fed_at, '%Y-%m-%d %H:%M:%S')
    
    
    return render_template('pet_page.html',timer=timer, pet=pet,ip=ip)

@app.route('/feed_pet')
def feed_pet():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = str(request.environ['REMOTE_ADDR'])
    else:
        ip = str(request.environ['HTTP_X_FORWARDED_FOR'])

    data = {
        'pet_ip':ip
    }
    pet = Pet.get_one(data)
    pet.feed_pet()
    return redirect('/this_ip_pet')

@app.route('/pet_stats')
def pet_stats():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = str(request.environ['REMOTE_ADDR'])
    else:
        ip = str(request.environ['HTTP_X_FORWARDED_FOR'])

    data = {
        'pet_ip':ip
    }
    pet = Pet.get_one(data)
    
    last_fed = pet.last_fed_at.strftime('%m/%d/%Y at %I:%S')
    born = pet.created_at.strftime('%m/%d/%Y at %I:%S')
    time_difference = datetime.now() - pet.created_at
    age = floor((time_difference.seconds/86400))
    print(age)
    return render_template('pet_stats.html', pet=pet, last_fed=last_fed, age=age, born=born)
