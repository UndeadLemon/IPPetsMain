from ip_pets.config.mysqlconnection import connectToMySQL
from ip_pets.models.SQL import SQL
from ip_pets import bcrypt, DB
from flask import flash
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

    @staticmethod
    def validate_user( user ):
        is_valid=True

        if len(user['username']) < 4:
            flash("Username is too short!")
            is_valid=False
        data = { 
            'username':user['username']
            }
        if User.get_one(data):
            flash('Username taken!')
            is_valid=False
        if not PASSWORD_REGEX.match(user['password']):
            flash('Invalid Password! Password must be at least 8 characters, and contain at least 1 special character, number, and capital letter!')
            is_valid=False
        return is_valid

