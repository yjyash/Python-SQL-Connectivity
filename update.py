import pymysql as pq

db = pq.connect(host="localhost",user="root",password="1236",database="college")

mycursor = db.cursor()

q = "update student set course=%s where name=%s"
val = ["Bcom","Hemant"]
mycursor.execute(q,val)
db.commit()





