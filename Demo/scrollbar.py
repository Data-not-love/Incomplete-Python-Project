import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Scrollbar Example")

    # Tạo một Listbox
    listbox = tk.Listbox(root, selectmode=tk.SINGLE)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Tạo một Scrollbar và liên kết nó với Listbox
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Liên kết Scrollbar với Listbox
    listbox.config(yscrollcommand=scrollbar.set)

    # Thêm một số mục vào Listbox
    for i in range(100):
        listbox.insert(tk.END, f"Item {i+1}")

    root.mainloop()

if __name__ == "__main__":
    main()
