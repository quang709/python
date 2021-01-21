import mysql.connector

#Kết nối đến csdl sakila
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "root",
    database = "qlsvpxu"
)


mycursor = mydb.cursor()

#Lấy tất cả dữ liệu trong bảng person
sql = "SELECT * FROM sinhvien"
mycursor.execute(sql)

my_result = mycursor.fetchall()

#In kết quả ra màn hình
for item in my_result:
    print(item)

#Câu sql khác
sql = "SELECT hoten, namsinh FROM sinhvien"
mycursor.execute(sql)

my_result = mycursor.fetchall()

#In kết quả ra màn hình
for item in my_result:
    print(item)

#Sự khác biệt giữa fetchall và fetchone
print("Sự khác biệt giữa fetchall và fetchone")
sql = "SELECT hoten, namsinh FROM sinhvien"
mycursor.execute(sql)
my_result = mycursor.fetchone()
print(my_result)

mydb.close()