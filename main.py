import random
import logging
import requests
import os
import shutil

from dotenv import load_dotenv

IMAGES_DIR = 'images'


def publish_pic_to_the_wall(description_of_comic, owner_id, vk_access_token, media_id, vk_group_id):
    params = {
        'access_token': vk_access_token,
        'owner_id': f'-{vk_group_id}',
        'v': 5.131,
        'from_group': 1,
        'message': description_of_comic,
        'attachments': f'photo{owner_id}_{media_id}'
    }
    url = 'https://api.vk.com/method/wall.post'
    response = requests.post(url, params=params)
    response.raise_for_status()


def upload_pic_to_group_album(vk_access_token, vk_group_id, photo_params, photo_hash, photo_server):
    params = {
        'access_token': vk_access_token,
        'group_id': vk_group_id,
        'photo': photo_params,
        'hash': photo_hash,
        'server': photo_server,
        'v': 5.131
    }
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    response = requests.post(url, params=params)
    response.raise_for_status()
    response_content = response.json()
    media_id = response_content['response'][0]['id']
    owner_id = response_content['response'][0]['owner_id']
    return media_id, owner_id


def upload_pic_on_vk_server(upload_url):
    with open(os.path.join('images', 'pc.jpg'), 'rb') as file:
        files = {
            'photo': file
        }
        response = requests.post(upload_url, files=files)
    response.raise_for_status()
    response_content = response.json()
    photo_params = response_content['photo']
    photo_hash = response_content['hash']
    photo_server = response_content['server']
    return photo_params, photo_hash, photo_server


def get_the_server_address(vk_access_token, vk_group_id):
    params = {
        'group_id': vk_group_id,
        'access_token': vk_access_token,
        'v': 5.131
    }
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    response = requests.get(url, params=params)
    response.raise_for_status()
    upload_url = response.json()['response']['upload_url']
    return upload_url


def get_comic():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    num = response.json()['num']
    url = f'https://xkcd.com/{random.randint(1, num)}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    response_content = response.json()
    img_link = response_content['img']
    description_of_comic = response_content['alt']
    return img_link, description_of_comic


def download_image(img_link, path, params=''):
    response = requests.get(img_link, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    load_dotenv()
    vk_group_id = os.getenv('VK_GROUP_ID')
    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    image_name = 'pc.jpg'
    os.makedirs(IMAGES_DIR, exist_ok=True)
    path = os.path.join(IMAGES_DIR, image_name)
    try:
        img_link, description_of_comic = get_comic()
        download_image(img_link, path, params='')
        upload_url = get_the_server_address(vk_access_token, vk_group_id)
        photo_params, photo_hash, photo_server = upload_pic_on_vk_server(upload_url)
        media_id, owner_id = upload_pic_to_group_album(vk_access_token, vk_group_id, photo_params, photo_hash, photo_server)
        publish_pic_to_the_wall(description_of_comic, owner_id, vk_access_token, media_id, vk_group_id)
    except requests.exceptions.HTTPError:
        logging.exception()
    finally:
        shutil.rmtree('images')
