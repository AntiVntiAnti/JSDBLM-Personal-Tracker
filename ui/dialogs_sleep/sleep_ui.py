# Form implementation generated from reading ui file 'sleep_ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(260, 157)
        Dialog.setStyleSheet("\n"
"QWidget {\n"
"    font: 11pt \"Helvetica\";\n"
"    border-radius:10px;\n"
"background:#121212;\n"
"\n"
"}\n"
"QFrame {\n"
"background: #121212;\n"
"}\n"
"/* //////////////////////////////////////////////////////////////\n"
"QSlider HORIZONTALALALALALAL\n"
"////////////////////////////////////////////////////////////// */\n"
"QSlider:horizontal {\n"
"    background:transparent;\n"
"    border:none;\n"
"    min-height:18px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 8px;\n"
"    height: 16px;\n"
"    margin: 0px;\n"
"    background:rgb(22, 22, 22);\n"
"    }\n"
"\n"
"QSlider::groove:horizontal:hover {\n"
"    background: rgb(38, 38, 38);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(255, 255, 255);\n"
"    height: 16px;\n"
"    width: 16px;\n"
"    margin: 0px;\n"
"    border-radius:8px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background:transparent;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: white;\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color:white;\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////\n"
"QSpinBox\n"
"/////////////////////////////////////////////////////////////// */\n"
"QSpinBox {color:rgb(143,148,255);}\n"
"QSpinBox:hover {color: rgb(203,208,255);}\n"
"QSpinBox:focus {color: rgb(173,178,255);}\n"
"\n"
"\n"
"/* ////////////////////////////////////////////////////////////////////////////////\n"
"QLabel\n"
"//////////////////////////////////////////////////////////////////////////////// */\n"
"QLabel {\n"
"    background:transparent;\n"
"    color:rgb(143,148,255);\n"
"}\n"
"QLabel:hover {\n"
"    color: rgb(203,208,255);\n"
"}\n"
"\n"
"/* ////////////////////////////////////////////////////////////////////////////////\n"
"QLineEdit\n"
"//////////////////////////////////////////////////////////////////////////////// */\n"
"QLineEdit {    font-size:11pt;\n"
"    border:none;\n"
"    color:rgb(143,148,255);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    color:rgb(173,178,255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    color:rgb(123,128,235);\n"
"}\n"
"\n"
"QDateEdit,\n"
"QTimeEdit {    font-size:11pt;\n"
"    border:none;\n"
"    color:rgb(143,148,255);\n"
"}\n"
"\n"
"QDateEdit:hover,\n"
"QTimeEdit:hover {\n"
"    color:rgb(173,178,255);\n"
"}\n"
"\n"
"QDateEdit:focus,\n"
"QTimeEdit:focus {\n"
"    color:rgb(123,128,235);\n"
"}\n"
"/* ////////////////////////////////////////////////////////////////////////////////\n"
"QPushButton\n"
"//////////////////////////////////////////////////////////////////////////////// */\n"
"QPushButton {\n"
"    min-width:65px;\n"
"    border:none;\n"
"    color:rgb(143,148,255);\n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(173,178,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #666;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color:rgb(123,128,235);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color:#fff;\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////\n"
"QSlider Colors\n"
"/////////////////////////////////////////////////////////////// */\n"
"\n"
"QSlider::handle:horizontal {background:rgb(143,148,255);}\n"
"QSlider::handle:horizontal:hover {background:rgb(173,178,255);}\n"
"QSlider::handle:horizontal:pressed {background:rgb(123,128,235);}\n"
"QSlider::groove:horizontal:hover {background:rgba(143,148,255,0.25);}\n"
"QSlider::groove:horizontal {background:rgba(143,148,255,0.15);}\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 127, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 2)
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame1 = QtWidgets.QFrame(parent=self.frame)
        self.frame1.setObjectName("frame1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame2 = QtWidgets.QFrame(parent=self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy)
        self.frame2.setStyleSheet("\n"
"/* ///////////////////////////////////////////////////////////////\n"
"QLabel\n"
"/////////////////////////////////////////////////////////////// */\n"
"QTimeEdit {\n"
"font-weight:300;\n"
"color:rgb(88,176,255);\n"
"}\n"
"QTimeEdit:hover {\n"
"color: rgb(128,216,255);\n"
"}\n"
"")
        self.frame2.setObjectName("frame2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.time_awake = QtWidgets.QTimeEdit(parent=self.frame2)
        self.time_awake.setStyleSheet("\n"
"/* ///////////////////////////////////////////////////////////////\n"
"QTimeEdit\n"
"/////////////////////////////////////////////////////////////// */\n"
"QTimeEdit {color:rgb(132,127,239);}\n"
"QTimeEdit:hover {color: rgb(152,147,255);}\n"
"QTimeEdit:focus {color: rgb(172,167,255);}\n"
"")
        self.time_awake.setFrame(False)
        self.time_awake.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.time_awake.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.time_awake.setObjectName("time_awake")
        self.gridLayout_5.addWidget(self.time_awake, 1, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.label = QtWidgets.QLabel(parent=self.frame2)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.frame2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)
        self.time_asleep = QtWidgets.QTimeEdit(parent=self.frame2)
        self.time_asleep.setStyleSheet("\n"
"/* ///////////////////////////////////////////////////////////////\n"
"QTimeEdit\n"
"/////////////////////////////////////////////////////////////// */\n"
"QTimeEdit {color:rgb(132,127,239);}\n"
"QTimeEdit:hover {color: rgb(152,147,255);}\n"
"QTimeEdit:focus {color: rgb(172,167,255);}\n"
"")
        self.time_asleep.setFrame(False)
        self.time_asleep.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.time_asleep.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.time_asleep.setObjectName("time_asleep")
        self.gridLayout_5.addWidget(self.time_asleep, 0, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.label_3 = QtWidgets.QLabel(parent=self.frame2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)
        self.total_hours_slept = QtWidgets.QLineEdit(parent=self.frame2)
        self.total_hours_slept.setFrame(False)
        self.total_hours_slept.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.total_hours_slept.setObjectName("total_hours_slept")
        self.gridLayout_5.addWidget(self.total_hours_slept, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame2)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame1)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 12)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.sleep_quality_lbl = QtWidgets.QLabel(parent=self.frame_2)
        self.sleep_quality_lbl.setObjectName("sleep_quality_lbl")
        self.gridLayout.addWidget(self.sleep_quality_lbl, 0, 0, 1, 1)
        self.sleep_quality = QtWidgets.QSpinBox(parent=self.frame_2)
        self.sleep_quality.setFrame(False)
        self.sleep_quality.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sleep_quality.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sleep_quality.setSuffix("")
        self.sleep_quality.setMinimum(0)
        self.sleep_quality.setMaximum(10)
        self.sleep_quality.setObjectName("sleep_quality")
        self.gridLayout.addWidget(self.sleep_quality, 0, 1, 1, 1)
        self.sleep_quality_slider = QtWidgets.QSlider(parent=self.frame_2)
        self.sleep_quality_slider.setStyleSheet("")
        self.sleep_quality_slider.setMinimum(0)
        self.sleep_quality_slider.setMaximum(10)
        self.sleep_quality_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sleep_quality_slider.setObjectName("sleep_quality_slider")
        self.gridLayout.addWidget(self.sleep_quality_slider, 0, 2, 1, 1)
        self.woke_like_lbl = QtWidgets.QLabel(parent=self.frame_2)
        self.woke_like_lbl.setObjectName("woke_like_lbl")
        self.gridLayout.addWidget(self.woke_like_lbl, 1, 0, 1, 1)
        self.woke_up_like = QtWidgets.QSpinBox(parent=self.frame_2)
        self.woke_up_like.setFrame(False)
        self.woke_up_like.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.woke_up_like.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.woke_up_like.setSuffix("")
        self.woke_up_like.setMinimum(0)
        self.woke_up_like.setMaximum(10)
        self.woke_up_like.setObjectName("woke_up_like")
        self.gridLayout.addWidget(self.woke_up_like, 1, 1, 1, 1)
        self.woke_up_like_slider = QtWidgets.QSlider(parent=self.frame_2)
        self.woke_up_like_slider.setStyleSheet("")
        self.woke_up_like_slider.setMinimum(0)
        self.woke_up_like_slider.setMaximum(10)
        self.woke_up_like_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.woke_up_like_slider.setObjectName("woke_up_like_slider")
        self.gridLayout.addWidget(self.woke_up_like_slider, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.frame1)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.frame)
        self.buttonBox.setStyleSheet("QPushButton:hover {\n"
"font-size:9pt;\n"
"margin: 2px 1px 0px 0px;\n"
"}\n"
"QPushButton:pressed {margin:0px;}")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.No|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 127, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.time_awake.setDisplayFormat(_translate("Dialog", "hh:mm AP"))
        self.label.setText(_translate("Dialog", "time.asleep"))
        self.label_2.setText(_translate("Dialog", "time.awake"))
        self.time_asleep.setDisplayFormat(_translate("Dialog", "hh:mm AP"))
        self.label_3.setText(_translate("Dialog", "total.hrs.slept"))
        self.total_hours_slept.setText(_translate("Dialog", "⌘+3"))
        self.total_hours_slept.setPlaceholderText(_translate("Dialog", "press opt+H to get total hours."))
        self.frame_2.setToolTip(_translate("Dialog", "<html><head/><body><p>What do you seek, my countrymen? Do you desire that I build for you gorgeous palaces, </p><p>decorated with words of empty meaning or temples roofed with dreams?</p><p>Do you command me to destroy what the liars and tyrants have built?</p><p>Shall I uproot with my fingers what the hypocrites and the wicked have *sown*?</p><p>Speak your insane wish! </p><p>What is it you would have me do my countrymen?</p><p>Shall I purr like the kitten to satisfy you, or roar like the lion to please myself?</p><p>I have sung for you, but you did not dance;</p><p>I have wept before you, but you did not cry.</p><p>Shall I sing and weep at the same time? </p><p>Your souls are suffering the pangs of hunger, </p><p>and yet the fruit of knowledge is more plentiful than the stones of the valleys.</p><p>Your hearts are withering from thirst, </p><p>and yet the springs of life are streaming about your homes.</p><p>Why do you not drink? </p><p>The sea has its ebb and flow,</p><p>The moon has its fullness and crescents,</p><p>And the ages have their winter and summer,</p><p>And all things vary like the shadow of an unborn god moving between earth and sun,</p><p>But truth cannot be changed, nor will it pass away;</p><p>Why, then, do you endeavour to disfigure its countenance? </p><p>I have called you in the silence of the night to point out the glory </p><p>of the moon and the dignity of the stars,</p><p>But you startled from your slumber and clutched your swords in fear, </p><p>Crying &quot;Where is the enemy? We must kill Him first!&quot;</p><p>At morning-tide when the enemy came, I called to you again,</p><p>But now you did not wake from your slumber,</p><p><br/></p></body></html>"))
        self.sleep_quality_lbl.setText(_translate("Dialog", "sleep.quality"))
        self.woke_like_lbl.setText(_translate("Dialog", "woke.up.like"))
