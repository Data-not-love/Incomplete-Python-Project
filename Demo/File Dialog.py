from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
class hien_anh:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1920x1080')
        self.frame_hien_anh = Frame(self.root)
        self.frame_hien_anh.grid(row=1,column=1)
        def show_image():
            self.file_name = filedialog.askopenfilename()
            self.mo_file = Image.open(self.file_name)
            self.width,self.heigth = self.mo_file.size
            if self.file_name and self.width >=1200 and self.heigth >=1200:
                messagebox.showerror('Error','File is to big')
            else:
                self.image_directory = ImageTk.PhotoImage(self.mo_file)  # Sửa ở đây
                self.label_image = Label(self.frame_hien_anh, image=self.image_directory)
                self.label_image.grid(row=0,column=0)
        self.Button_chose_file = Button(self.root, width=10, text='Choose Image ', command=lambda: show_image())
        self.Button_chose_file.grid(row=0,column=0)


        self.root.mainloop()
app = hien_anh()


