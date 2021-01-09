from Model import Car

import View

#Hàm in ra tất cả dữ liệu
def showAll():
   #Lấy danh sách các Person
   Car_in_db = Car.get_All_Car()
   #calls view
   View.showAllView(Car_in_db)

#Hàm tương tác với người dùng
def start():
   choice = View.startView()
   if choice == 'y':
      showAll()
   else:
      View.endView()

#Chương trình chính
if __name__ == "__main__":
   #running controller function
   start()