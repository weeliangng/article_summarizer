import config
import requests
import json
import scraped_database

def post_article_summary(image_location, caption, object_id):
    post_url_create = 'https://graph.facebook.com/v15.0/{}/media'.format(config.instagram_id)
    create_payload = {
            'image_url' : image_location,
            'caption' : caption,
            'access_token' : config.instagram_access_token

    }
    r = requests.post(post_url_create, data=create_payload)
    print(r.text)
    result = json.loads(r.text)
    if 'id' in result:
        creation_id = result['id']
        #publish 
        post_url_publish = 'https://graph.facebook.com/v15.0/{}/media_publish'.format(config.instagram_id)
        publish_payload = {
                'creation_id' : creation_id,
                'access_token' : config.instagram_access_token

        }

        r = requests.post(post_url_publish, data=publish_payload)
        print('--------Just posted to instagram--------')
        print(r.text)
        scraped_database.update_posted_on_insta('cna_articles', object_id)

    else:
        print('upload failed')
