from tkinter import *
from Login import Form_Attributes
from tkinter.ttk import Treeview

class menu:
    def __init__(self):
        self.food_form_root = Tk()
        self.food_form_root.title("Food Choices")
        self.food_form_root.geometry(Form_Attributes.geo2)
        self.food_form_root.configure(bg='white')
        self.food_form_root.resizable(False,False)
        self.menu_bar = Menu(self.food_form_root)
        self.food_form_root.config(menu=self.menu_bar)

        from Controller import Menu_Bar_Form_Controler, Login_Controller, Order_Controller
        # frame chứa coffee
        self.frame_coffee = Frame(self.food_form_root, bg='white')

        self.Coffee_Label = Label(self.frame_coffee, text='COFFEE CHOICES FOR YOU', font=Form_Attributes.font1, padx=150, bg='white')
        self.Coffee_Label.grid(row=0,column=0, columnspan=4)

        Label(self.frame_coffee, text="                                                  ", bg='white').grid(row=1, column=0, columnspan=4)

        self.capuchinno_image = PhotoImage(file=Form_Attributes.file_image_cappuchino)
        self.frame_cappuchinno = Frame(self.frame_coffee, height=185, width=155, bg='#b06719')
        self.Label_cappuchino = Label (self.frame_cappuchinno, image=self.capuchinno_image)
        self.Label_cappuchino.grid(row=0,column=0,columnspan=2)
        self.Heading_Cappuchino = Label (self.frame_cappuchinno, text="CAPPUCCINO", bg='#b06719')
        self.Heading_Cappuchino.grid(row=1, column=0,columnspan=2)
        self.Button_mua_cappuchinno = Button(self.frame_cappuchinno, text="BUY NOW  !")
        self.Button_mua_cappuchinno.grid(row=2, column=0)
        self.Button_add_cart_cappuchino = Button(self.frame_cappuchinno, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_Cappuchino))
        self.Button_add_cart_cappuchino.grid(row=2, column=1)
        self.frame_cappuchinno.grid(row=2,column=0)

        self.eppresso_image = PhotoImage(file=Form_Attributes.file_image_espresso)
        self.frame_eppresso = Frame(self.frame_coffee, height=185, width=155, bg='#fcb56b')
        self.Label_espresso = Label (self.frame_eppresso, image=self.eppresso_image)
        self.Label_espresso.grid(row=0, column=0,columnspan=2)
        self.Heading_Espresso = Label(self.frame_eppresso, text="ESPRESSO", bg='#fcb56b')
        self.Heading_Espresso.grid(row=1, column=0,columnspan=2)
        self.Button_mua_Espresso = Button(self.frame_eppresso, text="BUY NOW  !")
        self.Button_mua_Espresso.grid(row=2, column=0)
        self.Button_add_eppresso = Button(self.frame_eppresso, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_Espresso))
        self.Button_add_eppresso.grid(row=2, column=1)
        self.frame_eppresso.grid(row=2,column=1)

        self.black_coffee_image = PhotoImage(file=Form_Attributes.file_image_black_coffee)
        self.frame_black_coffee = Frame(self.frame_coffee, height=185, width=155, bg='#764e23')
        self.Label_black_coffee = Label(self.frame_black_coffee, image=self.black_coffee_image)
        self.Label_black_coffee.grid(row=0, column=0,columnspan=2)
        self.Heading_Black_coffee = Label(self.frame_black_coffee, text="BLACK COFFEE", bg='#764e23')
        self.Heading_Black_coffee.grid(row=1, column=0,columnspan=2)
        self.Button_mua_black_coffee = Button(self.frame_black_coffee, text="BUY NOW  !")
        self.Button_mua_black_coffee.grid(row=2, column=0)
        self.Button_add_black = Button(self.frame_black_coffee, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_Black_coffee))
        self.Button_add_black.grid(row=2, column=1)
        self.frame_black_coffee.grid(row=2,column=2)

        self.milk_coffee_image = PhotoImage(file=Form_Attributes.file_image_milk_coffee)
        self.frame_milk = Frame(self.frame_coffee, height=185, width=155, bg='#efd3a5')
        self.Label_milk_coffee = Label(self.frame_milk, image=self.milk_coffee_image)
        self.Label_milk_coffee.grid(row=0, column=0,columnspan=2)
        self.Heading_Milk_coffee = Label(self.frame_milk, text="MILK COFFEE", bg='#efd3a5')
        self.Heading_Milk_coffee.grid(row=1, column=0,columnspan=2)
        self.Button_mua_milk_coffee = Button(self.frame_milk, text="BUY NOW  !")
        self.Button_mua_milk_coffee.grid(row=2, column=0)
        self.Button_add_milk_coffee = Button(self.frame_milk, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_Milk_coffee))
        self.Button_add_milk_coffee.grid(row=2, column=1)
        self.frame_milk.grid(row=2,column=3)

        Label(self.frame_coffee, text="                                                  ", bg='white').grid(row=3, column=0)
        self.latte_image = PhotoImage(file=Form_Attributes.file_image_latte)
        self.frame_latte = Frame(self.frame_coffee, height=185, width=155, bg='#934f08')
        self.Label_latte = Label(self.frame_latte, image=self.latte_image)
        self.Label_latte.grid(row=0, column=0,columnspan=2)
        self.Heading_latte = Label(self.frame_latte, text="LATTE", bg='#934f08')
        self.Heading_latte.grid(row=1, column=0,columnspan=2)
        self.Button_mua_latte = Button(self.frame_latte, text="BUY NOW  !")
        self.Button_mua_latte.grid(row=2, column=0)
        self.Button_add_latte = Button(self.frame_latte, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_latte))
        self.Button_add_latte.grid(row=2, column=1)
        self.frame_latte.grid(row=4, column=0)

        self.menu_coffee = Menu (self.menu_bar,tearoff=0)
        self.menu_bar.add_cascade(label='COFFEE', menu=self.menu_coffee, font=Form_Attributes.font4)
        self.menu_coffee.add_command(label='All Coffee Types', font=Form_Attributes.font4, command=lambda:Menu_Bar_Form_Controler.show_frame(self.frame_coffee))
        self.menu_coffee.config(font=Form_Attributes.font4)
        # -------------------------------------------------------------------------------------------------------------------------------------------

        # frame chứa gà
        self.frame_chicken = Frame(self.food_form_root, bg='white')
        self.Chicken_Label = Label(self.frame_chicken, text="CHICKEN'S MENU FOR YOU", font=Form_Attributes.font1, padx=150, bg='white')
        self.Chicken_Label.grid(row=0, column=0, columnspan=4)
        Label(self.frame_chicken, text="                                                  ", bg='white').grid(row=1, column=0, columnspan=4)

        self.teriyaki_image = PhotoImage(file=Form_Attributes.file_image_teryaki)
        self.frame_teriyaki = Frame(self.frame_chicken, height=185, width=155, bg='#f66b13')
        self.Label_teriyaki = Label(self.frame_teriyaki, image=self.teriyaki_image)
        self.Label_teriyaki.grid(row=0, column=0,columnspan=2)
        self.Heading_Teriyaki = Label(self.frame_teriyaki, text="TERIYAKI", bg='#f66b13')
        self.Heading_Teriyaki.grid(row=1, column=0,columnspan=2)
        self.Button_mua_teriyaki = Button(self.frame_teriyaki, text="BUY NOW  !")
        self.Button_mua_teriyaki.grid(row=2, column=0)
        self.Button_add_teriyaki = Button(self.frame_teriyaki, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_Teriyaki))
        self.Button_add_teriyaki.grid(row=2, column=1)
        self.frame_teriyaki.grid(row=2,column=0)

        self.spicy_chick_image = PhotoImage(file=Form_Attributes.file_spicy_chick_image)
        self.frame_spicy_chick = Frame(self.frame_chicken, height=185, width=155, bg='#ff9f38')
        self.Label_spicy_chick = Label(self.frame_spicy_chick, image=self.spicy_chick_image)
        self.Label_spicy_chick.grid(row=0, column=0,columnspan=2)
        self.Heading_spicy_chick = Label(self.frame_spicy_chick, text="SPICY CHICKEN", bg='#ff9f38')
        self.Heading_spicy_chick.grid(row=1, column=0,columnspan=2)
        self.Button_mua_spicy_chicken = Button(self.frame_spicy_chick, text="BUY NOW  !")
        self.Button_mua_spicy_chicken.grid(row=2, column=0)
        self.Button_add_spicy_chicken = Button(self.frame_spicy_chick, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_spicy_chick))
        self.Button_add_spicy_chicken.grid(row=2, column=1)
        self.frame_spicy_chick.grid(row=2,column=1)

        self.orange_chicken_image = PhotoImage(file=Form_Attributes.file_image_orange_chicken)
        self.frame_orange_chicken = Frame(self.frame_chicken, height=185, width=155, bg='#ffb035')
        self.Label_orange_chicken = Label(self.frame_orange_chicken, image=self.orange_chicken_image)
        self.Label_orange_chicken.grid(row=0, column=0,columnspan=2)
        self.Heading_orange_chicken = Label(self.frame_orange_chicken, text="ORANGE CHICKEN", bg='#ffb035')
        self.Heading_orange_chicken.grid(row=1, column=0,columnspan=2)
        self.Button_mua_orange = Button(self.frame_orange_chicken, text="BUY NOW  !")
        self.Button_mua_orange.grid(row=2, column=0)
        self.Button_add_orange = Button(self.frame_orange_chicken, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_orange_chicken))
        self.Button_add_orange.grid(row=2, column=1)
        self.frame_orange_chicken.grid(row=2,column=2)

        self.cheesKen_image = PhotoImage(file=Form_Attributes.file_image_cheesKen)
        self.frame_cheesKen = Frame(self.frame_chicken, height=185, width=155, bg='#fcd76e')
        self.Label_cheesKen = Label(self.frame_cheesKen, image=self.cheesKen_image)
        self.Label_cheesKen.grid(row=0, column=0,columnspan=2)
        self.Heading_cheesKen = Label(self.frame_cheesKen, text="CHEESE CHICKEN", bg='#fcd76e')
        self.Heading_cheesKen.grid(row=1, column=0,columnspan=2)
        self.Button_mua_cheesKen = Button(self.frame_cheesKen, text="BUY NOW  !")
        self.Button_mua_cheesKen.grid(row=2, column=0)
        self.Button_add_cheesKen = Button(self.frame_cheesKen, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_cheesKen))
        self.Button_add_cheesKen.grid(row=2, column=1)
        self.frame_cheesKen.grid(row=2,column=3)

        Label(self.frame_chicken, text="                                                  ", bg='white').grid(row=3, column=0)

        self.mayo_chicken_image = PhotoImage(file=Form_Attributes.file_image_mayo_chicken)
        self.frame_mayo_chicken = Frame(self.frame_chicken, height=185, width=155, bg='#ffe084')
        self.Label_mayo_chicken = Label(self.frame_mayo_chicken, image=self.mayo_chicken_image)
        self.Label_mayo_chicken.grid(row=0, column=0,columnspan=2)
        self.Heading_mayo_chicken = Label(self.frame_mayo_chicken, text="MAYO CHICKEN", bg='#ffe084')
        self.Heading_mayo_chicken.grid(row=1, column=0,columnspan=2)
        self.Button_mua_mayo_chicken = Button(self.frame_mayo_chicken, text="BUY NOW  !")
        self.Button_mua_mayo_chicken.grid(row=2, column=0)
        self.Button_add_mayo_chicken = Button(self.frame_mayo_chicken, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_mayo_chicken))
        self.Button_add_mayo_chicken.grid(row=2, column=1)
        self.frame_mayo_chicken.grid(row=4, column=0)




        self.menu_chicken = Menu (self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='CHICKEN', menu=self.menu_chicken, font=Form_Attributes.font4)
        self.menu_chicken.add_command(label='Fried Chicken', font=Form_Attributes.font4, command=lambda:Menu_Bar_Form_Controler.show_frame(self.frame_chicken))

        # -----------------------------------------------------------------------------------------------------------------------------------------

        # frame trà sữa
        self.frame_boba = Frame(self.food_form_root,bg='white')
        self.boba_label = Label(self.frame_boba, text="HAVE FUN DRINKING BOBA", font=Form_Attributes.font1, padx=150, bg='white')
        self.boba_label.grid(row=0, column=0, columnspan=4)
        Label(self.frame_boba, text="                                                  ", bg='white').grid(row=1, column=0, columnspan=4)

        self.cherry_boba_image = PhotoImage(file=Form_Attributes.file_image_cherry_boba)
        self.frame_cherry_boba = Frame(self.frame_boba, height=185, width=155, bg='#ffb0b0')
        self.Label_cherry_boba = Label(self.frame_cherry_boba, image=self.cherry_boba_image)
        self.Label_cherry_boba.grid(row=0, column=0,columnspan=2)
        self.Heading_cherry_boba = Label(self.frame_cherry_boba, text="CHERRY BOBA", bg='#ffb0b0')
        self.Heading_cherry_boba.grid(row=1, column=0,columnspan=2)
        self.Button_mua_cherry_boba = Button(self.frame_cherry_boba, text="BUY NOW  !")
        self.Button_mua_cherry_boba.grid(row=2, column=0)
        self.Button_add_cherry_boba = Button(self.frame_cherry_boba, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_cherry_boba))
        self.Button_add_cherry_boba.grid(row=2, column=1)
        self.frame_cherry_boba.grid(row=2,column=0)

        self.choco_boba_image = PhotoImage(file=Form_Attributes.file_image_choco_boba)
        self.frame_chocolate_boba = Frame(self.frame_boba, height=185, width=155, bg='#965918')
        self.Label_choco_boba = Label(self.frame_chocolate_boba, image=self.choco_boba_image)
        self.Label_choco_boba.grid(row=0, column=0,columnspan=2)
        self.Heading_choco_boba = Label(self.frame_chocolate_boba, text="CHOCOLATE BOBA", bg='#965918')
        self.Heading_choco_boba.grid(row=1, column=0,columnspan=2)
        self.Button_mua_choco_boba = Button(self.frame_chocolate_boba, text="BUY NOW  !")
        self.Button_mua_choco_boba.grid(row=2, column=0)
        self.Button_add_choco_boba = Button(self.frame_chocolate_boba, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_choco_boba))
        self.Button_add_choco_boba.grid(row=2, column=1)
        self.frame_chocolate_boba.grid(row=2,column=1)

        self.blue_berry_boba_image = PhotoImage(file=Form_Attributes.file_image_blue_berry_boba)
        self.frame_blue_berry_boba = Frame(self.frame_boba, height=185, width=155, bg='#8e7cc3')
        self.Label_blue_berry_boba = Label(self.frame_blue_berry_boba, image=self.blue_berry_boba_image)
        self.Label_blue_berry_boba.grid(row=0, column=0,columnspan=2)
        self.Heading_blue_berry_boba = Label(self.frame_blue_berry_boba, text="BLUEBERRY BOBA", bg='#8e7cc3')
        self.Heading_blue_berry_boba.grid(row=1, column=0,columnspan=2)
        self.Button_mua_blue_berry = Button(self.frame_blue_berry_boba, text="BUY NOW  !")
        self.Button_mua_blue_berry.grid(row=2, column=0)
        self.Button_add_blue_berry_boba = Button(self.frame_blue_berry_boba, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_blue_berry_boba))
        self.Button_add_blue_berry_boba.grid(row=2, column=1)
        self.frame_blue_berry_boba.grid(row=2,column=2)

        self.cheese_boba_image = PhotoImage(file=Form_Attributes.file_image_cheese_boba)
        self.frame_cheese_boba = Frame(self.frame_boba, height=185, width=155, bg='#fce5cd')
        self.Label_cheese_boba = Label(self.frame_cheese_boba, image=self.cheese_boba_image)
        self.Label_cheese_boba.grid(row=0, column=0,columnspan=2)
        self.Heading_cheese_boba = Label(self.frame_cheese_boba, text="CHEESE BOBA", bg='#fce5cd')
        self.Heading_cheese_boba.grid(row=1, column=0,columnspan=2)
        self.Button_mua_cheese_boba = Button(self.frame_cheese_boba, text="BUY NOW  !")
        self.Button_mua_cheese_boba.grid(row=2, column=0)
        self.Button_add_cheese_boba = Button(self.frame_cheese_boba, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_cheese_boba))
        self.Button_add_cheese_boba.grid(row=2, column=1)
        self.frame_cheese_boba.grid(row=2,column=3)


        self.strawberry_boba_image = PhotoImage(file=Form_Attributes.file_image_strawberry_boba)
        self.frame_strawberry_boba = Frame(self.frame_boba, height=185, width=155, bg='#e06666')
        self.Label_strawberry_boba = Label(self.frame_strawberry_boba, image=self.strawberry_boba_image)
        self.Label_strawberry_boba.grid(row=0, column=0,columnspan=2)
        self.Heading_strawberry_boba = Label(self.frame_strawberry_boba, text="STRAWBERRY BOBA", bg='#e06666')
        self.Heading_strawberry_boba.grid(row=1, column=0,columnspan=2)
        self.Button_mua_strawberry_boba = Button(self.frame_strawberry_boba, text="BUY NOW  !")
        self.Button_mua_strawberry_boba.grid(row=2, column=0)
        self.Button_add_strawberry_boba = Button(self.frame_strawberry_boba, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_strawberry_boba))
        self.Button_add_strawberry_boba.grid(row=2, column=1)
        self.frame_strawberry_boba.grid(row=4, column=0)





        self.frame_tropical = Frame(self.food_form_root,bg='white')
        self.tropical_label = Label(self.frame_tropical, text="TROPICAL TEA IS THE BEST", font=Form_Attributes.font1, padx=150, bg='white')
        self.tropical_label.grid(row=0, column=0, columnspan=4)
        Label(self.frame_tropical, text="                                                  ", bg='white').grid(row=1, column=0, columnspan=4)

        self.peach_image = PhotoImage(file=Form_Attributes.file_image_peach_tea)
        self.frame_peach = Frame(self.frame_tropical, height=185, width=155, bg='#efb447')
        self.Label_peach = Label(self.frame_peach, image=self.peach_image)
        self.Label_peach.grid(row=0, column=0,columnspan=2)
        self.Heading_peach = Label(self.frame_peach, text="PEACH TEA", bg='#efb447')
        self.Heading_peach.grid(row=1, column=0,columnspan=2)
        self.Button_mua_peach = Button(self.frame_peach, text="BUY NOW  !")
        self.Button_mua_peach.grid(row=2, column=0)
        self.Button_add_peach = Button(self.frame_peach, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_peach))
        self.Button_add_peach.grid(row=2, column=1)
        self.frame_peach.grid(row=2,column=0)

        self.guava_image = PhotoImage(file=Form_Attributes.file_image_guava_tea)
        self.frame_guava = Frame(self.frame_tropical, height=185, width=155, bg='#93c47d')
        self.Label_guava = Label(self.frame_guava, image=self.guava_image)
        self.Label_guava.grid(row=0, column=0,columnspan=2)
        self.Heading_Guava = Label(self.frame_guava, text="GUAVA TEA", bg='#93c47d')
        self.Heading_Guava.grid(row=1, column=0,columnspan=2)
        self.Button_mua_guava = Button(self.frame_guava, text="BUY NOW  !")
        self.Button_mua_guava.grid(row=2, column=0)
        self.Button_add_guava = Button(self.frame_guava, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_Guava))
        self.Button_add_guava.grid(row=2, column=1)
        self.frame_guava.grid(row=2,column=1)

        self.honey_image = PhotoImage(file=Form_Attributes.file_image_honey)
        self.frame_honey = Frame(self.frame_tropical, height=185, width=155, bg='#fcd45b')
        self.Label_honey = Label(self.frame_honey, image=self.honey_image)
        self.Label_honey.grid(row=0, column=0,columnspan=2)
        self.Heading_honey = Label(self.frame_honey, text="HONEY TEA", bg='#fcd45b')
        self.Heading_honey.grid(row=1, column=0,columnspan=2)
        self.Button_mua_honey = Button(self.frame_honey, text="BUY NOW  !")
        self.Button_mua_honey.grid(row=2, column=0)
        self.Button_add_honey = Button(self.frame_honey, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_honey))
        self.Button_add_honey.grid(row=2, column=1)
        self.frame_honey.grid(row=2,column=2)

        self.lychee_image = PhotoImage(file=Form_Attributes.file_image_lychee)
        self.frame_lychee = Frame(self.frame_tropical, height=185, width=155, bg='#ffe9a9')
        self.Label_lychee = Label(self.frame_lychee, image=self.lychee_image)
        self.Label_lychee.grid(row=0, column=0,columnspan=2)
        self.Heading_Lychee = Label(self.frame_lychee, text="LYCHEE TEA", bg='#ffe9a9')
        self.Heading_Lychee.grid(row=1, column=0,columnspan=2)
        self.Button_mua_lychee = Button(self.frame_lychee, text="BUY NOW  !")
        self.Button_mua_lychee.grid(row=2, column=0)
        self.Button_lychee = Button(self.frame_lychee, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_Lychee))
        self.Button_lychee.grid(row=2, column=1)
        self.frame_lychee.grid(row=2,column=3)

        Label(self.frame_tropical, text="                                                  ", bg='white').grid(row=3, column=0)
        self.mango_image = PhotoImage(file=Form_Attributes.file_image_mango)
        self.frame_mango = Frame(self.frame_tropical, height=185, width=155, bg='#ffc000')
        self.Label_mango = Label(self.frame_mango, image=self.mango_image)
        self.Label_mango.grid(row=0, column=0,columnspan=2)
        self.Heading_mango = Label(self.frame_mango, text="MANGO TEA", bg='#ffc000')
        self.Heading_mango.grid(row=1, column=0,columnspan=2)
        self.Button_mua_mango = Button(self.frame_mango, text="BUY NOW  !")
        self.Button_mua_mango.grid(row=2, column=0)
        self.Button_mango = Button(self.frame_mango, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_mango))
        self.Button_mango.grid(row=2, column=1)
        self.frame_mango.grid(row=4, column=0)

        self.menu_tea = Menu (self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='TEA', menu=self.menu_tea, font=Form_Attributes.font4)
        self.menu_tea.add_command(label='Boba Tea', font=Form_Attributes.font4, command=lambda:Menu_Bar_Form_Controler.show_frame(self.frame_boba))
        self.menu_tea.add_separator()
        self.menu_tea.add_command(label='Tropical Tea', font=Form_Attributes.font4, command=lambda:Menu_Bar_Form_Controler.show_frame(self.frame_tropical))

        # -----------------------------------------------------------------------------------------------------------------------------
        self.frame_fruits = Frame(self.food_form_root,bg='white')
        self.fruits_label = Label(self.frame_fruits, text="FRUITS IS GOOD THE SKIN", font=Form_Attributes.font1, padx=150, bg='white')
        self.fruits_label.grid(row=0, column=0, columnspan=4)
        Label(self.frame_fruits, text="                                                  ", bg='white').grid(row=1, column=0, columnspan=4)

        self.apple_image = PhotoImage(file=Form_Attributes.file_image_apple)
        self.frame_apple = Frame(self.frame_fruits, height=185, width=155, bg='#ef5353')
        self.Label_apple = Label(self.frame_apple, image=self.apple_image)
        self.Label_apple.grid(row=0, column=0,columnspan=2)
        self.Heading_apple = Label(self.frame_apple, text="APPLE JUICE", bg='#ef5353')
        self.Heading_apple.grid(row=1, column=0,columnspan=2)
        self.Button_mua_apple = Button(self.frame_apple, text="BUY NOW  !")
        self.Button_mua_apple.grid(row=2, column=0)
        self.Button_add_apple = Button(self.frame_apple, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_apple))
        self.Button_add_apple.grid(row=2, column=1)
        self.frame_apple.grid(row=2,column=0)

        self.pineapple_image = PhotoImage(file=Form_Attributes.file_image_pineapple)
        self.frame_pineapple = Frame(self.frame_fruits, height=185, width=155, bg='#ebbf3b')
        self.Label_pineapple = Label(self.frame_pineapple, image=self.pineapple_image)
        self.Label_pineapple.grid(row=0, column=0,columnspan=2)
        self.Heading_pineapple = Label(self.frame_pineapple, text="PINEAPPLE JUICE", bg='#ebbf3b')
        self.Heading_pineapple.grid(row=1, column=0,columnspan=2)
        self.Button_mua_pineaple = Button(self.frame_pineapple, text="BUY NOW  !")
        self.Button_mua_pineaple.grid(row=2, column=0)
        self.Button_add_pineapple = Button(self.frame_pineapple, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_pineapple))
        self.Button_add_pineapple.grid(row=2, column=1)
        self.frame_pineapple.grid(row=2,column=1)

        self.kiwi_image = PhotoImage(file=Form_Attributes.file_image_kiwi)
        self.frame_kiwi = Frame(self.frame_fruits, height=185, width=155, bg='#8fce00')
        self.Label_kiwi = Label(self.frame_kiwi, image=self.kiwi_image)
        self.Label_kiwi.grid(row=0, column=0,columnspan=2)
        self.Heading_kiwi = Label(self.frame_kiwi, text="KIWI JUICE", bg='#8fce00')
        self.Heading_kiwi.grid(row=1, column=0,columnspan=2)
        self.Button_mua_kiwi = Button(self.frame_kiwi, text="BUY NOW  !")
        self.Button_mua_kiwi.grid(row=2, column=0)
        self.Button_add_kiwi = Button(self.frame_kiwi, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_kiwi))
        self.Button_add_kiwi.grid(row=2, column=1)
        self.frame_kiwi.grid(row=2,column=2)

        self.watermelon_image = PhotoImage(file=Form_Attributes.file_image_watermelon)
        self.frame_watermelon = Frame(self.frame_fruits, height=185, width=155, bg='#cc0000')
        self.Label_watermelon = Label(self.frame_watermelon, image=self.watermelon_image)
        self.Label_watermelon.grid(row=0, column=0,columnspan=2)
        self.Heading_watermelon = Label(self.frame_watermelon, text="WATERMELON JUICE", bg='#cc0000')
        self.Heading_watermelon.grid(row=1, column=0,columnspan=2)
        self.Button_watermelon = Button(self.frame_watermelon, text="BUY NOW  !")
        self.Button_watermelon.grid(row=2, column=0)
        self.Button_add_watermelon = Button(self.frame_watermelon, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_watermelon))
        self.Button_add_watermelon.grid(row=2, column=1)
        self.frame_watermelon.grid(row=2,column=3)

        Label(self.frame_fruits, text="                                                  ", bg='white').grid(row=3, column=0)
        self.lemon_image = PhotoImage(file=Form_Attributes.file_image_lemon)
        self.frame_lemon = Frame(self.frame_fruits, height=185, width=155, bg='#ffdb73')
        self.Label_lemon = Label(self.frame_lemon, image=self.lemon_image)
        self.Label_lemon.grid(row=0, column=0,columnspan=2)
        self.Heading_lemon = Label(self.frame_lemon, text="LEMON JUICE", bg='#ffdb73')
        self.Heading_lemon.grid(row=1, column=0,columnspan=2)
        self.Button_mua_lemon = Button(self.frame_lemon, text="BUY NOW  !")
        self.Button_mua_lemon.grid(row=2, column=0)
        self.Button_add_lemon = Button(self.frame_lemon, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_lemon))
        self.Button_add_lemon.grid(row=2, column=1)
        self.frame_lemon.grid(row=4, column=0)








        self.frame_vegetables = Frame(self.food_form_root,bg='white')
        self.vegetables_label = Label(self.frame_vegetables, text="BETTER YOUR GUT HEALTH", font=Form_Attributes.font1, padx=150, bg='white')
        self.vegetables_label.grid(row=0, column=0, columnspan=4)
        Label(self.frame_vegetables, text="                                                  ", bg='white').grid(row=1, column=0, columnspan=4)

        self.celery_image = PhotoImage(file=Form_Attributes.file_image_celery)
        self.frame_celery = Frame(self.frame_vegetables, height=185, width=155, bg='#3c7d1f')
        self.Label_celery = Label(self.frame_celery, image=self.celery_image)
        self.Label_celery.grid(row=0, column=0,columnspan=2)
        self.Heading_celery = Label(self.frame_celery, text="CELERY JUICE", bg='#3c7d1f')
        self.Heading_celery.grid(row=1, column=0,columnspan=2)
        self.Button_mua_celery = Button(self.frame_celery, text="BUY NOW  !")
        self.Button_mua_celery.grid(row=2, column=0)
        self.Button_add_celery = Button(self.frame_celery, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_celery))
        self.Button_add_celery.grid(row=2, column=1)
        self.frame_celery.grid(row=2,column=0)

        self.carrot_image = PhotoImage(file=Form_Attributes.file_image_carrot)
        self.frame_carrot = Frame(self.frame_vegetables, height=185, width=155, bg='#c98339')
        self.Label_carrot = Label(self.frame_carrot, image=self.carrot_image)
        self.Label_carrot.grid(row=0, column=0,columnspan=2)
        self.Heading_carrot = Label(self.frame_carrot, text="CARROT JUICE", bg='#c98339')
        self.Heading_carrot.grid(row=1, column=0,columnspan=2)
        self.Button_mua_carrot = Button(self.frame_carrot, text="BUY NOW  !")
        self.Button_mua_carrot.grid(row=2, column=0)
        self.Button_add_carrot = Button(self.frame_carrot, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_carrot))
        self.Button_add_carrot.grid(row=2, column=1)
        self.frame_carrot.grid(row=2,column=1)

        self.tomato_image = PhotoImage(file=Form_Attributes.file_image_tomato)
        self.frame_tomato = Frame(self.frame_vegetables, height=185, width=155, bg='#dc4646')
        self.Label_tomato = Label(self.frame_tomato, image=self.tomato_image)
        self.Label_tomato.grid(row=0, column=0,columnspan=2)
        self.Heading_tomato = Label(self.frame_tomato, text="TOMATO JUICE", bg='#dc4646')
        self.Heading_tomato.grid(row=1, column=0,columnspan=2)
        self.Button_mua_tomato = Button(self.frame_tomato, text="BUY NOW  !")
        self.Button_mua_tomato.grid(row=2, column=0)
        self.Button_add_tomato = Button(self.frame_tomato, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_tomato))
        self.Button_add_tomato.grid(row=2, column=1)
        self.frame_tomato.grid(row=2,column=2)

        self.lettuce_image = PhotoImage(file=Form_Attributes.file_image_lectuce)
        self.frame_lectucce = Frame(self.frame_vegetables, height=185, width=155, bg='#306618')
        self.Label_lectucce = Label(self.frame_lectucce, image=self.lettuce_image)
        self.Label_lectucce.grid(row=0, column=0,columnspan=2)
        self.Heading_lectuce = Label(self.frame_lectucce, text="LETTUCE JUICE", bg='#306618')
        self.Heading_lectuce.grid(row=1, column=0,columnspan=2)
        self.Button_mua_lectucce = Button(self.frame_lectucce, text="BUY NOW  !")
        self.Button_mua_lectucce.grid(row=2, column=0)
        self.Button_add_lectucce = Button(self.frame_lectucce, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_lectuce))
        self.Button_add_lectucce.grid(row=2, column=1)
        self.frame_lectucce.grid(row=2,column=3)

        Label(self.frame_vegetables, text="                                                  ", bg='white').grid(row=3, column=0)
        self.cucumber_image = PhotoImage(file=Form_Attributes.file_image_cucumber)
        self.frame_cucumber = Frame(self.frame_vegetables, height=185, width=155, bg='#7ab660')
        self.Label_cucumber = Label(self.frame_cucumber, image=self.cucumber_image)
        self.Label_cucumber.grid(row=0, column=0,columnspan=2)
        self.Heading_cucumber = Label(self.frame_cucumber, text="CUCUMBER JUICE", bg='#7ab660')
        self.Heading_cucumber.grid(row=1, column=0,columnspan=2)
        self.Button_mua_cucumber = Button(self.frame_cucumber, text="BUY NOW  !")
        self.Button_mua_cucumber.grid(row=2, column=0)
        self.Button_add_cucumber = Button(self.frame_cucumber, text="Add to Cart", command=lambda:Order_Controller.lay_so_luong(self.Heading_cucumber))
        self.Button_add_cucumber.grid(row=2, column=1)
        self.frame_cucumber.grid(row=4, column=0)

        self.menu_smoothie = Menu (self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='SMOOTHIE', menu=self.menu_smoothie, font=Form_Attributes.font4)
        self.menu_smoothie.add_command(label='Fruits', font=Form_Attributes.font4, command=lambda:Menu_Bar_Form_Controler.show_frame(self.frame_fruits))
        self.menu_smoothie.add_separator()
        self.menu_smoothie.add_command(label='Vegetables', font=Form_Attributes.font4, command=lambda:Menu_Bar_Form_Controler.show_frame(self.frame_vegetables))


        # order vs cart dùng table
        self.frame_cart_detail = Frame(self.food_form_root,bg="white")
        cart_details_label = Label(self.frame_cart_detail, text="BUY NOW PLEASE", font=Form_Attributes.font1, padx=150, bg='white')
        cart_details_label.grid(row=0, column=0,columnspan=4)
        Label(self.frame_cart_detail, text="                                                  ", bg='white').grid(row=1, column=0, columnspan=4)
        Bang_cart = Frame(self.frame_cart_detail, bg="white", padx=80)
        Bang_cart.grid(row=2,column=0,columnspan=4)

        cart_board = Treeview(Bang_cart)
        cart_board["columns"] = ("Id","Details","Total Price","Address","State")
        cart_board.column("#0", width=66,stretch=NO)
        cart_board.grid(row=3,column=0,columnspan=4)
        for col in cart_board["columns"]:
            cart_board.column(col,width=100)
            cart_board.heading(col,text=col)

        for i in range (167):
            cart_board.insert("","end",text="Row "+str(i+1), values=("Id"+str(i+1), "Details"+str(i+1),"Total Price"+str(i+1),"Address"+str(i+1),"State"+str(i+1)))
            scrollbar = Scrollbar(self.frame_cart_detail, orient="vertical", command=cart_board.yview())
        Label(self.frame_cart_detail, text="                                                  ", bg='white').grid(row=4, column=0, columnspan=4)

        self.Frame_nut_cart = Frame(self.frame_cart_detail, padx=180, bg='white')
        self.Frame_nut_cart.grid(row=5,column=0)
        self.Button_mua_all = Button(self.Frame_nut_cart, text="Buy all", width=12)
        self.Button_mua_all.grid(row=0,column=0)
        self.Button_huy_all = Button(self.Frame_nut_cart, text="Cancel all", width=12)
        self.Button_huy_all.grid(row=0,column=1)
        self.Button_buy_specific = Button(self.Frame_nut_cart, text="Buy specific", width=12)
        self.Button_buy_specific.grid(row=0,column=2)
        self.Button_cancel_specific = Button(self.Frame_nut_cart, text="Cancel specific", width=12)
        self.Button_cancel_specific.grid(row=0,column=3)



        menu_receipt = Menu (self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='CART',menu=menu_receipt,font=Form_Attributes.font4)
        menu_receipt.add_command(label='Receipt PDF',font=Form_Attributes.font4)
        menu_receipt.add_separator()
        menu_receipt.add_command(label='Cart Details', font=Form_Attributes.font4, command=lambda:Menu_Bar_Form_Controler.show_frame(self.frame_cart_detail))

        # xong log out
        menu_Log_out = Menu (self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='LOG OUT',menu=menu_Log_out,font=Form_Attributes.font4)
        menu_Log_out.add_command(label='Log out',font=Form_Attributes.font4,command=lambda:Menu_Bar_Form_Controler.quit_app(self.food_form_root))
        menu_Log_out.add_separator()
        menu_Log_out.add_command(label='Sign In with Another Account',font=Form_Attributes.font4,command=lambda:Login_Controller.call_sign_in())


        self.frame_nut = Frame (self.food_form_root, bg=Form_Attributes.bg_xanh)
        self.frame_nut.grid(row=0, column=0)


        # padx,pady : thiết lập khoảng cách giữa lề or widget
        frame_Account = Frame(self.food_form_root, bg=Form_Attributes.bg_xanh)
        Button_Account = Button(self.frame_nut, text='ACCOUNT', font=Form_Attributes.font4, width=24, height=9, bg=Form_Attributes.bg_xanh, command=lambda:Menu_Bar_Form_Controler.show_frame(frame_Account))
        Button_Account.grid(row=0,column=0)




        self.Button_Gio_hang = Button(self.frame_nut, text='ORDER', font=Form_Attributes.font4, width=24, height=3, bg=Form_Attributes.bg_xanh, command=lambda:Menu_Bar_Form_Controler.show_frame(frame_order))
        self.Button_Gio_hang.grid(row=1, column=0)
        frame_order = Frame(self.food_form_root,bg="white")
        Label_gio_hang = Label(frame_order,text="THIS IS THE CURRENT ORDER", font=Form_Attributes.font1,padx=150,bg="white")
        Label_gio_hang.grid(row=0,column=0,columnspan=2)
        Label(frame_order,text="                                                  ",bg='white').grid(row=1, column=0, columnspan=2)
        Bang_order = Frame(frame_order,bg="white",padx=80)
        Bang_order.grid(row=2,column=0)

        order_board = Treeview(Bang_order)
        order_board["columns"] = ("Id","Details","Total Price","Address","State")
        order_board.column("#0", width=66,stretch=NO)
        order_board.grid(row=3,column=0)
        for col in order_board["columns"]:
            order_board.column(col,width=100)
            order_board.heading(col,text=col)

        for i in range (167):
            order_board.insert("","end",text="Row "+str(i+1), values=("Id"+str(i+1), "Details"+str(i+1),"Total Price"+str(i+1),"Address"+str(i+1),"State"+str(i+1)))
            scrollbar = Scrollbar(frame_order,orient="vertical", command=order_board.yview())
        Label(frame_order,text="                                                  ",bg='white').grid(row=4, column=0,columnspan=3)

        Frame_nut_order = Frame(frame_order,padx=180,bg='white')
        Frame_nut_order.grid(row=5,column=0)
        Button_mua = Button(Frame_nut_order,text="Buy",width=12)
        Button_mua.grid(row=0,column=0)
        Button_huy = Button(Frame_nut_order,text="Cancel Order",width=12)
        Button_huy.grid(row=0,column=1)
        Button_change_address = Button(Frame_nut_order,text="Change Address",width=12)
        Button_change_address.grid(row=0,column=2)












        # xong policy
        Button_Policy = Button(self.frame_nut, text='POLICY', font=Form_Attributes.font4, width=24, height=3, bg=Form_Attributes.bg_xanh, command=lambda:Menu_Bar_Form_Controler.show_frame(frame_policy))
        Button_Policy.grid(row=2,column=0)
        # Tạo Frame để chứa nội dung của Policy
        frame_policy = Frame(self.food_form_root, bg=Form_Attributes.bg_xanh)
        policy_label = Label(frame_policy, text=Form_Attributes.text_policy, font=Form_Attributes.font5, bg=Form_Attributes.bg_white)
        policy_label.pack()




        Button_order_history = Button(self.frame_nut, text='ORDERS  HISTORY', font=Form_Attributes.font4, width=24, height=3, bg=Form_Attributes.bg_xanh, command=lambda:Menu_Bar_Form_Controler.show_frame(frame_order_history))
        Button_order_history.grid(row=3,column=0)
        frame_order_history = Frame(self.food_form_root,bg="white")
        Label_order_history = Label(frame_order_history,text="YOUR ORDER HISTORY", font=Form_Attributes.font1,padx=150,bg="white")
        Label_order_history.grid(row=0,column=0)
        Label(frame_order_history,text="                                                  ",bg='white').grid(row=1, column=0)
        Bang_order_history = Frame(frame_order_history,bg="white",padx=80)
        Bang_order_history.grid(row=2,column=0)

        order_history_board = Treeview(Bang_order_history)
        order_history_board["columns"] = ("Id","Details","Total Price","Address","State")
        order_history_board.column("#0", width=66,stretch=NO)
        order_history_board.grid(row=3,column=0)
        for col in order_history_board["columns"]:
            order_history_board.column(col,width=100)
            order_history_board.heading(col,text=col)

        for i in range (167):
            order_history_board.insert("","end",text="Row "+str(i+1), values=("Id"+str(i+1), "Details"+str(i+1),"Total Price"+str(i+1),"Address"+str(i+1),"State"+str(i+1)))
            scrollbar = Scrollbar(frame_order_history,orient="vertical", command=order_history_board.yview())
        Label(frame_order_history,text="                                                  ",bg='white').grid(row=4, column=0,columnspan=3)

        Frame_lsmh = Frame(frame_order_history,padx=180,bg='white')
        Frame_lsmh.grid(row=5,column=0)
        Button_mua_lai = Button(Frame_lsmh,text="Re-purchase",width=12)
        Button_mua_lai.grid(row=0,column=0)


        self.Button_canceled = Button(self.frame_nut, text='CANCELLED  ORDERS', font=Form_Attributes.font4, width=24, height=3, bg=Form_Attributes.bg_xanh, command=lambda:Menu_Bar_Form_Controler.show_frame(frame_cancelled_order))
        self.Button_canceled.grid(row=4, column=0)
        frame_cancelled_order = Frame(self.food_form_root,bg="white")
        Label_cancel_order = Label(frame_cancelled_order,text="THE CANCELLED ORDERS", font=Form_Attributes.font1,padx=150,bg="white")
        Label_cancel_order.grid(row=0,column=0)
        Label(frame_cancelled_order,text="                                                  ",bg='white').grid(row=1, column=0)
        Bang_cancel_order = Frame(frame_cancelled_order,bg="white",padx=80)
        Bang_cancel_order.grid(row=2,column=0)

        cancel_board = Treeview(Bang_cancel_order)
        cancel_board["columns"] = ("Id","Details","Total Price","Address","State")
        cancel_board.column("#0", width=66,stretch=NO)
        cancel_board.grid(row=3,column=0)
        for col in cancel_board["columns"]:
            cancel_board.column(col,width=100)
            cancel_board.heading(col,text=col)

        for i in range (167):
            cancel_board.insert("","end",text="Row "+str(i+1), values=("Id"+str(i+1), "Details"+str(i+1),"Total Price"+str(i+1),"Address"+str(i+1),"State"+str(i+1)))
            scrollbar = Scrollbar(frame_cancelled_order,orient="vertical", command=cancel_board.yview())
        Label(frame_cancelled_order,text="                                                  ",bg='white').grid(row=4, column=0,columnspan=3)
        self.Frame_mua_lai = Frame(frame_cancelled_order,padx=180,bg='white')
        self.Frame_mua_lai.grid(row=5, column=0)
        self.Button_mua_lai = Button(self.Frame_mua_lai, text="Re-purchase cancelled order")
        self.Button_mua_lai.grid(row=0,column=0)
        self.food_form_root.mainloop()




my_main_app = menu()