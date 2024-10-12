from PyQt6.QtWidgets import QLineEdit, QSlider, QSpinBox
from PyQt6.QtCore import Qt


def setup_ui(dialog):
    """
    Sets up the UI elements for the sleep tracking dialog.
    Parameters:
    dialog (QDialog): The dialog window containing the UI elements to be set up.
    UI Elements:
    - total_hours_slept (QLineEdit): Input field for total hours slept, with a placeholder text "00:00".
    - sleep_quality_slider (QSlider): Slider for sleep quality, with a range from 0 to 10.
    - sleep_quality (QSpinBox): Spin box for sleep quality, with a range from 0 to 10.
    - woke_up_like_slider (QSlider): Slider for how the user felt upon waking up, with a range from 0 to 10.
    - woke_up_like (QSpinBox): Spin box for how the user felt upon waking up, with a range from 0 to 10.
    """
    dialog.total_hours_slept.setPlaceholderText("00:00")
    
    dialog.sleep_quality_slider.setRange(0, 10)
    dialog.sleep_quality.setRange(0, 10)
    
    dialog.woke_up_like_slider.setRange(0, 10)
    dialog.woke_up_like.setRange(0, 10)
    
    



