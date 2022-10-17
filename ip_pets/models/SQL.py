
from ip_pets.config.mysqlconnection import connectToMySQL
from ip_pets import DB


class SQL:
    @classmethod
    def get_one(cls,data):
        query = f'SELECT * FROM {cls.table} WHERE '#Table Name passed in
        query += 'AND '.join(f'{key} = %({key})s ' for key in data)#Join every key as a condition
        query += 'LIMIT 1;' #Only ever get 1 result
        results = connectToMySQL(DB).query_db(query, data)
        if results:
            return cls(results[0])
    @classmethod
    def create(cls, data):
        query = f"INSERT INTO {cls.table} ("  #Table name passed in
        query += ", ".join(key for key in data) #This is the join code, joining all columns together
        query += ") VALUES (" #Separator, closing and opening next section
        query += ", ".join(f'%{key})s' for key in data) #Joins keys here again, f string for mogrify!?!
        query += ");" #This finishes the query.
        return connectToMySQL(DB).query_db(query, data)
        
    def update(cls, data):
        query = f'UPDATE {cls.table} SET ' #Table name passed in
        query += ', '.join(f'{key} = %({key})s' for key in data if not key == 'id') #This one loops through the keys, but excludes 'id' since it shouldn't change.
        query += ' WHERE id = %(id)s;' #Conditional to only update at 'id' position
        return connectToMySQL(DB).query_db(query, data)

    def delete (cls, data):
        query = f'DELETE FROM {cls.table}'
        query += ' WHERE '
        query += ' AND '.join(f'{key} = %({key})s' for key in data)
        query += ';'
        return connectToMySQL(DB).query_db(query, data)