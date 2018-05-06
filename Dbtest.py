# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("192.168.50.138", "root", "7798", "testDB", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("select * from pytest")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print ("first record : ",data)

# 关闭数据库连接
db.close()