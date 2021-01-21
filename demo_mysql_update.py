import mysql.connector

#Kết nối đến csdl sakila
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "root",
    database = "qlsvpxu"
)

mycursor = mydb.cursor()

#Cập nhật dữ liệu
sql = """ UPDATE sinhvien
                SET hoten = %s,
                    namsinh = %s,
                    sdt = %s
                WHERE idsinhvien = %s """
val = ("Duc","11112000",32, "1")

mycursor.execute(sql, val)
mydb.commit()

print('Finished')

mycursor.close()
mydb.close()