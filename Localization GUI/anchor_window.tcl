if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family Calibri -size 13 -weight normal -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font9
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 1
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#ffffff} 
    wm focusmodel $top passive
    wm geometry $top 600x450
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 1
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Anchor"
    vTcl:DefineAlias "$top" "Anchor_top" vTcl:Toplevel:WidgetProc "" 1
    label $top.lab45 \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -text {Anchor ID :} 
    vTcl:DefineAlias "$top.lab45" "Label1" vTcl:WidgetProc "Anchor_top" 1
    ttk::combobox $top.tCo46 \
        -font TkTextFont -textvariable combobox -foreground {} -background {} \
        -takefocus {} 
    vTcl:DefineAlias "$top.tCo46" "TCombobox1" vTcl:WidgetProc "Anchor_top" 1
    label $top.lab47 \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -text {X - coordinate :} 
    vTcl:DefineAlias "$top.lab47" "Label2" vTcl:WidgetProc "Anchor_top" 1
    entry $top.ent48 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$top.ent48" "Entry1" vTcl:WidgetProc "Anchor_top" 1
    label $top.lab49 \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -text {Y -  coordinate :} 
    vTcl:DefineAlias "$top.lab49" "Label3" vTcl:WidgetProc "Anchor_top" 1
    entry $top.ent50 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$top.ent50" "Entry2" vTcl:WidgetProc "Anchor_top" 1
    label $top.lab51 \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -text {Z - coordinate :} 
    vTcl:DefineAlias "$top.lab51" "Label4" vTcl:WidgetProc "Anchor_top" 1
    entry $top.ent52 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$top.ent52" "Entry3" vTcl:WidgetProc "Anchor_top" 1
    button $top.but53 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#F3F3F3} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text SAVE 
    vTcl:DefineAlias "$top.but53" "Button1" vTcl:WidgetProc "Anchor_top" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab45 \
        -in $top -x 70 -y 50 -width 142 -relwidth 0 -height 36 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tCo46 \
        -in $top -x 220 -y 50 -width 247 -relwidth 0 -height 36 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 40 -y 140 -width 172 -relwidth 0 -height 36 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent48 \
        -in $top -x 220 -y 140 -width 244 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 40 -y 200 -width 162 -relwidth 0 -height 36 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent50 \
        -in $top -x 220 -y 200 -width 244 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab51 \
        -in $top -x 40 -y 260 -width 172 -relwidth 0 -height 36 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent52 \
        -in $top -x 220 -y 260 -width 244 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but53 \
        -in $top -x 230 -y 340 -width 126 -relwidth 0 -height 43 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

