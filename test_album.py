from init_photo_service import service

response = service.albums().list().execute()
print(response)