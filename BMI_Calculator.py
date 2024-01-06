from tkinter import *
import tkinter as tk

def calculate_bmi():
    height = slider1.get()
    weight = slider2.get()
    if not (0 < height <= 230 and 0 < weight <= 200):
        result.config(text="Please enter valid values for height and weight.")
        return

    bmi = weight / (height / 100) ** 2

    if bmi <= UNDERWEIGHT_THRESHOLD:
        result.config(text=f"Your BMI is {bmi:.2f}\nYou are underweight", fg="blue")
    elif UNDERWEIGHT_THRESHOLD < bmi < HEALTHY_THRESHOLD:
        result.config(text=f"Your BMI is {bmi:.2f}\nYou are healthy", fg="green")
    elif bmi >= HEALTHY_THRESHOLD:
        result.config(text=f"Your BMI is {bmi:.2f}\nYou are overweight (obese)", fg="red")

UNDERWEIGHT_THRESHOLD = 18.5
HEALTHY_THRESHOLD = 25

ui = Tk()
ui.title("Internship Task-1")
ui.geometry("400x450")
ui.resizable(False, False)
ui.configure(bg="#f0f0f0")

# Frame for the title
f0 = Frame(ui, bg="#f0f0f0", borderwidth=6)
f0.pack()

# Title label
htext = Label(f0, text="BMI CALCULATOR", bg="lightblue", borderwidth=6, width=450, font="Arial 18 bold")
htext.pack()

# Frame for height slider
f1 = Frame(ui, bg="white", borderwidth=6)
f1.place(x=20, y=80)
htext = Label(f1, text="HEIGHT (cm's)", fg="#333", bg="white", font="Arial 12 bold")
htext.pack()
slider1 = tk.Scale(f1, from_=0, to=230, orient="horizontal", length=200)
slider1.pack()

# Frame for weight slider
f2 = Frame(ui, bg="white", borderwidth=6)
f2.place(x=20, y=200)
htext = Label(f2, text="WEIGHT (kg's)", fg="#333", bg="white", font="Arial 12 bold")
htext.pack(pady=0)
slider2 = tk.Scale(f2, from_=0, to=200, orient="horizontal", length=200)
slider2.pack(pady=0)

# Frame for the result button
f3 = Frame(ui, bg="white")
f3.place(y=300)

b = Button(f3, text="Compute BMI", bg="#4CAF50", fg="#f0f0f0", font="Arial 14 bold", command=calculate_bmi)
b.pack(pady=20, padx=120)

# Frame for the result label
f4 = Frame(ui, bg="lightblue", borderwidth=6, width=450, height=80)
f4.place(y=400)

# Result label
result = Label(ui, text="", font="Arial 13 bold", bg="lightblue", fg="#333")
result.place(x=17, y=400)

ui.mainloop()
from tkinter import *
import tkinter as tk

def calculate_bmi():
    height = slider1.get()
    weight = slider2.get()
    if not (0 < height <= 230 and 0 < weight <= 200):
        result.config(text="Please enter valid values for height and weight.")
        return

    bmi = weight / (height / 100) ** 2

    if bmi <= UNDERWEIGHT_THRESHOLD:
        result.config(text=f"Your BMI is {bmi:.2f}\nYou are underweight", fg="blue")
    elif UNDERWEIGHT_THRESHOLD < bmi < HEALTHY_THRESHOLD:
        result.config(text=f"Your BMI is {bmi:.2f}\nYou are healthy", fg="green")
    elif bmi >= HEALTHY_THRESHOLD:
        result.config(text=f"Your BMI is {bmi:.2f}\nYou are overweight (obese)", fg="red")

UNDERWEIGHT_THRESHOLD = 18.5
HEALTHY_THRESHOLD = 25

ui = Tk()
ui.title("Internship Task-1")
ui.geometry("400x450")
ui.resizable(False, False)
ui.configure(bg="#f0f0f0")

# Frame for the title
f0 = Frame(ui, bg="#f0f0f0", borderwidth=6)
f0.pack()

# Title label
htext = Label(f0, text="BMI CALCULATOR", bg="lightblue", borderwidth=6, width=450, font="Arial 18 bold")
htext.pack()

# Frame for height slider
f1 = Frame(ui, bg="white", borderwidth=6)
f1.place(x=20, y=80)
htext = Label(f1, text="HEIGHT (cm's)", fg="#333", bg="white", font="Arial 12 bold")
htext.pack()
slider1 = tk.Scale(f1, from_=0, to=230, orient="horizontal", length=200)
slider1.pack()

# Frame for weight slider
f2 = Frame(ui, bg="white", borderwidth=6)
f2.place(x=20, y=200)
htext = Label(f2, text="WEIGHT (kg's)", fg="#333", bg="white", font="Arial 12 bold")
htext.pack(pady=0)
slider2 = tk.Scale(f2, from_=0, to=200, orient="horizontal", length=200)
slider2.pack(pady=0)

# Frame for the result button
f3 = Frame(ui, bg="white")
f3.place(y=300)

b = Button(f3, text="Compute BMI", bg="#4CAF50", fg="#f0f0f0", font="Arial 14 bold", command=calculate_bmi)
b.pack(pady=20, padx=120)

# Frame for the result label
f4 = Frame(ui, bg="lightblue", borderwidth=6, width=450, height=80)
f4.place(y=400)

# Result label
result = Label(ui, text="", font="Arial 13 bold", bg="lightblue", fg="#333")
result.place(x=17, y=400)

ui.mainloop()
