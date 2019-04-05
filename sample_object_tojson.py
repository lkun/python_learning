#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

# json.dumps()

# 构造字典
python2json = {}
# 构造list
listData = [1, 2, 3]
python2json["listData"] = listData
python2json["strData"] = "test python obj 2 json"

# 转换成json字符串
json_str = json.dumps(python2json)
print json_str
