#create user
import mysql.connector
try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="prathyusha@231",
        database="pydb"
    )
    cursor=conn.cursor() 
    cursor.execute("create table users(username varchar(20),password varchar(20));")
    for data in cursor.fetchall():
        print(data)
except Exception as e:
    print("check your connection",e) 


#registration
import mysql.connector
try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="prathyusha@231",
        database="pydb"
    )
    username=input("enter the name:")
    password=input("enter the password:")
    sql="""
    insert into users values(%s,%s)"""
    data=(username,password)
    cursor=conn.cursor() 
    cursor.execute(sql,data)
    conn.commit()
    print("Registration successful...!")
except Exception as e:
    print("check your connection",e) 
    
    
    
#login
import mysql.connector
try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="prathyusha@231",
        database="pydb"
    )
    username=input("enter the name:")
    password=input("enter the password:")
    sql="select*from users where username=%s and password=%s;"
    cursor=conn.cursor()
    cursor.execute(sql,(username,password))
    user=cursor.fetchone()
    if user:
        print("Login succefully...!")
        print("welcome to",username)
    else:
        print("Invalid username or password")
except Exception as e:
    print("Check your connection:", e)
