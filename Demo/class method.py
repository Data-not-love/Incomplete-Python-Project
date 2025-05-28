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
    # biến + phương thức của class có thể gọi qua 1 đối tượng cụ thể hoặc qua tên class và sửa giá trị thông qua đối tượng cụ thể or tên class
    # biến + phương thức static nếu muốn sửa giá trị là phải qua class
    @classmethod
    def Tach_data (cls,str1):
        id, date, price = str1.split('--')
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        price = int (price)
        # truyền  init vào class method
        return cls(id, date, price)


hoa_don_temp = "666767--2023-04-11--20000"

randint1 = random.randint(100000,999999)
may_date = datetime.datetime.now()
hd1 = Hoa_Don(randint1,may_date,30000)
hd1.setThue()
print (Hoa_Don.tax)
print (f"{hd1.ID()} date {hd1.date} price {hd1.getValue()}")
hd3 = Hoa_Don.Tach_data(hoa_don_temp)
print (f"{hd3.id} date {hd3.date} price {hd3.price}")