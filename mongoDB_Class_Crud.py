from pymongo import MongoClient

connection = MongoClient('mongodb://localhost:27017')

class m_conecction:
    def __init__(self, connection):
        self.connection = connection
        self.database = self.connection['my_database']

    def collection_db(self, name):
        collection = self.database[name]
        return collection

    def create_db(self, jsonData):
        collection = self.collection_db(jsonData['name'])
        jsonData.pop('name')
        print(jsonData)
        collection.insert_one(jsonData)
        return True

    def get_user(self, jsonData):
        collection = self.collection_db(jsonData['name'])
        jsonData.pop('name')
        result = collection.find_one(jsonData)
        print(result)
        return result

    def get_all(self, jsonData):
        result_data = []
        collection = self.collection_db(jsonData['name'])
        result = collection.find()
        for result in result:
            result_data.append(result)
        print(result_data)
        return result_data

    def update_user(self, jsonData):
        collection = self.collection_db(jsonData['name'])
        jsonData.pop('name')
        self.collection.update_one(jsonData)
        return True

    def delete(self, jsonData):
        collection = self.collection_db(jsonData['name'])
        jsonData.pop('name')
        result = collection.delete_one(jsonData)
        return True

    def delete_all(self, jsonData):
        collection = self.collection_db(jsonData['name'])
        result = collection.delete_many({})
        return True

    def get(self, jsonData):
        collection = self.collection_db(jsonData['name'])
        jsonData.pop('name')
        result = collection.find_one(jsonData)
        for key, value in result.items():
            print(key)
        print(result)
        print(type(result))
        return result

        
db = m_conecction(connection)
jsonData = {'name':'db_test3','_id':3, 'edad': 5, 'nombre': 'kabsduhqbhidbQJDUQWD', 'email': 'QEFLNqeojfnQEOFNUqew@slns.com'}
#db.create_db(jsonData)
# get_jsonData = {'name':'db_test3', '_id': 3}
# db.get_user(get_jsonData)

# get_jsonData = {'name':'db_test3', '_id': 2}
# db.delete(get_jsonData)

# get_jsonData = {'name':'user'}
# db.delete_all(get_jsonData)

# get_jsonData = {'name':'db_test3'}
# db.get_all(get_jsonData)

# get_jsonData = {'name':'db_test3','_id':3, 'edad': 5}
# db.update_user(get_jsonData)

get_jsonData = {'name':'db_test3', '_id': 3}
db.get(get_jsonData)
