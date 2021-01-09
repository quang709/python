


class Car:
    # Thuộc tính có thể khơi tạo mặc định hoặc để trống


    # Phương thức khởi tạo
    def __init__(self, name, engine, color):
        # Khởi tạo thuộc tính của lớp ngay trong hàm init
        self.name = name
        self.engine = engine
        self.color = color



    # Lấy thông tin của đối tượng
    def __str__(self):
        return "{} có tuổi là {} và quốc tịch là {}".format(self.name, self.engine, self.color)

    @classmethod
    #Phương thức giả định lấy dữ liệu
    def get_All_Car(self):
        database = [("ab", 1.2,"vang"), ("sh", 23.5,"vang"), ("ex", 1.6,"vang"), ("eb", 1.8,"vang"), ("vb", 2.0,"vang")]
        result = []  #Trả về kết quả là list gồm các đối tượng Person
        #Chuyển database ở trên thành các đối tượng CAr - tương tự việc lấy trong CSDL sau này
        for idx, (name, engine,color) in enumerate(database):
            tam = Car(name,engine,color)
            result.append(tam)
        return result