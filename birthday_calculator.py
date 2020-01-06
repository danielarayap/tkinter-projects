"""
In this age calculator app, users can type in their date of birth, and the app will calculate and display their age
automatically. Isn’t that cool?
"""


import tkinter as tk
import datetime
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry('500x780')
window.title('Age Calculator App')

name = tk.Label(text="Name")
name.grid(column=0, row=1)
year = tk.Label(text="Year")
year.grid(column=0, row=2)
month = tk.Label(text="Month")
month.grid(column=0, row=3)
date = tk.Label(text="Day")
date.grid(column=0, row=4)

nameEntry = tk.Entry()
nameEntry.grid(column=1, row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1, row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1, row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1, row=4)


def get_input():
    person_name = nameEntry.get()
    person = Person(person_name, datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get())))
    text_area = tk.Text(window, height=10, width=25)
    text_area.grid(column=1, row=6)
    answer = 'Heyy {}!!!. You are {} years old!'.format(person_name, person.age())
    text_area.insert(tk.END, answer)


button = tk.Button(window, text='Calculate age', command=get_input, bg='pink')
button.grid(column=1, row=5)


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birth_date = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year
        return age


image = Image.open('Birthday-homepage.jpg')
image.thumbnail((300, 300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)


window.mainloop()
