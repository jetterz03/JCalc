from tkinter import *
import tkinter.font as font

global f_num
global math

root = Tk()

# Giving my application a name
root.title("JCalculator")

myFont = font.Font(family="Fira Code")
e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "Addition"
    f_num = float(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "Subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "Multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "Division"
    f_num = float(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "Addition":
        e.insert(0, f_num + float(second_number))
    elif math == "Subtraction":
        e.insert(0, f_num - float(second_number))
    elif math == "Multiplication":
        e.insert(0, f_num*float(second_number))
    elif math == "Division":
        e.insert(0, f_num/float(second_number))


# region Define Buttons
button_1 = Button(root, text="1", padx=30, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=20, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=20, pady=20, command=button_subtract)
button_multiply = Button(root, text="×", padx=20, pady=20, command=button_multiply)
button_divide = Button(root, text="÷", padx=20, pady=20, command=button_divide)
button_equal = Button(root, text="=", padx=30, pady=20, command=button_equal)
button_clear = Button(root, text="CE", padx=25, pady=20, command=button_clear)
# endregion

# region Define Font
button_1["font"] = myFont
button_2["font"] = myFont
button_3["font"] = myFont
button_4["font"] = myFont
button_5["font"] = myFont
button_6["font"] = myFont
button_7["font"] = myFont
button_8["font"] = myFont
button_9["font"] = myFont
button_0["font"] = myFont
button_add["font"] = myFont
button_subtract["font"] = myFont
button_multiply["font"] = myFont
button_divide["font"] = myFont
button_equal["font"] = myFont
button_clear["font"] = myFont
# endregion

# region Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_divide.grid(row=4, column=3)
# endregion
root.mainloop()
