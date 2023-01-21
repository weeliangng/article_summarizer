import pymongo
import config
from datetime import datetime, date, time, timedelta


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
    projection = {'article_url': 1, 'article_published_datetime': 1 , 'article_image' : 1, 'article_title' : 1, 'article_text': 1, '_id': 0}
    cur = collection.find(query, projection)
    for doc in cur:
        documents.append(doc)
    return documents

def delete_documents(collection, days_ago = 30):
    client = create_client(config.mongodb_user, config.mongodb_cluster_pass, config.mongodb_cluster)
    db = client.scraped_articles
    collection = db[collection]
    cutoff = datetime.now() - timedelta(days = days_ago)
    collection.delete_many({'article_published_datetime' : { '$lt': cutoff}})

#print(get_documents('cna_articles',date(2022,12,17),date(2022,12,19)))
#print(get_existing_documents_url('cna_articles'))

print(datetime(2022,12,19))
#delete_documents('cna_articles', 0 )