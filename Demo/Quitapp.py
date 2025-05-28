from tkinter import *
from tkinter import messagebox

class LoginApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Login App")
        self.root.geometry("300x200")

        self.username_label = Label(self.root, text="Username")
        self.username_label.pack()

        self.username_entry = Entry(self.root)
        self.username_entry.pack()

        self.password_label = Label(self.root, text="Password")
        self.password_label.pack()

        self.password_entry = Entry(self.root, show="*")
        self.password_entry.pack()

        self.login_button = Button(self.root, text="Login", command=self.login)
        self.login_button.pack()
        self.root.mainloop()
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password")




