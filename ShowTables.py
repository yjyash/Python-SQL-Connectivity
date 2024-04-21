import pymysql as mq
myser=mq.connect(host="localhost",user="root",password="",database="helloworld")
a=myser.cursor()
q="show tables"
a.execute(q)
data=a.fetchall()
for d in data:
    print(d[0])

