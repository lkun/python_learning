#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests

# http://docs.python-requests.org/zh_CN/latest/user/quickstart.html

r = requests.get('https://api.github.com/events')
print r.content
print r.json()

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print r.url

r = requests.post('http://httpbin.org/post', data={'key': 'value'})
print r.status_code

# 定制请求头
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print r.json()

# 复杂POST
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
