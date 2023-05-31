import pymongo


def get_db(database):
    conn = pymongo.MongoClient(
        host='127.0.0.1',
        port=27017
    )
    db = conn[database]
    return db


def add_one(table, data):
    db = get_db('sanqi')
    db[table].insert_one(data)


def update(table, ex, data):
    db = get_db('sanqi')
    db['stu'].update_many(ex, {'$set': data})


def delete(table, ex):
    db = get_db('sanqi')
    db[table].delete_many(ex)


