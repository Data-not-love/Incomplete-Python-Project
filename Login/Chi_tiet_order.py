from Login import Frame_each_food
from abc import abstractmethod
class chi_tiet:
    thu_tu = 0
    def __init__(self,foodID,foodLabel,price,number_food):
        self.__food_frame = foodID
        self.__food_name = foodLabel
        self.__price = price
        self.__quantity = number_food
        #id là thứ tự
        self.thu_tu += 1

    @abstractmethod
    def insert(self):
        values = (self.food_frame,str(self.quantity), str(self.price))
        return values
    @property
    def thu_tu(self):
        return self.thu_tu
    @property
    def food_frame_Id(self):
        return self.__food_frame
    @property
    def food_name(self):
        return self.__food_name
    @property
    def quantity(self):
        return self.__quantity
    @property
    def price(self):
        return self.__price
    @quantity.setter
    def quantity (self,value):
        self.__quantity = value
    @food_frame_Id.setter
    def food_frame (self,value):
        self.food_frame_Id = value
    @price.setter
    def price (self,value):
        self.__price = value
    @food_name.setter
    def food_name (self,value):
        self.__food_frame = value
    def Total_price(self):
        return self.price * self.__quantity

    def chi_tiet_info(self):
        values = (self.__food_frame,self.food_name , str(self.quantity) , str(self.price))
        return values

