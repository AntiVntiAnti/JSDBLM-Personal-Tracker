stylesheet = """
QWidget {
	font: 11pt "Helvetica Neue";
	background: #161616;
	padding-top: 8px;
    padding-bottom: 8px;
    padding-left: 8px;
    padding-right: 8px;
    border-radius:10px;
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
CSPR
/////////////////////////////////////////////////////////////// */

#calm_slider::handle:vertical {background:rgb(52,121,71);}
#calm_slider::handle:vertical:hover {background:rgb(92,161,111);}
#calm_slider::handle:vertical:pressed {background:rgb(32,100,51);}
#calm_slider::groove:vertical:hover {background:rgba(52,121,71,0.25);}
#calm_slider::groove:vertical {background:rgba(52,121,71,0.15);}

#stress_slider::handle:vertical {background:rgb(77,176,104);}
#stress_slider::handle:vertical:hover {background:rgb(117,216,144);}
#stress_slider::handle:vertical:pressed {background:rgb(52,121,71);}
#stress_slider::groove:vertical:hover {background:rgba(77,176,104,0.25);}
#stress_slider::groove:vertical {background:rgba(77,176,104,0.15);}


#pain_slider::handle:vertical {background:rgb(90,207,122);}
#pain_slider::handle:vertical:hover {background:rgb(130,247,162);}
#pain_slider::handle:vertical:pressed {background:rgb(52,121,71);}
#pain_slider::groove:vertical:hover {background:rgba(90,207,122,0.25);}
#pain_slider::groove:vertical {background:rgba(90,207,122,0.15);}

#rage_slider::handle:vertical {background:rgb(123,241,155);}
#rage_slider::handle:vertical:hover {background:rgb(163,255,195);}
#rage_slider::handle:vertical:pressed  {background:rgb(52,121,71);}
#rage_slider::groove:vertical:hover {background:rgba(123,241,155,0.25);}
#rage_slider::groove:vertical {background:rgba(123,241,155,0.15);}





/*
QSpinBoxes
*/

/*CSPR*/
#calm_spinbox {color:rgb(52,121,71);}
#calm_spinbox:hover {color: rgb(112,181,131);}
#calm_spinbox:focus {color: rgb(82,151,101);}

#stress_spinbox {color:rgb(73,167,98);}
#stress_spinbox:hover {color: rgb(133,227,158);}
#stress_spinbox:focus {color: rgb(103,197,128);}

#pain_spinbox{color:rgb(90,208,122);}
#pain_spinbox:hover {color: rgb(150,255,182);}
#pain_spinbox:focus {color: rgb(120,238,152);}

#rage_spinbox {color:rgb(123,241,155);}
#rage_spinbox:hover {color: rgb(183,255,215);}
#rage_spinbox:focus {color: rgb(153,255,185);}


"""
