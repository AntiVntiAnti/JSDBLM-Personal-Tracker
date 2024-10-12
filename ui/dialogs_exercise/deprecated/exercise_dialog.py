from PyQt6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QSpinBox, QSlider, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import Qt
from ui.dialogs_exercise.exer_style import exer_dialog
from ui.dialogs_exercise.ui_setup import setup_ui
from ui.dialogs_exercise.layout_creation import create_layout
from ui.dialogs_exercise.signal_connections import connect_signals


class ExerciseDetailsDialog(QDialog):
    """
    A dialog for entering details about an exercise session.

    Attributes:
        exlbl (QLabel): Label for exercise type input.
        exlbl1 (QLabel): Label for length of exercise input.
        exlbl2 (QLabel): Label for effort rating input.
        exlbl3 (QLabel): Label for intensity rating input.
        exercise_type_input (QLineEdit): Input field for exercise type.
        length_of_exercise (QSpinBox): Spin box for length of exercise in minutes.
        effort_slider (QSlider): Slider for effort rating.
        effort_spinbox (QSpinBox): Spin box for effort rating.
        intensity_slider (QSlider): Slider for intensity rating.
        intensity_spinbox (QSpinBox): Spin box for intensity rating.
        ok_button (QPushButton): Button to confirm the input.
        cancel_button (QPushButton): Button to cancel the dialog.

    Methods:
        __init__(parent=None):
            Initializes the dialog with optional parent widget.
        setup_ui():
            Sets up the user interface elements.
        create_layout():
            Creates and arranges the layout of the dialog.
        connect_signals():
            Connects signals and slots for interactivity.
    """
    def __init__(self, parent=None):
        """
        Initializes the ExerciseDialog.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.

        Attributes:
            exlbl (QLabel): Label asking the type of exercise.
            exlbl1 (QLabel): Label asking the duration of exercise.
            exlbl2 (QLabel): Label asking the effort rating.
            exlbl3 (QLabel): Label asking the intensity of exercise.
            exercise_type_input (QLineEdit): Input field for the type of exercise.
            length_of_exercise (QSpinBox): Spin box for the duration of exercise.
            effort_slider (QSlider): Slider for rating the effort.
            effort_spinbox (QSpinBox): Spin box for rating the effort.
            intensity_slider (QSlider): Slider for rating the intensity.
            intensity_spinbox (QSpinBox): Spin box for rating the intensity.
            ok_button (QPushButton): Button to confirm the input.
            cancel_button (QPushButton): Button to cancel the input.
        """
        super().__init__(parent)
        self.resize(300,300)
        self.exlbl = QLabel("What Kind of Exercise?")
        self.exlbl1 = QLabel("How Long did you Exercise For?")
        self.exlbl2 = QLabel("How would you rate your effort?")
        self.exlbl3 = QLabel("How intense was the exercise?")
        self.exercise_type_input = QLineEdit()
        self.length_of_exercise = QSpinBox()
        self.effort_slider = QSlider(Qt.Orientation.Horizontal)
        self.effort_spinbox = QSpinBox()
        self.intensity_slider = QSlider(Qt.Orientation.Horizontal)
        self.intensity_spinbox = QSpinBox()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        self.setWindowTitle("Exercise Details")
        setup_ui(self)
        create_layout(self)
        connect_signals(self)
        self.setStyleSheet(exer_dialog)
