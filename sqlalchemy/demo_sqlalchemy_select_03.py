import sqlalchemy as db

#Thiết lập engine
engine = db.create_engine("mysql://root:root@localhost/qlsvpxu", echo=False)

#Kết nối tới csdl
connection = engine.connect()
metadata = db.MetaData()
sinhvien = db.Table('sinhvien', metadata, autoload = True, autoload_with = engine)

#Lọc dữ liệu SELECT * FROM actor WHERE first_name = 'Joe'
query = db.select([sinhvien]).where(sinhvien.columns.hoten == 'Loo')

ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
#In kết quả ra màn hình
for item in ResultSet:
    print(item)

#Đóng kết nối
ResultProxy.close()