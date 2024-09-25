import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox

window = tk.Tk()
window.title("Calculator")
window.geometry("720x500")



def result():
    p = p_ent.get()
    r = rate_ent.get()
    y = yer_ent.get()
    chose = sel_oper.get()
    radio = var.get()
    print(f"{radio}")
    if chose == "Simple Interest":
        simple = int(p)*int(r)*int(y)/100
        messagebox.showinfo(title="Result",message=f"Simple Interest = {simple}")

    elif chose == "Compound Interest":
        cam = int(p) * (1 + int(r) / 100) ** int(y)
        messagebox.showinfo(title="Result",message=f"Compound Interest = {cam}")

    else:
        messagebox.showinfo(title="Result",message="Select the Option from the list")
no = tk.StringVar()
no.set(None)

hlabel = tk.Label(window,text="Calculator Simple and Compound Interst",font=("Book Antiqua",15,"bold"))
hlabel.place(x=150,y=50)

pno = tk.Label(window,text="Enter Principle Amount ",font=("Book Antiqua",10))
pno.place(x=200,y=150)

p_ent = tk.Entry(window)
p_ent.place(x=400,y=150)

rate = tk.Label(window,text="Enter Rate of Interest ",font=("Book Antiqua",10))
rate.place(x=200,y=190)

rate_ent = tk.Entry(window)
rate_ent.place(x=400,y=190)

years = tk.Label(window,text="Enter Years ",font=("Book Antiqua",10))
years.place(x=200,y=230)

yer_ent = tk.Entry(window)
yer_ent.place(x=400,y=230)


operation = tk.Label(window,text="Select Operation ",font=("Book Antiqua",10))
operation.place(x=200,y=270)



sel_oper = Combobox(window, values=["Simple Interest","Compound Interest"],font=("Book Antiqua",12),state='r',width=20)
sel_oper.place(x=400,y=270)

r_lable = tk.Label(window,text="Gender",font=("Book Antiqua",12))
r_lable.place(x=200,y=310)

var = tk.StringVar(value="Male")

r1_male = tk.Radiobutton(window,text="Male",value="Male",variable=var,font=("Book Antiqua",12))
r1_male.place(x=400,y=310)

r2_female = tk.Radiobutton(window,text="Female",value="Female",variable=var,font=("Book Antiqua",12))
r2_female.place(x=480,y=310)



button = tk.Button(window,text="Result",font=("Book Antiqua",12),width=12,command=result)
button.place(x=350,y=370)

window.mainloop()