"""
This is an app using Python’s Tkinter library. It's a user interface in which we can view three buttons: Rock, Paper,
and Scissors. Users of the app can press any button to make their choice.

In this game, we will be playing against the computer, that can also select its choice automatically (random). It is a
game with three choices: rock, paper, and scissors. Two players can play this game at a time. Each one has to choose
from the three options available.

So, both the user and the computer will choose their options. And then, we will apply the following rules.
    If the user chooses rock, and computer chooses scissors, rock wins.
    If the user chooses rock, and computer chooses paper, paper wins.
    If the user chooses scissors, and computer chooses paper, scissors wins.
    If both the choices are the same, then no one will win. Both the user and the computer will not get any points.
"""


import tkinter as tk
import random

window = tk.Tk()
window.geometry('200x300')
window.title('Rock Paper Scissors Game')

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ''
COMP_CHOICE = ''


def choice_to_number(choice):
    rps = {'rock': 0, 'paper': 1, 'scissors': 2}
    return rps[choice]


def number_to_choice(number):
    rps = {0: 'rock', 1: 'paper', 2: 'scissors'}
    return rps[number]


def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def result(human_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)
    if user == comp:
        print('Tie')
    elif (user - comp) % 3 == 1:
        print('You win')
        USER_SCORE += 1
    else:
        print('Computer wins')
        COMP_SCORE += 1
    text_area = tk.Text(window, height=12, width=30, bg='#FFFF99')
    text_area.grid(column=0, row=4)
    answer = "Your choice: {}\nComputer's Choice: {}\nYour Score: {}\nComputer Score: {}".\
        format(USER_CHOICE, COMP_CHOICE, USER_SCORE, COMP_SCORE)
    text_area.insert(tk.END, answer)


def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'rock'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'paper'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def scissors():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'scissors'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


rock_button = tk.Button(text="   Rock   ", bg="skyblue", command=rock)
paper_button = tk.Button(text="   Paper   ", bg="pink", command=paper)
scissors_button = tk.Button(text="   Scissors   ", bg="lightgreen", command=scissors)
rock_button.grid(column=0, row=1)
paper_button.grid(column=0, row=2)
scissors_button.grid(column=0, row=3)

window.mainloop()

# to run as .exe use -->  pyinstaller -F -w  rock_paper_scissors.py on the terminal where the script is located
# to add icon use --> pyinstaller -F -w -i  Cornmanthe3rd-Plex-Other-python.ico  rock_paper_scissors.py

