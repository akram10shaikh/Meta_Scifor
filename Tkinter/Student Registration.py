import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x800")
root.title("Qr Code Generator")

def popup():
    messagebox.showinfo("Registration ","Registration Complete Successfully")


lable1H = tk.Label(root, text="Student Registration Form",font=("Book Antiqua",20,"bold"),bg="lightgrey")
lable1H.place(x=30,y=100)


fname = tk.Label(root, text="Full Name",font=("Book Antiqua",15))
fname.place(x=35,y=200)

ffname = tk.Entry(root, font=("Book Antiqua",15,"bold"),width=20)
ffname.place(x=200,y=200)

email = tk.Label(root, text="Email ID",font=("Book Antiqua",15))
email.place(x=35,y=250)

eemail = tk.Entry(root, font=("Book Antiqua",15,"bold"),width=20)
eemail.place(x=200,y=250)


fname = tk.Label(root, text="Phone",font=("Book Antiqua",15))
fname.place(x=35,y=300)

ffname = tk.Entry(root, font=("Book Antiqua",15,"bold"),width=20)
ffname.place(x=200,y=300)

email = tk.Label(root, text="Address",font=("Book Antiqua",15))
email.place(x=35,y=350)

eemail = tk.Entry(root, font=("Book Antiqua",15,"bold"),width=20)
eemail.place(x=200,y=350)





b = tk.Button(root, text="Save",font=("Times new roomen",12,),command=popup,width=10)
b.place(x=250,y=400)


# button2 = tk.Button(root, text="Color",font=("Times new roomen",12,),width=8)
# button2.place(x=180,y=260)
#
# button1 = tk.Button(root,text="Submit",font=("Times new roomen",15,),width=12)
# button1.place(x=180,y=260)



root.mainloop()