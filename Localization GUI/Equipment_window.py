import sys
import json

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

import Equipment_window_support

input_data = open("Config.json", "r")
json_data = json.load(input_data)
tags = [json_data["tags1"]]
ip = []
for i in tags:
    for j in range(len(i)):
        ip.append(i[j]["ip"])
eq_type = ["Type-1", "Type-2", "Type-3"]

def vp_start_gui(self):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    Equipment_window_support.set_Tk_var()
    top = equip_window (root)
    Equipment_window_support.init(root, top)
    root.mainloop()

w = None
def create_equip_window(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    Equipment_window_support.set_Tk_var()
    top = equip_window (w)
    Equipment_window_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_equip_window():
    global w
    w.destroy()
    w = None

class equip_window:
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

        top.geometry("681x581+589+215")
        top.title("Equipment")
        top.configure(background="#ffffff")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.132, rely=0.103, height=46, width=182)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Equipment Type :''')
        self.Label1.configure(width=182)

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1['value'] = eq_type
        self.TCombobox1.place(relx=0.455, rely=0.103, relheight=0.079
                , relwidth=0.377)
        self.TCombobox1.configure(textvariable=Equipment_window_support.combobox)
        self.TCombobox1.configure(width=257)
        self.TCombobox1.configure(takefocus="")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.132, rely=0.224, height=46, width=212)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Tag Allocated :''')
        self.Label2.configure(width=212)

        self.TCombobox2 = ttk.Combobox(top)
        self.TCombobox2['values'] = ip
        self.TCombobox2.place(relx=0.455, rely=0.224, relheight=0.079
                , relwidth=0.377)
        self.TCombobox2.configure(textvariable=Equipment_window_support.combobox)
        self.TCombobox2.configure(width=257)
        self.TCombobox2.configure(takefocus="")

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.22, rely=0.344, height=46, width=142)
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Length :''')
        self.Label3.configure(width=142)

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.455, rely=0.344,height=44, relwidth=0.373)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=254)

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.22, rely=0.448, height=56, width=132)
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Breadth :''')
        self.Label4.configure(width=132)

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.455, rely=0.448,height=44, relwidth=0.373)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=254)

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.059, rely=0.551, height=46, width=222)
        self.Label5.configure(background="#ffffff")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font9)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Protective Area Length :''')
        self.Label5.configure(width=222)

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.455, rely=0.551,height=44, relwidth=0.373)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(width=254)

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.029, rely=0.654, height=46, width=242)
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Protective Area Breadth :''')
        self.Label6.configure(width=242)

        self.Entry4 = tk.Entry(top)
        self.Entry4.place(relx=0.455, rely=0.654,height=44, relwidth=0.373)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(width=254)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.396, rely=0.792, height=53, width=126)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#f3f3f3")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''SAVE''')
        self.Button1.configure(width=126)

if __name__ == '__main__':
    vp_start_gui()





