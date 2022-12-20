import pymongo
import config

def insert_many_db(scraped_data ,collection):

    conn_str = "mongodb+srv://{}:{}@{}.obvuaet.mongodb.net/?retryWrites=true&w=majority".format(config.mongodb_user, config.mongodb_cluster_pass, config.mongodb_cluster)
    client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
    db = client.scraped_articles
    db[collection].insert_many(scraped_data)
    