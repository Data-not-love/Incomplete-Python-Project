import tkinter as tk
from tkinter import ttk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Order History Board")

# Tạo khung chứa bảng
frame_order_history = ttk.Frame(root)
frame_order_history.pack(fill=tk.BOTH, expand=True)

# Tạo bảng Treeview
order_history_board = ttk.Treeview(frame_order_history)
order_history_board["columns"] = ("Id", "Details", "Total Price", "Address", "State")
order_history_board.column("#0", width=66, stretch=False)
order_history_board.pack()

for col in order_history_board["columns"]:
    order_history_board.column(col, width=100)
    order_history_board.heading(col, text=col)

# Dữ liệu mẫu để thêm vào bảng
data = [
    {"Id": "001", "Details": "Order 1 Details", "Total Price": "$50.00", "Address": "123 Main St", "State": "CA"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "003", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},
    {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"}, {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"}, {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"}, {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"}, {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"}, {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"}, {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"}, {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"}, {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"}, {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"}, {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"}, {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"}, {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"}, {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"}, {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"}, {"Id": "002", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"}, {"Id": "012", "Details": "Order 2 Details", "Total Price": "$75.00", "Address": "456 Elm St", "State": "NY"},]

# Thêm dữ liệu vào bảng
for item in data:
    order_history_board.insert("", "end", text=item["Id"], values=(item["Id"], item["Details"], item["Total Price"], item["Address"], item["State"]))

# Tạo thanh cuộn cho bảng
# scrollbar = ttk.Scrollbar(frame_order_history, orient="vertical", command=order_history_board.yview)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Liên kết thanh cuộn với bảng
# order_history_board.config(yscrollcommand=scrollbar.set)

# Chạy ứng dụng
root.mainloop()
