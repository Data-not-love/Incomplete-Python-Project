import smtplib
from email.mime.text import MIMEText
import random
import Login.Form_Attributes

code_dangky = random.randint(10000,999999)
my_message = MIMEText('Code dang ky cua ban : ' + str(code_dangky))
my_message['Subject'] = 'Xác thực mật khẩu cho người đăng nhập mới'
my_message['From'] = Login.Form_Attributes.server_mail
my_message['To'] = 'ledinhnhuan1917@gmail.com'

send_the_mail = smtplib.SMTP('smtp.gmail.com', 587)
send_the_mail.starttls()
send_the_mail.login(Login.Form_Attributes.server_mail,Login.Form_Attributes.server_mail_password)
send_the_mail.send_message(my_message)
send_the_mail.quit()

