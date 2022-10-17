from flask import Flask
from flask_bcrypt import Bcrypt
DB = 'ip_pets'
app = Flask(__name__)
bcrypt=Bcrypt(app)
app.secret_key = "Take 4d4 bludgeoning damage, 2d4 psychic damage."