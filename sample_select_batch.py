#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql

# 连接database
conn = pymysql.connect("192.168.93.132", "root", "123456", "python_sample", charset='utf8')
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()

# 查询数据的SQL语句
sql = "SELECT id,name,age from python_user;"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取多条查询数据
    ret = cursor.fetchall()
    for id, name, age in ret:
        str1 = "select * from python_user where id="
        str1 = str1 + str(id)
        print (str1)
        print (id, name, age)
except Exception as e:
    print (ret)
cursor.close()
conn.close()
# 打印下查询结果
print(ret)
