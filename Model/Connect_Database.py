from DataBase import Database_Attributes
# tạo cursor để làm truy vấn
my_cursor = Database_Attributes.db.cursor()
if Database_Attributes.db.is_connected():
    print("No Problem. Database Is Connected")
else:
    print("No connection")
# Thực hiện câu truy vấn SQL với tham số để tránh SQL injection
sql_dang_nhap = 'SELECT * FROM User_For_App WHERE username = %s AND pass = %s'
sql_dang_ky = ("INSERT INTO User_For_App (User_ID,username, pass, email, Date_Of_Birth, address) "
                       "VALUES (%s, %s, %s, %s, %s, %s)")
sql_reset_pass = 'UPDATE User_For_App SET pass = %s WHERE username = %s'
sql_nhap_detail = ''
sql_them_order = ''