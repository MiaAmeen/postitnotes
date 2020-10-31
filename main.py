'''
Created on Jan 4, 2020

@author:
'''
from tkinter import *
import time
from datetime import datetime
from random import choice

root = Tk()
root.geometry('800x600')

wall= PhotoImage(file= "/Users/destroyerofworlds/Documents/Gum3/wall.png")
BG = Label(root, image= wall)
BG.place(x=0, y=0, relwidth=1, relheight=1)
prplegumPng= PhotoImage(file= "/Users/destroyerofworlds/Documents/Gum3/prpleGum.png")
gumPng= PhotoImage(file= "/Users/destroyerofworlds/Documents/Gum3/gum.png")
blugumPng= PhotoImage(file= "/Users/destroyerofworlds/Documents/Gum3/blugum.png")
greengumPng= PhotoImage(file= "/Users/destroyerofworlds/Documents/Gum3/greengum.png")

colors= [['magenta',prplegumPng],['pink',gumPng],['light blue',blugumPng],['light green',greengumPng]]

def new(X,Y):
    td= datetime.today().strftime("%d/%m/%y %H:%M\n\n")
    color= choice(colors)

    def toggle(event):
        note.lift(event.widget)

    def untoggle(event):
        note.lower(BG)

    def Disable(event):
        try:
            print(note.get(CURRENT), "<location")

        except BaseException as msg:
            print(msg)

        finally:
            note.pi= note.place_info()
            print(note.pi)
            note.unbind('<Return>')
            note.unbind('<FocusOut>')
            event.widget.config(state= DISABLED)
            event.widget.lower(BG)
            gum.bind('<Button>',toggle)
            gum.bind('<Leave>',untoggle)

    gum = Label(root, image = color[1])
    gum.place(x= X, y= Y, anchor= CENTER)

    note = Text(root, height= 8, width=16, bg= color[0], bd= 0,font= ('Times',10), wrap= WORD, padx= 2, pady= 2)
    note.insert(INSERT,td)
    note.place(x= (X), y= Y, anchor= CENTER)
    note.focus()
    note.bind('<Return>',Disable)
    note.bind('<FocusOut>',Disable)

def newgum():
    def unbind(event):
        A= event.x
        B= event.y
        new(A,B)
        BG.unbind('<Button>')

    BG.bind('<Button>',unbind)

def delgum():
    def unbind(event):
        widg= str(event.widget)
        if event.widget== BG or widg== '.add' or widg== '.remove':
            print('error')
            pass
        else:
            event.widget.destroy()
            print('destroyed')
        root.unbind('<Button>')

    root.bind('<Button>',unbind)

def old(X,Y):
    td= datetime.today().strftime("%d/%m/%y %H:%M\n\n")
    color= choice(colors)

    def toggle(event):
        note.lift(event.widget)

    def untoggle(event):
        note.lower(BG)

    gum = Label(root, image = color[1])
    gum.place(x= X, y= Y, anchor= CENTER)

    note = Text(root, height= 8, width=16, bg= color[0], bd= 0,font= ('Times',10), wrap= WORD, padx= 2, pady= 2)
    note.insert(INSERT,td)
    note.place(x= (X), y= Y, anchor= CENTER)

add= Button(root, name= 'add',text= 'ADD',command= newgum, font= ('Times',20)).place(x= 100,y=100, anchor= CENTER)
remove= Button(root, name= 'remove', text= 'REMOVE',command= delgum, font= ('Times',20)).place(x= 100,y=200, anchor= CENTER)
root.mainloop()
