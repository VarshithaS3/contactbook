from tkinter import*
from tkinter import messagebox

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    
    if name and phone:
        contact_list.insert(END, f"{name} - {phone}")
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Please enter both name and phone number.")

def delete_contact():
    try:
        selected_index = contact_list.curselection()[0]
        contact_list.delete(selected_index)
    except IndexError:
        messagebox.showerror("Error", "No contact selected.")

def clear_contacts():
    contact_list.delete(0, END)

def get_selected_contact(event):
    try:
        selected_index = contact_list.curselection()[0]
        selected_contact = contact_list.get(selected_index)
        name, phone = selected_contact.split(" - ")
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
        name_entry.insert(END, name)
        phone_entry.insert(END, phone)
    except IndexError:
        pass

root = Tk()
root.title("Contact Book")
root.geometry("500x600")  # Set the window size to 500x600
root.configure(bg="#C6F4D6")  # Set the background color to lightest green

# Create UI elements
headline = Label(root, text="Contact Book", font=("Arial", 24, 'bold'), bg="#C6F4D6")
headline.pack(pady=20)

name_label = Label(root, text="Name:", font=('times', 15), bg="#C6F4D6")
name_label.pack()
name_entry = Entry(root, width=40)
name_entry.pack()

phone_label = Label(root, text="Phone:", font=('times', 15), bg="#C6F4D6")
phone_label.pack()
phone_entry = Entry(root, width=40)
phone_entry.pack()

add_button = Button(root, text="Add Contact", command=add_contact, width=20)
add_button.pack(pady=10)

delete_button = Button(root, text="Delete Contact", command=delete_contact, width=20)
delete_button.pack(pady=10)

clear_button = Button(root, text="Clear Contacts", command=clear_contacts, width=20)
clear_button.pack(pady=10)

contact_list = Listbox(root, width=60, height=15)
contact_list.pack(pady=20)

contact_list.bind('<<ListboxSelect>>', get_selected_contact)

root.mainloop()