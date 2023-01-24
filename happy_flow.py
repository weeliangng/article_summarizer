from create_instagram_post import create_instagram_image, create_instagram_caption
from upload_freeimage import upload_freeimage
from insta import post_article_summary
from datetime import datetime, time
import scraped_database
import transformerModel
import scraper


date = datetime(2023, 1, 23)
start_time = time.min
end_time = time.max

article_startdatetime = datetime.combine(date, start_time)
article_enddatetime = datetime.combine(date, end_time)

documents = scraped_database.get_longest_document('cna_articles', article_startdatetime, article_enddatetime)

document = documents[0]
print(document)

img_url = document['article_image']
caption = create_instagram_caption(document)
print(caption)
summarized_text = transformerModel.sliding_window_summarization(document['article_text'])
print(summarized_text)
image_path = create_instagram_image(img_url, 'images', summarized_text)

image_url = upload_freeimage(image_path)

print(image_url)
post_article_summary(image_url, caption, document['_id'])