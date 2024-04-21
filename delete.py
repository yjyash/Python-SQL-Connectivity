import pymysql as pq

db = pq.connect(host="localhost",user="root",password="1236",database="college")

mycursor = db.cursor()

q = "delete from student where name='Hemant'"

mycursor.execute(q)
db.commit()
