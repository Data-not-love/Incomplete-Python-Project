from tkinter import *
from Login.Form_Attributes import *
class Sign_Up_app:
    def __init__(self):
        self.Sign_Up_Root = Tk()

        self.Sign_Up_Root.title('Sign Up')
        self.Sign_Up_Root.geometry("840x500")
        self.Sign_Up_Root.configure(bg="#fff")
        self.Sign_Up_Root.resizable(False,False)

        try:
            self.sign_up_image = PhotoImage(file='F:/3.5 Years/First Year/Python/Fast_food_app/Assets/signup.png')
            self.Label_image = Label(self.Sign_Up_Root, image=self.sign_up_image, bg=bg_white)
            self.Label_image.place(x=50, y=90)
        except Exception as e:
            print(f"An error occurred: {e}")

        self.frame = Frame(self.Sign_Up_Root, width=350, height=420, bg=bg_white)
        self.frame.place(x=480, y=50)

        self.heading_Sign_Up = Label(self.frame, text='SIGN UP', fg='#4da029', bg=bg_white, font=font1)
        self.heading_Sign_Up.place(x=100, y=5)

        self.User_name_Input = Entry(self.frame, width=25, fg='black', border=border, bg='white', font=font2)
        self.User_name_Input.place(x=30, y=80)
        self.User_name_Input.insert(0, 'UserName')

        from Controller import Login_Controller
        self.User_name_Input.bind('<FocusIn>',lambda event:Login_Controller.remove_string_enter(event,self.User_name_Input,'UserName'))
        self.User_name_Input.bind('<FocusOut>',lambda event:Login_Controller.refill_string_enter(event,self.User_name_Input,'UserName'))

        Label(self.frame, text='__________________________________________________________', height=1, background='white').place(x=25, y=97)

        self.password_Input = Entry(self.frame, width=25, fg='black', border=border, bg=bg_white, font=font2 )
        self.password_Input.place(x=30, y=150)
        self.password_Input.insert(0, "Password")
        self.password_Input.bind('<FocusIn>',lambda event:Login_Controller.remove_string_enter(event,self.password_Input,'Password'))
        self.password_Input.bind('<FocusOut>',lambda event:Login_Controller.refill_string_enter(event,self.password_Input,'Password'))

        Label(self.frame, text='__________________________________________________________', height=1, background='white').place(x=25, y=167)

        self.password_confirm_Input = Entry(self.frame, width=25, fg='black', border=border, bg=bg_white, font=font2)
        self.password_confirm_Input.place(x=30, y=220)
        self.password_confirm_Input.insert(0, "Re_Enter Password")
        self.password_confirm_Input.bind('<FocusIn>',lambda event:Login_Controller.remove_string_enter(event,self.password_confirm_Input,'Re_Enter Password'))
        self.password_confirm_Input.bind('<FocusOut>',lambda event:Login_Controller.refill_string_enter(event,self.password_confirm_Input,'Re_Enter Password'))

        Label(self.frame, text='__________________________________________________________', height=1, background='white').place(x=25, y=237)

        self.email_Input = Entry(self.frame, width=25, fg='black', border=border, bg=bg_white, font=font2)
        self.email_Input.place(x=30, y=290)
        self.email_Input.insert(0, "Email")
        self.email_Input.bind('<FocusIn>', lambda event: Login_Controller.remove_string_enter(event, self.email_Input, 'Email'))
        self.email_Input.bind('<FocusOut>', lambda event: Login_Controller.refill_string_enter(event, self.email_Input, 'Email'))

        Label(self.frame, text='__________________________________________________________', height=1, background='white').place(x=25, y=307)

        self.Button_Sign_Up = Button(self.frame, width=39, pady=7, text='Sign Up', bg='#4da029', fg='white', border=border, command=lambda:Login_Controller.create_account(self.User_name_Input,self.password_Input,self.password_confirm_Input,self.email_Input,self))
        self.Button_Sign_Up.place(x=35, y=340)

        self.sign_in_Button = Button(self.frame,width=6, text='Already have an account ?  Sign In', border=border, bg=bg_white,cursor='hand2',fg='#4da029', padx=120,command=lambda:Login_Controller.call_sign_in_Sign_up(self))
        self.sign_in_Button.place(x=35, y=390)

        self.Sign_Up_Root.mainloop()
    def destroy_Sign_Up(self):
        self.Sign_Up_Root.destroy()

    def getEmail(self):
        return self.email_Input
    def getUserName(self):
        return self.User_name_Input
    def getPass(self):
        return self.password_Input
    def getPass (self):
        return self.password_confirm_Input