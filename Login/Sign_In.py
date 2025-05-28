from tkinter import *
from Login.Form_Attributes import *
class my_sign_In:
    def __init__(self):
        # tạo của sổ vs Tk()
        self.Sign_In_root = Tk()
        self.Sign_In_root.title('LOGIN')
        self.Sign_In_root.geometry("850x450")
        # configure : thay đổi thuộc tính của widget sau khi đã tạo ra
        self.Sign_In_root.configure(bg="#fff")
        self.Sign_In_root.resizable(False,False)
        try:
            self.sign_in_image = PhotoImage(file='F:/3.5 Years/First Year/Python/Fast_food_app/Assets/login.png')
            self.Label_Imange = Label(self.Sign_In_root, image=self.sign_in_image, bg=bg_white)
            self.Label_Imange.place(x=50, y=50)
        except Exception as e:
            print(f"Error : {e}")


        # đặt container Frame vào trong root và đặt vào vị trí
        self.frame = Frame(self.Sign_In_root,width=350, height=350, bg=bg_white)
        self.frame.place(x=480, y=70)

        # đặt heading vào frame thì chỉ có thể di chuyển trong frame
        self.heading_Sign_In = Label(self.frame, text='  LOGIN', fg=fg1, bg=bg_white, font=font1)
        self.heading_Sign_In.place(x=100, y=5)

        Label(self.frame,text='__________________________________________________________',height=1,background='white').place(x=25, y=90)
        Label(self.frame, text='__________________________________________________________', height=1, background='white').place(x=25, y=160)

        # chỉ import khi cần để tránh import vòng
        from Controller import Login_Controller
        self.Username_Input = Entry(self.frame, width=25, fg='black', border=border, bg=bg_white, font=font2)
        self.Username_Input.place(x=30,y=80)
        self.Username_Input.insert(0,'UserName')
        self.Username_Input.bind('<FocusIn>', lambda event:Login_Controller.remove_string_enter(event,self.Username_Input,'UserName'))
        self.Username_Input.bind('<FocusOut>', lambda event:Login_Controller.refill_string_enter(event,self.Username_Input,'UserName'))


        self.Password_Input = Entry(self.frame, width=25, fg='black', border=border, bg=bg_white, font=font2)
        self.Password_Input.place(x=30, y=150)
        self.Password_Input.insert(0, 'Password')
        self.Password_Input.bind('<FocusIn>', lambda event:Login_Controller.remove_string_enter(event, self.Password_Input, 'Password'))
        self.Password_Input.bind('<FocusOut>', lambda event:Login_Controller.refill_string_enter(event, self.Password_Input, 'Password'))

        self.Sign_In_Button = Button(self.frame, width=39, pady=7, text='Sign In', bg=fg1, fg='white', border=0, command=lambda:Login_Controller.check_Sign_In(self.Username_Input, self.Password_Input,self))
        self.Sign_In_Button.place(x=35,y=200)

        self.Sign_up_Button = Button(self.frame, width=6, text='No account ?  Sign Up ', border=border, bg=bg_white, cursor='hand2', fg=fg1, padx=117, command=lambda:Login_Controller.call_sign_up(self))
        # command=lambda event:Login_Controller.No_Account_Sign_Up_Clicked())
        self.Sign_up_Button.place(x=35,y=245)

        self.Forgot_Pass_Button = Button(self.frame, width=6, text="Forgot Password ?", border=border, bg=bg_white, cursor='hand2', fg=fg1, padx=117, command=lambda:Login_Controller.call_forget_pass(self))
        self.Forgot_Pass_Button.place(x=35,y=276)

        self.Sign_In_root.mainloop()

    def destroy_Sign_In(self):
        self.Sign_In_root.destroy()









