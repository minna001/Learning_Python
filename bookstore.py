from tkinter import *
import tkinter.messagebox
import backend

def get_selected_row(event):
    try:
        if list1.curselection():
            global selected_tuple
            index=list1.curselection()[0]
            selected_tuple=list1.get(index)
            e1.delete(0,END)
            e1.insert(END,selected_tuple[1])
            e2.delete(0,END)
            e2.insert(END,selected_tuple[2])
            e3.delete(0,END)
            e3.insert(END,selected_tuple[3])
            e4.delete(0,END)
            e4.insert(END,selected_tuple[4])
    except IndexError:
         pass
    

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),title_Author.get(),title_year.get(),title_isbn.get()):
        list1.insert(END,row)

def add_command():
    msgbox1 = tkinter.messagebox.askquestion("Correct?","Are Your Entry Fields Correct?")
    if msgbox1 == 'yes':
        tkinter.messagebox.showinfo("BookStore",title_text.get() + " " + "Added")
        backend.insert(title_text.get(),title_Author.get(),title_year.get(),title_isbn.get())
        list1.delete(0,END)
        list1.insert(END,(title_text.get(),title_Author.get(),title_year.get(),title_isbn.get()))
    else:
        tkinter.messagebox.showinfo('Return','You will now return to the application screen')

def delete_command():
    msgbox2 = tkinter.messagebox.askquestion("askquestion", "Are you sure?")
    if msgbox2 == 'yes':
        tkinter.messagebox.showinfo("Success",selected_tuple()[0] + " " + "Deleted",icon='warning')
        backend.delete(selected_tuple[0])
    else:
        tkinter.messagebox.showinfo('Return','You will now return to the application screen')


def update_command():
    msgbox3= tkinter.messagebox.askyesnocancel(title="Update?", message="Are You sure You want to update" + title_text.get() + " " + "?")
    if msgbox3 == 'yes':
        backend.update(selected_tuple[0],title_text.get(),title_Author.get(),title_year.get(),title_isbn.get())
        tkinter.messagebox.showinfo("Success")
    else:
        tkinter.messagebox.showinfo('Return','You will now return to the application screen')


def close_command():
    print("Window Closed" , window.destroy())


window=Tk()
window.wm_title("Bookstore")

############################################ Labels
l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)
###########################################
#buttons

#button1
b1=Button(window,text="view all",width=12,bg='brown',fg='white',command=view_command)
b1.grid(row=2,column=3)
########
#button2
b2=Button(window,text="Search entry",width=12,bg='brown',fg='white',command=search_command)
b2.grid(row=3,column=3)
########
#button3
b3=Button(window,text="Add entry",width=12,bg='brown',fg='white',command=add_command)
b3.grid(row=4,column=3)
########
#button4
b4=Button(window,text="Update",width=12,bg='brown',fg='white',command=update_command)
b4.grid(row=5,column=3)
########
#button5
b5=Button(window,text="Delete",width=12,bg='brown',fg='white',command=delete_command)
b5.grid(row=6,column=3)
########
#button6
b6=Button(window,text="Close",width=12,bg='brown',fg='white',command=close_command)
b6.grid(row=7,column=3)
########

#############################################Boxes
##box 1
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

##box 2
title_Author=StringVar()
e2=Entry(window,textvariable=title_Author)
e2.grid(row=0,column=3)

##box 3
title_year=StringVar()
e3=Entry(window,textvariable=title_year)
e3.grid(row=1,column=1)

##box 4
title_isbn=StringVar()
e4=Entry(window,textvariable=title_isbn)
e4.grid(row=1,column=3)

####################################### List view
list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)
list1.bind('<<listboxSelect>>',get_selected_row)

#############################################Scroll bar
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
sb1.configure(command=list1.yview)
list1.configure(yscrollcommand=sb1.set)
############################################

window.mainloop()


