import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import pyperclip
BG="#2b2b2b"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generat_password():
   
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_ent.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_ent.get()
    email = user_ent.get()
    pas = password_ent.get()
    if email == "" or web =="" or pas == "":
        messagebox.showerror(title="ERORR" , message="make sure u did fill all the empty boxes")
    else:    
        mssg=messagebox.askokcancel(title=website , message="Are you sure you want to save?")
        if mssg :
            with open("./day_29/data.txt" , mode="a") as data:
                data.write(f"Website:{web} | Email/Username:{email} | Password:{pas}\n")
            website_ent.delete(0, "end")
            password_ent.delete(0, "end")
            user_ent.delete(0, "end")
            website_ent.focus_set()
        else:
            pass
# ---------------------------- UI SETUP ------------------------------- #
window = ctk.CTk()
window.minsize(width=400 , height=400)
window.configure(fg_color=BG ,pady=50 , padx=50 )
window.title("Passowrd Manager")

#LOGO
canvas = ctk.CTkCanvas(width=200 , height=200 , bg="#2b2b2b" , highlightthickness=0)
logo = tk.PhotoImage(file="./day_29/logo.png")
pic =  canvas.create_image(100 , 100 ,image=logo)
canvas.grid(column=2 , row=1 ,padx=20,pady=20)

#Labels
website = ctk.CTkLabel(master=window , text="Website:")
website.grid(column=1 , row=2,pady=5 , padx=5, sticky="w")

user = ctk.CTkLabel(master=window , text="Email/Username:")
user.grid(column=1 , row=3,pady=5 , padx=5, sticky="w")

password = ctk.CTkLabel(master=window , text="Password:")
password.grid(column=1 , row=4,pady=5 , padx=5, sticky="w")

#Entries
website_ent = ctk.CTkEntry(master=window , width=35)
website_ent.grid(column = 2 , row = 2 ,columnspan=2 , sticky="ew",pady=5 , padx=5)
window.update()
website_ent.focus_set()

user_ent = ctk.CTkEntry(master=window , width=35)
user_ent.grid(column = 2 , row = 3 ,columnspan=2 , sticky="ew",pady=5 , padx=5)

password_ent = ctk.CTkEntry(master=window , width=35)
password_ent.grid(column = 2 , row = 4 ,sticky="ew",pady=5 , padx=5)

#buttons 
password_but = ctk.CTkButton(master=window , text="Generate Password" , command=generat_password)
password_but.grid(column=3 , row=4,pady=5 , padx=5)

add_but = ctk.CTkButton(master=window , text="Add" , command=save)
add_but.grid(column=2 , row=5 , columnspan=2 ,sticky="ew" ,pady=5 , padx=5)











window.mainloop()


