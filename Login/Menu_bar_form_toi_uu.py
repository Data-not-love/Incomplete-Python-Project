import Controller.Order_Controller
import Login.Frame_each_food
from Login import Form_Attributes
from tkinter.ttk import Treeview
from Login.Frame_each_food import *
from tkinter import filedialog
from PIL import Image, ImageTk
from Login.Chi_tiet_order import *
import random
from Controller.Order_Controller import *
class menu1:
    def __init__(self):
        self.food_form_root = Tk()
        self.food_form_root.title("My_FAST_FOOD")
        self.food_form_root.geometry(Form_Attributes.geo2)
        self.food_form_root.configure(bg='white')
        self.food_form_root.resizable(False,False)
        self.menu_bar = Menu(self.food_form_root)
        self.food_form_root.config(menu=self.menu_bar)

        from Controller import Menu_Bar_Form_Controler, Login_Controller
            # frame chứa coffee
        self.frame_coffee = Frame(self.food_form_root, bg='white')

        self.Coffee_Label = Label(self.frame_coffee, text='COFFEE CHOICES FOR YOU', font=Form_Attributes.font1, padx=150, bg='white')
        self.Coffee_Label.grid(row=0, column=0, columnspan=5)

        Label(self.frame_coffee, text="____________________________________________________________________________________________________________________________________", bg='white').grid(row=1, column=0, columnspan=4)
        Label(self.frame_coffee, text="                                                  ", bg='white').grid(row=2, column=0, columnspan=4)
        Cappuccino = food_frame(self.frame_coffee, 'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/Cappuchino.png', 'CAPUCINNO',3,0,'#b06719',110,35.00)
        espresso = food_frame(self.frame_coffee, 'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/espresso.png', 'ESPRESSO', 3,1,'#fcb56b',120,40.00)
        black_coffee = food_frame(self.frame_coffee, 'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/black_coffee.png', 'BLACK COFFEE',3,2, '#764e23',130,25.00)
        milk_coffee = food_frame(self.frame_coffee, 'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/milk_coffee.png', 'MILK COFFEE',3,3,'#efd3a5',140,15.00)
        latte = food_frame(self.frame_coffee, 'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/latte.png', 'LATTE', 5,0,'#934f08',150,30.00)
        Label(self.frame_coffee, text="                                                  ", bg='white').grid(row=4, column=0)

        self.menu_coffee = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='COFFEE', menu=self.menu_coffee, font=Form_Attributes.font4)
        self.menu_coffee.add_command(label='All Coffee Types', font=Form_Attributes.font4, command=lambda: Menu_Bar_Form_Controler.show_frame(self.frame_coffee))
        self.menu_coffee.config(font=Form_Attributes.font4)

            # -------------------------------------------------------------------------------------------------------------------------------------------

            # frame chứa gà
        self.frame_chicken = Frame(self.food_form_root, bg='white')
        self.Chicken_Label = Label(self.frame_chicken, text="CHICKEN'S MENU FOR YOU", font=Form_Attributes.font1, padx=150, bg='white')
        self.Chicken_Label.grid(row=0, column=0, columnspan=4)

        Label(self.frame_chicken, text="____________________________________________________________________________________________________________________________________", bg='white').grid(row=1, column=0, columnspan=4)
        Label(self.frame_chicken, text="                                                  ", bg='white').grid(row=2, column=0, columnspan=4)

        teriyaki = food_frame(self.frame_chicken, 'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/grilled-teriyaki.png', 'TERIYAKI', 3, 0, '#f66b13',210,50.00)
        spicy_chicken = food_frame(self.frame_chicken, 'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/spicy-chicken.png', 'SPICY CHICKEN', 3, 1, '#ff9f38',220,45.00)
        orange_chicken = food_frame(self.frame_chicken, 'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/orange_chicken.png', 'ORANGE CHICKEN', 3, 2, '#ffb035',230,45.00)
        cheese_chicken = food_frame(self.frame_chicken, 'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/cheese-ken.png', "CHEESE CHICKEN", 3, 3, '#fcd76e',240,60.00)
        mayo_chicken = food_frame(self.frame_chicken, 'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/mayo_chicken.png', "MAYO CHICKEN", 5, 0, '#ffe084',250,65.00)
        Label(self.frame_chicken, text="                                                  ", bg='white').grid(row=4, column=0)

        self.menu_chicken = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='CHICKEN', menu=self.menu_chicken, font=Form_Attributes.font4)
        self.menu_chicken.add_command(label='Fried Chicken', font=Form_Attributes.font4, command=lambda: Menu_Bar_Form_Controler.show_frame(self.frame_chicken))

            # -----------------------------------------------------------------------------------------------------------------------------------------
            # frame trà sữa
        self.frame_boba = Frame(self.food_form_root, bg='white')
        self.boba_label = Label(self.frame_boba, text="HAVE FUN DRINKING BOBA", font=Form_Attributes.font1, padx=150, bg='white')
        self.boba_label.grid(row=0, column=0, columnspan=4)
        Label(self.frame_boba, text="____________________________________________________________________________________________________________________________________", bg='white').grid(row=1, column=0, columnspan=4)
        Label(self.frame_boba, text="                                                  ", bg='white').grid(row=2, column=0, columnspan=4)

        cherry_boba   =   food_frame(self.frame_boba,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/cherry_boba.png', "CHERRY BOBA", 3, 0, '#ffb0b0',310,15.00)
        choco_boba    =   food_frame(self.frame_boba,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/chocolate_boba.png', "CHOCOLATE BOBA",3, 1, '#965918',320,20.00)
        blue_berry_boba = food_frame(self.frame_boba,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/blue_berry_boba.png', "BLUEBERRY BOBA",3, 2, '#8e7cc3',330,25.00)
        cheese_boba   =   food_frame(self.frame_boba,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/cheese_boba.png', "CHEESE BOBA", 3,3,'#fce5cd',340,30.00)
        strawberry_boba = food_frame(self.frame_boba,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/strawberry_boba.png', "STRAWBERRY BOBA",5,0,'#e06666',350,30.00)
        Label(self.frame_boba, text="                                                  ", bg='white').grid(row=4, column=0)

        self.frame_tropical = Frame(self.food_form_root, bg='white')
        self.tropical_label = Label(self.frame_tropical, text="TROPICAL TEA IS THE BEST", font=Form_Attributes.font1, padx=150, bg='white')
        self.tropical_label.grid(row=0, column=0, columnspan=4)
        Label(self.frame_tropical, text="____________________________________________________________________________________________________________________________________", bg='white').grid(row=1, column=0, columnspan=4)
        Label(self.frame_tropical, text="                                                  ", bg='white').grid(row=2, column=0, columnspan=4)

        peach = food_frame(self.frame_tropical,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/peach_tea.png', "PEACH TEA", 3, 0, '#efb447',410,25.00)
        guava = food_frame(self.frame_tropical,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/Guava.png', "GUAVA TEA", 3, 1, '#93c47d',420,25.00)
        honey = food_frame(self.frame_tropical,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/honey_tea.png', "HONEY TEA", 3, 2, '#fcd45b',430,25.00)
        lychee = food_frame(self.frame_tropical,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/lychee.png', "LYCHEE TEA", 3, 3, '#ffe9a9',440,25.00)
        mango = food_frame(self.frame_tropical,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/mango_tea.png', "MANGO TEA", 5, 0, '#ffc000',450,25.00)
        Label(self.frame_tropical, text="                                                  ", bg='white').grid(row=4, column=0)


        self.menu_tea = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='TEA', menu=self.menu_tea, font=Form_Attributes.font4)
        self.menu_tea.add_command(label='Boba Tea', font=Form_Attributes.font4, command=lambda: Menu_Bar_Form_Controler.show_frame(self.frame_boba))
        self.menu_tea.add_separator()
        self.menu_tea.add_command(label='Tropical Tea', font=Form_Attributes.font4, command=lambda: Menu_Bar_Form_Controler.show_frame(self.frame_tropical))
        # -----------------------------------------------------------------------------------------------------------------------------
        self.frame_fruits = Frame(self.food_form_root, bg='white')
        self.fruits_label = Label(self.frame_fruits, text="FRUITS IS GOOD THE SKIN", font=Form_Attributes.font1, padx=150, bg='white')
        self.fruits_label.grid(row=0, column=0, columnspan=4)
        Label(self.frame_fruits, text="____________________________________________________________________________________________________________________________________", bg='white').grid(row=1, column=0, columnspan=4)
        Label(self.frame_fruits, text="                                                  ", bg='white').grid(row=2, column=0, columnspan=4)
        apple = food_frame(self.frame_fruits,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/apple-juice.png', "APPLE JUICE", 3, 0, '#ef5353',510,25.00)
        pineapple = food_frame(self.frame_fruits,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/pineapple.png', "PINEAPPLE JUICE", 3, 1, '#ebbf3b',520,30.00)
        kiwi = food_frame(self.frame_fruits,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/Kiwi-Juice.png', 'KIWI JUICE', 3, 2, '#8fce00',530,35.00)
        watermelon = food_frame(self.frame_fruits,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/watermelon.png', "WATERMELON JUICE", 3, 3, '#cc0000',540,20.00)
        lemon = food_frame(self.frame_fruits,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/lemon-juice.png', "LEMON JUICE", 5, 0, '#ffdb73',550,65.00)
        Label(self.frame_fruits, text="                                                  ", bg='white').grid(row=4, column=0)


        self.frame_vegetables = Frame(self.food_form_root, bg='white')
        self.vegetables_label = Label(self.frame_vegetables, text="BETTER YOUR GUT HEALTH", font=Form_Attributes.font1, padx=150, bg='white')
        self.vegetables_label.grid(row=0, column=0, columnspan=4)
        Label(self.frame_vegetables, text="____________________________________________________________________________________________________________________________________", bg='white').grid(row=1, column=0, columnspan=4)
        Label(self.frame_vegetables, text="                                                  ", bg='white').grid(row=2, column=0, columnspan=4)
        celery = food_frame(self.frame_vegetables,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/CeleryJuice.png', "CELERY JUICE", 3, 0, '#3c7d1f',610,20.00)
        carrot = food_frame(self.frame_vegetables,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/carrot-juice-recipe.png', "CARROT JUICE", 3, 1, '#c98339',620,30.00)
        tomato = food_frame(self.frame_vegetables,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/tomato.png', "TOMATO JUICE", 3, 2, '#dc4646',630,15.00)
        lectucce = food_frame(self.frame_vegetables,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/lectuce.png', "LETTUCE JUICE", 3, 3, '#306618',640,15.00)
        cucumber = food_frame(self.frame_vegetables,'F:/3.5 Years/First Year/Python/Fast_food_app/Assets/cuccumber.png', "CUCUMBER JUICE", 5, 0, '#7ab660',650,25.00)
        Label(self.frame_vegetables, text="                                                  ", bg='white').grid(row=4, column=0)

        self.menu_smoothie = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='SMOOTHIE', menu=self.menu_smoothie, font=Form_Attributes.font4)
        self.menu_smoothie.add_command(label='Fruits', font=Form_Attributes.font4, command=lambda: Menu_Bar_Form_Controler.show_frame(self.frame_fruits))
        self.menu_smoothie.add_separator()
        self.menu_smoothie.add_command(label='Vegetables', font=Form_Attributes.font4, command=lambda: Menu_Bar_Form_Controler.show_frame(self.frame_vegetables))


        # order vs cart dùng table
        self.frame_cart_detail = Frame(self.food_form_root, bg="white")
        cart_details_label = Label(self.frame_cart_detail, text="YOUR CART", font=Form_Attributes.font1, padx=150, bg='white')
        cart_details_label.grid(row=0, column=0, columnspan=4)
        Label(self.frame_cart_detail, text="                                                  ", bg='white').grid(row=1, column=0, columnspan=5)
        Bang_cart = Frame(self.frame_cart_detail, bg="white", padx=80)
        Bang_cart.grid(row=2, column=0, columnspan=4)
        self.cart_board = Treeview(Bang_cart)
        self.cart_board["columns"] = ("Food Id", "Food Name", "Quantity", "Price")
        self.cart_board.column("#0", width=0, stretch=NO)
        self.cart_board.grid(row=3, column=0, columnspan=4)
        for col in self.cart_board["columns"]:
            self.cart_board.column("Food Id",width=65)
            self.cart_board.column("Food Name", width=250)
            self.cart_board.column("Quantity", width=75)
            self.cart_board.column("Price", width=70)
            self.cart_board.heading(col, text=col)

            data = [black_coffee]
            data2 = [celery]
            data3 = [strawberry_boba]
        for item in data3:
            self.cart_board.insert("", "end", values=(
                "350",
                "CELERY",
                "1",
                "30000"))
        for item in data2:
                self.cart_board.insert("", "end", values=(
                    "610",
                    "CELERY",
                    "1",
                    "20000"))

        for item in data:
            self.cart_board.insert("", "end",values=(
                                "130",
                                "BLACK COFFEE",
                                "1",
                                "25000"))
            scrollbar = Scrollbar(self.frame_cart_detail, orient="vertical", command=self.cart_board.yview())
        Label(self.frame_cart_detail, text="                                                  ", bg='white').grid(row=4, column=0, columnspan=4)



        self.Frame_nut_cart = Frame(self.frame_cart_detail, padx=180, bg='white')
        self.Frame_nut_cart.grid(row=5, column=0)
        self.Button_mua_all = Button(self.Frame_nut_cart, text="Buy all", width=12,command=lambda:Order_Controller.lay_dia_chi())
        self.Button_mua_all.grid(row=0, column=0)
        self.Button_huy_all = Button(self.Frame_nut_cart, text="Cancel all", width=12)
        self.Button_huy_all.grid(row=0, column=1)
        self.Button_buy_specific = Button(self.Frame_nut_cart, text="Buy specific", width=12)
        self.Button_buy_specific.grid(row=0, column=2)
        self.Button_cancel_specific = Button(self.Frame_nut_cart, text="Cancel specific", width=12)
        self.Button_cancel_specific.grid(row=0, column=3)

        menu_receipt = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='CART', menu=menu_receipt, font=Form_Attributes.font4)
        menu_receipt.add_command(label='Receipt PDF', font=Form_Attributes.font4)
        menu_receipt.add_separator()
        menu_receipt.add_command(label='Cart Details', font=Form_Attributes.font4, command=lambda: Menu_Bar_Form_Controler.show_frame(self.frame_cart_detail))

            # xong log out
        menu_Log_out = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='LOG OUT', menu=menu_Log_out, font=Form_Attributes.font4)
        menu_Log_out.add_command(label='Log out', font=Form_Attributes.font4, command=lambda: Menu_Bar_Form_Controler.quit_app(self.food_form_root))
        menu_Log_out.add_separator()
        menu_Log_out.add_command(label='Sign In with Another Account', font=Form_Attributes.font4, command=lambda: Login_Controller.call_sign_in_main_app(self))


        # -----------------------------------------------------------------------------------------------------------------------------
        self.frame_nut = Frame(self.food_form_root, bg=Form_Attributes.bg_xanh)
        self.frame_nut.grid(row=0, column=0)

            # padx,pady : thiết lập khoảng cách giữa lề or widget
        frame_Account = Frame(self.food_form_root, bg='white')
        self.Button_Account = Button(self.frame_nut, text='ACCOUNT', font=Form_Attributes.font4, width=24, height=9, bg=Form_Attributes.bg_xanh, command=lambda: Menu_Bar_Form_Controler.show_frame(frame_Account))
        Label_Profile = Label(frame_Account,text='      CUSTOMER PROFILE', font=Form_Attributes.font1, padx=150, bg="white")
        Label_Profile.grid(row=0, column=0, columnspan=5)
        Label(frame_Account,text="                                                  ", bg='white').grid(row=1, column=0, columnspan=5)

        def show_image():
            self.file_name = filedialog.askopenfilename()
            self.mo_file = Image.open(self.file_name)
            self.width,self.heigth = self.mo_file.size
            if self.file_name and self.width >= 151 and self.heigth >= 151:
                messagebox.showerror('Error','Image is too big.Choose an image that no more than 150px')
            else:
                self.image_directory = ImageTk.PhotoImage(self.mo_file)  # Sửa ở đây
                self.label_image = Label(self.frame_hien_anh,image=self.image_directory,background='white')
                self.label_image.grid(row=0,column=0)
        self.frame_hien_anh = Frame(frame_Account, background='black', height=100, width=100)
        self.frame_hien_anh.grid(row=2,column=2)
        self.Button_chon_anh = Button(frame_Account,width=15,text='CHOOSE IMAGE',command=lambda :show_image())
        self.Button_chon_anh.grid(row=3,column=2)
        Label(frame_Account,text='               ___________________________________________________________________________________________________________________',background='white').grid(row=4,column=0,columnspan=5)
        Label(frame_Account,text='                                                                        ', background='white').grid(row=5, column=0, columnspan=5)
        self.Label_ten_user = Label(frame_Account,width=30,background='gray',text='@UserName',height=3)
        self.Label_ten_user.grid(row=6,column=2)
        self.Label_Email = Label(frame_Account,width=30,background='gray',text='Email',height=3)
        self.Label_Email.grid(row=6, column=3)

        Label(frame_Account, text='                                                                        ', background='white').grid(row=7, column=0, columnspan=5)

        self.Label1 = Label(frame_Account,width=30,background='gray',text='DD/MM/YYYY',height=3)
        self.Label1.grid(row=9,column=2)

        Label(frame_Account, text='                                                                        ', background='white').grid(row=10, column=0, columnspan=5)

        self.Label2 = Label(frame_Account,width=30,background='gray',text='Address',height=3)
        self.Label2.grid(row=11,column=2)






        self.Button_Account.grid(row=0, column=0)

        self.Button_Gio_hang = Button(self.frame_nut, text='YOUR ORDER', font=Form_Attributes.font4, width=24, height=3, bg=Form_Attributes.bg_xanh, command=lambda: Menu_Bar_Form_Controler.show_frame(frame_order))
        self.Button_Gio_hang.grid(row=1, column=0)
        frame_order = Frame(self.food_form_root, bg="white")
        Label_gio_hang = Label(frame_order, text="THIS IS THE CURRENT ORDER", font=Form_Attributes.font1, padx=150, bg="white")
        Label_gio_hang.grid(row=0, column=0, columnspan=2)
        Label(frame_order, text="                                                  ", bg='white').grid(row=1, column=0, columnspan=2)
        Bang_order = Frame(frame_order, bg="white", padx=80)
        Bang_order.grid(row=2, column=0)

        order_board = Treeview(Bang_order)
        order_board["columns"] = ("Id", "Details", "Total Price", "Date","Address", "State")
        order_board.column("#0", width=0, stretch=NO)
        # Set column widths

        order_board.grid(row=3, column=0)
        for col in order_board["columns"]:
            order_board.column("Id", width=50)
            order_board.column("Details", width=130)
            order_board.column("Total Price", width=70)
            order_board.column("Date", width=80)
            order_board.column("Address", width=150)
            order_board.column("State", width=70)
            #order_board.column(col, width=100)
            order_board.heading(col, text=col)
        data = [peach]
        data1 = [choco_boba]
        data2 =[tomato]
        for i in data:
            order_board.insert("", "end",
                               values=(str(random.randint(100000,999999)),
                                "PEACH TEA",
                                "25000" ,
                                "10/06/2024",
                                "28 Huynh Van Nghe, Ngu Hanh Son",
                                "Incomplete"
                                       ))
        for i in data1:
            order_board.insert("", "end",
                               values=(str(random.randint(100000, 999999)),
                                       "CHOCOLATE BOBA",
                                       "20000",
                                       "11/06/2024",
                                       "28 Huynh Van Nghe, Ngu Hanh Son",
                                       "Incomplete"
                                       ))
        for i in data2:
            order_board.insert("", "end",
                               values=(str(random.randint(100000, 999999)),
                                       "TOMATO JUICE",
                                       "15000",
                                       "20/06/2024",
                                       "28 Huynh Van Nghe, Ngu Hanh Son",
                                       "Incomplete"
                                       ))
            scrollbar = Scrollbar(frame_order, orient="vertical", command=order_board.yview())
        Label(frame_order, text="                                                  ", bg='white').grid(row=4, column=0, columnspan=3)

        Frame_nut_order = Frame(frame_order, padx=180, bg='white')
        Frame_nut_order.grid(row=5, column=0)
        Button_mua = Button(Frame_nut_order, text="Buy", width=12)
        Button_mua.grid(row=0, column=0)
        Button_huy = Button(Frame_nut_order, text="Cancel Order", width=12)
        Button_huy.grid(row=0, column=1)
        Button_change_address = Button(Frame_nut_order, text="Change Address", width=12)
        Button_change_address.grid(row=0, column=2)

            # xong policy
        Button_Policy = Button(self.frame_nut, text='MY POLICY', font=Form_Attributes.font4, width=24, height=3, bg=Form_Attributes.bg_xanh, command=lambda: Menu_Bar_Form_Controler.show_frame(frame_policy))
        Button_Policy.grid(row=2, column=0)
            # Tạo Frame để chứa nội dung của Policy
        frame_policy = Frame(self.food_form_root, bg=Form_Attributes.bg_xanh)
        policy_label = Label(frame_policy, text=Form_Attributes.text_policy, font=Form_Attributes.font5, bg=Form_Attributes.bg_white)
        policy_label.pack()

        Button_order_history = Button(self.frame_nut, text='ORDERS  HISTORY', font=Form_Attributes.font4, width=24, height=3, bg=Form_Attributes.bg_xanh, command=lambda: Menu_Bar_Form_Controler.show_frame(frame_order_history))
        Button_order_history.grid(row=3, column=0)
        frame_order_history = Frame(self.food_form_root, bg="white")
        Label_order_history = Label(frame_order_history, text="YOUR ORDER HISTORY", font=Form_Attributes.font1, padx=150, bg="white")
        Label_order_history.grid(row=0, column=0)
        Label(frame_order_history, text="                                                  ", bg='white').grid(row=1, column=0)
        Bang_order_history = Frame(frame_order_history, bg="white", padx=80)
        Bang_order_history.grid(row=2, column=0)

        order_history_board = Treeview(Bang_order_history)
        order_history_board["column"] = ("Id", "Details", "Total Price","Date" ,"Address", "State")
        order_history_board.column("#0", width=0, stretch=NO)
        order_history_board.grid(row=3, column=0)
        for col in order_history_board["columns"]:
            order_history_board.column("Id", width=50)
            order_history_board.column("Details", width=200)
            order_history_board.column("Total Price", width=70)
            order_history_board.column("Date", width=70)
            order_history_board.column("Address", width=150)
            order_history_board.column("State", width=70)
            order_history_board.heading(col, text=col)


        for i in range(6):
            order_history_board.insert("", "end",
                                       values=(str(random.randint(100000,999999)),
                                       "Details" + str(i + 1),
                                       "Total Price" + str(i + 1),
                                       "Address" + str(i + 1),
                                       "State" + str(i + 1)))
            scrollbar = Scrollbar(frame_order_history, orient="vertical", command=order_history_board.yview())
        Label(frame_order_history, text="                                                  ", bg='white').grid(row=4, column=0, columnspan=3)



        Frame_lsmh = Frame(frame_order_history, padx=180, bg='white')
        Frame_lsmh.grid(row=5, column=0)
        Button_mua_lai = Button(Frame_lsmh, text="Re-purchase", width=12)
        Button_mua_lai.grid(row=0, column=0)
        self.Button_canceled = Button(self.frame_nut, text='CANCELLED  ORDERS', font=Form_Attributes.font4, width=24, height=3, bg=Form_Attributes.bg_xanh, command=lambda: Menu_Bar_Form_Controler.show_frame(frame_cancelled_order))
        self.Button_canceled.grid(row=4, column=0)
        frame_cancelled_order = Frame(self.food_form_root, bg="white")
        Label_cancel_order = Label(frame_cancelled_order, text="THE CANCELLED ORDERS", font=Form_Attributes.font1, padx=150, bg="white")
        Label_cancel_order.grid(row=0, column=0)
        Label(frame_cancelled_order, text="                                                  ", bg='white').grid(row=1, column=0)
        Bang_cancel_order = Frame(frame_cancelled_order, bg="white", padx=80)
        Bang_cancel_order.grid(row=2, column=0)
        cancel_board = Treeview(Bang_cancel_order)
        cancel_board["columns"] = ("Id", "Details", "Total Price","Date", "Address", "State")
        cancel_board.column("#0", width=0, stretch=NO)
        cancel_board.grid(row=3, column=0)
        for col in cancel_board["columns"]:
            cancel_board.column("Id", width=50)
            cancel_board.column("Details", width=200)
            cancel_board.column("Total Price", width=70)
            cancel_board.column("Date", width=70)
            cancel_board.column("Address", width=150)
            cancel_board.column("State", width=70)
            cancel_board.heading(col, text=col)

        for i in range(6):
            cancel_board.insert("", "end",
                                values=(str(random.randint(100000,999999)),
                                        "Details" + str(i + 1),
                                        "Total Price" + str(i + 1),
                                        "Address" + str(i + 1),
                                        "State" + str(i + 1)))
            scrollbar = Scrollbar(frame_cancelled_order, orient="vertical", command=cancel_board.yview())
        Label(frame_cancelled_order, text="                                                  ", bg='white').grid(row=4, column=0, columnspan=3)
        self.Frame_mua_lai = Frame(frame_cancelled_order, padx=180, bg='white')
        self.Frame_mua_lai.grid(row=5, column=0)
        self.Button_mua_lai = Button(self.Frame_mua_lai, text="Re-purchase cancelled order")
        self.Button_mua_lai.grid(row=0, column=0)
        self.food_form_root.mainloop()
    def destroy_main_menu(self):
        self.food_form_root.destroy()

    @property
    def Label_ten_user(self):
        return self._Label_ten_user

    @Label_ten_user.setter
    def Label_ten_user(self, value):
        self._Label_ten_user = value

    # Getter và Setter cho Label_Email
    @property
    def Label_Email(self):
        return self._Label_Email

    @Label_Email.setter
    def Label_Email(self, value):
        self._Label_Email = value

    # Getter và Setter cho Label1
    @property
    def Label1(self):
        return self._Label1

    @Label1.setter
    def Label1(self, value):
        self._Label1 = value

    # Getter và Setter cho Label2
    @property
    def Label2(self):
        return self._Label2

    @Label2.setter
    def Label2(self, value):
        self._Label2 = value

    def update_user_info(self, username,email,dob,address):
        # Assuming user_info is a tuple with (username, email, dob, ...)
        self.Label_ten_user.config(text=username)  # Username
        self.Label_Email.config(text=email)  # Email
        self.Label1.config(text=dob)  # Date of Birth
        self.Label2.config(text=address)
