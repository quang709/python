import mysql.connector

#Kết nối đến csdl sakila
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "root",
    database = "qlsvpxu"
)

mycursor = mydb.cursor()

sql = "DELETE FROM sinhvien WHERE idsinhvien = %s"
val = ("3", )

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, " bảng ghi đã bị xóa")

mycursor.close()
mydb.close()