import pymongo
import config
from datetime import datetime, date, time, timedelta
from bson import Code


def create_client(mongodb_user, mongodb_cluster_pass, mongodb_cluster):
    conn_str = "mongodb+srv://{}:{}@{}.obvuaet.mongodb.net/?retryWrites=true&w=majority".format(mongodb_user, mongodb_cluster_pass, mongodb_cluster)
    client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
    return client

def insert_many_db(scraped_data ,collection):
    if len(scraped_data) != 0:
        client = create_client(config.mongodb_user, config.mongodb_cluster_pass, config.mongodb_cluster)
        db = client.scraped_articles
        db[collection].insert_many(scraped_data)
    
#retrieve records from mongodb
#get article text
#article image
def get_documents(collection, article_startdatetime, article_enddatetime):
    documents = []
    client = create_client(config.mongodb_user, config.mongodb_cluster_pass, config.mongodb_cluster)
    db = client.scraped_articles
    collection = db[collection]
    query = {'article_published_datetime' : {'$gt': article_startdatetime, '$lt': article_enddatetime} }
    projection = {'article_url': 1, 'article_published_datetime': 1 , 'article_image' : 1, 'article_title' : 1, 'article_text': 1, '_id': 1, 'posted_on_insta': 1}
    cur = collection.find(query, projection)
    for doc in cur:
        documents.append(doc)
    return documents

def get_longest_document(collection, article_startdatetime, article_enddatetime):
    documents = []
    client = create_client(config.mongodb_user, config.mongodb_cluster_pass, config.mongodb_cluster)
    db = client.scraped_articles
    collection = db[collection]
    query = {'article_published_datetime' : {'$gt': article_startdatetime, '$lt': article_enddatetime} ,  'posted_on_insta': {'$eq': 'no'} }
    projection = {'article_url': 1, 'article_published_datetime': 1 , 'article_image' : 1, 'article_title' : 1, 'article_text': 1, '_id': 1, 'posted_on_insta': 1}
    cur = collection.aggregate([
    {"$match": query},
    {"$project": {'article_url': 1, 'article_published_datetime': 1 , 'article_image' : 1, 'article_title' : 1, 'article_text': 1, '_id': 1, 'posted_on_insta': 1, "tokens": {"$size": { "$split": ["$article_text", " "] }}}},
    {"$match": {'tokens':{'$lt': 3500}}},
    {"$sort": {"tokens": -1}},
    {"$limit": 1}
    ])
    for doc in cur:
        documents.append(doc)
    return documents

def delete_documents(collection, days_ago = 30):
    client = create_client(config.mongodb_user, config.mongodb_cluster_pass, config.mongodb_cluster)
    db = client.scraped_articles
    collection = db[collection]
    cutoff = datetime.now() - timedelta(days = days_ago)
    collection.delete_many({'article_published_datetime' : { '$lt': cutoff}})

def update_posted_on_insta(collection, object_id):
    client = create_client(config.mongodb_user, config.mongodb_cluster_pass, config.mongodb_cluster)
    db = client.scraped_articles
    collection = db[collection]
    query = {"_id": object_id}
    new_values = {"$set": {"posted_on_insta": "yes"}}
    # Update the document
    result = collection.update_one(query, new_values)

#print(get_documents('cna_articles',date(2022,12,17),date(2022,12,19)))
#print(get_existing_documents_url('cna_articles'))

#print(datetime(2022,12,23))
#delete_documents('cna_articles', 0 )
#print(get_longest_document('cna_articles',datetime.combine(datetime(2023,1,23),time.min),datetime.combine(datetime(2023,1,23), time.max)))