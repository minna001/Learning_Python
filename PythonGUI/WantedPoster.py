from guizero import App,Text,Picture

app = App("Wanted!")
app.bg = "#FBFBD0"
wanted_Text = Text(app,"WANTED")
wanted_Text.text_size = 59
wanted_Text.font = "Times New Roman"
catPic = Picture(app, image="PythonGUI/cat.jpg")



app.display()