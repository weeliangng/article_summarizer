import requests
from bs4 import BeautifulSoup
import re
from newspaper import Article
from datetime import datetime

import scraped_database

def scrape_article(article_url):
    #print(article_url)
    article = Article(article_url)
    article.download()
    article.parse()
    article_title = article.title
    article_text = article.text
    article_published_datetime = get_article_published_date(article_url)
    article_img = get_article_img(article_url)
    return article_title, article_published_datetime, article_text, article_img

def get_article_img(article_url):
    r = requests.get(article_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    article_figure = soup.find('figure', class_ = re.compile('figure block detail-hero-media block-mc-hero-emphasis block-hero-emphasis clearfix'))
    if article_figure is None:
        article_figure = soup.find('div', class_ = re.compile('photo-gallery block detail-hero-media block-mc-hero-emphasis block-hero-emphasis clearfix'))
    article_img = article_figure.find('img', class_ = 'image')['src']
    return article_img

def get_article_published_date(article_url):
    r = requests.get(article_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    #print((soup.find('div', class_=re.compile('article-publish'))))
    article_published_date_textblock = (soup.find('div', class_=re.compile('article-publish'))).text
    article_published_date_string = article_published_date_textblock.split("\n")[1].strip()
    article_published_datetime = datetime.strptime(article_published_date_string, "%d %b %Y %I:%M%p")
    return article_published_datetime

def get_article_links(site):
    r = requests.get(site)
    soup = BeautifulSoup(r.content, 'html.parser')
    articles_a = soup.find_all('a', class_=re.compile('heading'))
    filtered_articles_a = [article_a for article_a in articles_a if ('interactives' not in str(article_a) and 'watch' not in str(article_a)) ]
    return list(filtered_articles_a)

def start_scraping(site):
    scraped_doc_list = []
    articles_a = get_article_links(site)
    for article_a in articles_a:
        article_url = "{}{}".format(site, article_a["href"])
        article_title, article_published_datetime, article_text, article_img = scrape_article(article_url)
        scraped_doc = {
            'article_url': article_url,
            'article_title': article_title,
            'article_published_datetime': article_published_datetime,
            'article_text': article_text,
            'article_image': article_img
        }
        scraped_doc_list.append(scraped_doc)
    return scraped_doc_list

site = 'https://www.channelnewsasia.com'
scraped_doc_list = start_scraping(site)
scraped_database.insert_many_db(scraped_doc_list, 'cna_articles')



