from tkinter import *
from Login.Form_Attributes import *
class Forgot_pass_window:
    def __init__(self):
        self.forget_pass_root = Tk()
        self.forget_pass_root.title('Forgot Password')
        self.forget_pass_root.geometry("890x415")
        self.forget_pass_root.configure(bg="#fff")
        self.forget_pass_root.resizable(False,False)

        try:
            self.forget_pass_image = PhotoImage(file='F:/forgot pass.png')
            self.forget_Label = Label(self.forget_pass_root, image=self.forget_pass_image, bg=bg_white)
            self.forget_Label.place(x=50, y=50)
        except Exception as e:
            print(f"Error: {e}")
        self.frame = Frame(self.forget_pass_root, width=350, height=380, bg=bg_white)
        self.frame.place(x=480, y=70)

        Label(self.frame, text='__________________________________________________________', height=1, background='white').place(x=25, y=92)

        Label(self.frame, text='__________________________________________________________', height=1, background='white').place(x=25, y=162)

        Label(self.frame, text='__________________________________________________________', height=1, background='white').place(x=25, y=232)

        self.heading_Forget = Label(self.frame, text='RESET PASSWORD', fg='purple', bg=bg_white, font=font1)
        self.heading_Forget.place(x=30, y=5)

        from Controller import Login_Controller
        self.New_UserName_Input = Entry(self.frame, width=25, fg='black', border=border, bg=bg_white, font=font2)
        self.New_UserName_Input.place(x=30, y=80)
        self.New_UserName_Input.insert(0, 'Enter UserName')
        self.New_UserName_Input.bind('<FocusIn>', lambda event: Login_Controller.remove_string_enter(event, self.New_UserName_Input, 'Enter UserName'))
        self.New_UserName_Input.bind('<FocusOut>', lambda event: Login_Controller.refill_string_enter(event, self.New_UserName_Input, 'Enter UserName'))


        self.New_password_Input = Entry(self.frame, width=25, fg='black', border=border, bg=bg_white, font=font2)
        self.New_password_Input.place(x=30, y=150)
        self.New_password_Input.insert(0,'Enter New Password')
        self.New_password_Input.bind('<FocusIn>', lambda event:Login_Controller.remove_string_enter(event, self.New_password_Input, 'Enter New Password'))
        self.New_password_Input.bind('<FocusOut>', lambda event:Login_Controller.refill_string_enter(event, self.New_password_Input, 'Enter New Password'))

        self.New_pass_confirm = Entry(self.frame, width=25, fg='black', border=border, bg=bg_white, font=font2)
        self.New_pass_confirm.place(x=30,y=220)
        self.New_pass_confirm.insert(0,'Re Enter New Password')
        self.New_pass_confirm.bind('<FocusIn>', lambda event:Login_Controller.remove_string_enter(event, self.New_pass_confirm, 'Re Enter New Password'))
        self.New_pass_confirm.bind('<FocusOut>', lambda event:Login_Controller.refill_string_enter(event, self.New_pass_confirm, 'Re Enter New Password'))

        self.Create_Account_Button = Button(self.frame, width=39, pady=7, text='Reset Account', bg='purple', fg='white', border=0, command=lambda :Login_Controller.reset_password(self.New_UserName_Input,self.New_password_Input, self.New_pass_confirm,self))
        self.Create_Account_Button.place(x=35,y=270)

        self.forget_pass_root.mainloop()
    def destroy_forget_pass(self):
        self.forget_pass_root.destroy()


