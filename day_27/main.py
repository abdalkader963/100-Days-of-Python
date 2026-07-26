import tkinter as tk

window = tk.Tk()
window.title("Mile to Km converter")
window.config(padx=20 , pady=20)

is_equal = tk.Label(text = "Is equal to")
is_equal.grid(column=1,row=2)

miles = tk.Label(text="Miles")
miles.grid(column=3 , row=1)

kms = tk.Label(text="0")
kms.grid(column=2 , row=2)

km=tk.Label(text="Km")
km.grid(column=3 , row=2)

def cal():
    try:
        miles=float(entry.get())
    except ValueError:
        miles=0
    km = round(miles*1.609)
    kms.config(text=f"{km}")

button = tk.Button(text="Calculate" ,command=cal )
button.grid(column=2,row=3)

entry = tk.Entry(width=7)
entry.grid(column=2,row=1)





window.mainloop()