from sqlite3 import connect
from ip_pets.config.mysqlconnection import connectToMySQL
from ip_pets import DB
from ip_pets.models.SQL import SQL
from datetime import datetime
import random, re, urllib, requests, asyncio, time

class Pet(SQL):
    table = "pets"
    def __init__(self, data):
        self.feed_timer = data['feed_timer']
        self.created_at = data['created_at']
        self.last_fed_at = data['last_fed_at']
        self.name = data['name']
        self.pet_ip = data['pet_ip']
        self.pet_image = data['pet_image']

    def process_update(self):
        hunger = datetime.now() - self.last_fed_at
        if (hunger.seconds/3600) > self.feed_timer:
            data = {
                'pet_ip':self.pet_ip
            }
            self.delete(data)
            return True
    def feed_pet(self):
        data = {
            'pet_ip':self.pet_ip
            }
        query = """UPDATE pets
        SET last_fed_at = NOW()
        WHERE pet_ip = %(pet_ip)s
        """
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def initialize_pet(cls, data):
        data['name'] = Pet.random_name()
        print("Name selected")
        data['feed_timer'] = random.randint(18, 240)
        print("Timer Set")
        response = requests.get("https://zoo-animal-api.herokuapp.com/animals/rand")
        status = True
        while status:
            if (response.status_code != 200):
        
                response = requests.get("https://zoo-animal-api.herokuapp.com/animals/rand")
                
                time.sleep(1)
            else:
                status = False
        
        response_info = response.json()
        data['pet_image'] = response_info['image_link']
        query = "INSERT INTO pets (name, pet_ip, feed_timer, pet_image, last_fed_at) VALUES ( %(name)s, %(pet_ip)s, %(feed_timer)s, %(pet_image)s, NOW())"
        
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def check_ip(cls, data):
        query = "SELECT * FROM pets WHERE pet_ip = %(pet_ip)s"
        result = connectToMySQL(DB).query_db(query, data)
        if result:
            return True
        

    @staticmethod
    def random_name():
        names = ["Abigail","Ace","Adam","Mew Mew","Mojo","Spooky","Misu","Mister","Doomkitty Lightsaber","Hachi","Artemis","Addie","Admiral","Aggie","Aires","Aj","Ajax","Aldo","Alex","Alexus","Alf","Alfie","Allie","Ally","Amber","Amie","Amigo","Amos","Amy","Andy","Angel","Angus","Annie","Apollo","April","Archie","Argus","Aries","Armanti","Arnie","Arrow","Ashes","Ashley","Astro","Athena","Atlas","Audi","Augie","Aussie","Austin","Autumn","Axel","Axle","Babbles","Babe","Baby","Baby-doll","Babykins","Bacchus","Bailey","Bam-bam","Bambi","Bandit","Banjo","Barbie","Barclay","Barker","Barkley","Barley","Barnaby","Barney","Baron","Bart","Basil","Baxter","Bb","Beamer","Beanie","Beans","Bear","Beau","Beauty","Beaux","Bebe","Beetle","Bella","Belle","Ben","Benji","Benny","Benson","Bentley","Bernie","Bessie","Biablo","Bibbles","Big Boy","Big Foot","Biggie","Billie","Billy","Bingo","Binky","Birdie","Birdy","Biscuit","Bishop","Gus","Guy","Gypsy","Hailey","Haley","Hallie","Hamlet","Hammer","Hank","Hanna","Hannah","Hans","Happy","Hardy","Harley","Harpo","Harrison","Harry","Harvey","Heather","Heidi","Henry","Hercules","Hershey","Higgins","Hobbes","Holly","Homer","Honey","Honey-Bear","Hooch","Hoover","Hope","Houdini","Howie","Hudson","Huey","Hugh","Hugo","Humphrey","Hunter","India","Indy","Iris","Isabella","Isabelle","Itsy","Itsy-bitsy","Ivory","Ivy","Izzy","Jack","Jackie","Jackpot","Jackson","Jade","Jagger","Jags","Jaguar","Jake","Jamie","Jasmine","Jasper","Jaxson","Jazmie","Jazz","Jelly","Jelly-bean","Jenna","Jenny","Jerry","Jersey","Jess","Jesse","Jesse James","Jessie","Jester","Jet","Jethro","Jett","Jetta","Jewel","Jewels","Jimmy","Jingles","JJ","Joe","Joey","Johnny","Jojo","Joker","Jolie","Jolly","Jordan","Josie","Joy","JR","Judy","Julius","June","Misty","Mitch","Mittens","Mitzi","Mitzy","Mo","Mocha","Mollie","Molly","Mona","Muffy","Nakita","Nala","Nana","Natasha","Nellie","Nemo","Nena","Peanut","Peanuts","Pearl","Pebbles","Penny","Phoebe","Phoenix","Sara","Sarah","Sasha","Sassie","Sassy","Savannah","Scarlett","Shasta","Sheba","Sheena","Shelby","Shelly","Sienna","Sierra","Silky","Silver","Simone","Sissy","Skeeter","Sky","Skye","Skyler","Waldo","Wallace","Wally","Walter","Wayne","Weaver","Webster","Wesley","Westie",]
        name = random.choice(names)
        return name

    # @staticmethod
    # async def get_image():

