from tkinter import *
from PIL import Image ,ImageTk
from Controller import Order_Controller
class food_frame:
    def __init__(self, parent_frame, image_path,text,row,column,bg_color,ident,price):
        self.food_image = None
        self.parent_frame = parent_frame
        self.row = row
        self.column = column
        self.bg_color = bg_color
        self.frame_food = Frame(self.parent_frame, height=185, width=155, bg=self.bg_color)
        self.Label_food = Label(self.frame_food)
        self.Heading_food = Label(self.frame_food, text=text, bg=self.bg_color)
        self.Button_mua_food = Button(self.frame_food, text="BUY NOW!")
        self.id = ident
        self.price = price
        self.Button_add_cart_food = Button(self.frame_food, text="Add to Cart", command=lambda: Order_Controller.lay_so_luong(self.Heading_food))
        # Tạo hàm riêng để tải và quản lý PhotoImage
        self.load_image(image_path)

        # Đặt các widget vào frame_food
        self.Label_food.grid(row=0, column=0, columnspan=2)
        self.Heading_food.grid(row=1, column=0, columnspan=2)
        self.Button_mua_food.grid(row=2, column=0)
        self.Button_add_cart_food.grid(row=2, column=1)

        # Thêm frame_food vào parent_frame
        self.frame_food.grid(row=self.row, column=self.column)

    def load_image(self, image_path):
        try:
            myimage = Image.open(image_path)
            self.food_image = ImageTk.PhotoImage(myimage)
            self.Label_food.config(image=self.food_image)
            self.Label_food.image = self.food_image  # Lưu trữ tham chiếu đến PhotoImage
        except Exception as e:
            print(f"Error: {e}")
    @property
    def foodLabel (self):
        return self.Label_food
    @property
    def getFood (self):
        return self.frame_food

    def foodID (self):
        return self.id


    def Price (self):
        return self.price


