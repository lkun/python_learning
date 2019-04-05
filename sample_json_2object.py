#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

# json.loads()

str1 = '{"listData": [1, 2, 3], "strData": "test python obj 2 json"}'
json2python = json.loads(str1)
print (json2python['listData'][0])
print (json2python['strData'])
print type(json2python)
