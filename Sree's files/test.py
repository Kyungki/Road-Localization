from tkinter import *
from tkinter.dnd import Tester as Dragwindow, Icon as Dragable

root=Tk() #make our root window
root.withdraw() #hide it since we don't need it
main=Dragwindow(root) #make our actual main window, it can have dragable objects on
#def create():
#    Dragable('B').attach(main.canvas)
def make_btn(): #make a new 'B' button
    Dragable('A').attach(main.canvas) #make it and attach it to our window's functioning part, the canvas
Button(main.top, text='Anchor', command=make_btn).pack()#make a button 'A' for our window
mainloop() #start the mainloop