import pymysql as mq
myser=mq.connect(host="localhost",user="root",password="")
a=myser.cursor()
q="create database helloworld"
a.execute(q)
print("database created")
