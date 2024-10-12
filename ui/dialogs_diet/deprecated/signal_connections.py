def connect_signals(dialog):
    """
    Connects the signals for the dialog buttons.

    This function connects the 'clicked' signals of the dialog's 'ok_button' 
    and 'cancel_button' to the dialog's 'accept' and 'reject' slots, respectively.

    Args:
        dialog (QDialog): The dialog whose buttons' signals are to be connected.
    """
    # Connect buttons
    dialog.ok_button.clicked.connect(dialog.accept)
    dialog.cancel_button.clicked.connect(dialog.reject)
