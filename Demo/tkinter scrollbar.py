# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
# root.geometry('500x500')
# root.resizable(False,False)
# root.title('Scroller')
#
# # tạo 2 labelframe khác nhau.Giống như Frame nhưng sẽ quản lý được Label
# wrapper1 = LabelFrame(root)
# wrapper2 = LabelFrame(root)
#
# # tạo đối tượng canvas vì thanh cuộn không thể add trực tiếp và đưa vào trong root
# my_canvas = Canvas(wrapper1)
# my_canvas.pack(side=LEFT, fill="both",expand="yes" )
#
# # tạo scrollbar và add vào cha nó là wrapper1 và có thể kéo đc vs phương thức my_canvas.yview
# y_srcollbar = ttk.Scrollbar(wrapper1,orient=VERTICAL, command=my_canvas.yview)
# y_srcollbar.pack(side=RIGHT,fill='y')
#
#
# # config canvas
#
# # thanh cuộn sẽ gửi các tín hiệu cuộn tới Canvas thông qua phương thức set() của y_srcollbar. Điều này cho phép Canvas
# # biết được vị trí hiện tại của thanh cuộn để hiển thị phần tương ứng của nội dung.#
# my_canvas.configure(yscrollcommand=y_srcollbar.set)
# # thêm vùng để cuộn
# my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox('all')))
#
# my_frame = Frame(my_canvas)
# my_canvas.create_window((0,0),window=my_frame,anchor='nw')
#
# wrapper1.pack (fill="both",expand="yes", padx=10, pady=10)
#
# # label frame cách nhau 10 pixel
#
# wrapper2.pack (fill="both",expand="yes", padx=10, pady=10)
#
# for i in range (150):
#     Button(my_frame, text="My_Button -"+str(i)).pack()
#
#
#
# my_canvas2 = Canvas(wrapper2)
# my_canvas2.pack(side=LEFT, fill="both", expand="yes" )
#
# x_scrollbar = ttk.Scrollbar(wrapper2,orient=HORIZONTAL, command=my_canvas2.xview)
# x_scrollbar.pack(side=BOTTOM,fill='x')
# my_canvas2.configure(xscrollcommand=x_scrollbar.set)
#
# my_canvas2.bind('<Configure>',lambda e:my_canvas2.configure(scrollregion=my_canvas2.bbox('all')))
# my_Frame2 = Frame(my_canvas2)
# my_canvas2.create_window((0,0),window=my_Frame2,anchor='nw')
#
#
# in1 = 0
# for i in range (150):
#     in1 = i+1
#     Button(my_Frame2, text="My_Button "+str(i)).grid(row=1, column=in1)
# root.mainloop()

from tkinter import *
from tkinter import ttk

# Tạo cửa sổ
food_form_root = Tk()
food_form_root.title("Food Choices")

# Tạo canvas
canvas = Canvas(food_form_root)
canvas.pack(side=LEFT, fill="both", expand=True)

# Thêm thanh cuộn dọc
y_scrollbar = ttk.Scrollbar(food_form_root, orient=VERTICAL, command=canvas.yview)
y_scrollbar.pack(side=RIGHT, fill="y")

# Thiết lập canvas để sử dụng thanh cuộn dọc
canvas.configure(yscrollcommand=y_scrollbar.set)

# Tạo frame coffee
frame_coffee = Frame(canvas, bg='white')

# Thêm frame coffee vào canvas
canvas.create_window((0, 0), window=frame_coffee, anchor='nw')

# Thiết lập kích thước của frame coffee khi thay đổi kích thước
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Kích hoạt hành động cuộn khi cửa sổ thay đổi kích thước
def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

frame_coffee.bind("<Configure>", on_frame_configure)
frame_coffee.bind("<MouseWheel>", on_mousewheel)

# Thêm nội dung vào frame_coffee
Coffee_Label = Label(frame_coffee, text='COFFEE CHOICES FOR YOU', font=("Arial", 12), padx=150, bg='white')
Coffee_Label.grid(row=0, column=0)

frame_cappuchinno = Frame(frame_coffee, height=105, width=600, bg='black', border=1)
frame_cappuchinno.grid(row=1, column=0)

# Thêm các frame con và thanh ngang vào frame_coffee
for i in range(2, 34):
    frame = Frame(frame_coffee, width=400, height=1, bg='white')
    frame.grid(row=i, column=0)

# Hiển thị cửa sổ
food_form_root.mainloop()
