import tkinter.ttk
from tkinter import *
import requests
from PIL import ImageTk, Image

def f2():
    """This function is called when the 'Get Weather' button is clicked.
    It displays a frame which consists of weather information."""
    frame2 = Frame(ui)
    frame2.configure(bg="#2196f3", width=300, height=300)
    frame2.propagate(False)
    frame2.place(y=30)

    # Labels for weather information
    weather = Label(frame2, text="Weather :", font="arial 12 bold", bg="#2196f3", fg="black")
    weather.place(x=15, y=20)
    weather_r = Label(frame2, text="", font="arial 12 bold", bg="#2196f3", fg="white")
    weather_r.place(x=150, y=20)

    temperature = Label(frame2, text="Temperature :", font="arial 12 bold", bg="#2196f3", fg="black")
    temperature.place(x=15, y=60)
    temperature_r = Label(frame2, text="", font="arial 12 bold", bg="#2196f3", fg="white")
    temperature_r.place(x=150, y=60)

    pressure = Label(frame2, text="Pressure :", font="arial 12 bold", bg="#2196f3", fg="black")
    pressure.place(x=15, y=100)
    pressure_r = Label(frame2, text="", font="arial 12 bold", bg="#2196f3", fg="white")
    pressure_r.place(x=150, y=100)

    humidity = Label(frame2, text="Humidity :", font="arial 12 bold", bg="#2196f3", fg="black")
    humidity.place(x=15, y=140)
    humidity_r = Label(frame2, text="", font="arial 12 bold", bg="#2196f3", fg="white")
    humidity_r.place(x=150, y=140)

    windspeed = Label(frame2, text="Wind Speed :", font=("arial", 12, "bold"), bg="#2196f3", fg="black")
    windspeed.place(x=15, y=180)
    windspeed_r = Label(frame2, text="", font=("arial", 12, "bold"), bg="#2196f3", fg="white")
    windspeed_r.place(x=150, y=180)

    city = cityname.get()
    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f80454e8694580f0740f9a511461da8a").json()
    weather_r.config(text=data["weather"][0]["description"])
    temperature_r.config(text=data["main"]["temp"])
    pressure_r.config(text=data["main"]["pressure"])
    humidity_r.config(text=data["main"]["humidity"])
    windspeed_r.config(text=data["wind"]["speed"])

# Create the main UI window
ui = Tk()
ui.geometry("300x300")
ui.title("Internship Task-3")
ui.config(bg="lightblue")
ui.maxsize(500, 400)

# Set the background image for the entire window
image_path = "Weather.jpg"
img = Image.open(image_path)
img = ImageTk.PhotoImage(img)
background_label = Label(ui, image=img)
background_label.place(relwidth=1, relheight=1)

# Display the header text
txt = Label(ui, text="Weather Application", fg="black", font=("Lucida Handwriting", 15, "italic"), bg="#2196f3")
txt.pack(pady=5)
frame1=Frame(ui,bg="lightblue")
frame1.pack(padx=10)

# Frame to hold city selection and 'Get Weather' button
frame1 = Frame(ui, bd=5, bg="#90caf9")  # Use a different background color
frame1.pack(padx=10)

# Label and ComboBox for city selection with improved styling
country = Label(frame1, text="Select or enter city name", bg="#90caf9", font=("arial", 12, "italic"), fg="black")
country.pack()

city_list = ["Hyderabad", "Warangal", "Nizamabad", "Karimnagar", "Ramagundam", "Khammam", "Mahbubnagar", "Nalgonda",
             "Adilabad", "Siddipet", "Miryalaguda"]

cityname = StringVar()

cities = tkinter.ttk.Combobox(frame1, values=city_list, font="arial 10", textvariable=cityname)
cities.pack()

# Button to get weather information with improved styling
bt1 = Button(ui, text="Get Weather Info", command=f2, font="timenewroman 8 italic", borderwidth=5, bg="#2196f3", fg="white")
bt1.place(relx=0.5, rely=0.50, relwidth=0.5, anchor='n')

ui.mainloop()
