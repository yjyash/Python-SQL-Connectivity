import pymysql as pq

myconn = pq.connect(host="localhost",user="root",password="1236",database="practice")

mycurs = myconn.cursor()

q="select * from test"

mycurs.execute(q)

result =  mycurs.fetchall()

for x in result:
    print(x[1]+x[2]*2+x[3])

myconn.commit()


