import datetime
import random


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
        return self.price * Hoa_Don.tax
        # gọi biến class thông qua tên class.

randint1 = random.randint(100000,999999)
may_date = datetime.datetime.now()
hd1 = Hoa_Don(randint1,may_date,30000)
print (f"{hd1.ID()} date {hd1.date} price {hd1.getValue()}")

randint2 = random.randint(100000,999999)
may_date2 = datetime.datetime.now()
hd2 = Hoa_Don(randint2,may_date2,400000)
print (f"{hd2.ID()} date {hd2.date} price {hd2.getValue()}")

print(Hoa_Don.sl_hoaDon)