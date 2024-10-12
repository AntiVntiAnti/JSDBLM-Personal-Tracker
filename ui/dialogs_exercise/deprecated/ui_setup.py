from PyQt6.QtWidgets import QLineEdit, QSlider, QSpinBox
from PyQt6.QtCore import Qt


def setup_ui(dialog):
    """
    Sets up the UI components for the exercise dialog.

    This method initializes the following UI elements:
    - Exercise type input with a placeholder text "Exercise type".
    - Length of exercise spinbox with a suffix "mins" and a range from 0 to 1440 minutes (up to 24 hours).
    - Effort slider and spinbox with a range from 0 to 10.
    - Intensity slider and spinbox with a range from 0 to 10.
    """
    # exercise type input
    dialog.exercise_type_input.setPlaceholderText("Exercise type")
    # length of exercise spinbox
    dialog.length_of_exercise.setSuffix(" mins")
    dialog.length_of_exercise.setRange(0, 1440)  # Up to 24 hours
    # Effort slider and spinbox
    dialog.effort_slider.setRange(0, 10)
    dialog.effort_spinbox.setRange(0, 10)
    # Intensity slider and spinbox
    dialog.intensity_slider.setRange(0, 10)
    dialog.intensity_spinbox.setRange(0, 10)
