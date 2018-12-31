from tkinter import * #global tkinter import
from tkinter.dnd import Tester as Dragwindow, Icon as Draggable #import screen and object dragable classes

root=Tk() #make our root window
root.withdraw() #hide it since we don't need it

main=Dragwindow(root) #make our actual main window, it can have dragable objects on


def open_window(self):
    top = Toplevel()


def make_btn(self): #make a new 'B' button
    Draggable('Anchor').attach(main.canvas) #make it and attach it to our window's functioning part, the canvas


def make_btn2(self): #make a new 'B' button
    Draggable('TAG').attach(main.canvas)


anchor = Button(main.top, text='Anchor')
anchor.bind('<Button-1>', make_btn)
anchor.bind('<Double-Button-1>', open_window)
anchor.pack(side=TOP)

tag = Button(main.top, text='TAG')
tag.pack(side=TOP)
tag.bind('<Button-3>', make_btn2)
tag.bind('<Double-Button-1>', open_window)

mainloop() #start the mainloop