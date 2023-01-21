import requests
import config
import json


def upload_freeimage(image_path):

    requests_url = 'https://freeimage.host/api/1/upload'
    img = open(image_path, 'rb').read()
    payload = {
                'key': config.freeimage_api_key,
                'action' : 'upload', 
                'format' : 'json'
    }

    response = requests.post(requests_url, params = payload, files = {'source': img})

    return json.loads(response.text)['image']['url'] 

image_path = 'images/54c87dec3f6ffca05d225434c4f65897b02a5fff.jpg'

#print(upload_freeimage(image_path))
