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

import main_support_module_support
import anchor_window as aw
import tag as tw
import Equipment_window as ew
import worker_window as ww

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    main_support_module_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    main_support_module_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font19 = "-family Calibri -size 13 -weight normal -slant roman"  \
            " -underline 0 -overstrike 0"
        font20 = "-family Calibri -size 12 -weight normal -slant roman"  \
            " -underline 0 -overstrike 0"
        font22 = "-family Calibri -size 16 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("1124x759+351+148")
        top.title("GUI")
        top.configure(background="#ffffff")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.018, rely=0.105, relheight=0.876
                , relwidth=0.173)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(width=195)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.103, rely=0.015, height=36, width=152)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font22)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Items''')
        self.Label1.configure(width=152)

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.051, rely=0.09, relheight=0.203, relwidth=0.897)

        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(background="#6495ED")
        self.Frame2.configure(width=175)

        self.Anchor_button = tk.Button(self.Frame2)
        self.Anchor_button.place(relx=0.114, rely=0.074, height=43, width=136)
        self.Anchor_button.configure(activebackground="#ececec")
        self.Anchor_button.configure(activeforeground="#000000")
        self.Anchor_button.configure(background="#ffffff")
        self.Anchor_button.configure(disabledforeground="#a3a3a3")
        self.Anchor_button.configure(font=font19)
        self.Anchor_button.configure(foreground="#000000")
        self.Anchor_button.configure(highlightbackground="#d9d9d9")
        self.Anchor_button.configure(highlightcolor="#000000")
        self.Anchor_button.configure(pady="0")
        self.Anchor_button.configure(text='''Anchor''')
        self.Anchor_button.configure(width=136)
        self.Anchor_button.bind("<Button-1>", aw.vp_start_gui)

        self.tag_button = tk.Button(self.Frame2)
        self.tag_button.place(relx=0.114, rely=0.519, height=43, width=136)
        self.tag_button.configure(activebackground="#ececec")
        self.tag_button.configure(activeforeground="#000000")
        self.tag_button.configure(background="#ffffff")
        self.tag_button.configure(disabledforeground="#a3a3a3")
        self.tag_button.configure(font=font19)
        self.tag_button.configure(foreground="#000000")
        self.tag_button.configure(highlightbackground="#d9d9d9")
        self.tag_button.configure(highlightcolor="black")
        self.tag_button.configure(pady="0")
        self.tag_button.configure(text='''Tags''')
        self.tag_button.configure(width=136)
        self.tag_button.bind("<Button-1>", tw.vp_start_gui)

        self.Frame3 = tk.Frame(self.Frame1)
        self.Frame3.place(relx=0.051, rely=0.316, relheight=0.188
                , relwidth=0.897)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(background="#6495ED")
        self.Frame3.configure(width=175)

        self.Equip_button = tk.Button(self.Frame3)
        self.Equip_button.place(relx=0.114, rely=0.08, height=43, width=136)
        self.Equip_button.configure(activebackground="#ececec")
        self.Equip_button.configure(activeforeground="#000000")
        self.Equip_button.configure(background="#ffffff")
        self.Equip_button.configure(disabledforeground="#a3a3a3")
        self.Equip_button.configure(font=font19)
        self.Equip_button.configure(foreground="#000000")
        self.Equip_button.configure(highlightbackground="#d9d9d9")
        self.Equip_button.configure(highlightcolor="black")
        self.Equip_button.configure(pady="0")
        self.Equip_button.configure(text='''Equipment''')
        self.Equip_button.configure(width=136)
        self.Equip_button.bind("<Button-1>", ew.vp_start_gui)

        self.Worker_button = tk.Button(self.Frame3)
        self.Worker_button.place(relx=0.114, rely=0.56, height=43, width=136)
        self.Worker_button.configure(activebackground="#ececec")
        self.Worker_button.configure(activeforeground="#000000")
        self.Worker_button.configure(background="#ffffff")
        self.Worker_button.configure(disabledforeground="#a3a3a3")
        self.Worker_button.configure(font=font19)
        self.Worker_button.configure(foreground="#000000")
        self.Worker_button.configure(highlightbackground="#d9d9d9")
        self.Worker_button.configure(highlightcolor="black")
        self.Worker_button.configure(pady="0")
        self.Worker_button.configure(text='''Workers''')
        self.Worker_button.configure(width=136)
        self.Worker_button.bind("<Button-1>", ww.vp_start_gui)

        self.Frame4 = tk.Frame(self.Frame1)
        self.Frame4.place(relx=0.051, rely=0.526, relheight=0.353
                , relwidth=0.897)
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(background="#6495ED")
        self.Frame4.configure(width=175)

        self.Road_button = tk.Button(self.Frame4)
        self.Road_button.place(relx=0.114, rely=0.043, height=53, width=136)
        self.Road_button.configure(activebackground="#ececec")
        self.Road_button.configure(activeforeground="#000000")
        self.Road_button.configure(background="#ffffff")
        self.Road_button.configure(disabledforeground="#a3a3a3")
        self.Road_button.configure(font=font19)
        self.Road_button.configure(foreground="#000000")
        self.Road_button.configure(highlightbackground="#d9d9d9")
        self.Road_button.configure(highlightcolor="black")
        self.Road_button.configure(pady="0")
        self.Road_button.configure(text='''Road''')
        self.Road_button.configure(width=136)

        self.UA_button = tk.Button(self.Frame4)
        self.UA_button.place(relx=0.114, rely=0.34, height=53, width=136)
        self.UA_button.configure(activebackground="#ececec")
        self.UA_button.configure(activeforeground="#000000")
        self.UA_button.configure(background="#ffffff")
        self.UA_button.configure(disabledforeground="#a3a3a3")
        self.UA_button.configure(font=font19)
        self.UA_button.configure(foreground="#000000")
        self.UA_button.configure(highlightbackground="#d9d9d9")
        self.UA_button.configure(highlightcolor="black")
        self.UA_button.configure(pady="0")
        self.UA_button.configure(text='''Unsafe Area''')
        self.UA_button.configure(width=136)

        self.OA_button = tk.Button(self.Frame4)
        self.OA_button.place(relx=0.114, rely=0.638, height=53, width=136)
        self.OA_button.configure(activebackground="#ececec")
        self.OA_button.configure(activeforeground="#000000")
        self.OA_button.configure(background="#ffffff")
        self.OA_button.configure(disabledforeground="#a3a3a3")
        self.OA_button.configure(font=font19)
        self.OA_button.configure(foreground="#000000")
        self.OA_button.configure(highlightbackground="#d9d9d9")
        self.OA_button.configure(highlightcolor="black")
        self.OA_button.configure(pady="0")
        self.OA_button.configure(text='''Other Areas''')
        self.OA_button.configure(width=136)

        self.Rules_button = tk.Button(self.Frame1)
        self.Rules_button.place(relx=0.154, rely=0.902, height=53, width=136)
        self.Rules_button.configure(activebackground="#ececec")
        self.Rules_button.configure(activeforeground="#000000")
        self.Rules_button.configure(background="#f3f3f3")
        self.Rules_button.configure(disabledforeground="#a3a3a3")
        self.Rules_button.configure(font=font19)
        self.Rules_button.configure(foreground="#000000")
        self.Rules_button.configure(highlightbackground="#d9d9d9")
        self.Rules_button.configure(highlightcolor="black")
        self.Rules_button.configure(pady="0")
        self.Rules_button.configure(text='''Safety Rules''')
        self.Rules_button.configure(width=136)

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.196, rely=0.105, relheight=0.874
                , relwidth=0.786)
        self.Canvas1.configure(background="#ffffff")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief='ridge')
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=883)

        self.Label2 = tk.Label(self.Canvas1)
        self.Label2.place(relx=0.34, rely=0.015, height=46, width=292)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font22)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Construction Site''')
        self.Label2.configure(width=292)

        self.newproject_button = tk.Button(top)
        self.newproject_button.place(relx=0.534, rely=0.026, height=43
                , width=146)
        self.newproject_button.configure(activebackground="#ececec")
        self.newproject_button.configure(activeforeground="#000000")
        self.newproject_button.configure(background="#f3f3f3")
        self.newproject_button.configure(disabledforeground="#a3a3a3")
        self.newproject_button.configure(font=font20)
        self.newproject_button.configure(foreground="#000000")
        self.newproject_button.configure(highlightbackground="#d9d9d9")
        self.newproject_button.configure(highlightcolor="black")
        self.newproject_button.configure(pady="0")
        self.newproject_button.configure(text='''New Project''')
        self.newproject_button.configure(width=146)

        self.load_button = tk.Button(top)
        self.load_button.place(relx=0.685, rely=0.026, height=43, width=136)
        self.load_button.configure(activebackground="#ececec")
        self.load_button.configure(activeforeground="#000000")
        self.load_button.configure(background="#f3f3f3")
        self.load_button.configure(disabledforeground="#a3a3a3")
        self.load_button.configure(font=font19)
        self.load_button.configure(foreground="#000000")
        self.load_button.configure(highlightbackground="#d9d9d9")
        self.load_button.configure(highlightcolor="black")
        self.load_button.configure(pady="0")
        self.load_button.configure(text='''Load Project''')
        self.load_button.configure(width=136)

        self.save_button = tk.Button(top)
        self.save_button.place(relx=0.827, rely=0.026, height=43, width=126)
        self.save_button.configure(activebackground="#ececec")
        self.save_button.configure(activeforeground="#000000")
        self.save_button.configure(background="#f3f3f3")
        self.save_button.configure(disabledforeground="#a3a3a3")
        self.save_button.configure(font=font19)
        self.save_button.configure(foreground="#000000")
        self.save_button.configure(highlightbackground="#d9d9d9")
        self.save_button.configure(highlightcolor="black")
        self.save_button.configure(pady="0")
        self.save_button.configure(text='''Save Project''')
        self.save_button.configure(width=126)

if __name__ == '__main__':
    vp_start_gui()





