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
        set dflt,origin 0
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
    wm geometry $top 600x450+605+231
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Tag"
    vTcl:DefineAlias "$top" "tag_toplevel" vTcl:Toplevel:WidgetProc "" 1
    label $top.lab43 \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -text {Tag IP   :  } 
    vTcl:DefineAlias "$top.lab43" "Label1" vTcl:WidgetProc "tag_toplevel" 1
    ttk::combobox $top.tCo44 \
        -font TkTextFont -textvariable combobox -foreground {} -background {} \
        -takefocus {} 
    vTcl:DefineAlias "$top.tCo44" "TCombobox1" vTcl:WidgetProc "tag_toplevel" 1
    label $top.lab45 \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -text {X- coordinate :} 
    vTcl:DefineAlias "$top.lab45" "Label2" vTcl:WidgetProc "tag_toplevel" 1
    entry $top.ent46 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$top.ent46" "Entry1" vTcl:WidgetProc "tag_toplevel" 1
    label $top.lab47 \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -text {Y - coordinate :} 
    vTcl:DefineAlias "$top.lab47" "Label3" vTcl:WidgetProc "tag_toplevel" 1
    entry $top.ent48 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$top.ent48" "Entry2" vTcl:WidgetProc "tag_toplevel" 1
    label $top.lab49 \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -text {Z - coordinate :} 
    vTcl:DefineAlias "$top.lab49" "Label4" vTcl:WidgetProc "tag_toplevel" 1
    entry $top.ent50 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$top.ent50" "Entry3" vTcl:WidgetProc "tag_toplevel" 1
    button $top.but51 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#f3f3f3} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text SAVE 
    vTcl:DefineAlias "$top.but51" "Button1" vTcl:WidgetProc "tag_toplevel" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab43 \
        -in $top -x 80 -y 50 -width 182 -relwidth 0 -height 46 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tCo44 \
        -in $top -x 240 -y 50 -width 257 -relwidth 0 -height 46 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 60 -y 130 -width 152 -relwidth 0 -height 46 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent46 \
        -in $top -x 240 -y 130 -width 254 -relwidth 0 -height 44 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 50 -y 190 -width 172 -relwidth 0 -height 56 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent48 \
        -in $top -x 240 -y 200 -width 254 -relwidth 0 -height 44 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 50 -y 260 -width 172 -relwidth 0 -height 46 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent50 \
        -in $top -x 240 -y 260 -width 254 -relwidth 0 -height 44 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but51 \
        -in $top -x 250 -y 340 -width 96 -relwidth 0 -height 43 -relheight 0 \
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

