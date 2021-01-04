from tkinter import *
from tkinter import messagebox

#create and set window
window=Tk(className="Convert KG")
window.geometry("550x100")
window.configure(bg='green')

#function to do the conversion and set inser the values
def kgtoothers():
    grams= float(e1_value.get())*1000
    pounds= float(e1_value.get())*2.2
    ounces= float(e1_value.get())*35.2
    t1.insert(END,grams)
    t2.insert(END,pounds)
    t3.insert(END,ounces)

def successMessage():
    messagebox.showinfo("Success","Converted from KG to Grams,Pounds,and Ounces")   

#button 1
b1=Button(window,text ="Go",command=lambda: [kgtoothers(),successMessage()])
b1.grid(row=0,column=0)

#label 1
labelText = StringVar()
label1 = Label(window,textvariable=labelText,relief=RAISED)
label1.grid(row=0,column=2)
labelText.set("Kg")

#entry widget set
e1_value=StringVar()
e1=Entry(window)
e1= Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

#text box 1
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

#text box 2
t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

#text box 3
t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)

window.mainloop() 



""" from tkinter import *
def mult(n):
    print (n*3)

top = Tk()
B1 = Button(top, text = "Enter Number", command = lambda: mult(5))
B1.pack()
top.mainloop() """