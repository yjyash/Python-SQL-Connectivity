import pymysql as pq

host="localhost"
user="root"
passk="1236"
data="auth"

a=input("Enter your username : ")
b=input("Enter your password : ")

try:
    myconn = pq.connect(host=host,user=user,password=passk,database=data)
    print("Connection to server successfull !")
    mycurs = myconn.cursor()
    q="select * from user where username='{}' and passkey='{}' ".format(a,b)
    try:
        mycurs.execute(q)
        result = mycurs.fetchall()
        print("Your details :")

        for x in result:
            print("Name :",x[0])
            print("Username : ",x[1])
            print("Passkey : ",x[2])
            print("-------------------------------")
    except Exception as e:
        print("No record found",e)
        

except Exception as E:
    print("Try Again:",E)

finally:
    print("Thank You")
    mycurs.close
    myconn.close
