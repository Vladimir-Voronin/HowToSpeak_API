import requests
import json

API_URL_BASE = r'http://127.0.0.1:5000/howtospeak/api'


def db_register(username, password):
    url_add = r'/register'
    data = {'username': username, 'password': password}
    json_data = json.dumps(data)
    r = requests.post(API_URL_BASE + url_add, headers={'Content-Type': 'application/json'}, data=json_data)
    print(r.text)


def db_login(username, password):
    url_add = r'/login'
    data = {'username': username, 'password': password}
    json_data = json.dumps(data)
    r = requests.post(API_URL_BASE + url_add, headers={'Content-Type': 'application/json'}, data=json_data)
    print(r.text)
    return r.cookies


def upgrade_vocabulary(cookies, username, data: list):
    url_add = r'/vocabulary/update'
    data = {'username': username,
            'words': data}
    json_data = json.dumps(data)
    r = requests.post(API_URL_BASE + url_add, headers={'Content-Type': 'application/json'}, cookies=cookies,
                      data=json_data)
    print(r.text)


def get_actual_words(cookies, username, frequency_method_name, number_of_words, handler_method):
    url_add = r'/vocabulary/get'
    data = {'username': username, 'frequency_method_name': frequency_method_name,
            'number_of_words': number_of_words, 'handler_method': handler_method}
    json_data = json.dumps(data)
    r = requests.post(API_URL_BASE + url_add, headers={'Content-Type': 'application/json'}, cookies=cookies,
                      data=json_data)
    print(r.text)
