from guizero import App, TextBox, Drawing,Combo,Slider

def draw_meme():
    meme.clear()
    meme.image(0,0,"PythonGUI/cat.jpg")
    meme.text(20,20, top_text.value)
    meme.text(20,320,bottom_text.value)
    meme.text(
    20,20, top_text.value,color= colors.value,
    size=sizeSlider.value,
    font=fonts.value
    )
    meme.text(
    20,320,bottom_text.value,
    color=colors.value,
    size=sizeSlider.value,
    font=fonts.value
    )

app = App("meme")
top_text = TextBox(app, "",command=draw_meme)
bottom_text = TextBox(app, "",command=draw_meme)
colors = Combo(app, options=["black","white","blue","green"],command=draw_meme)
fonts = Combo(app,options=["times new roman", "verdana", "courier", "impact"])



sizeSlider = Slider(app, start=20, end=40, command=draw_meme)
meme = Drawing(app,width="fill", height="fill" )
draw_meme()
app.display()