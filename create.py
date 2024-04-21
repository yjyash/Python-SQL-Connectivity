import pymysql as pq

db = pq.connect(host="localhost",user="root",password="1236",database="college")

mycursor = db.cursor()

q = "create table student(rollno int ,name varchar(8),course varchar(8))"
mycursor.execute(q)




