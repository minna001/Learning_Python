from guizero import App, Text,Combo, PushButton
from string import ascii_letters

def flash_text():
 if title.visible:
    title.hide()
 else:
    title.show()

def are_you_sure():
    if app.yesno("Confirmation","Are you sure?"):
        app.info("Thanks", "button pressed")
    else:
        app.error("ok","Cancelling")

app = App("it's all gone wrong", bg="dark green")
app.error("Application started", "Well done you started the application")

a_letter = Combo(app,options=" " + ascii_letters,align="left")
b_letter = Combo(app, options=" " + ascii_letters, align="left")
c_letter = Combo(app, options=" " + ascii_letters, align="left")
button = PushButton(app,command=are_you_sure)
title = Text(app, text="Some hard-to-read text", size="14",
font="Comic Sans", color="green")
app.repeat(1000,flash_text)
myText = Text(app,"This is an example of really bad GUI")
app.display()