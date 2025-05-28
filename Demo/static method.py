import random
import datetime

class Hoa_Don():
    # class var
    tax = 9
    sl_hoaDon = 0
    def __init__(self,id,date,price):
        self.id = id
        self.date = date
        self.price = price
        Hoa_Don.sl_hoaDon += 1
    def date (self):
        return self.date
    def ID (self):
        return self.id
    def getValue (self):
        return self.price * self.tax
        # gọi biến class thông qua tên class
    @classmethod
    def setThue (cls):
        cls.tax = 1.5 # truy cập đến class variable
    @staticmethod
    def danh_gia_hoa_don (price):
        if price > 100000:
            print("Gia tri cao")
        else:
            print("Gia tri thap")

    # biến + phương thức của class có thể gọi qua 1 đối tượng cụ thể hoặc qua tên class và sửa giá trị thông qua đối tượng cụ thể or tên class
    # biến + phương thức static nếu muốn sửa giá trị là phải qua class
randint1 = random.randint(100000,999999)
may_date = datetime.datetime.now()
hd1 = Hoa_Don(randint1,may_date,30000)
print (f"{hd1.ID()} date {hd1.date} price {hd1.getValue()}")
hd1.danh_gia_hoa_don(hd1.price)

randint2 = random.randint(100000,999999)
may_date2 = datetime.datetime.now()
hd2 = Hoa_Don(randint2,may_date2,400000)
print (f"{hd2.ID()} date {hd2.date} price {hd2.getValue()}")
hd2.danh_gia_hoa_don(hd2.price)