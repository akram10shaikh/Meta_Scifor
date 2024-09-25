import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("340x330")

main_entry = tk.Entry(window,font=("Arial",25),width=14)
main_entry.place(x=17,y=10)

global pos,temp
pos = 0
temp = 0
def one_click():
    global pos
    main_entry.insert(pos,1)
    pos = pos + 1

def two_click():
    global pos
    main_entry.insert(pos, 2)
    pos = pos + 1

def three_click():
    global pos
    main_entry.insert(pos, 3)
    pos = pos + 1


def four_click():
    global pos
    main_entry.insert(pos, 4)
    pos = pos + 1

def five_click():
    global pos
    main_entry.insert(pos, 5)
    pos = pos + 1

def six_click():
    global pos
    main_entry.insert(pos, 6)
    pos = pos + 1

def seven_click():
    global pos
    main_entry.insert(pos, 7)
    pos = pos + 1

def eight_click():
    global pos
    main_entry.insert(pos, 8)
    pos = pos + 1

def nine_click():
    global pos
    main_entry.insert(pos, 9)
    pos = pos + 1

def zero_click():
    global pos
    main_entry.insert(pos, 0)
    pos = pos + 1

def plus_click():
    global temp
    temp = int(main_entry.get())
    main_entry.delete(0,tk.END)
    main_entry.insert(0,"+")


def minus_click():
    global temp
    temp = int(main_entry.get())
    main_entry.delete(0, tk.END)
    main_entry.insert(0, "-")

def multiply_click():
    global temp
    temp = int(main_entry.get())
    main_entry.delete(0, tk.END)
    main_entry.insert(0, "*")

def divide_click():
    global temp
    temp = int(main_entry.get())
    main_entry.delete(0, tk.END)
    main_entry.insert(0, "/")


def equal_click():
    global temp
    sign = main_entry.get()
    print(temp)
    print(sign)
    second_no = sign[1:]
    print(f"second no {second_no}")
    main_entry.delete(0, tk.END)
    if sign[0] == "+":
        final = int(second_no) + int(temp)
        main_entry.insert(0, final)
    elif sign[0] == "-":
        final = int(second_no) - int(temp)
        main_entry.insert(0, final)
    elif sign[0] == "*":
        final = int(second_no) * int(temp)
        main_entry.insert(0, final)
    elif sign[0] == "/":
        final = int(temp) / int(second_no)
        main_entry.insert(0, final)
    else:
        res = main_entry.get()
        main_entry.insert(0,res)
def clear_click():
    global temp
    main_entry.delete(0,tk.END)
    temp = 0


no_nine = tk.Button(window,text="9",font=(10),width=5,command=nine_click)
no_nine.place(x=20,y=80)

no_eight = tk.Button(window,text="8",font=(10),width=5,command=eight_click)
no_eight.place(x=100,y=80)

no_seven = tk.Button(window,text="7",font=(10),width=5,command=seven_click)
no_seven.place(x=180,y=80)

no_six = tk.Button(window,text="6",font=(10),width=5,command=six_click)
no_six.place(x=20,y=130)

no_five = tk.Button(window,text="5",font=(10),width=5,command=five_click)
no_five.place(x=100,y=130)

no_four = tk.Button(window,text="4",font=(10),width=5,command=four_click)
no_four.place(x=180,y=130)

no_three = tk.Button(window,text="3",font=(10),width=5,command=three_click)
no_three.place(x=20,y=180)

no_two = tk.Button(window,text="2",font=(10),width=5,command=two_click)
no_two.place(x=100,y=180)

no_one = tk.Button(window,text="1",font=(10),width=5,command=one_click)
no_one.place(x=180,y=180)

no_zero = tk.Button(window,text="0",font=(10),width=5,command=zero_click)
no_zero.place(x=20,y= 230)

no_equal = tk.Button(window,text="=",font=(10),width=12,command=equal_click)
no_equal.place(x=100,y=230)

no_multiply = tk.Button(window,text="*",font=(10),width=5,command=multiply_click)
no_multiply.place(x=260,y=80)

no_divide = tk.Button(window,text="/",font=(10),width=5,command=divide_click)
no_divide.place(x=260,y=130)


no_minus = tk.Button(window,text="-",font=(10),width=5,command=minus_click)
no_minus.place(x=260,y=180)



no_plus = tk.Button(window,text="+",font=(10),width=5,command=plus_click)
no_plus.place(x=260,y=230)

no_clear = tk.Button(window,text="Clear",font=(10),width=27,command=clear_click)
no_clear.place(x=20,y=280)

window.mainloop()


