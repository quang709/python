from Model import Car

def startView():
    print('Ví dụ về mô hình MVC - dạng đơn giản nhất')
    key = input('Bạn có muốn xem tất cả dữ liệu không? [y/n] ')
    return key

def endView():
    print('See You')

def showAllView(danhsach):
    for Car in danhsach:
        print(Car.name, '--', Car.engine, '--',Car.color)
    print('Tổng cộng có ', len(danhsach), ' Car')