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

post_article_summary('https://lh3.googleusercontent.com/uUuHL_5iChEdog_eFWEtsdRVOLkGoPHK85G-88kI8aIHkqBvOZzBupEgqBOC9MMWyyYOVSA6DXmoeVZ5kpBTdIeUZ-I6crfNleJdxKuVS1_W-w6G7igY95tP2IHcoJP2WHwQWY3HON_zOyEWcrg5Djpzn09ovcnLiDLDqPOkUkPFmhkxoCIc2IYEurj0TYqLs546IYPEiyRi_pecgSnhhQ066VdwcB9mqySLXJAaqhUJX3jgYhdiG8ywVRupQfrn_d2-2phGmE4bH9zSiGh1qi3QCS0ai5Kj5nE9f-uTDNXXVnOOPHaHARQtacNROmfzLugq1vgcLMkGjfAglZQJXqvGc98JDX1HQbgdmK7gkcAIDfkY8S9R3BuPrZRUbIND8jGaXglIyB_f6RDx_QXulL1q4uXyHIAxXvrcGBvORB_1btRapehfk5Qukmb_0gPOoiaJG1wwWG2VqFuW8yOPGZhXdfMtl_1a6nswpCo-TxgqnQa9nzbRtFrheCCHOpJyhPG6hafLWd0dYyxsQN7FKo88r5LsXGhXx_Bayxm8a4pRzwPowKI2-yYtJz2LVpsdG3cN9iT_k8Sor8qdvU1vxLjazfmV83JRWhmFPA3pDawFPYy9lPoplGaII2iQzbs4Q0haTmJKb_N-CHF5EjRnv4nwBbkPxm2YZXs0-SA0Ol5j24wD8Ts_KBWSCTtReIb8wbbhLD6i0BGRTeWYHxjPhGPS-hWhQWUNoQnV8u26kQeotf3nth_J-99glVRvRx7QxJCAT90c1HSuCKMyzgr_h1rSQX58Jgz_s7Cqn4GulXxMwHJs-TuGfDOPEK-mcWsiJTwDsm8aShzTYA3kD2lRuKL0arFRMAOJhbFHa64-Cgl0_a2tjn49vDB0se7T0UcQ4D-vPM5blSIqZYe4ZodiCWsQjTpmg_g2LzL88enmt4X1kWCP=s750-no?authuser=0')