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
MMDMR
/////////////////////////////////////////////////////////////// */
#mood_slider::handle:vertical {background:rgb(109,92,128);}
#mood_slider::handle:vertical:hover {background:rgb(149,132,168);}
#mood_slider::handle:vertical:pressed {background:rgb(89,72,100);}
#mood_slider::groove:vertical:hover {background:rgba(109,92,128,0.25);}
#mood_slider::groove:vertical {background:rgba(109,92,128,0.15);}

#mania_slider::handle:vertical {background:rgb(135,114,159);}
#mania_slider::handle:vertical:hover {background:rgb(175,154,199);}
#mania_slider::handle:vertical:pressed {background:rgb(109,92,128);}
#mania_slider::groove:vertical:hover {background:rgba(135,114,159,0.25);}
#mania_slider::groove:vertical {background:rgba(135,114,159,0.15);}

#depression_slider::handle:vertical {background:rgb(174,146,204);}
#depression_slider::handle:vertical:hover {background:rgb(214,186,244);}
#depression_slider::handle:vertical:pressed {background:rgb(109,92,128);}
#depression_slider::groove:vertical:hover {background:rgba(174,146,204,0.25);}
#depression_slider::groove:vertical {background:rgba(174,146,204,0.15);}

#mixed_risk_slider::handle:vertical {background:rgb(211,191,232);}
#mixed_risk_slider::handle:vertical:hover {background:rgb(251,231,255);}
#mixed_risk_slider::handle:vertical:pressed {background:rgb(109,92,128);}
#mixed_risk_slider::groove:vertical:hover {background:rgba(211,191,232,0.25);}
#mixed_risk_slider::groove:vertical {background:rgba(211,191,232,0.15);}


/*MMDMR*/
#mood {color:rgb(109,92,128);}
#mood:hover {color: rgb(169,152,188);}
#mood:focus {color: rgb(139,122,158);}

#mania {color:rgb(135,114,159);}
#mania:hover {color: rgb(195,174,219);}
#mania:focus {color: rgb(165,144,189);}

#depression {color:rgb(174,146,204);}
#depression:hover {color: rgb(234,206,255);}
#depression:focus {color: rgb(204,176,234);}


#mixed_risk {color:rgb(211,191,232);}
#mixed_risk:hover {color: rgb(255,251,255);}
#mixed_risk:focus {color: rgb(241,221,255);}
"""
