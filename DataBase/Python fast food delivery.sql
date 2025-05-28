create database MY_FAST_FOOD;
use MY_FAST_FOOD;


create table FOOD (
Food_ID INT NOT NULL unique, primary key (Food_ID),
Food_name nvarchar(30) not null,
price DECIMAL(6,2) not null,
quantity_left int not null
);

insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (110,'CAPUCHINNO',35000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (120,'ESPRESSO',40000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (130,'BLACK COFFEE',25000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (140,'MILK COFFEE',15000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (150,'LATTE',30000.0,100);

insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (210,'TERIYAKI',50000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (220,'SPICY CHICKEN',45000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (230,'ORANGE CHICKEN',45000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (240,'CHEESE CHICKEN',60000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (250,'MAYO CHICKEN',65000.0,100);

insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (310,'CHERRY BOBA',15000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (320,'CHOCOLATE BOBA',20000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (330,'BLUE BERRY BOBA',25000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (340,'CHEESE BOBA',30000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (350,'STRAWBERRY BOBA',30000.0,100);

insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (410,'PEACH',25000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (420,'GUAVA',25000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (430,'HONEY',25000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (440,'LYCHEE',25000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (450,'MANGO',25000.0,100);

insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (510,'APPLE JUICE',25000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (520,'PINEAPPLE JUICE',30000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (530,'KIWI JUICE',35000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (540,'WATERMELON JUICE',20000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (550,'LEMON JUICE',65000.0,100);

insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (610,'CELERY JUICE',20000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (620,'CARROT JUICE',30000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (630,'TOMATO JUICE',15000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (640,'LECTUCE JUICE',15000.0,100);
insert Into FOOD (Food_ID,Food_name,price,quantity_left) values (650,'CUCUMBER JUICE',25000.0,100);


create table User_For_App (
username varchar (50) not null ,
pass varchar (50) not null ,
email varchar (50) not null,
User_ID int not null unique,
primary key (User_ID),
Date_Of_Birth DATE NOT NULL,
address varchar (300) not null
);
insert into User_For_App (username,pass,email,User_ID,Date_Of_Birth,address) values ('cuong','c111','hihi@gmail.com',11,'1980-03-03','Quảng Bình');


create table Admin_app (
admin_Id int not null unique,
primary key(admin_Id),
ad_UserName varchar (50) not null ,
pass_ad  varchar (50) not null 
);



create table Order_Food (
Order_ID int not null unique,
primary key (Order_ID),
Order_Date datetime,
User_ID_FK INT NOT NULL,
state Enum ('Cancelled','In Delivery','Complete') not null,
    FOREIGN KEY (User_ID_FK) REFERENCES User_For_App(User_ID)
);

create table Details (
Total_price decimal(10,2) not null,
Quantity int not null,
Order_ID_FK int Not null,
foreign key (Order_ID_FK) references Order_Food (Order_ID)
 );
 
create table OrderHistory (
Order_ID_FK int Not null,
foreign key (Order_ID_FK) references Order_Food (Order_ID)
);

create table Cancelled_Order (
Order_ID_FK int Not null,
foreign key (Order_ID_FK) references Order_Food (Order_ID)
);

create table Cart (
Order_ID_FK int Not null,
foreign key (Order_ID_FK) references Order_Food (Order_ID)
);