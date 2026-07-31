import customtkinter as ctk
import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#83b890"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
my_timer = None
marks =""
# ---------------------------- TIMER RESET ------------------------------- # 
def rest_timer():
    global marks
    marks = ""
    check_marks.configure(text = marks)
    window.after_cancel(my_timer)
    canvas.itemconfig(timer , text="00:00")
    lab.configure(text="Timer" , text_color=GREEN)
    global reps 
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global my_timer
    if my_timer != None:
        window.after_cancel(my_timer)
    global reps
    reps +=1
    work_secs = WORK_MIN * 60
    short_break_Secs = SHORT_BREAK_MIN * 60
    long_brake_secs = LONG_BREAK_MIN * 60
    if  reps %2 ==0:
        lab.configure(text="Short brake" , text_color=PINK)
        countdown(short_break_Secs)
    elif reps % 8 ==0:
        lab.configure(text="Brake" , text_color=RED)
        countdown(long_brake_secs)
    else:
        lab.configure(text="Work" , text_color=GREEN)
        countdown(work_secs)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(time):
    global repr
    mins= math.floor(time/60)
    secs = time % 60    
    if secs == 0 :
        secs = "00"
    elif secs <10:
        secs = f"0{secs}"
    if time>=0:
        global my_timer
        my_timer=window.after(1000 , countdown , time -1)
        canvas.itemconfig(timer , text= f"{mins}:{secs}")
    if time == 0:
        start_timer()    
        global marks 
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks+= "✓"
        check_marks.configure(text = marks)
# ---------------------------- UI SETUP ------------------------------- #
window = ctk.CTk()
window.title("pomodoro")
window.config(padx=100 , pady=50)

#tomato pic
canvas=tk.Canvas(width=200 , height=224 , bg="#2b2b2b" , highlightthickness=0)
tomato=tk.PhotoImage(file="day_28/tomato.png")
canvas.create_image(100,112,image=tomato)
#timer
timer = canvas.create_text(100 , 130 , text="00:00" , font=(FONT_NAME , 35 , "bold" ))
canvas.grid(column=2 , row=2 , padx=10 , pady=10)

#label
lab = ctk.CTkLabel(master=window , text="Timer" , text_color=GREEN ,font=(FONT_NAME , 40 , "bold"))
lab.grid(column=2 , row = 1 , padx=10 , pady=10)

#buttons
rest_bu=ctk.CTkButton(master=window , text="Rest" , command=rest_timer)
rest_bu.grid(column=3 , row=3 , padx=10 , pady=10)
##
start_bu=ctk.CTkButton(master=window , text="Start" , command=start_timer)
start_bu.grid(column=1 , row=3 , padx=10 , pady=10 )
#check marks
check_marks = ctk.CTkLabel( master=window,text="" , text_color=GREEN )
check_marks.grid(column=2 , row=3)


window.mainloop()
