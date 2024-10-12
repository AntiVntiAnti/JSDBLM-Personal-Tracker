exer_dialog = """
QWidget {
	font: 11pt "Helvetica";

}



/* ///////////////////////////////////////////////////////////////
QSpinBox
/////////////////////////////////////////////////////////////// */
QSpinBox {color:rgb(143,148,255);}
QSpinBox:hover {color: rgb(203,208,255);}
QSpinBox:focus {color: rgb(173,178,255);}


/* ////////////////////////////////////////////////////////////////////////////////
QLabel
//////////////////////////////////////////////////////////////////////////////// */
QLabel {
    background:transparent;
    color:rgb(143,148,255);
}
QLabel:hover {
    color: rgb(203,208,255);
}

/* ////////////////////////////////////////////////////////////////////////////////
QLineEdit
//////////////////////////////////////////////////////////////////////////////// */
QLineEdit {	font-size:11pt;
    border:none;
	color:rgb(143,148,255);
}

QLineEdit:hover {
    color:rgb(173,178,255);
}

QLineEdit:focus {
    color:rgb(123,128,235);
}
/* ////////////////////////////////////////////////////////////////////////////////
QPushButton
//////////////////////////////////////////////////////////////////////////////// */
QPushButton {
    min-width:65px;
    border:none;
    color:rgb(143,148,255);
}
QPushButton:hover {
    color:rgb(173,178,255);
}
QPushButton:pressed {
    color: #666;
}

QPushButton {
    color:rgb(123,128,235);
}

QPushButton:focus {
    color:#fff;
}

/* ///////////////////////////////////////////////////////////////
QSlider Colors
/////////////////////////////////////////////////////////////// */

QSlider::handle:horizontal {background:rgb(143,148,255);}
QSlider::handle:horizontal:hover {background:rgb(173,178,255);}
QSlider::handle:horizontal:pressed {background:rgb(123,128,235);}
QSlider::groove:horizontal:hover {background:rgba(143,148,255,0.25);}
QSlider::groove:horizontal {background:rgba(143,148,255,0.15);}


"""
