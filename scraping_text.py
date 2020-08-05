import requests
from time import sleep


group_id = '-71474813'
token = 'bf61d237bf61d237bf61d237e3bf12d086bbf61bf61d237e06aab056d9877dd4aa4c3df'
version = '5.72'


def write_txt(filename, text):
    with open(filename, 'a') as file:
        file.write(text + '\n')


def get_all_post_id():
    sleep(1)
    offset = 0
    arr_posts_id = []
    while True:
        sleep(1)
        r = requests.get('https://api.vk.com/method/wall.get',
                         params={'owner_id': group_id, 'count': 100,
                                  'offset': offset, 'access_token': token,
                                   'v': version})
        for i in range(100):
            post_id = r.json()['response']['items'][i]['id']
            arr_posts_id.append(post_id)

        if offset > 20000:
            break
        offset += 100
    return arr_posts_id


def get_all_comments(arr_posts_id):
    offset = 0
    for post_id in arr_posts_id:
        r = requests.get('https://api.vk.com/method/wall.getComments',
                         params={'owner_id': group_id, 'post_id': post_id, 'count': 100,
                                 'offset': offset, 'access_token': token,
                                 'v': version})
        for i in range(100):
            try:
                write_txt('comments.txt', r.json()['response']['items'][i]['text'])

            except IndexError:
                pass


if __name__ == '__main__':
    arr_posts_id = get_all_post_id()
    get_all_comments(arr_posts_id)
