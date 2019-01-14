import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import anchor_window_support
import json

input_data = open("Config.json", "r")
json_data = json.load(input_data)
anchors = [json_data["anchors1"]]
id = []
for i in anchors:
    for j in range(len(i)):
        id.append(i[j]["id"])

def vp_start_gui(self):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    anchor_window_support.set_Tk_var()
    top = Anchor_top (root)
    anchor_window_support.init(root, top)
    root.mainloop()

w = None
def create_Anchor_top(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    anchor_window_support.set_Tk_var()
    top = Anchor_top (w)
    anchor_window_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Anchor_top():
    global w
    w.destroy()
    w = None

class Anchor_top:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font9 = "-family Calibri -size 13 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450")
        top.title("Anchor")
        top.configure(background="#ffffff")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.117, rely=0.111, height=36, width=142)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Anchor ID :''')
        self.Label1.configure(width=142)

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1['values'] = id
        self.TCombobox1.place(relx=0.367, rely=0.111, relheight=0.08
                , relwidth=0.412)
        self.TCombobox1.configure(textvariable=anchor_window_support.combobox)
        self.TCombobox1.configure(width=247)
        self.TCombobox1.configure(takefocus="")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.067, rely=0.311, height=36, width=172)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''X - coordinate :''')
        self.Label2.configure(width=172)

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.367, rely=0.311,height=34, relwidth=0.407)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=244)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.067, rely=0.444, height=36, width=162)
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Y -  coordinate :''')
        self.Label3.configure(width=162)

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.367, rely=0.444,height=34, relwidth=0.407)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=244)

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.067, rely=0.578, height=36, width=172)
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Z - coordinate :''')
        self.Label4.configure(width=172)

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.367, rely=0.578,height=34, relwidth=0.407)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(width=244)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.383, rely=0.756, height=43, width=126)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#F3F3F3")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''SAVE''')
        self.Button1.configure(width=126)

if __name__ == '__main__':
    vp_start_gui()





