from ip_pets.config.mysqlconnection import connectToMySQL
from ip_pets import DB
from ip_pets.models.SQL import SQL
import re

class Pet(SQL):
    table = "pets"
    def __init__(self, data):
        self.feed_timer = data['feed_timer']
        self.created_at = data['created_at']
        self.last_fed_at = data['last_fed_at']
        self.name = data['name']
        self.pet_ip = data['pet_ip']