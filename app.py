import os
import json
import pymongo
from flask import Flask
import certifi

app = Flask(__name__)

ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://read_only:hsUEg6HWFEfWALSV@cluster0.3aeaw8v.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client['db_examenf']
collection = db['Camisetas Manchester City camisetas']

@app.route('/')
def get():
    nombre = collection.find()
    response = []
    for document in nombre:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)
if __name__ == '__main__':
    app.run()
