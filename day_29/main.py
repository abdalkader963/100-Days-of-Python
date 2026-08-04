import customtkinter as ctk
import tkinter as tk
BG="#2b2b2b"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_ent.get()
    email = user_ent.get()
    pas = password_ent.get()
    with open("./day_29/data.txt" , mode="a") as data:
        data.write(f"Website:{web} | Email/Username:{email} | Password:{pas}\n")
    website_ent.delete(0, "end")
    password_ent.delete(0, "end")
    user_ent.delete(0, "end")
    website_ent.focus_set()

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
password_but = ctk.CTkButton(master=window , text="Generate Password")
password_but.grid(column=3 , row=4,pady=5 , padx=5)

add_but = ctk.CTkButton(master=window , text="Add" , command=save)
add_but.grid(column=2 , row=5 , columnspan=2 ,sticky="ew" ,pady=5 , padx=5)












window.mainloop()


