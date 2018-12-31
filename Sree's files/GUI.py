from tkinter import *
from tkinter import Frame
from tkinter.dnd import Tester as Dragwindow, Icon as Dragable

root = Tk()

#root.withdraw()
#main=Dragwindow(root)


#def make_btn(): #make a new 'B' button
#    Dragable('anchor').attach(main.canvas)


title = Label(root, text="Items", fg="black")
# placing the title top center
title.place(x=25, y=10)
title.config(font=("Calibri", 20))

frame = Frame(root, bg="blue")

Anchor = Button(frame, text="Anchor", bg="grey", fg="black", padx = 20)
Anchor.place(x=25, y=60)
Anchor.config(font=("Calibri", 15))


Tags = Button(root, text="Tag", bg="grey", fg="black", padx = 35)
Tags.place(x=25, y=110)
Tags.config(font=("Calibri", 15))


Eqip = Button(root, text="Equipment", bg="grey", fg="black", padx = 4)
Eqip.place(x=25, y=160)
Eqip.config(font=("Calibri", 15))

work = Button(root, text="Workers", bg="grey", fg="black", padx = 15)
work.place(x=25, y=210)
work.config(font=("Calibri", 15))

road = Button(root, text="Road", bg="grey", fg="black", padx = 30)
road.place(x=25, y=260)
road.config(font=("Calibri", 15))

UA = Button(root, text="Unsafe Area", bg="grey", fg="black")
UA.place(x=25, y=310)
UA.config(font=("Calibri", 15))

OA = Button(root, text="Other Area", bg="grey", fg="black", padx = 5)
OA.place(x=25, y=360)
OA.config(font=("Calibri", 15))

SR = Button(root, text="Safety Rules", bg="white", fg="black")
SR.place(x=25, y=410)
SR.config(font=("Calibri", 15))

NP = Button(root, text="New Project", bg="white", fg="black")
NP.place(x=525, y=10)
NP.config(font=("Calibri", 15))

SP = Button(root, text="Save Project", bg="white", fg="black")
SP.place(x=650, y=10)
SP.config(font=("Calibri", 15))

LP = Button(root, text="Load Project", bg="white", fg="black")
LP.place(x=775, y=10)
LP.config(font=("Calibri", 15))

root.mainloop()
