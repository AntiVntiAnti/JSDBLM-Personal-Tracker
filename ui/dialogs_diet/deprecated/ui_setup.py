from PyQt6.QtWidgets import QLineEdit, QSlider, QSpinBox
from PyQt6.QtCore import Qt


def setup_ui(dialog):
    """
    Sets up the UI elements for the given dialog.

    Args:
        dialog: The dialog object containing UI elements to be configured.

    Configures:
        dialog.calories: Sets the suffix to " Cal" and the range to 0-3000.
    """
    dialog.calories.setSuffix(" Cal")
    dialog.calories.setRange(0, 3000)
