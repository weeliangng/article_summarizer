import config
import requests
import json

def post_article_summary(image_location):
    post_url_create = 'https://graph.facebook.com/v15.0/{}/media'.format(config.instagram_id)
    create_payload = {
            'image_url' : image_location,
            'caption' : 'test post',
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
    else:
        print('upload failed')
