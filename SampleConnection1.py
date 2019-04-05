#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql

# 连接database
conn = pymysql.connect("192.168.93.132", "root", "123456", "python_sample", charset='utf8')
# 得到一个可以执行SQL语句的光标对象
# cursor = conn.cursor()
# 得到一个可以执行SQL语句并且将结果作为字典返回的游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 定义要执行的SQL语句
sql = """
CREATE TABLE python_user1 (
id INT auto_increment PRIMARY KEY ,
name CHAR(10) NOT NULL UNIQUE,
age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;
"""
# 执行SQL语句
cursor.execute(sql)
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()
