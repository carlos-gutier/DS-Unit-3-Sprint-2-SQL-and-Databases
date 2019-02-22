# -*- coding: utf-8 -*-
"""LS_DS1_MongoDB_Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12b9W3SxUZyI1M3RzyQRlUYCkZ05yktt8

# Assignment - Mongo DB

Loading the database using Mongo was easier than with Postgress. Pymongo's method `test.insert_many()` makes it simple to instert an entire database into MongoDB. Nevertheless, when it comes to quering data I would rather use SQL. It's more intuitive and straight forward compared to JSON.
"""

! curl ipecho.net/plain



!pip install pymongo

connection_string = 'mongodb://mongorandom_ds1:wrSZ4J6DwhaTMuET@cgds1-shard-00-00-yqzzd.mongodb.net:27017,cgds1-shard-00-01-yqzzd.mongodb.net:27017,cgds1-shard-00-02-yqzzd.mongodb.net:27017/test?ssl=true&replicaSet=CGDS1-shard-0&authSource=admin&retryWrites=true'

import pymongo
client = pymongo.MongoClient(connection_string)

dir(client)

# actual servers that are running where our data lives (or will live)
client.nodes

# server info
client.server_info()

# line to connect to the database
db = client.test

# to actually get the data
dir(db)

# method to insert data (client.test.test.insert)
db.test.insert

# way to store key, value pair / dictionary ({'x': 1})
help(db.test.insert_one)

help(db.test.insert_many)

# not found so it does not return anything
v_doc = {'favorite animal':'dolphin'}
db.test.find_one(v_doc)

v_doc = {'favorite animal':'dolphin'}
if not db.test.find_one(v_doc):
    print('Inserting...')
    db.test.insert_one(v_doc)

db.test.find_one(v_doc)

results = db.test.find()

results

list(results)

list(results)

"""# Assignment

## RPG data

Importing `urllib.request` and `json` libraries to open the RPG .json file from the given URL and to then load the data to then iterate.
"""

import urllib.request, json 
with urllib.request.urlopen("https://raw.githubusercontent.com/LambdaSchool/Django-RPG/master/testdata.json") as url:
    data = json.loads(url.read().decode())
    print(data)

len(data[0])

"""Incorrectly loading the `data` with the wrong instance (`db` was previously used for in-class code above)"""

db.test.insert_many(data)

db.test.find_one(data)

list(db.test.find({}))

"""Inserting RPG data into MongoDB using `insert_many()` method"""

db2 = client.test2

db2.test.insert_many(data)

"""Looking through the entire inserted data by creating a list after using `db2.test.find({})`"""

list(db2.test.find({}))

"""Learning how to look into .json with Python"""

character8 = list(db2.test.find({'model': 'charactercreator.character','pk': 9}))
character8

character8[0]['fields']

character8[0]['fields']['name']