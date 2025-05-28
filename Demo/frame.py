from tkinter import *

def main():
    food_form_root = Tk()
    food_form_root.title("Food Choices")
    food_form_root.geometry("500x500")

    # Tạo frame_coffee và đặt nó vào food_form_root
    frame_coffee = Frame(food_form_root)
    frame_coffee.pack(fill=BOTH, expand=True)

    # Tạo Canvas bên trong frame_coffee
    canvas = Canvas(frame_coffee)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Tạo Scrollbar và liên kết nó với Canvas
    scrollbar = Scrollbar(frame_coffee, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Liên kết Scrollbar với Canvas
    canvas.config(yscrollcommand=scrollbar.set)

    # Tạo Frame con bên trong Canvas để chứa các widget khác
    inner_frame = Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor=NW)

    # Thêm các widget vào inner_frame
    for i in range(100):
        Label(inner_frame, text=f"Item {i+1}").pack()

    # Cập nhật kích thước của Canvas để phù hợp với nội dung
    canvas.config(scrollregion=canvas.bbox(ALL))

    food_form_root.mainloop()

if __name__ == "__main__":
    main()
