# import mysql.connector
# try:
#     conn=mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="prathyusha@231",
#         database="pyDB"
#     )
#     cursor=conn.cursor() 
#     cursor.execute("create table student(id int,name varchar(10),rln varchar(10));")
#     for data in cursor.fetchall():
#         print(data)
# except Exception as e:
#     print("check your connection",e) 


import mysql.connector
try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="prathyusha@231",
        database="pydb"
    )
    sql="""
    insert into student values(%s,%s,%s)"""
    data=(1,"Reena","2f3")
    cursor=conn.cursor() 
    cursor.execute(sql,data)
    conn.commit()
    print("table created successful...!")
except Exception as e:
    print("check your connection",e) 