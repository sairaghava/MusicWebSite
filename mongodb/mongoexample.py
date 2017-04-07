def get_db():
    from pymango import MongoClient
    client = MongoClient('localhost:27017')
    db = client.myFirstMB
    print(db)
    return db


def add_currency(db):
    db.currency.insert({"name" : "Dollars"})

def get_currency(db):
    return db.currency.find_one()

if(__name__ == "_main_"):
    db = get_db()
    add_currency(db)
    print(get_currency(db))