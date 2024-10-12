stylesheet = """

QWidget {
	font: 11pt "Helvetica";
    background:#161616;
    color:rgb(255,255,255);
    padding-top: 8px;
    padding-bottom: 8px;
    padding-left: 8px;
    padding-right: 8px;
    border-radius:10px;
}

/* /////////////////////////////////////////////////////////////////////////////
QTimeEdit, QDoubleSpinBox, QSpinBox
///////////////////////////////////////////////////////////////////////////// */
QDoubleSpinBox,
QSpinBox {
    border:none;
}
/* /////////////////////////////////////////////////////////////////////////////
QSlider
///////////////////////////////////////////////////////////////////////////// */
QSlider::groove:vertical {
border-radius: 5px;
width: 30px;
margin: 0px;
background:rgb(22, 24, 29);
}

QSlider::groove:vertical:hover {
background: rgba(233,123,111,0.25);
}

QSlider::handle:vertical {
background: rgb(233,123,111);
height: 25px;
width: 40px;
margin: 0px -9px 0px -9px;
border-radius:5px;
}

QSlider::add-page:vertical {
background:transparent;
}

QSlider::handle:vertical:hover {
background-color: rgb(255,163,151);
}

QSlider::handle:vertical:pressed {
background-color:rgb(188,78,66);
}




/* ///////////////////////////////////////////////////////////////
WEFE SLIDERS
/////////////////////////////////////////////////////////////// */

#wellbeing_slider::handle:vertical {background:rgb(142,150,255);}
#wellbeing_slider::handle:vertical:hover {background:rgb(182,190,255);}
#wellbeing_slider::handle:vertical:pressed {background:rgb(92,100,205);}
#wellbeing_slider::groove:vertical:hover {background:rgba(142,150,255,0.25);}
#wellbeing_slider::groove:vertical {background:rgba(142,150,255,0.15);}



/* ///////////////////////////////////////////////////////////////
QSlider Colors
/////////////////////////////////////////////////////////////// */

#energy_slider::handle:vertical {background:rgb(64,68,132);}
#energy_slider::handle:vertical:hover {background:rgb(104,108,172);}
#energy_slider::handle:vertical:pressed {background:rgb(44,58,122);}
#energy_slider::groove:vertical:hover {background:rgba(64,68,132,0.25);}
#energy_slider::groove:vertical {background:rgba(64,68,132,0.15);}



/* ///////////////////////////////////////////////////////////////
QSlider Colors
/////////////////////////////////////////////////////////////// */

#excite_slider::handle:vertical {
	background:rgb(113,119,203);
}
#excite_slider::handle:vertical:hover {
	background:rgb(153,159,243);
}
#excite_slider::handle:vertical:pressed {
	background:rgb(64,68,132);
}
#excite_slider::groove:vertical:hover {
	background:rgba(113,119,203,0.25);
}
#excite_slider::groove:vertical {
	background:rgba(113,119,203,0.15);
}

#focus_slider::handle:vertical {background:rgb(87,90,156);}
#focus_slider::handle:vertical:hover {background:rgb(127,130,196);}
#focus_slider::handle:vertical:pressed {background:rgb(64,68,132);}
#focus_slider::groove:vertical:hover {background:rgba(87,90,156,0.25);}
#focus_slider::groove:vertical {background:rgba(87,90,156,0.15);}

/*WEFE*/
#excite_spinbox{color:rgb(96,103,171);}
#excite_spinbox:hover {color: rgb(156,163,231);}
#excite_spinbox:focus {color: rgb(126,133,201);}

#wellbeing_spinbox {color:rgb(96,103,171);}
#wellbeing_spinbox:hover {color: rgb(156,163,231);}
#wellbeing_spinbox:focus {color: rgb(126,133,201);}

#focus_spinbox {color:rgb(96,103,171);}
#focus_spinbox:hover {color: rgb(156,163,231);}
#focus_spinbox:focus {color: rgb(126,133,201);}

#energy_spinbox {color:rgb(96,103,171);}
#energy_spinbox:hover {color: rgb(156,163,231);}
#energy_spinbox:focus {color: rgb(126,133,201);}

"""
