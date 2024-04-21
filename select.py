import pymysql as pq

db = pq.connect(host="localhost",user="root",password="1236",database="college")

mycursor = db.cursor()

q = "select * from student"

mycursor.execute(q)
myresult = mycursor.fetchall()

for x in myresult:
    print("Roll No=",x[0])
    print("Student Name=",x[1])
    print("course =",x[2])

    print("--------------------------")




