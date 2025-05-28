from tkinter import *
from Login.Form_Attributes import *
import ast

sign_up_window = Tk()
sign_up_window.title('Sign Up')
sign_up_window.geometry(geo)
sign_up_window.configure(bg="#fff")
# ko cho cửa số Login kéo giãn kích thước
sign_up_window.resizable(False, False)


def Sign_In():
    pass
def signup ():
    username = user.get()
    password_1st = password.get()
    password_check = password_confirm.get()

    if password_check == password_1st:
        pass



img = PhotoImage (file=file_img_2)
label_image = Label(sign_up_window, image=img, bg=bg_white)
label_image.place(x=50, y=90)


frame = Frame(sign_up_window, width=350, height=380, bg=bg_white)
frame.place(x=480, y=50)

heading = Label(frame, text='Sign up', fg=fg1, bg=bg_white, font=font1 )
heading.place(x=100, y=5)
#--------------------------------------------------------------------------------
def on_enter (e):
    user.delete(0,'end')
def on_leave (e):
    name = user.get()
    if name == '':
        user.insert(0, 'UserName')

user = Entry(frame, width=25, fg='black', border=border, bg=bg_white, font=font2)
user.place(x=30, y=80)
user.insert(0, "UserName")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame (frame, width=295, height=2, bg='black').place ( x=25, y=107)
#---------------------------------------------
def on_enter_pass (e):
    password.delete(0,'end')
def on_leave_pass (e):
    pass_word = password.get()
    if pass_word == '':
        user.insert(0, 'Password')

password = Entry(frame, width=25, fg='black', border=border, bg=bg_white, font=font2 )
password.place(x=30, y=150)
password.insert(0, "Password")
password.bind('<FocusIn>', on_enter_pass)
password.bind('<FocusOut>', on_leave_pass)

Frame (frame, width=295, height=2, bg='black').place ( x=25, y=177 )

#--------------------------------------------------------------------------------
def on_enter_pass_confirm (e):
    password_confirm.delete(0,'end')
def on_leave_pass_confirm (e):
    pass_word_confirm = user.get()
    if pass_word_confirm == '':
        user.insert(0, 'Re Enter Password')

password_confirm = Entry(frame, width=25, fg='black', border=border, bg=bg_white, font=font2)
password_confirm.place(x=30, y=220)
password_confirm.insert(0, "Re Enter Password")
password_confirm.bind('<FocusIn>', on_enter_pass_confirm)
password_confirm.bind('<FocusOut>', on_leave_pass_confirm)

Frame (frame, width=295, height=2, bg='black').place ( x=25, y=247 )
#-----------------------------------------------------------------------------------
Button_Sign_Up = Button(frame, width=39, pady=7, text='Sign Up', bg=fg1, fg='white', border=border, command=signup)
Button_Sign_Up.place(x=35, y=280)


sign_in = Button(frame,width=6, text='Already have an account ?  Sign In', border=border, bg=bg_white,cursor='hand2',fg=fg1, padx=120)
sign_in.place(x=30, y=340)


sign_up_window.mainloop()