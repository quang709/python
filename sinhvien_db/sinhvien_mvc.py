import db_exceptions
import sinhvien_db
import  sinhvien_model,sinhvien_view,sinhvien_controller


def start():
 try:
    #Khởi tạo đối tượng model
    model = sinhvien_model.SinhVienModel("localhost", "root", "root", "qlsvpxu")
    #Khởi tạo đối tượng view
    view = sinhvien_view.SinhVienView()
    #Khởi tạo controller
    controller = sinhvien_controller.SinhVienController(model, view)
    item = menu()
    while item in ["1", "2", "3", "4"]:
        if item == "1":
            controller.show_all_sinhvien()
        elif item == "2":
            hoten = input("Nhập họ tên: ")
            namsinh = input("Nhập năm sinh: ")
            sdt = int(input("Nhập sdt: "))
            controller.them_sinhvien(hoten, namsinh,sdt)
        elif item =="3":
            idsinhvien = input("nhập id:")
            hoten = input("Nhập họ tên: ")
            namsinh = input("Nhập năm sinh: ")
            sdt = int(input("Nhập sdt: "))
            controller.sua_sinhvien(idsinhvien,hoten, namsinh, sdt)
        elif item =="4":
            idsinhvien = input("nhập id:")
            controller.xoa_sinhvien(idsinhvien)

        item = menu()
    # #Hiển thị tất cả dữ liệu của bảng person
    # controller.show_all_sinhvien()

    # Them Tuan Anh vao csdl
    # controller.them_sinhvien("TuanAnh","1232000",44)
    # controller.sua_sinhvien(8,"tu","8/8/2000",44)
    # controller.xoa_sinhvien(11)
    # Hiển thị tất cả dữ liệu của bảng person
    # controller.show_all_sinhvien()
 except db_exceptions.DatabaseConnection as err:
     print(err)

def menu():
    print("1: Hiển thị tất cả Sinhvien")
    print("2: Thêm mới Sinhvien")
    print("3: Cập nhật Sinhvien ")
    print("4: Xóa Sinhvien")
    choice = input("Bạn hãy chọn các số từ 1 đến 4.")
    return choice
if __name__ == "__main__":
    start()