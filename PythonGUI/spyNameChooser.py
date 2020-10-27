# Imports ---------------
from guizero import App, Text, PushButton,TextBox
from random import choice

# Functions -------------
def choose_name():
    #print("Button was pressed")
    first_names = ["Mike","John","Nick","Smokey","Hobo"]
    last_names = ["Williams","Johnson","Kennedy","Cateye","Flamingo"]

    spy_Name = choice(first_names) + " " + choice(last_names)
    #print(spy_Name)
    name.value = spy_Name

# App -------------------
app = App("TOP SECRET")
# Widgets ---------------
title = Text(app, "Push the red button to find out your spy name")
button1 = PushButton(app, choose_name, text="Tell me")
name = Text(app, text="")
button1.bg = "red"
button1.text_size = 20
button1.text_color = "black"








# Display ---------------
app.display()
