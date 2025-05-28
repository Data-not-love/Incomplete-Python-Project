import datetime
import random
import Login.Chi_tiet_order
import Login.User_for_app

class Real_Order:
    def __init__(self,receving_adress):
        self.__User_Id = Login.User_for_app.User
        self.__Id_order = random.randint(100000,999999)
        self.__chi_tiet = Login.Chi_tiet_order.chi_tiet()
        self.__thu_tu = Login.Chi_tiet_order.chi_tiet.thu_tu
        self.__order_date = datetime.datetime.now()
        self.__receving_adress = receving_adress
    @property
    def receiving_adress(self):
        return self.__receving_adress