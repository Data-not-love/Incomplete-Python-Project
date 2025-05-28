current_frame = None
def hello():
    print("Hello!")
# thoát app
def quit_app(root):
    from tkinter import messagebox
    messagebox.showinfo("Quit app","Goodbye")
    root.quit()

# cho các nút Account,cart
# vì trong hàm này frame mẹ được đặt sẵn ở ví 0,1 r nên việc cần làm là chỉ đặt thành phần frame con vào
def show_frame(frame):
    global current_frame
    # Nếu frame đang hiện thì ẩn frame đi và ngược lại
    if frame.winfo_viewable():
        # Nếu frame hiện tại đang được hiển thị, không làm gì cả
        pass
    else:
        # Nếu có frame hiện tại đang được hiển thị, ẩn nó
        if current_frame is not None and current_frame.winfo_viewable():
            current_frame.grid_remove()
        # Hiển thị frame mới
        frame.grid(row=0, column=1)
        # update frame hiện tại
        current_frame = frame