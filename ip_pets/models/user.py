from ip_pets.config.mysqlconnection import connectToMySQL
import SQL
from ip_pets import bcrypt, DB
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

class User(SQL):
    table = 'users'
    def __init__(self, data):
        self.email=data['email']
        self.username=data['username']
        self.id=data['id']
        self.password=data['password']


