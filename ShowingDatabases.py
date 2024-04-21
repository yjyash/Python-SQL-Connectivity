import pymysql as mq
myser=mq.connect(host="localhost",user="root",password="")
a=myser.cursor()
q="show databases"
a.execute(q)
data=a.fetchall()
for d in data:
    print(d[0])
