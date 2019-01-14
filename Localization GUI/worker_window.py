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

import worker_window_support
input_data = open("Config.json", "r")
json_data = json.load(input_data)
tags = [json_data["tags1"]]
ip = []
for i in tags:
    for j in range(len(i)):
        ip.append(i[j]["ip"])

def vp_start_gui(self):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    worker_window_support.set_Tk_var()
    top = worker_window (root)
    worker_window_support.init(root, top)
    root.mainloop()

w = None
def create_worker_window(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    worker_window_support.set_Tk_var()
    top = worker_window (w)
    worker_window_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_worker_window():
    global w
    w.destroy()
    w = None

class worker_window:
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

        top.geometry("600x346+650+150")
        top.title("Worker")
        top.configure(background="#ffffff")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.15, rely=0.173, height=46, width=162)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Worker Name :''')
        self.Label1.configure(width=162)

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.45, rely=0.173,height=44, relwidth=0.44)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=264)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.15, rely=0.405, height=56, width=172)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Tag Allocated :''')
        self.Label2.configure(width=172)

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1['values'] = ip
        self.TCombobox1.place(relx=0.45, rely=0.405, relheight=0.133
                , relwidth=0.445)
        self.TCombobox1.configure(textvariable=worker_window_support.combobox)
        self.TCombobox1.configure(width=267)
        self.TCombobox1.configure(takefocus="")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.4, rely=0.723, height=43, width=116)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#f3f3f3")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''SAVE''')
        self.Button1.configure(width=116)

if __name__ == '__main__':
    vp_start_gui()





