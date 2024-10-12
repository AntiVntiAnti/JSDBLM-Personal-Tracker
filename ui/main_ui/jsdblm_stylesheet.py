mainStackStyle = """
QWidget {
font: 13pt "Helvetica";
background:#121212;
color:rgb(255,255,255);
}
QSplitter::handle {
image: url(:/newPrefix/BludeBulb.png);
}
QSplitter::handle:horizontal { width: 2px;
}
QSplitter::handle:vertical { height: 2px;
}
QSplitter::handle:pressed {

image: url(:/newPrefix/whiteBulb.png);
}
/* /////////////////////////////////////////////////////////////////////////////
QTextEdit
///////////////////////////////////////////////////////////////////////////// */
QTextEdit {
border:none;
}

/* /////////////////////////////////////////////////////////////////////////////
QTimeEdit, QDoubleSpinBox, QSpinBox
///////////////////////////////////////////////////////////////////////////// */
QDoubleSpinBox,
QSpinBox {
border:none;
}

/* /////////////////////////////////////////////////////////////////////////////
QLabel
///////////////////////////////////////////////////////////////////////////// */
QLabel {
background:transparent;
}

/* /////////////////////////////////////////////////////////////////////////////
QComboBox
///////////////////////////////////////////////////////////////////////////// */
QComboBox {
background-color: transparent;
border:1px inset rgb(28,32,23);
border-radius:2px;
padding: 3px;
}

/* /////////////////////////////////////////////////////////////////////////////
QLineEdit
///////////////////////////////////////////////////////////////////////////// */
QLineEdit {
border:none;
background: transparent;
}
QLineEdit:hover {
border-bottom:1px solid rgba(123, 123, 123, 150);
}
QLineEdit:focus {
border-bottom:1px solid rgba(123, 123, 123, 200);
}

/* /////////////////////////////////////////////////////////////////////////////
QCheckBox
///////////////////////////////////////////////////////////////////////////// */
QCheckBox::indicator {
font-weight:bold;
background-color: transparent;
border: 2px solid rgb(33,143,109);
border-radius: 6px;
width: 8px;
height: 8px;
margin-left:8px;
margin-right:8px;
}
QCheckBox::indicator:hover {
border: 2px solid white;
}
QCheckBox::indicator:checked {
background: rgb(33,143,109);
border: 2px solid rgb(33,143,109);
}

/* //////////////////////////////////////////////////////////////
QSlider HORIZONTALALALALALAL
////////////////////////////////////////////////////////////// */
QSlider:horizontal {
background:transparent;
border:none;
min-height:18px;
}
QSlider::groove:horizontal {
border-radius: 8px;
height: 16px;
margin: 0px;
background:rgb(22, 22, 22);
}

QSlider::groove:horizontal:hover {
background: rgb(38, 38, 38);
}
QSlider::handle:horizontal {
background: rgb(255, 255, 255);
height: 16px;
width: 16px;
margin: 0px;
border-radius:8px;
}
QSlider::sub-page:horizontal {
background:transparent;
}
QSlider::handle:horizontal:hover {
background-color: white;
}
QSlider::handle:horizontal:pressed {
background-color:white;
}
/* ///////////////////////////////////////////////////////////
QSlider VERTICAL
////////////////////////////////////////////////////////////// */
QSlider::groove:vertical {
border-radius: 11px;
width: 22px;
margin: 0px;
background-color: rgba(33,33,33,100);
}

QSlider::groove:vertical:hover {
background-color: rgba(44,44,44,100);
}
QSlider::handle:vertical {
background-color: rgb(255, 88, 71);
border: none;
height: 22px;
width: 22px;
margin: 0px;
border-radius: 11px;
}
QSlider::handle:vertical:hover {
background-color: rgb(195, 155, 255);
}
QSlider::handle:vertical:pressed {
background-color: rgb(255, 121, 198);
}

/* /////////////////////////////////////////////////////////////////////////////
Time/DateEdit
///////////////////////////////////////////////////////////////////////////// */
QTimeEdit,
QDateEdit {
background-color: transparent;
border:None;
}

/* //////////////////////////////////////////////////////////////////////////////
AGENDA SIDEBAR BTN primer
////////////////////////////////////////////////////////////////////////////// */
QPushButton {
color:#fff;
text-align:left;
border-radius:3px;
font:9pt "Arial";
border:none;
font-weight:900;
padding:4px;
min-width:25px;
max-width:25px;
max-height:20px;
min-height:20px;
text-align:center;
}
QPushButton:hover {
color:#fff;
margin-top:2px;
padding-top:4px;
}
QPushButton:checked {
font-weight:bold;
font-size:10pt;
color:#fff;
}
QPushButton:pressed {
font-weight:bold;
font-size:9pt;
margin-top:4px;
color:#fff;
}

QPushButton:checked:hover {
font-weight:bold;
margin:0px;
color:#fff;
margin-top:1px;
}

QPushButton:checked:pressed {
font-weight:bold;
margin-top:2px;
color:#fff;
}

/* //////////////////////////////////////////////////////////////
QDateEdit
////////////////////////////////////////////////////////////// */

QDateEdit {
font-size:10pt;
}



/* //////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////
DIET WIDGETS
//////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////// */
#shower_commit {
image:url(:/newPrefix/blueShowerhead.png);
}

#shower_commit:hover {
image:url(:/newPrefix/Mac App icon 30.png);
}

#teeth_commit {
min-height:40px;
max-height:40px;
min-width:40px;
max-width:40px;
border-radius:28px;
image:url(:/newPrefix/blueteeth.png);
}

#exercise_commit {
image: url(:/newPrefix/blueYogai.png);
}
#exercise_commit:hover {
image: url(:/newPrefix/basics2Wh.png);
}

#teeth_commit:hover {
border-radius:27px;
image:url(:/newPrefix/teethPressed.png);
}

#eight_ounce_cup {
min-width:23px;
max-width:23px;
min-height:23px;
max-height:23px;
border-radius:17px;
image: url(:/newPrefix/waterBottles/8ozWaterBottle.png);
}
#eight_ounce_cup:hover {
border-radius:16px;
image: url(:/newPrefix/waterBottles/8ozpress.png);
}

#sixteen_ounce_cup {
min-width:40px;
max-width:40px;
min-height:40px;
max-height:40px;
border-radius:26px;
image: url(:/newPrefix/waterBottles/16ozWaterbottle.png);
}
#sixteen_ounce_cup:hover {
image: url(:/newPrefix/waterBottles/16ozpress.png);
border-radius:25px;
}


#twenty_four_ounce_cup {
min-width:40px;
max-width:40px;
min-height:40px;
max-height:40px;
border-radius:26px;
image: url(:/newPrefix/waterBottles/24ox.png);

}
#twenty_four_ounce_cup:hover {
image: url(:/newPrefix/waterBottles/24ozPress.png);
border-radius:25px;
}


#thirty_two_ounce_cup {
min-width:23px;
max-width:23px;
min-height:23px;
max-height:23px;
border-radius:17px;
image: url(:/newPrefix/waterBottles/32oz.png);
}
#thirty_two_ounce_cup:hover {
border-radius:16px;
image: url(:/newPrefix/waterBottles/32ozpress.png);
}

#total_hours_slept {color:rgb(132,127,239);border:none;}
#total_hours_slept:hover {color: rgb(152,147,255);border:none;}
#total_hours_slept:focus {color: rgb(172,167,255);border:none;}

/* ///////////////////////////////////////////////////////////////
QTimeEdit
/////////////////////////////////////////////////////////////// */
#time_awake,
#time_asleep {color:rgb(132,127,239);}
#time_awake:hover,
#time_asleep:hover {color: rgb(152,147,255);}
#time_awake:focus,
#time_asleep:focus {color: rgb(172,167,255);}

/* ///////////////////////////////////////////////////////////////
QSlider Colors
/////////////////////////////////////////////////////////////// */
#woke_up_like_slider::handle:horizontal,
#sleep_quality_slider::handle:horizontal {background:rgb(132,127,239);}
#woke_up_like_slider::handle:horizontal:horizontal,
#sleep_quality_slider::handle:horizontal:hover {background:rgb(162,157,255);}
#woke_up_like_slider::handle:horizontal:pressed,
#sleep_quality_slider::handle:horizontal:pressed {background:rgb(112,107,219);}
#woke_up_like_slider::groove:horizontal:hover,
#sleep_quality_slider::groove:horizontal:hover {background:rgba(132,127,239,0.35);}
#woke_up_like_slider::groove:horizontal,
#sleep_quality_slider::groove:horizontal {background:rgba(132,127,239,0.15);}



/*
Calories spinbox
*/
#calories {
color:rgb(132,127,239);
}
#calories:hover {
color: rgb(152,147,255);
}
#calories:focus {
color: rgb(172,167,255);
}

/*
FOOD EATEN lineedit
*/
#food_eaten {
border:none;
font-size:11pt;
font-weight:12;
color:rgb(144, 141, 255);
background: transparent;
margin-top:4px;
margin-bottom:4px;
}
#food_eaten:hover {
border:none;
}
#food_eaten:focus {
border:none;
}

/* /////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
AGENDA STYLES
////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////// */

/*
SUNDAY
*/
#sun_journal_nav_btn {
color:rgb(230, 77, 60);
}
#sun_journal_nav_btn:hover {
border-left-color: rgb(230, 77, 60);
}
#sun_journal_nav_btn:checked {
background-color: rgb(230, 77, 60);
color:#fff;
}
/*
MONDAY
*/
#mon_journal_nav_btn {
color:rgb(236, 77, 114);
}
#mon_journal_nav_btn:hover {
border-left-color: rgb(236, 77, 114);
}
#mon_journal_nav_btn:checked {
color:#fff;
background-color: rgb(236, 77, 114);
}

/*
Tuesday
*/
#tues_journal_nav_btn {
color:rgb(222, 94, 160);
}
#tues_journal_nav_btn:hover {
border-left-color: rgb(222, 94, 160);
}
#tues_journal_nav_btn:checked {
color:#fff;
background:rgb(222, 94, 160);
}

/* Wednesday */
#wed_journal_nav_btn {
color:#c176c2;
}
#wed_journal_nav_btn:hover {
border-left-color: #c176c2;
}
#wed_journal_nav_btn:checked {
color:#fff;
background:#c176c2;
}

/* Thursday */
#thurs_journal_nav_btn {
color: #9d8bd4;
}
#thurs_journal_nav_btn:hover {
border-left-color: #9d8bd4;
}
#thurs_journal_nav_btn:checked {
color:#fff;
background:#9d8bd4;
}

/* friday */
#fri_journal_nav_btn {
color:#7f9ad6;
}
#fri_journal_nav_btn:hover {
border-left-color: #7f9ad6;
}
#fri_journal_nav_btn:checked {
color:#fff;
background:#7f9ad6;
}

/* Saturday */
#sat_journal_nav_btn {
color:rgb(116, 164, 204);
}
#sat_journal_nav_btn:hover {
border-left-color: #73a5cc;
}
#sat_journal_nav_btn:checked {
color:#fff;
background:#73a5cc;
}


/* ///////////////////////////////////////////////////////////////////////////
SLEEP//BASICS
/////////////////////////////////////////////////////////////////////////// */
#woke_up_like_spinbox,
#sleep_quality,
#effort_spinbox {
font-size:10pt;
background:transparent;
}
#woke_up_like_spinbox:hover,
#sleep_quality:hover,
#effort_spinbox:hover {
background:transparent;
color:rgb(33, 143, 109);
}

#basics_basics_frame > QCheckBox {
background:transparent;
font-size:10pt;
}
#basics_basics_frame > QCheckBox:hover {
background:transparent;
color:rgb(33, 143, 109);
}
#basics_basics_frame > QCheckBox::indicator {
border: 2px solid rgb(33, 143, 109);
width: 7px;
height: 7px;
border-radius: 5px;
}

/*
BASICS||sleep Labels
*/
#awake_lbl,
#sleep_lbl,
#sleep_quality_lbl,
#woke_like_lbl,
#hrs_slept_lbl,
#bedtime_lbl {
color:#fff;
}

#awake_lbl:hover,
#sleep_lbl:hover,
#sleep_quality_lbl:hover,
#woke_like_lbl:hover,
#hrs_slept_lbl:hover,
#bedtime_lbl:hover {
color:rgb(34, 143, 109);
}
#basics_basics_frame > QCheckBox::indicator:hover {
border: 2px solid rgb(245, 245, 245);
}
#basics_basics_frame > QCheckBox::indicator:checked {
border: 2px solid rgb(33, 143, 109);
background: rgb(33, 143, 109);
}



/* ///////////////////////////////////////////////////////////////
QLabel
/////////////////////////////////////////////////////////////// */
#awakeLbl,
#sleep_quality_lbl,
#thsleptLbl,
#woke_like_lbl,
#asleepLbl {
font-weight:300;
color: rgb(132, 127, 239);
}
#sleep_quality_lbl:hover,
#thsleptLbl:hover,
#woke_like_lbl:hover,
#awakeLbl:hover,
#asleepLbl:hover {
color: rgb(162, 157, 255);
}

/*
BASICS MOD QCheckBox
*/
#basics_sleep_frame > QCheckBox,
#basics_basics_frame > QCheckBox {
background:transparent;
font-size:10pt;
}
#basics_sleep_frame > QCheckBox:hover,
#basics_basics_frame > QCheckBox:hover {
background:transparent;
color:rgb(33, 143, 109);
}
#basics_sleep_frame > QCheckBox::indicator,
#basics_basics_frame > QCheckBox::indicator {
border: 2px solid rgb(33, 143, 109);
width: 7px;
height: 7px;
border-radius: 5px;
}
#basics_sleep_frame > QCheckBox::indicator:hover,
#basics_basics_frame > QCheckBox::indicator:hover {
border: 2px solid rgb(245, 245, 245);
}
#basics_sleep_frame > QCheckBox::indicator:checked,
#basics_basics_frame > QCheckBox::indicator:checked {
border: 2px solid rgb(33, 143, 109);
background: rgb(33, 143, 109);
}
/* BASICS MOD QTimeEdit
//////////////////////////////////////////////////////////////////////////////////////////////// */
#basics_commit_pane > QDateEdit,
#basics_sleep_frame > QTimeEdit,
#basics_basics_frame > QTimeEdit {
background-color: transparent;
}
#basics_commit_pane > QDateEdit:hover,
#basics_sleep_frame > QTimeEdit:hover,
#basics_basics_frame > QTimeEdit:hover {
color:rgb(33, 143, 109);
}
#basics_commit_pane > QDateEdit:focus,
#basics_sleep_frame > QTimeEdit:focus,
#basics_basics_frame > QTimeEdit:focus {
color:rgb(33, 143, 109);
}



/* QLabel
//////////////////////////////////////////////////////////////////////////////////////////////// */
#basics_sleep_frame > QLabel,
#basics_basics_frame > QLabel {
background-color: transparent;
font-size:10pt;
}

#basics_sleep_frame > QLabel:hover,
#basics_basics_frame > QLabel:hover {
color:rgb(33, 143, 109);
}

/* ////////////////////////////////////////////////////////////////////////////
BASICS QSpinBox STYLE
//////////////////////////////////////////////////////////////////////////// */
#basics_sleep_frame > QSpinBox,
#basics_basics_frame > QSpinBox {
background:transparent;
}

#basics_sleep_frame > QSpinBox:hover,
#basics_basics_frame > QSpinBox:hover {
background:transparent;
color:rgb(33, 143, 109);
}

#basics_sleep_frame > QSpinBox:indicator,
#basics_basics_frame > QSpinBox:indicator {
border: 2px solid rgb(33, 143, 109);
width: 7px;
height: 7px;
border-radius: 5px;
}

#basics_sleep_frame > QSpinBox::indicator:hover,
#basics_basics_frame > QSpinBox::indicator:hover {
border: 2px solid rgb(245, 245, 245);
}

#basics_sleep_frame > QSpinBox::indicator:checked,
#basics_basics_frame > QSpinBox::indicator:checked {
border: 2px solid rgb(33, 143, 109);
background: 2px solid rgb(33, 143, 109);
}

/* ////////////////////////////////////////////////////////////////////////
    LILY'S MODULE STYLES
//////////////////////////////////////////////////////////////////////// */
/*
LILY TEXT EDITS
*/
#lily_walk_note {	font-size:11pt;
border:none;
color:rgb(160,130,160);
}

#lily_walk_note:hover {
color: rgb(200,170,200);
}

#lily_walk_note:focus {
color: rgb(180,150,180);
}

#lily_notes {
font-size:11pt;
border:none;
color:rgb(160,130,160);
}

#lily_notes:hover {
color: rgb(200,170,200);
}

#lily_notes:focus {
color: rgb(180,150,180);
}

/*
lily behavior sliders
*/
#lily_behavior_slider::handle:horizontal {
background:rgb(205,178,214);
}
#lily_behavior_slider::handle:horizontal:hover {
background:rgb(235,208,244);
}
#lily_behavior_slider::handle:horizontal:pressed {
background:rgb(185,158,194);
}
#lily_behavior_slider::groove:horizontal:hover {
background:rgba(205,178,214,45);
}
#lily_behavior_slider::groove:horizontal {
background:rgba(205,178,214,.15);
}

/* LILY TIME IN ROOM SLIDER */
#lily_time_in_room_slider::handle:horizontal {
background:rgb(205,178,214);
}

#lily_time_in_room_slider::handle:horizontal:hover {
background:rgb(235,208,244);
}
#lily_time_in_room_slider::handle:horizontal:pressed {
background:rgb(185,158,194);
}
#lily_time_in_room_slider::groove:horizontal:hover {
background:rgba(205,178,214,45);
}
#lily_time_in_room_slider::groove:horizontal {
background:rgba(205,178,214,45);
}
/* LILY MOOD SLIDER */
#lily_mood_slider::handle:horizontal {
background:rgb(160,130,160);
}

#lily_mood_slider::handle:horizontal:hover {
background:rgb(190,160,190);
}
#lily_mood_slider::handle:horizontal:pressed {
background:rgb(140,110,140);
}
#lily_mood_slider::groove:horizontal:hover {
background:rgba(160,130,160,45);
}
#lily_mood_slider::groove:horizontal {
background:rgba(160,130,160,45);
}
/* LILY ACTIVITY SLIDER */
#lily_mood_activity_slider::handle:horizontal {
background:rgb(130,100,130);
}

#lily_mood_activity_slider::handle:horizontal:hover {
background:rgb(160,130,160);
}
#lily_mood_activity_slider::handle:horizontal:pressed {
background:rgb(110,80,110);
}
#lily_mood_activity_slider::groove:horizontal:hover {
background:rgba(130,100,130,45);
}
#lily_mood_activity_slider::groove:horizontal {
background:rgba(130,100,130,45);
}

/* lily_gait_slider */
#lily_gait_slider::handle:horizontal {
background:rgb(144,114,144);
}

#lily_gait_slider::handle:horizontal:hover {
background:rgb(174,144,174);
}
#lily_gait_slider::handle:horizontal:pressed {
background:rgb(124,94,124);
}
#lily_gait_slider::groove:horizontal:hover {
background:rgba(144,114,144,0.25);
}
#lily_gait_slider::groove:horizontal {
background:rgba(144,114,144,0.15);
}

/* LILY ENERGY SLIDER */
#lily_energy_slider::handle:horizontal {
background:rgb(100,70,100);
}


#lily_energy_slider::handle:horizontal:hover {
background:rgb(130,100,130);
}

#lily_energy_slider::handle:horizontal:pressed {
background:rgb(80,50,80);
}

#lily_energy_slider::groove:horizontal:hover {
background:rgba(100,70,100,45);
}
#lily_energy_slider::groove:horizontal {
background:rgba(100,70,100,45);
}

/* Time in Room */
#lily_time_in_room {
background:transparent;
color:rgb(205,178,214);
}

#lily_time_in_room:hover {
color: rgb(225,198,234);
}
#lily_time_in_room:focus {
color: rgb(245,218,254);
}

/* Lily Mood */
#lily_mood {
background:transparent;
color:rgb(160,130,160);
}
#lily_mood:hover {
color: rgb(180,150,180);
}
#lily_mood:focus {
color: rgb(200,170,200);
}

/* Lily Activity */
#lily_activity  {
background:transparent;
color:rgb(130,100,130);
}
#lily_activity:hover {
color: rgb(150,120,150);
}
#lily_activity:focus {
color: rgb(170,140,170);
}

/* Lily Energy */
#lily_energy {
background:transparent;
color:rgb(100,70,100);
}
#lily_energy:hover {
color: rgb(120,90,120);
}
#lily_energy:focus {
color: rgb(140,110,140);
}
/* /////////////////////////////////////////////////////////////////////////////
#lily_mood_entry_date, #lily_diet_date, #lily_walk_date
///////////////////////////////////////////////////////////////////////////// */
#lily_diet_delete_btn,
#lily_mood_delete_btn,
#lily_walk_delete_btn {
border:none;
image: url(:/icons/UpdatedIcons/lily_d_norm.png);
max-width:20px;
min-width:20px;
max-height:20px;
min-height:20px;
}
#lily_diet_delete_btn:hover,
#lily_mood_delete_btn:hover,
#lily_walk_delete_btn:hover {
image: url(:/icons/UpdatedIcons/lily_c_hover.png);
}
#lily_diet_delete_btn:pressed,
#lily_mood_delete_btn:pressed,
#lily_walk_delete_btn:pressed {
image: url(:/icons/UpdatedIcons/lily_d_press.png);
}

#lily_mood_entry_date,
#lily_diet_date,
#lily_walk_date {
color:rgb(200,170,200);
}

#lily_mood_entry_date:focus,
#lily_diet_date:focus,
#lily_walk_date:focus {
color:#fff;
}

/* -------------------------------------------------
Data // TableView nav btn frame
-------------------------------------------------  */
#lilys_data_nav_btn_frame > QPushButton {
border-radius:3px;
padding:2px 4px;
border:none;
color:#fff;
min-width:35px;
max-width:35px;
min-height:35px;
max-height:35px;
background:transparent;
}

#lilys_data_nav_btn_frame > QPushButton:hover {
color:#fff;
font-size:11pt;
margin-top:2px;
margin-left:2px;
background:transparent;
/*background-color:rgb(255,255,255); */
}

#lilys_data_nav_btn_frame > QPushButton:checked {
font-weight:bold;
margin:0px;
background:transparent;
color:#fff;
}

#lilys_data_nav_btn_frame > QPushButton:pressed {
background:transparent;
font-weight:bold;
font-size:12pt;
margin:0px;
color:#fff;
}

#lilys_data_nav_btn_frame > QPushButton:checked:hover {
font-weight:bold;
margin:0px;
color:#fff;
background:transparent;
}

#lilys_data_nav_btn_frame > QPushButton:checked:pressed {
background:transparent;
font-weight:bold;
margin:0px;
color:#fff;
}

#lily_walk_btn,
#lily_walk_btn_2,
#lily_walk_btn_3 {
border:none;
max-width:35px;
min-width:35px;
max-height:35px;
min-height:35px;
image: url(:/icons/UpdatedIcons/lily_w_norm.png);
}

#lily_walk_btn:hover,
#lily_walk_btn_2:hover,
#lily_walk_btn_3:hover {
image: url(:/icons/UpdatedIcons/lily_w_hover.png);
}

#lily_walk_btn:pressed,
#lily_walk_btn_2:pressed,
#lily_walk_btn_3:pressed {
image: url(:/icons/UpdatedIcons/lily_w_press.png);
}

#lily_ate_check_2,
#lily_ate_check {
border:none;
image: url(:/icons/UpdatedIcons/lily_e_norm.png);
max-width:40px;
min-width:40px;
max-height:40px;
min-height:40px;
}

#lily_ate_check_2:hover,
#lily_ate_check:hover {
image: url(:/icons/UpdatedIcons/lily_e_hover.png);
}

#lily_ate_check_2:pressed,
#lily_ate_check:pressed {
image: url(:/icons/UpdatedIcons/lily_e_press.png);
}

#lily_ate_check_2:checked,
#lily_ate_check:checked {
image: url(:/icons/UpdatedIcons/lilybowlchecked.png);
}

#lily_walk_btn:checked:hover,
#lily_walk_btn_2:checked:hover,
#lily_walk_btn_3:checked:hover {
image: url(:/icons/UpdatedIcons/lily_paw_hovered.png);
}

#lily_walk_btn:checked:pressed,
#lily_walk_btn_2:checked:pressed,
#lily_walk_btn_3:checked:pressed {
image: url(:/icons/UpdatedIcons/lily_paw_pressed.png);
}


#lily_walk_btn:checked,
#lily_walk_btn_2:checked,
#lily_walk_btn_3:checked {
image: url(:/icons/UpdatedIcons/lilychecked.png);
}

#lily_behavior_3,
#lily_behavior_2,
#lily_behavior {
color:rgb(205,178,214);
}

#lily_behavior_3:hover,
#lily_behavior_2:hover,
#lily_behavior:hover {
color: rgb(225,198,234);
}

#lily_behavior_3:focus,
#lily_behavior_2:focus,
#lily_behavior:focus {
color: rgb(245,218,254);
}


#lily_gait,
#lily_gait_2,
#lily_gait_3 {
color:rgb(100,70,100);
}
#lily_gait:hover,
#lily_gait_2:hover,
#lily_gait_3:hover {
color: rgb(120,90,120);
}
#lily_gait:focus,
#lily_gait_2:focus,
#lily_gait_3:focus {
color: rgb(140,110,140);
}

/* ////////////////////////////////////////////////////////////////////////////////////////////////
        QScrollBar
//////////////////////////////////////////////////////////////////////////////////////////////// */
QScrollBar:horizontal {
border: none;
background:transparent;
height: 12px;
margin: 0px 10px 0px 10px;
border-radius: 3px;
}
QScrollBar::handle:horizontal {
background: rgb(25,25,25);
min-width:24px;
border-radius: 4px
}
QScrollBar::add-line:horizontal {
border: none;
background: transparent;
width: 20px;
border-top-right-radius: 4px;
border-bottom-right-radius: 4px;
subcontrol-position: right;
subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal {
border: none;
background: transparent;
width: 20px;
border-top-left-radius: 4px;
border-bottom-left-radius: 4px;
subcontrol-position: left;
subcontrol-origin: margin;
}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
background: none;
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
background: transparent;
}
QScrollBar:vertical {
border: none;
background-color:transparent;
width: 12px;
margin: 10px 0px 10px 0px;
border-radius: 4px;
}
QScrollBar::handle:vertical {
background: rgb(25, 25,25);
min-height: 12px;
border-radius: 4px
}
QScrollBar::add-line:vertical {
border: none;
background: transparent;
height: 20px;
border-bottom-left-radius: 4px;
border-bottom-right-radius: 4px;
subcontrol-position: bottom;
subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical {
border: none;
background: transparent;
height: 20px;
border-top-left-radius: 4px;
border-top-right-radius: 4px;
subcontrol-position: top;
subcontrol-origin: margin;
}
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
background: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
background: transparent;
}

/* -------------------------------------------------
Lilys Table Views
------------------------------------------------- */
#lily_walk_gait_table,
#lily_walk_behavior_table,
#lily_walk_note_table,
#time_in_room_table,
#lily_diet_table,
#lily_mood_table,
#lily_walk_table,
#lily_notes_table {
background-color: transparent;
alternate-background-color: rgb(100, 157, 220);
selection-background-color: #7e57c2;
gridline-color:transparent;
color:#fff;
}
#lily_walk_gait_table::item,
#lily_walk_behavior_table::item,
#lily_walk_note_table::item,
#time_in_room_table::item,
#lily_diet_table::item,
#lily_mood_table::item,
#lily_walk_table::item,
#lily_notes_table::item {
padding: 1px;
background:rgb(180, 149, 210);
}
#lily_walk_gait_table::item:selected,
#lily_walk_behavior_table::item:selected,
#lily_walk_note_table::item:selected,
#lily_notes_table::item:selected,
#time_in_room_table::item:selected,
#lily_diet_table::item:selected,
#lily_mood_table::item:selected,
#lily_walk_table::item:selected {
color:#fff;
background:rgb(23,23,23);
}


/* ////////////////////////////////////////////////////////////////////////
TABLE VIEWS
//////////////////////////////////////////////////////////////////////// */
#sleep_table,
#exercise_intensity_table,
#exercise_effort_table,
#exercise_length_table,
#exercise_type_table,
#total_hours_slept_table,
#woke_up_like_table,
#sleep_quality_table,
#diet_table,
#hydration_table,
#shower_table,
#tooth_table,
#yoga_table {
background-color: transparent;
selection-background-color: #7e57c2;
gridline-color:transparent;
color:#fff;
}
#exercise_intensity_table::item,
#exercise_effort_table::item,
#exercise_length_table::item,
#exercise_type_table::item,
#sleep_table::item,
#total_hours_slept_table::item,
#woke_up_like_table::item,
#sleep_quality_table::item,
#diet_table::item,
#hydration_table::item,
#shower_table::item,
#tooth_table::item,
#yoga_table::item {
padding: 1px;
background:rgb(132,127,239);
}
#exercise_intensity_table::item:selected,
#exercise_effort_table::item:selected,
#exercise_length_table::item:selected,
#exercise_type_table::item:selected,
#sleep_table::item:selected,
#total_hours_slept_table::item:selected,
#woke_up_like_table::item:selected,
#sleep_quality_table::item:selected,
#diet_table::item:selected,
#hydration_table::item:selected,
#shower_table::item:selected,
#tooth_table::item:selected,
#yoga_table::item:selected {
color:#fff;
background:rgb(23,23,23);
}

"""
