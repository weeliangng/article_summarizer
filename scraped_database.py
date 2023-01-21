import pymongo
import config
from datetime import datetime, date, time


def create_client(mongodb_user, mongodb_cluster_pass, mongodb_cluster):
    conn_str = "mongodb+srv://{}:{}@{}.obvuaet.mongodb.net/?retryWrites=true&w=majority".format(mongodb_user, mongodb_cluster_pass, mongodb_cluster)
    client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
    return client

def insert_many_db(scraped_data ,collection):
    client = create_client(config.mongodb_user, config.mongodb_cluster_pass, config.mongodb_cluster)
    db = client.scraped_articles
    db[collection].insert_many(scraped_data)
    
#retrieve records from mongodb
#get article text
#article image
def get_documents(collection, article_startdate, article_enddate):
    documents = []
    client = create_client(config.mongodb_user, config.mongodb_cluster_pass, config.mongodb_cluster)
    db = client.scraped_articles
    collection = db[collection]
    start_date = datetime.combine(article_startdate, time.min)
    end_date = datetime.combine(article_enddate, time.max)
    query = {'article_published_datetime' : {'$gt': start_date, '$lt': end_date} }
    projection = {'article_url': 1, 'article_published_datetime': 1 , 'article_image' : 1, 'article_title' : 1, 'article_text': 1, '_id': 0}
    cur = collection.find(query, projection)
    for doc in cur:
        documents.append(doc)
    return documents



print(get_documents('cna_articles',date(2022,12,17),date(2022,12,19)))

print(datetime(2022,12,19))