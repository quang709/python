import mysql.connector

#Kết nối đến csdl qlsv
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

#Chèn dữ liệu vào bảng person
sql = "INSERT INTO sinhvien (hoten, namsinh,sdt) VALUES (%s, %s,%s)"
val = ("Long","11112000","19")
val = ("Li","11112000","49")

mycursor.execute(sql, val)

mydb.commit()

#Lấy id vừa được sinh ra (do personID được sinh tự động)
if mycursor.lastrowid:
    print('ID của sinhvien vừa được tạo là ', mycursor.lastrowid)
else:
    print('Không tìm thấy ID của record vừa được tạo')

mydb.close()