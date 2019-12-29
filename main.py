import tkinter
from datetime import date,time,datetime

root = tkinter.Tk()
root.geometry('500x500')

class Notes:

  def __init__(self, text, owner, Type, date):
    self.text= text
    self.owner= owner
    self.date= date.today()
    self.type= Type

  def open():
    pass


def nono():
  def callback(event):
      print ("clicked at", event.x, event.y)

  canvas= tkinter.Frame(root, width=500, height=500)
  canvas.bind("<Button-1>", callback)
  canvas.pack()

root.mainloop()
