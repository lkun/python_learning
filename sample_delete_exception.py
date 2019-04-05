#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql

# 连接database
conn = pymysql.connect("192.168.93.132", "root", "123456", "python_sample", charset='utf8')
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()

sql = "DELETE FROM python_user WHERE id=%s;"
try:
    cursor.execute(sql, [4])
    # 提交事务
    conn.commit()
except Exception as e:
    # 有异常，回滚事务
    conn.rollback()
cursor.close()
conn.close()
