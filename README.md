# 🍔 Fast Food Delivery App - Python + Tkinter + MySQL

Dự án phần mềm bán đồ ăn nhanh (Fast Food Delivery) được xây dựng bằng **Python** sử dụng thư viện **Tkinter** cho giao diện và **MySQL** cho quản lý dữ liệu. Hệ thống hỗ trợ người dùng đặt món, đăng nhập/đăng ký, quản lý đơn hàng, hóa đơn, và nhiều chức năng khác.

---

## 🧰 Công nghệ sử dụng

- **Python 3.x**
- **Tkinter** – GUI framework
- **MySQL** – Quản lý cơ sở dữ liệu
- **SQL script** – `Python fast food delivery.sql` để tạo CSDL

---

## 📁 Cấu trúc thư mục
```
├── Assets/ # Tài nguyên tĩnh (ảnh, icon...)
├── Controller/ # Logic xử lý chính
│ ├── Full_Order.py
│ ├── Hoa_Don_Controller.py
│ ├── Login_Controller.py
│ ├── Menu_Bar_Form_Controler.py
│ ├── Model_Controller.py
│ └── Order_Controller.py
├── DataBase/
│ ├── Database_Attributes.py # Thuộc tính và kết nối DB
│ └── Python fast food delivery.sql
├── Demo/ # Giao diện mẫu hoặc thử nghiệm
├── Login/ # Các form xử lý đăng nhập/đăng ký
│ ├── Chi_tiet_order.py
│ ├── Forget_Pass.py
│ ├── Sign_In.py
│ ├── Sign_Up.py
│ └── ...
├── Model/
│ └── Connect_Database.py # Hàm kết nối CSDL
├── View/
│ └── main.py # Điểm khởi chạy ứng dụng
├── .env # Biến môi trường (ẩn thông tin DB)
├── .gitignore
├── README.md
├── De_Cuong_Do_An_CS1_2024.docx
└── KHMT_De_Cuong_Do_An_Template_update_2024.docx

```


---

## 🚀 Khởi chạy dự án

1. **Clone dự án**

```bash
git clone <repo-url>
cd <tên-thư-mục>
Cài đặt môi trường ảo và package cần thiết (nếu có)

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate     # Trên Linux/macOS
.venv\Scripts\activate        # Trên Windows
Tạo database MySQL

Import file Python fast food delivery.sql vào MySQL để khởi tạo dữ liệu.

Cấu hình .env

Tạo file .env (nếu chưa có) với nội dung như sau:

ini

DB_HOST=localhost
DB_PORT=3306
DB_NAME=fastfood_db
DB_USER=root
DB_PASSWORD=your_password
Chạy ứng dụng

bash
python View/main.py
💡 Chức năng chính
👤 Đăng nhập / Đăng ký / Quên mật khẩu

🛒 Đặt món, chi tiết đơn hàng

📋 Xem menu, lựa chọn món tối ưu

🧾 Xuất hóa đơn

🔐 Quản lý người dùng

📦 Quản lý đơn hàng (Order Controller)