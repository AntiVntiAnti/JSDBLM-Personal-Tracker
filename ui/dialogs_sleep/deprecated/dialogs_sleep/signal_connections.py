def connect_signals(dialog):
    """
    Connects the signals and slots for the given dialog.

    This function sets up the connections between the UI elements and their corresponding actions:
    - Synchronizes the value of the sleep quality slider with the sleep quality value.
    - Synchronizes the value of the woke up like slider with the woke up like value.
    - Connects the OK button to the dialog's accept method.
    - Connects the Cancel button to the dialog's reject method.

    Args:
        dialog: The dialog object containing the UI elements to be connected.
    """
    dialog.sleep_quality_slider.valueChanged.connect(dialog.sleep_quality.setValue)
    dialog.sleep_quality.valueChanged.connect(dialog.sleep_quality_slider.setValue)
    dialog.woke_up_like_slider.valueChanged.connect(dialog.woke_up_like.setValue)
    dialog.woke_up_like.valueChanged.connect(dialog.woke_up_like_slider.setValue)

    dialog.ok_button.clicked.connect(dialog.accept)
    dialog.cancel_button.clicked.connect(dialog.reject)

