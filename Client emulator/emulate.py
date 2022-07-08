from time import sleep

import requests
import json


def db_register():
    api_url = r"http://127.0.0.1:5000/howtospeak/api"
    print(requests.get(api_url))
    data = {'username': 'Vava', 'password': 'idontknowanything'}
    json_data = json.dumps(data)
    r = requests.post(api_url + r'/register', headers={'Content-Type': 'application/json'}, data=json_data)
    print(r.text)


def db_login():
    api_url = r"http://127.0.0.1:5000/howtospeak/api"
    data = {'username': 'Vava', 'password': 'idontknowanything'}
    json_data = json.dumps(data)
    r = requests.post(api_url + r'/login', headers={'Content-Type': 'application/json'}, data=json_data)
    print(r.text)


def db_login_by_api_key():
    api_url = r"http://127.0.0.1:5000/howtospeak/api"
    data = {'api_key': 'd24e79e8dc14186aae7e0b960eef504e'}
    json_data = json.dumps(data)
    r = requests.post(api_url + r'/login', headers={'Content-Type': 'application/json'}, data=json_data)
    print(r.text)


def db_login_check():
    api_url = r"http://127.0.0.1:5000/howtospeak/api"
    data = {'api_key': 'd24e79e8dc14186aae7e0b960eef504e'}
    json_data = json.dumps(data)
    r = requests.get(api_url + r'/login', headers={'Content-Type': 'application/json'}, data=json_data)
    print(r.text)


def db_update_session():
    api_url = r"http://127.0.0.1:5000/howtospeak/api"
    data = {'api_key': 'd24e79e8dc14186aae7e0b960eef504e'}
    json_data = json.dumps(data)
    r = requests.get(api_url + r'/updatesession', headers={'Content-Type': 'application/json'}, data=json_data)
    print(r.text)


def upgrade_vocabulary():
    api_url = r"http://127.0.0.1:5000/howtospeak/api"
    data = {'api_key': 'd24e79e8dc14186aae7e0b960eef504e',
            'words': ['man', 'legend', 'fork', 'kfegf', 'man', 'new', 'use']}
    json_data = json.dumps(data)
    r = requests.post(api_url + r'/upgrade_vocabulary', headers={'Content-Type': 'application/json'}, data=json_data)
    print(r.text)


def get_actual_words():
    api_url = r"http://127.0.0.1:5000/howtospeak/api"
    data = {'api_key': 'd24e79e8dc14186aae7e0b960eef504e', 'frequency_method_name': 'top_20000_google',
            'number_of_words': 100}
    json_data = json.dumps(data)
    r = requests.get(api_url + r'/actual_words', headers={'Content-Type': 'application/json'}, data=json_data)
    print(json.loads(r.content)['words_list'])


if __name__ == '__main__':
    db_login_by_api_key()
    upgrade_vocabulary()
    get_actual_words()
