import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta

import scraped_database

def scrape_article(article_url):
    print("Scraping {}".format(article_url))
    soup = get_article_soup(article_url)
    article_title = get_article_title(soup)
    article_text = get_article_text(soup)
    article_published_datetime = get_article_published_date(soup)
    article_img = get_article_img(soup)
    return article_title, article_published_datetime, article_text, article_img

def get_article_soup(article_url):
    headers = {
                    'User-Agent': 'My User Agent 1.0',
                    'From': 'youremail@domain.example'  # This is another valid field
                    }
    r = requests.get(article_url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def get_article_img(soup):
    article_figure = soup.find('figure', class_ = re.compile('figure block detail-hero-media block-mc-hero-emphasis block-hero-emphasis clearfix'))
    if article_figure is None:
        article_figure = soup.find('div', class_ = re.compile('photo-gallery block detail-hero-media block-mc-hero-emphasis block-hero-emphasis clearfix'))
    try:
        article_img = article_figure.find('img', class_ = 'image')['src']
    except AttributeError:
        article_img = 'no_image'
    finally:
        return article_img

def get_article_published_date(soup):
    #print((soup.find('div', class_=re.compile('article-publish'))))
    article_published_date_textblock = (soup.find('div', class_=re.compile('article-publish'))).text
    article_published_date_string = article_published_date_textblock.split("\n")[1].strip()
    article_published_datetime = datetime.strptime(article_published_date_string, "%d %b %Y %I:%M%p")
    return article_published_datetime

def get_article_text(soup):
    article_text_p = soup.select('div.text-long p')
    article_text = ' '.join([p.text for p in article_text_p])
    return article_text

def get_article_title(soup):
    article_title = soup.find('h1', class_ = re.compile('h1 h1--page-title')).text
    return article_title.strip()

def get_article_links(site):
    r = requests.get(site)
    soup = BeautifulSoup(r.content, 'html.parser')
    articles_a = soup.find_all('a', class_=re.compile('heading'))
    #exclude watch and interactives articles
    filtered_articles_a = list()
    exclude_categories = ['interactives', 'watch', 'listen', 'brandstudio', 'high-time','brand-studio']
    for article_a in articles_a:
        href = article_a['href']
        category = href.split('/')[1]
        if category not in exclude_categories: 
            filtered_articles_a.append(article_a) 
    return list(filtered_articles_a)

def start_scraping(site, collection,  timedelta_hours = 24):
    scraped_doc_list = []
    articles_a = get_article_links(site)
    article_enddatetime = datetime.now()
    article_startdatetime = article_enddatetime - timedelta(hours=timedelta_hours)
    for article_a in articles_a:
        article_url = "{}{}".format(site, article_a["href"])
        article_title, article_published_datetime, article_text, article_img = scrape_article(article_url)
        if article_published_datetime > article_startdatetime:
            scraped_doc = {
                'article_url': article_url,
                'article_title': article_title,
                'article_published_datetime': article_published_datetime,
                'article_text': article_text,
                'article_image': article_img,
                'posted_on_insta': 'no'
            }
            scraped_doc_list.append(scraped_doc)
    #print(len(scraped_doc_list))
    existing_articles = scraped_database.get_documents(collection, article_startdatetime, article_enddatetime)
    #print(len(existing_articles))
    existing_articles_url = [doc['article_url'] for doc in existing_articles]
    scraped_doc_list = remove_existing_documents(scraped_doc_list, existing_articles_url)
    return scraped_doc_list

def remove_existing_documents(doc_list, existing_articles):
    new_doc_list = []
    for doc in doc_list:
        if doc['article_url'] not in existing_articles:
            new_doc_list.append(doc)
    return new_doc_list

def remove_duplicate_documents(doc_list):
    unique_urls = set()
    new_doc_list = list()
    for doc in doc_list:
        if doc['article_url'] not in unique_urls:
            new_doc_list.append(doc)
            unique_urls.add(doc['article_url'])
    return new_doc_list

scraped_database.delete_documents('cna_articles', days_ago = 7)
site = 'https://www.channelnewsasia.com'
scraped_doc_list = start_scraping(site, 'cna_articles', 24)
#print(len(scraped_doc_list))
scraped_doc_list = remove_duplicate_documents(scraped_doc_list)
#print(len(scraped_doc_list))
scraped_database.insert_many_db(scraped_doc_list, 'cna_articles')


