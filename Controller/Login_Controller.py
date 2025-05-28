import random
from tkinter import messagebox

import DataBase.Database_Attributes
import Login.User_for_app
from Model import Connect_Database
# import trong hàm để tránh việc import vòng trong python
# import Login.Sign_Up : import module
# from Login import Sign_Up : import lớp cụ thể của Module đó
def call_sign_in_main_app(destroy_main_app_instance):
    destroy_main_app_instance.destroy_main_menu()
    import View.main
    View.main.my_main_login
def call_sign_in_Sign_up(destroy_main_app_instance):
    destroy_main_app_instance.destroy_Sign_Up()
    import View.main
    View.main.my_main_login

# đón sign_in sau khi nhấn Sign_Up
def call_sign_up (destroy_sign_in_instance):
    destroy_sign_in_instance.destroy_Sign_In()
    from Login.Sign_Up import Sign_Up_app
    my_sign_up = Sign_Up_app()
def call_forget_pass (destroy_sign_in_instance):
    destroy_sign_in_instance.destroy_Sign_In()
    from Login.Forget_Pass import Forgot_pass_window
    main_forget_pass = Forgot_pass_window()
# run != Popen
# run phải chạy xong tác vụ thì mới đc hủy , ko thi máy shut down chậm .Popen thì ngược lại
def remove_string_enter (event,widget, default_text):
    widget.delete(0,'end')

def refill_string_enter (event,widget, default_text):
    if not widget.get():
        widget.insert(0, default_text)



# hàm kiểm tra Sign_Up trong Sign_Up
def create_account (widget1,widget2,widget3,widget4,destroy_main_app_instance):
    user_Name = widget1.get()
    pass_word = widget2.get()
    re_enter_pass = widget3.get()
    email = widget4.get()

# vì các hàng insert ở Sign_Up luôn chèn string nên phải loại bỏ string đó ra
    if user_Name == '' or user_Name == 'UserName' or pass_word == '' or pass_word == 'Password' or re_enter_pass == '' or re_enter_pass == 'Re_Enter Password' or email == '' or email == 'Email':
        messagebox.showerror("Not enough info","Please provide enough info")
    elif pass_word != re_enter_pass:
        messagebox.showerror("Error","Password do not match")
    elif pass_word == re_enter_pass and (user_Name != '' or user_Name != 'UserName'):
        address = 'Đà Nẵng'
        Id = random.randint(10000, 99999)

        dob = '2003-04-03'
        user = Login.User_for_app.User(Id,user_Name, pass_word, email,  dob, address)

        val_dang_ky = (user.UserID, user.UserName, user.PassWord, user.Email, user.BirthDay, user.Address)

        try:
                Connect_Database.my_cursor.execute(Connect_Database.sql_dang_ky, val_dang_ky)
                #lưu tên người dùng
                DataBase.Database_Attributes.db.commit()
                messagebox.showinfo("Successfully","You've created an account")
                # viết hàm mở cửa sổ sign IN
                destroy_main_app_instance.destroy_Sign_Up()
                import View.main
                View.main.my_main_login
        except Exception as e:
            print("Error", f" {e}")


def reset_password(user_name, password, password_reenter, destroy_main_app_instance):
    username = user_name.get()
    password_1 = password.get()
    password_2 = password_reenter.get()

    val_reset = (password_1,username)
    if password_1 != password_2 and not (username == '' or username == 'Enter UserName' or password_1 == '' or password_1 == 'Enter New Password' or password_2 == '' or password_2 == 'Re Enter New Password'):
        # in messagebox error ra
        messagebox.showerror("Error", "Passwords do not match")
    if username == '' or username == 'Enter UserName' or password_1 == '' or password_1 == 'Enter New Password' or password_2 == '' or password_2 == 'Re Enter New Password':
        messagebox.showerror("Error", "Please provide info")
    if password_1 == password_2 and (username != '' or username != 'Enter UserName'):
        try:
            Connect_Database.my_cursor.execute(Connect_Database.sql_reset_pass,val_reset)
            DataBase.Database_Attributes.db.commit()
            # in messagebox thành công
            messagebox.showinfo("Successfully reset password", "Welcome back!")
            # mở của sổ sign up
            # import View.Forget_Pass
            # View.Forget_Pass.main_forget_pass.destroy_forget_pass()

            destroy_main_app_instance.destroy_forget_pass()
            import View.main
            View.main.my_main_login
        except Exception as e:
            print("Error", f" {e}")


def check_Sign_In (widget_user,widget_pass,sign_In_Instance):
    username = widget_user.get()
    password = widget_pass.get()
    val = (username, password)
# so sánh username vs password có trùng trong cơ sở dữ liệu không
    if username == "" or password == "":
        messagebox.showerror("Error", "Please provide enough info")
    else:
        try:

            address = Connect_Database.my_cursor.execute(Connect_Database.sql_dang_nhap, val)
            query_result = Connect_Database.my_cursor.fetchall()
            if query_result:

                messagebox.showinfo("Success", "Login successful!")
                from Login.Menu_bar_form_toi_uu import menu1

                sign_In_Instance.destroy_Sign_In()
                app_chinh = menu1()

                # Close the Sign In window
                # làm Sign_In biến mất sau khi đăng nhập thành công.Lỗi pyimage xảy ra vì python chỉ xử lý 1 file 1 lần
                # ko xử lý đc 2 file cùng lúc
                return username
            else:
                messagebox.showerror("Error", "Invalid username or password")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# sai  thì ở lại show ra messagebox
# gọi các file đã được định nghĩa




