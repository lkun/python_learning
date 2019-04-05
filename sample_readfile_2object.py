#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json


def json_to_python_from_file():
    """ 从文件读取内容，并转换成python对象 """
    # 以只读的格式，utf-8 的编码读取
    f = open('./static/book.json', 'r')
    s = f.read()
    print(s)
    rest = json.loads(s)
    print(rest['name'])
    # 打开文件后一定要关闭
    f.close()


json_to_python_from_file()
