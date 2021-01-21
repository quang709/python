import sqlalchemy as db

#Thiết lập engine
engine = db.create_engine("mysql://root:root@localhost/qlsvpxu", echo=False)

#Kết nối tới csdl
connection = engine.connect()
metadata = db.MetaData()
sinhvien = db.Table('sinhvien', metadata, autoload = True, autoload_with = engine)

#Lấy tất cả dữ liệu của bảng actor - tương đương câu lênh SELECT * FROM actor
query = db.select([sinhvien])

ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
#In kết quả ra màn hình
for item in ResultSet:
    print(item)

#Đóng kết nối
ResultProxy.close()