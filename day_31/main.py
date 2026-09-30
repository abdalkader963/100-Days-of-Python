BACKGROUND_COLOR = "#B1DDC6"
import customtkinter as ctk
import tkinter as tk 
import pandas as pd
import random

"""functionality"""

try:
    data = pd.read_csv("./data/words_to_learn.csv")
    words = data.to_dict(orient="records")
    
except (FileNotFoundError):
    data = pd.read_csv("./data/french_words.csv")
    words = data.to_dict(orient="records")

current_card = {}
timer = None

def right():
    words.remove(current_card)
    data_to_save = pd.DataFrame(words)
    data_to_save.to_csv("./data/words_to_learn.csv", index=False)
    new_flash()

def flip_card():
    canvas.itemconfig(lang , text="English")
    canvas.itemconfig(word , text=current_card["English"])
    canvas.itemconfig(image_fr , image=back_image)

def new_flash():
    global current_card, timer
    if timer:
        window.after_cancel(timer)
    try:
        current_card = random.choice(words)
        canvas.itemconfig(image_fr, image=front_image)
        canvas.itemconfig(lang, text="French")
        canvas.itemconfig(word, text=current_card["French"])
        timer = window.after(3000, flip_card)
    except (IndexError):
        canvas.itemconfig(image_fr, image=front_image)
        canvas.itemconfig(lang, text="Done!", fill="black", font=("Arial", 50, "bold"))
        canvas.itemconfig(word,text="Great job! All words learned.",fill="black",font=("Arial", 24, "normal"))
        return
    
window = ctk.CTk()
window.config(padx=50 , pady=50 , background=BACKGROUND_COLOR)  



"""USER INTERFACE"""


#FRONT CARD
canvas = tk.Canvas(width=800 , height=526 , bg= BACKGROUND_COLOR , highlightthickness=0)
front_image = tk.PhotoImage(file="./images/card_front.png")
image_fr = canvas.create_image(400,263, image = front_image)

back_image = tk.PhotoImage(file="./images/card_back.png")
#TEXT
lang = canvas.create_text(400 , 150 , text="" , font=("Arial" , 40 , "italic"))
word = canvas.create_text(400 , 263 , text="" , font=("Arial" , 60 , "bold"))
canvas.grid(column=1 , row=1 ,columnspan=2)

#BUTTONS
right_image=tk.PhotoImage(file="./images/right.png")
right_bu = tk.Button(image=right_image, highlightthickness=0, bd=0 , command=right)
right_bu.grid(column=2 , row=2)

wrong_image=tk.PhotoImage(file="./images/wrong.png")
wrong_bu = tk.Button(image=wrong_image, highlightthickness=0, bd=0, command=new_flash)
wrong_bu.grid(column=1 , row=2)






new_flash()
window.mainloop()