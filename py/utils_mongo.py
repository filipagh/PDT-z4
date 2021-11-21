def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://172.26.0.2:27017"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['PDT']

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    pass

def insert_one(coll_name, doc):
    conn = get_database()[coll_name]
    return conn.insert_one(doc)
