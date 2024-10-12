lily_styles = """

/* ////////////////////////////////////////////////////////////////////////////////
QSpinBox
//////////////////////////////////////////////////////////////////////////////// */
QSpinBox {
    background:transparent;
    color:rgb(160,130,160);
}
QSpinBox:hover {
    color: rgb(180,150,180);
}
QSpinBox:focus {
    color: rgb(200,170,200);
}

/* ////////////////////////////////////////////////////////////////////////////////
QLabel
//////////////////////////////////////////////////////////////////////////////// */
QLabel {
    background:transparent;
    color:rgb(160,130,160);
}
QLabel:hover {
    color: rgb(180,150,180);
}

/* ////////////////////////////////////////////////////////////////////////////////
QLineEdit
//////////////////////////////////////////////////////////////////////////////// */
QLineEdit {	font-size:11pt;
    border:none;
	color:rgb(160,130,160);
}

QLineEdit:hover {
    color: rgb(200,170,200);
}

QLineEdit:focus {
    color: rgb(180,150,180);
}
/* ////////////////////////////////////////////////////////////////////////////////
QPushButton
//////////////////////////////////////////////////////////////////////////////// */
QPushButton {
    min-width:65px;
    border:none;
    color:rgb(200,160,200);
}
QPushButton:hover {
    color:rgb(240,200,240);
}
QPushButton:pressed {
    color: #666;
}

QPushButton {
    color:rgb(200,170,200);
}

QPushButton:focus {
    color:#fff;
}
/* ////////////////////////////////////////////////////////////////////////////////
QSlider
//////////////////////////////////////////////////////////////////////////////// */
QSlider::handle:horizontal {
    background:rgb(205,178,214);
}
/*
QSlider::sub-page:horizontal {
    background:rgb(205,178,214);
}
*/
QSlider::handle:horizontal:hover {
    background:rgb(235,208,244);
}
QSlider::handle:horizontal:pressed {
    background:rgb(185,158,194);
}
QSlider::groove:horizontal:hover {
    background:rgba(205,178,214,45);
}
QSlider::groove:horizontal {
    background:rgba(205,178,214,.15);
}

"""
