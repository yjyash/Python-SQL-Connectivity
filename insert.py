import pymysql as pq

db = pq.connect(host="localhost",user="root",password="1236",database="college")

mycursor = db.cursor()

q = "insert into student(name,course,rollno) values(%s,%s,%s)"
val = [("Yash","BTech","31"),("Hemant","BCA","32")]
mycursor.executemany(q,val)
db.commit()





