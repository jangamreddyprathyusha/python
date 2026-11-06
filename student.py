import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="prathyusha@231",
    database="pydb"
)
print(conn.is_connected())

#register 
def studenthomepage():
    print("Welcome to studenthomepage..!")
def teacherhomepage():
    print("Welcome to studenthomepage..!")
    
print("1.register")
print("2.login")
n=int(input("select any one opt:"))
if(n==1):
    st_name=input("Enter student name....!")
    st_email=input("Enter student email...!")
    st_password=input("Enter password...!")
    st_role=input("Enter student role...!")
    sql="insert into student1(name,email,password,role)values(%s,%s,%s,%s);"
    cursor=conn.cursor()
    cursor.execute(sql,(st_name,st_email,st_password,st_role))
    conn.commit()
    print("register successful..!")
if(n==2):
    st_email=input("Enter student email...!")
    st_password=input("Enter password...!")
    sql="select*from student1 where email=%s and password=%s;"
    cursor=conn.cursor()
    cursor.execute(sql,(st_email,st_password))
    user=cursor.fetchone()
    if(user[4]=="student"):
        print("Login succefully...!")
        print("welcome to student portal",user[1])
        studenthomepage()
    elif(user[4]=="teacher"):
        print("Login succefully...!")
        print("welcome to teacher portal",user[1])
        teacherhomepage()
    else:
        print("check the details...")