from init_photo_service import service
import pickle
import requests

upload_url = 'https://photoslibrary.googleapis.com/v1/uploads'

def upload_image(image_path, upload_filename, token):
    headers = {
        'Authorization': 'Bearer ' + token.token,
        'Content-type': 'application/octet-stream',
        'X-Goog-Upload-Protocol': 'raw',
        'X-Goog-File-Name': upload_filename
    }

    img = open(image_path, 'rb').read()
    response = requests.post(upload_url, data=img, headers=headers)
    print('\nUpload token: {0}'.format(response.content.decode('utf-8')))
    return response

image_path = 'images/54c87dec3f6ffca05d225434c4f65897b02a5fff.jpg'
token = pickle.load(open('token_photoslibrary_v1.pickle', 'rb'))

tokens = []
response = upload_image(image_path, 'test', token)

tokens.append(response.content.decode('utf-8'))

new_media_items = [{'simpleMediaItem': {'uploadToken': tok}}for tok in tokens]

request_body = {
    'newMediaItems': new_media_items
}

upload_response = service.mediaItems().batchCreate(body=request_body).execute()
print(upload_response)