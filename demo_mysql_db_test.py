import mysql.connector

#Kết nối đến csdl sakila
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "root",
    database = "qlsvpxu"
)

#Liệt kê các bảng dữ liệu trong csdl sakila
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for item in mycursor:
    print(item)

mydb.close()