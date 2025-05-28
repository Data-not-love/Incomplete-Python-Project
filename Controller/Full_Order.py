import datetime
from Login.Chi_tiet_order import *
from enum import Enum
import random
import Order_Controller,Login_Controller
from abc import ABC,abstractmethod
class State (Enum):
    CANCELLED = 'Cancelled'
    IN_DELIVERY = 'In Delivery'
    COMPLETE = 'Complete'
class order(ABC):
    def __init__(self):
        self.id = random.randint(100000,999999)
        self.detail = chi_tiet()
        self.total_price = self.detail.Total_price()
        self.date = datetime.datetime.now()
        self.receiving_address = Order_Controller.lay_dia_chi()
        self.state = State.IN_DELIVERY
        self.user = Login_Controller.check_Sign_In()

    @abstractmethod
    def insert(self):
        pass
    def lay_info (self):
        return str(self.id) + self.detail + self.total_price + self.date + self.receiving_address + self.state

