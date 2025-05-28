from tkinter import *
from tkinter.ttk import Treeview

main_window = Tk()
frame = Frame (main_window)
frame.grid(row=0,column=0)

board = Treeview(frame)
board["columns"] = ("Id","Name","Price_tag","Quantity")
# Cấu hình cột "#0"
board.column("#0", width=66,stretch=NO)

for col in board["columns"]:
    board.column(col, width=80)
    board.heading(col, text=col)

for i in range (23) :
    board.insert("","end",text="Row "+str(i+1), values=("ID"+str(i+1), "NAME"+str(i+1), "PRICE"+str(i+1), "QUANTITY"+str(i+1)))

scrollbar = Scrollbar(frame,orient="vertical", command=board.yview())
board.configure(yscrollcommand=scrollbar.set)
frame_nut = Frame(main_window)
frame_nut.grid(row=1,column=0)
board.grid(row=0, column=0, columnspan=1,sticky='nsew')
scrollbar.grid(row=0, column=1,columnspan=3,sticky='ns')
Button_add_cart = Button(frame_nut,text="Add to cart",width=18)
Button_add_cart.grid(row=1, column=0)
Button_buy = Button(frame_nut,text="Buy now",width=18)
Button_buy.grid(row=1, column=1)
Button_add_cart = Button(frame_nut,text="Cancel Order",width=18)
Button_add_cart.grid(row=1, column=2)
main_window.mainloop()
#
#def update_value(row_id, new_values):
#    board.item(row_id, values=new_values)
#update_value(board.get_children()[0], ("NewID", "NewName", "NewPrice", "NewQuantity"))

#
#