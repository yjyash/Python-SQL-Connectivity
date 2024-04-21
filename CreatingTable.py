import pymysql as mq
myser=mq.connect(host="localhost",user="root",password="",database="helloworld")
a=myser.cursor()
q="create table plant(plant_id INT auto_increment primary key, plant_name varchar(25), colour varchar(25))"
a.execute(q)
print("table created")
