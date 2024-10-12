# exercise_details_dialog.py
from PyQt6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QSpinBox, QSlider, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import Qt
from ui.exer_style import exer_dialog
from utility.logger_setup import create_logger
logger = create_logger(__name__)


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
        self.setup_ui()
        self.create_layout()
        self.connect_signals()
        self.setStyleSheet(exer_dialog)

    def setup_ui(self):
        """
        Sets up the UI components for the exercise dialog.

        This method initializes the following UI elements:
        - Exercise type input with a placeholder text "Exercise type".
        - Length of exercise spinbox with a suffix "mins" and a range from 0 to 1440 minutes (up to 24 hours).
        - Effort slider and spinbox with a range from 0 to 10.
        - Intensity slider and spinbox with a range from 0 to 10.
        """
        # exercise type input
        self.exercise_type_input.setPlaceholderText("Exercise type")
        # length of exercise spinbox
        self.length_of_exercise.setSuffix(" mins")
        self.length_of_exercise.setRange(0, 1440)  # Up to 24 hours
        # Effort slider and spinbox
        self.effort_slider.setRange(0, 10)
        self.effort_spinbox.setRange(0, 10)
        # Intensity slider and spinbox
        self.intensity_slider.setRange(0, 10)
        self.intensity_spinbox.setRange(0, 10)

    def create_layout(self):
        """
        Creates and sets the layout for the exercise dialog.

        This method initializes and arranges the widgets in a vertical layout.
        It includes the following sections:
        - Exercise type input
        - Length of exercise input
        - Effort input with a slider and spinbox
        - Intensity input with a slider and spinbox
        - OK and Cancel buttons

        The layout is set to the main layout of the dialog.
        """
        main_layout = QVBoxLayout()

        # Exercise type
        main_layout.addWidget(self.exlbl)
        main_layout.addWidget(self.exercise_type_input)

        # Length of exercise
        main_layout.addWidget(self.exlbl1)
        main_layout.addWidget(self.length_of_exercise)

        # Effort
        main_layout.addWidget(self.exlbl2)
        effort_layout = QHBoxLayout()
        effort_layout.addWidget(self.effort_slider)
        effort_layout.addWidget(self.effort_spinbox)
        main_layout.addLayout(effort_layout)

        # Intensity
        main_layout.addWidget(self.exlbl3)
        intensity_layout = QHBoxLayout()
        intensity_layout.addWidget(self.intensity_slider)
        intensity_layout.addWidget(self.intensity_spinbox)
        main_layout.addLayout(intensity_layout)

        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def connect_signals(self):
        """
        Connects the signals and slots for the UI elements in the exercise dialog.

        This method synchronizes the values between sliders and spinboxes for effort and intensity,
        ensuring that changes in one are reflected in the other. It also connects the OK and Cancel
        buttons to their respective accept and reject actions.
        """
        # Synchronize effort slider and spinbox
        self.effort_slider.valueChanged.connect(self.effort_spinbox.setValue)
        self.effort_spinbox.valueChanged.connect(self.effort_slider.setValue)

        # Synchronize intensity slider and spinbox
        self.intensity_slider.valueChanged.connect(self.intensity_spinbox.setValue)
        self.intensity_spinbox.valueChanged.connect(self.intensity_slider.setValue)

        # Connect buttons
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
