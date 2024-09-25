
import tkinter as tk

window = tk.Tk()
window.title("Covid Form")
window.geometry("600x660")

def sel():
    gender = var.get()
    return gender
def submit():
    name = hinput.get()
    age = ageinput.get()
    email = eminput.get()
    contact = coninput.get()
    country = contryinput.get()
    state = stinput.get()
    address = addinput.get("1.0",tk.END)
    gender = sel()
    print(f'{name} {age} {gender} {email} {address} {contact} {country} {state}')


hlabel = tk.Label(window,text="Covid Registration Form",font=("Book Antiqua",15),bg="lightgrey")
hlabel.place(x=150,y=50)


name = tk.Label(window,text="Name of the Visitor ",font=("Book Antiqua",10))
name.place(x=100,y=150)
hinput = tk.Entry(window,width=20)
hinput.place(x=300,y=150)

age = tk.Label(window,text="Age of the Visitor ",font=("Book Antiqua",10))
age.place(x=100,y=200)
ageinput = tk.Entry(window,width=20)
ageinput.place(x=300,y=200)


gender = tk.Label(window,text="Gender ",font=("Book Antiqua",10))
gender.place(x=100,y=250)

var = tk.StringVar()

gmbutton = tk.Radiobutton(window,text="Male",value="male",variable=var,command=sel)
gmbutton.place(x=300,y=250)

gfbutton = tk.Radiobutton(window,text="Female",value="female",variable=var,command=sel)
gfbutton.place(x=360,y=250)

address = tk.Label(window,text="Address ",font=("Book Antiqua",10))
address.place(x=100,y=300)

addinput = tk.Text(window,height=2,width=16)
addinput.place(x=300,y=300)


email = tk.Label(window,text="Email ",font=("Book Antiqua",10))
email.place(x=100,y=350)
eminput = tk.Entry(window,width=20)
eminput.place(x=300,y=350)

contact= tk.Label(window,text="Contact No ",font=("Book Antiqua",10))
contact.place(x=100,y=400)
coninput = tk.Entry(window,width=20)
coninput.place(x=300,y=400)

country= tk.Label(window,text="Country ",font=("Book Antiqua",10))
country.place(x=100,y=450)
contryinput = tk.Entry(window,width=20)
contryinput.place(x=300,y=450)

state= tk.Label(window,text="State ",font=("Book Antiqua",10))
state.place(x=100,y=500)
stinput = tk.Entry(window,width=20)
stinput.place(x=300,y=500)

state= tk.Label(window,text="Select Disease ",font=("Book Antiqua",10))
state.place(x=100,y=550)

checkbox1 = tk.Checkbutton(window,text="Cold")
checkbox1.place(x=230,y=550)

checkbox2 = tk.Checkbutton(window,text="Cough")
checkbox2.place(x=290,y=550)

checkbox3 = tk.Checkbutton(window,text="Fever")
checkbox3.place(x=360,y=550)

checkbox4 = tk.Checkbutton(window,text="Headache")
checkbox4.place(x=420,y=550)

button = tk.Button(window,text="Submit",font=("Book Antiqua",10),width=15,command=submit)
button.place(x=250,y=600)

window.mainloop()