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

import tag_support

def vp_start_gui(self):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    tag_support.set_Tk_var()
    top = tag_toplevel (root)
    tag_support.init(root, top)
    root.mainloop()

input_data = open("Config.json", "r")
json_data = json.load(input_data)
tags = [json_data["tags1"]]
ip = []
for i in tags:
    for j in range(len(i)):
        ip.append(i[j]["ip"])



w = None
def create_tag_toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    tag_support.set_Tk_var()
    top = tag_toplevel (w)
    tag_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_tag_toplevel():
    global w
    w.destroy()
    w = None

class tag_toplevel:
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

        top.geometry("600x450+605+231")
        top.title("Tag")
        top.configure(background="#ffffff")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.133, rely=0.111, height=46, width=182)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Tag IP   :''')
        self.Label1.configure(width=182)

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1['values'] = ip
        self.TCombobox1.place(relx=0.4, rely=0.111, relheight=0.102
                , relwidth=0.428)
        self.TCombobox1.configure(textvariable=tag_support.combobox)
        self.TCombobox1.configure(width=257)
        self.TCombobox1.configure(takefocus="")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.1, rely=0.289, height=46, width=152)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''X- coordinate :''')
        self.Label2.configure(width=152)

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.4, rely=0.289,height=44, relwidth=0.423)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=254)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.083, rely=0.422, height=56, width=172)
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Y - coordinate :''')
        self.Label3.configure(width=172)

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.4, rely=0.444,height=44, relwidth=0.423)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=254)

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.083, rely=0.578, height=46, width=172)
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Z - coordinate :''')
        self.Label4.configure(width=172)

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.4, rely=0.578,height=44, relwidth=0.423)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(width=254)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.417, rely=0.756, height=43, width=96)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#f3f3f3")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''SAVE''')
        self.Button1.configure(width=96)

if __name__ == '__main__':
    vp_start_gui()





