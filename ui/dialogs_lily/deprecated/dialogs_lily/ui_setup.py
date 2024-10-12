from PyQt6.QtWidgets import QLineEdit, QSlider, QSpinBox
from PyQt6.QtCore import Qt


def setup_ui(dialog):
    """
    Sets up the UI elements for the given dialog.
    This function configures the following UI elements:
    - Sets the placeholder text for the lily_walk_note field to "Notes".
    - Sets the range for the lily_behavior slider and spinbox to 0-10.
    - Sets the range for the lily_gait slider and spinbox to 0-10.
    Args:
        dialog: The dialog object containing the UI elements to be configured.
    """
    dialog.lily_walk_note.setPlaceholderText("Notes")
    
    dialog.lily_behavior.setRange(0, 10)
    dialog.lily_behavior_spinbox.setRange(0, 10)
    
    dialog.lily_gait.setRange(0, 10)
    dialog.lily_gait_spinbox.setRange(0, 10)
