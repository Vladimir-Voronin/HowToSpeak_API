import time

import requests
import json


def db_register():
    api_url = r"http://127.0.0.1:5000/howtospeak/api"
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
    return r.cookies


def db_login_by_api_key():
    api_url = r"http://127.0.0.1:5000/howtospeak/api"
    data = {'api_key': 'd24e79e8dc14186aae7e0b960eef504e'}
    json_data = json.dumps(data)
    r = requests.post(api_url + r'/login', headers={'Content-Type': 'application/json'}, data=json_data)
    print(r.text)


def db_update_session():
    api_url = r"http://127.0.0.1:5000/howtospeak/api"
    data = {'api_key': 'd24e79e8dc14186aae7e0b960eef504e'}
    json_data = json.dumps(data)
    r = requests.get(api_url + r'/updatesession', headers={'Content-Type': 'application/json'}, data=json_data)
    print(r.text)


def upgrade_vocabulary(cookies):
    api_url = r"http://127.0.0.1:5000/howtospeak/api"
    data = {'username': 'Vava', 'session_info': 'Vava',
            'words': ['man', 'legend', 'fork', 'house', 'man', 'new', 'use', 'page', 'software', "home", "time",
                      "search", "service", "free", "one", "information", "list", "post", "make", "get", "site", "may",
                      "find", "price", "see", "news", "state", "view", "book", "work", "contact", "help", "review",
                      "business", "right", "web", "also", "link", "say", "online", "include", "date", "first", "name",
                      "would", "click", "game", "add", "take", "like", "need", "program", "provide", "back", "buy",
                      "top", "message", "report", "people", "rat", "show", "support", "school", "order", "know",
                      "email", "shop", "number", "store", "group", "year", "day", "comment", "company", "two", "health",
                      "read", "world", "last", "result", "next", "change", "file", "products", "music", "set", "data",
                      "part", "look", "product", "system", "map", "please", "term", "give", "ship", "city", "design",
                      "copyright", "policy", "write", "detail", "call", "available", "mail", "well", "best", "send",
                      "plan", "line"]}
    json_data = json.dumps(data)
    r = requests.post(api_url + r'/vocabulary/update', headers={'Content-Type': 'application/json'}, cookies=cookies,
                      data=json_data)
    print(r.text)


def get_actual_words(cookies):
    api_url = r"http://127.0.0.1:5000/howtospeak/api"
    data = {'username': 'Vava', 'frequency_method_name': 'top_20000_google',
            'number_of_words': 100, 'handler_method': 'words_using_less_than_5'}
    json_data = json.dumps(data)
    r = requests.post(api_url + r'/vocabulary/get', headers={'Content-Type': 'application/json'}, cookies=cookies,
                      data=json_data)
    print(r.text)
    # print(json.loads(r.content)['words_list'])


if __name__ == '__main__':
    db_register()
    cookies = db_login()
    upgrade_vocabulary(cookies)
    get_actual_words(cookies)
