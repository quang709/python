import sqlalchemy as db

#Thiết lập engine
engine = db.create_engine("mysql://root:root@localhost/qlsvpxu", echo=True)

#Kết nối tới csdl
connection = engine.connect()
metadata = db.MetaData()
sinhvien = db.Table('sinhvien', metadata, autoload = True, autoload_with = engine)

#Cú pháp delete
#db.delete(table_name).where(condition)
query_delete = db.delete(sinhvien).where(sinhvien.columns.sdt > 30)
ResultProxy = connection.execute(query_delete)

#In kết quả ra màn hình
query_select = db.select([sinhvien])
ResultProxy = connection.execute(query_select)
ResultSet = ResultProxy.fetchall()
#In kết quả ra màn hình
for item in ResultSet:
    print(item)

#Đóng kết nối
ResultProxy.close()