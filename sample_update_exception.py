#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql

# 连接database
conn = pymysql.connect("192.168.93.132", "root", "123456", "python_sample", charset='utf8')
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()

# 修改数据的SQL语句
sql = "UPDATE python_user SET age=%s WHERE name=%s;"
username = "Alex"
age = 80
try:
    # 执行SQL语句
    cursor.execute(sql, [age, username])
    # 提交事务
    conn.commit()
except Exception as e:
    # 有异常，回滚事务
    conn.rollback()
cursor.close()
conn.close()
