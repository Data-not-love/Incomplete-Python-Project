from tkinter import *
from Controller import Login_Controller
from Form_Attributes import *

class ForgotPasswordWindow:
    def __init__(self,root):
        self.root = root
        self.root.title('Forgot Password')
        self.root.geometry("830x415")
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        self.forget_pass_image = PhotoImage(file=file_img_3)
        self.forget_label = Label(self.root, image=self.forget_pass_image, bg=bg_white)
        self.forget_label.place(x=50, y=50)

        self.frame = Frame(self.root, width=350, height=380, bg=bg_white)
        self.frame.place(x=480, y=70)

        self.heading_forget = Label(self.frame, text='PASSWORD', fg='purple', bg=bg_white, font=font1)
        self.heading_forget.place(x=100, y=5)

        self.new_password_input = Entry(self.frame, width=25, fg='black', border=border, bg=bg_white, font=font2)
        self.new_password_input.place(x=30, y=80)
        self.new_password_input.insert(0, 'Enter New Password')
        self.new_password_input.bind('<FocusIn>', lambda event: Login_Controller.remove_string_enter(event, self.new_password_input, 'Enter New Password'))
        self.new_password_input.bind('<FocusOut>', lambda event: Login_Controller.refill_string_enter(event, self.new_password_input, 'Enter New Password'))

        self.new_pass_confirm = Entry(self.frame, width=25, fg='black', border=border, bg=bg_white, font=font2)
        self.new_pass_confirm.place(x=30, y=150)
        self.new_pass_confirm.insert(0, 'Re Enter New Password')
        self.new_pass_confirm.bind('<FocusIn>', lambda event: Login_Controller.remove_string_enter(event, self.new_pass_confirm, 'Re Enter New Password'))
        self.new_pass_confirm.bind('<FocusOut>', lambda event: Login_Controller.refill_string_enter(event, self.new_pass_confirm, 'Re Enter New Password'))

        self.create_account_button = Button(self.frame, width=39, pady=7, text='Create Account', bg='purple', fg='white', border=0,
                                            command=lambda: Login_Controller.check_newly_created_pass_Forget_Pass(self.new_password_input, self.new_pass_confirm))
        self.create_account_button.place(x=35, y=230)

if __name__ == "__main__":
    root = Tk()
    app = ForgotPasswordWindow(root)
    root.mainloop()
