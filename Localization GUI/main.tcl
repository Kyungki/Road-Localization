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
    vTcl:font19
vTcl:font:add_font \
    "-family Calibri -size 12 -weight normal -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font20
vTcl:font:add_font \
    "-family Calibri -size 16 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font22
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
    wm geometry $top 1124x759+351+148
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
    wm title $top "GUI"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra44 \
        -borderwidth 2 -relief groove -background {#ffffff} -height 665 \
        -width 195 
    vTcl:DefineAlias "$top.fra44" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra44
    label $site_3_0.lab45 \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font22,object) -foreground {#000000} \
        -text Items 
    vTcl:DefineAlias "$site_3_0.lab45" "Label1" vTcl:WidgetProc "Toplevel1" 1
    frame $site_3_0.fra46 \
        -borderwidth 2 -relief groove -background {#6495ED} -height 135 \
        -width 175 
    vTcl:DefineAlias "$site_3_0.fra46" "Frame2" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra46
    button $site_4_0.but48 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font19,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor {#000000} -pady 0 \
        -text Anchor 
    vTcl:DefineAlias "$site_4_0.but48" "Anchor_button" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_0.but49 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font19,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Tags 
    vTcl:DefineAlias "$site_4_0.but49" "tag_button" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.but48 \
        -in $site_4_0 -x 20 -y 10 -width 136 -relwidth 0 -height 43 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.but49 \
        -in $site_4_0 -x 20 -y 70 -width 136 -relwidth 0 -height 43 \
        -relheight 0 -anchor nw -bordermode ignore 
    frame $site_3_0.fra50 \
        -borderwidth 2 -relief groove -background {#6495ED} -height 125 \
        -width 175 
    vTcl:DefineAlias "$site_3_0.fra50" "Frame3" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra50
    button $site_4_0.but51 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font19,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Equipment 
    vTcl:DefineAlias "$site_4_0.but51" "Equip_button" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_0.but52 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font19,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Workers 
    vTcl:DefineAlias "$site_4_0.but52" "Worker_button" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.but51 \
        -in $site_4_0 -x 20 -y 10 -width 136 -relwidth 0 -height 43 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.but52 \
        -in $site_4_0 -x 20 -y 70 -width 136 -relwidth 0 -height 43 \
        -relheight 0 -anchor nw -bordermode ignore 
    frame $site_3_0.fra53 \
        -borderwidth 2 -relief groove -background {#6495ED} -height 235 \
        -width 175 
    vTcl:DefineAlias "$site_3_0.fra53" "Frame4" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra53
    button $site_4_0.but54 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font19,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Road 
    vTcl:DefineAlias "$site_4_0.but54" "Road_button" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_0.but55 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font19,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Unsafe Area} 
    vTcl:DefineAlias "$site_4_0.but55" "UA_button" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_0.but56 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font19,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Other Areas} 
    vTcl:DefineAlias "$site_4_0.but56" "OA_button" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.but54 \
        -in $site_4_0 -x 20 -y 10 -width 136 -relwidth 0 -height 53 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.but55 \
        -in $site_4_0 -x 20 -y 80 -width 136 -relwidth 0 -height 53 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.but56 \
        -in $site_4_0 -x 20 -y 150 -width 136 -relwidth 0 -height 53 \
        -relheight 0 -anchor nw -bordermode ignore 
    button $site_3_0.but57 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#f3f3f3} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font19,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Safety Rules} 
    vTcl:DefineAlias "$site_3_0.but57" "Rules_button" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab45 \
        -in $site_3_0 -x 20 -y 10 -width 152 -relwidth 0 -height 36 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.fra46 \
        -in $site_3_0 -x 10 -y 60 -width 175 -relwidth 0 -height 135 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.fra50 \
        -in $site_3_0 -x 10 -y 210 -width 175 -relwidth 0 -height 125 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.fra53 \
        -in $site_3_0 -x 10 -y 350 -width 175 -relwidth 0 -height 235 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but57 \
        -in $site_3_0 -x 30 -y 600 -width 136 -relwidth 0 -height 53 \
        -relheight 0 -anchor nw -bordermode ignore 
    canvas $top.can58 \
        -background {#ffffff} -borderwidth 2 -closeenough 1.0 -height 663 \
        -insertbackground black -relief ridge -selectbackground {#c4c4c4} \
        -selectforeground black -width 883 
    vTcl:DefineAlias "$top.can58" "Canvas1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.can58
    label $site_3_0.lab59 \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font22,object) -foreground {#000000} \
        -text {Construction Site} 
    vTcl:DefineAlias "$site_3_0.lab59" "Label2" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab59 \
        -in $site_3_0 -x 300 -y 10 -width 292 -relwidth 0 -height 46 \
        -relheight 0 -anchor nw -bordermode ignore 
    button $top.but60 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#f3f3f3} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font20,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {New Project} 
    vTcl:DefineAlias "$top.but60" "newproject_button" vTcl:WidgetProc "Toplevel1" 1
    button $top.but61 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#f3f3f3} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font19,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Load Project} 
    vTcl:DefineAlias "$top.but61" "load_button" vTcl:WidgetProc "Toplevel1" 1
    button $top.but62 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#f3f3f3} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font19,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Save Project} 
    vTcl:DefineAlias "$top.but62" "save_button" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra44 \
        -in $top -x 20 -y 80 -width 195 -relwidth 0 -height 665 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.can58 \
        -in $top -x 220 -y 80 -width 883 -relwidth 0 -height 663 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but60 \
        -in $top -x 600 -y 20 -width 146 -relwidth 0 -height 43 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but61 \
        -in $top -x 770 -y 20 -width 136 -relwidth 0 -height 43 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but62 \
        -in $top -x 930 -y 20 -width 126 -relwidth 0 -height 43 -relheight 0 \
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

