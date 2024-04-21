import pymysql as mq
myser=mq.connect(host="localhost",user="root",password="",database="helloworld")
a=myser.cursor()
a=input("Enter plant name:")
b=input("Enter its colour:")
q="insert into plant (plant_name,colour) values(%s,%s)"
t=(a,b)
a.execute(q,t)
myser.commit()
