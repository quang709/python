import sqlalchemy as db

#Thiết lập engine
engine = db.create_engine("mysql://root:root@localhost/qlsvpxu", echo=True)

#Kết nối tới csdl
connection = engine.connect()
metadata = db.MetaData()
sinhvien = db.Table('sinhvien', metadata, autoload = True, autoload_with = engine)

#Lấy tất cả dữ liệu của bảng sinhvien - tương đương câu lênh SELECT * FROM person
def show_all_person(sinhvien, connection):
    query = db.select([sinhvien])

    proxy = connection.execute(query)
    rs = proxy.fetchall()
    #In kết quả ra màn hình
    for item in rs:
        print(item)

    #Đóng kết nối
    proxy.close()

#Hiển thị dữ liệu
show_all_person(sinhvien, connection)

#Chèn 1 dòng vào bảng person
query = db.insert(sinhvien).values(hoten='Hoang', namsinh = '20112000',sdt='24')
ResultProxy = connection.execute(query)
#In ra màn hình giá trị id vừa được sinh
print(ResultProxy.inserted_primary_key)

#Hiển thị dữ liệu
print('---Sau khi INSERT--')
show_all_person(sinhvien, connection)

#Chèn nhiều dòng vào bảng person
query = db.insert(sinhvien)
values = [{'hoten': 'Loan', 'namsinh': '20112000','sdt':24},
          {'hoten': 'Hoa', 'namsinh': '20112000','sdt':24},
          {'hoten': 'Lien', 'namsinh': '20112000','sdt':24}]
ResultProxy = connection.execute(query, values)

#Hiển thị dữ liệu
print('----Batch INSERT-----')
show_all_person(sinhvien, connection)

ResultProxy.close()