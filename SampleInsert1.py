#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql.cursors

# 打开数据库连接
conn = pymysql.connect("192.168.93.132", "root", "123456", "easyweb", charset='utf8')

cur = conn.cursor()
cur.execute("insert into sys_authorities(authority,authority_name,create_time) values('get:/v1/user/xxx','get',"
            "'2019-04-05 10:04:00')")
conn.commit()
