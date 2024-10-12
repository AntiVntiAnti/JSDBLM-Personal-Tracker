from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout


def create_layout(dialog):
    """
    Creates and sets the layout for the given dialog.
    This function organizes various widgets into layouts and sets the main layout for the dialog.
    The layout includes sections for time asleep, time awake, total hours slept, sleep quality, 
    and how the user woke up, along with OK and Cancel buttons.
    Args:
        dialog (QDialog): The dialog for which the layout is being created. The dialog is expected 
                          to have the following attributes:
                          - time_asleep_lbl (QLabel)
                          - time_asleep (QWidget)
                          - time_awake_lbl (QLabel)
                          - time_awake (QWidget)
                          - total_hours_lbl (QLabel)
                          - total_hours_slept (QWidget)
                          - sleep_quality_lbl (QLabel)
                          - sleep_quality_slider (QSlider)
                          - sleep_quality (QWidget)
                          - woke_up_lbl (QLabel)
                          - woke_up_like_slider (QSlider)
                          - woke_up_like (QWidget)
                          - ok_button (QPushButton)
                          - cancel_button (QPushButton)
    """
    main_layout = QVBoxLayout()
    
    time_asleep_layout = QHBoxLayout()
    time_asleep_layout.addWidget(dialog.time_asleep_lbl)
    time_asleep_layout.addWidget(dialog.time_asleep)
    main_layout.addLayout(time_asleep_layout)
    
    time_awake_layout = QHBoxLayout()
    time_awake_layout.addWidget(dialog.time_awake_lbl)
    time_awake_layout.addWidget(dialog.time_awake)
    main_layout.addLayout(time_awake_layout)
    
    main_layout.addWidget(dialog.total_hours_lbl)
    main_layout.addWidget(dialog.total_hours_slept)
    
    sleep_quality_layout = QVBoxLayout()
    sleep_quality_layout.addWidget(dialog.sleep_quality_lbl)
    sleep_quality_layout.addWidget(dialog.sleep_quality_slider)
    sleep_quality_layout.addWidget(dialog.sleep_quality)
    main_layout.addLayout(sleep_quality_layout)
    
    woke_up_like_layout = QVBoxLayout()
    woke_up_like_layout.addWidget(dialog.woke_up_lbl)
    woke_up_like_layout.addWidget(dialog.woke_up_like_slider)
    woke_up_like_layout.addWidget(dialog.woke_up_like)
    main_layout.addLayout(woke_up_like_layout)
    
    
    # Buttons
    button_layout = QHBoxLayout()
    button_layout.addWidget(dialog.ok_button)
    button_layout.addWidget(dialog.cancel_button)
    main_layout.addLayout(button_layout)
    
    dialog.setLayout(main_layout)






