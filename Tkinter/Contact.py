import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("700x600")
window.title("Address Book")


# Saving the contact

global contact_lst
contact_lst = {}
def add_contact():
    def save_contact():
        name = cont_entry.get()
        phone = phone_entry.get()
        contact_lst[name]=phone
        a = messagebox.showinfo("Save","Contact is saved")

    abc = tk.Tk()
    abc.geometry("300x300")
    h_lable = tk.Label(abc, text="Add Contact", font=(20), bg="lightyellow")
    h_lable.place(x=120, y=50)
    cont_label = tk.Label(abc, text="Name")
    cont_label.place(x=50, y=100)

    cont_entry = tk.Entry(abc)
    cont_entry.place(x=100, y=100)

    phone_label = tk.Label(abc, text="Phone")
    phone_label.place(x=50, y=150)

    phone_entry = tk.Entry(abc)
    phone_entry.place(x=100, y=150)

    save_button = tk.Button(abc, text="Save",width=10, command=save_contact)
    save_button.place(x=120, y=200)

# View contact
def view_contact():
    v_window = tk.Tk()
    v_window.geometry("300x300")
    h_lable = tk.Label(v_window, text="View Contact", font=(20), bg="lightyellow")
    h_lable.place(x=100, y=50)

    a = 70
    b = 50
    for i,j in contact_lst.items():
        label = tk.Label(v_window,text=f"{i} {j}",font=(10))
        label.place(x=a,y=b)
        b = b + 40

    print(contact_lst)

def edit_contact():
    def e_contact():
        name = edit_entry.get()
        phone = ephone_entry.get()
        contact_lst[name]=phone
        a = messagebox.showinfo("Save","Contact is Edited successfully")



    e_window = tk.Tk()
    e_window.geometry("300x300")
    e_lable = tk.Label(e_window, text="Enter the Contact Name and phone", font=(20), bg="lightyellow")
    e_lable.place(x=50, y=50)


    edit_label = tk.Label(e_window, text="Name")
    edit_label.place(x=50, y=100)

    edit_entry = tk.Entry(e_window)
    edit_entry.place(x=100, y=100)

    edit_plabel = tk.Label(e_window, text="Phone")
    edit_plabel.place(x=50, y=150)

    ephone_entry = tk.Entry(e_window)
    ephone_entry.place(x=100, y=150)

    save_button = tk.Button(e_window, text="Save", width=10,command=e_contact)
    save_button.place(x=120, y=200)


h_lable = tk.Label(window,text="Address Book",font=(20),bg="lightyellow")
h_lable.place(x=280,y=50)

add_cont = tk.Button(window,text="Add Contact",command=add_contact,width=15)
add_cont.place(x=300,y=200)

edit_cont = tk.Button(window,text="Edit Contact",width=15,command=edit_contact)
edit_cont.place(x=300,y=250)

view_cont = tk.Button(window,text="View Contact",width=15,command=view_contact)
view_cont.place(x=300,y=300)



view_cont = tk.Button(window,text="Exit",width=15,command=window.quit)
view_cont.place(x=300,y=350)



window.mainloop()

