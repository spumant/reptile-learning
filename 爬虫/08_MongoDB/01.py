import pymongo

conn = pymongo.MongoClient(
    host='127.0.0.1',
    port=27017
)

db = conn['sanqi']
table = db['c1']
result = table.find()
for r in result:
    print(r)
