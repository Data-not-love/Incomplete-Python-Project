from tkinter import messagebox
from tkinter.simpledialog import askstring
import DataBase.Database_Attributes
import Login.Chi_tiet_order,Login.Frame_each_food
import Model.Connect_Database
def lay_so_luong(label_widget_heading):
    food_number = askstring("Enter Number", "Enter your quantity:")
    heading = label_widget_heading.cget("text")
    id = Login.Frame_each_food.food_frame.foodID
    price = Login.Frame_each_food.food_frame.Price

    # lấy label
    if not food_number.isdigit():
        messagebox.showerror("Error", "Please enter a valid number not text and not empty ")
    elif int(food_number) < 1 or int(food_number) > 100:
        messagebox.showerror("Error", "The quantity must is invalid")
        print("INVALID QUANTITY")
    else:
        messagebox.showinfo("Thank You", f"Successfully add {food_number} {heading} orders")
        print("SUCCESSFULLY ADD DETAILS TO CART")
        from Login.Chi_tiet_order import chi_tiet
        # tạo đối tượng chi tiết
        try:
            chi_tiet = Login.Chi_tiet_order.chi_tiet(id, heading, price, food_number)
            val_them = (chi_tiet.food_frame(id),
                        chi_tiet.food_name(heading),
                        chi_tiet.price(price),
                        chi_tiet.quantity(food_number))
            Model.Connect_Database.my_cursor.execute(Model.Connect_Database.sql_nhap_detail,val_them)
            DataBase.Database_Attributes.db.commit()

        except Exception as e:
            print("Error", f"{e}")
def lay_dia_chi ():
    address = askstring("Enter Address","Your Receiving address?")
    if address == '':
        messagebox.showerror("Error","Address can't be empty")
    else:
        messagebox.showinfo("Thank You For Order", "Please check the Order Button, Especially the details to make sure")
        from Login.Real_Order import Real_Order
        try:
            order = Login.Real_Order.Real_Order(address)
            val_them_order = (order.receiving_adress)
            Model.Connect_Database.my_cursor.execute(Model.Connect_Database.sql_them_order,val_them_order)
            DataBase.Database_Attributes.db.commit()
        except Exception as e:
            print("Error", f" {e}")

def add_to_cart():


    ordered_list = []
def buy_now(entry_wid,button_buynow_wid):
# ý tưởng là nếu dem_so_luong mà bằng 1 tức là buy now hoặc bấm nút Buy Now
# đưa vào order
    if lay_so_luong(entry_wid) == 1 or button_buynow_wid.get():
# hiển thị mã sản phẩm + id user
        pass



