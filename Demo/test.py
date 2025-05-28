from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring

def show_entry_box(label_widget):

    result = askstring("Input Box", "Enter something:")
    messagebox.showinfo("Result", f"You entered: {result}")

main_window = Tk()
button = Button(main_window, text="Click me", command=show_entry_box)
button.pack()

main_window.mainloop()
