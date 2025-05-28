from tkinter import *
from tkinter import messagebox
from Login.Form_Attributes import *


root_Login = Tk()
root_Login.title('Sign In')
root_Login.geometry('925x500+300+200')
root_Login.configure(bg="#fff")
root_Login.resizable(False, False)

# ở phương thức sign in này (Tạo thêm Sign Up form, rồi đưa vào trong hàm này
def Forget_Password():
    pass

def signin():
    username = user_Input.get()
    pass_word = password_Input.get()
    if username == 'admin' and pass_word == '1234':
        screen = Toplevel(root_Login)
        screen.title ("App")
        screen.geometry('925x500+300+200')
        screen.configure(bg="white")


        Label(screen,text='Hello Nigga',bg='#fff', font=font3).pack(expand=True)
        screen.mainloop()
    elif username != 'admin' or pass_word != '1234' or pass_word == '':
        messagebox.showerror("INVALID", "INCORRECT USERNAME or PASSWORD")
    elif username != 'admin' and pass_word != '1234':
        messagebox.showerror("INVALID","RE ENTER AGAIN")



img = PhotoImage(file=file_img)
Label(root_Login, image=img, bg=bg_white).place(x=50, y=50)

# container bên trong root window
frame = Frame(root_Login, width=350, height=350, bg=bg_white)
frame.place(x=480, y=70)

# đặt Heading trong frame
heading = Label(frame, text='Sign In', fg=fg1, bg=bg_white, font=font1)
heading.place(x=100, y=5)
#----------------------------------------------------------------------------------------------------------------------------


# xóa chuỗi tên user name khi click chuột vào o
def on_enter (e):
    user_Input.delete(0,'end')
def on_leave (e):
    name = user_Input.get()
    if name == '':
        user_Input.insert(0, 'UserName')
# đặt trường nhập văn bản Entry vào
user_Input= Entry(frame, width=25, fg='black', border=border, bg=bg_white, font=font2)
user_Input.place(x= 30,y= 80)
user_Input.insert(0,'Username')
user_Input.bind('<FocusIn>', on_enter)
user_Input.bind('<FocusOut>', on_leave)



Frame (frame, width=295, height=2, bg='black').place(x=25, y=107)

#---------------------------------------------------------------------------
def on_enter_pass (e):
    password_Input.delete(0, 'end')

def on_leave_pass (e):
    refill_password = password_Input.get()
    if refill_password == '':
        password_Input.insert(0, 'Password')


password_Input = Entry(frame,width=25,fg='black',border=border,bg=bg_white, font=font2)
password_Input.place(x= 30,y= 150)
password_Input.insert(0,'Password')
password_Input.bind('<FocusIn>', on_enter_pass)
password_Input.bind('<FocusOut>', on_leave_pass)

Frame ( frame,width=295, height=2,bg='black').place(x=25, y=177)

#---------------------------------------------------------------------------------------
Sign_In_Button = Button(frame, width=39 ,pady=7, text='Sign In', bg=fg1,fg='white',border=0, command=signin)
Sign_In_Button.place(x=35,y=200)


sign_up_Button = Button(frame, width=6, text='No account ?  Sign Up ', border=border, bg=bg_white, cursor='hand2', fg=fg1, padx=117)
sign_up_Button.place(x=35,y=245)

forgot_Pass_Button = Button(frame, width=6, text="Forget Password ?", border=border, bg=bg_white, cursor='hand2', fg=fg1, padx=117 , command=Forget_Password)
forgot_Pass_Button.place(x=35, y=276)


root_Login.mainloop()# main Loop để theo dõi cursor của chuột