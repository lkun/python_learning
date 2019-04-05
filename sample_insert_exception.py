#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 连接database
conn = pymysql.connect("192.168.93.132", "root", "123456", "python_sample", charset='utf8')
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
sql = "INSERT INTO python_user(name, age) VALUES (%s, %s);"
username = "Alex"
age = 18

sql_batch = "INSERT INTO python_user(name, age) VALUES (%s, %s);"
data = [("Alex1", 18), ("Egon", 20), ("Yuan", 21)]

try:
    # 执行SQL语句-单条插入
    cursor.execute(sql, [username, age])
    # 执行SQL语句-批量插入
    cursor.executemany(sql_batch, data)
    # 提交事务
    conn.commit()
    # 提交之后，获取刚插入的数据的ID
    last_id = cursor.lastrowid
except Exception as e:
    # 有异常，回滚事务
    conn.rollback()
cursor.close()
conn.close()
