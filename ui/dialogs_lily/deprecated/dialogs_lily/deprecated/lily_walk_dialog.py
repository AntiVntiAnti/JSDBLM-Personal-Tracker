# exercise_details_dialog.py
from PyQt6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QSpinBox, QSlider, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import Qt
from ui.lily_style import lily_styles

class LilyWalkDialog(QDialog):
    """
    LilyWalkDialog is a custom QDialog that allows users to input details about Lily's walk.
    Attributes:
        exlbl (QLabel): Label for notes section.
        lily_walk_note (QLineEdit): Input field for notes.
        exlbl2 (QLabel): Label for gait evaluation section.
        exlbl1 (QLabel): Label for behavior evaluation section.
        lily_gait (QSlider): Slider to evaluate Lily's gait.
        lily_gait_spinbox (QSpinBox): Spinbox to display gait value.
        lily_behavior (QSlider): Slider to evaluate Lily's behavior.
        lily_behavior_spinbox (QSpinBox): Spinbox to display behavior value.
        ok_button (QPushButton): Button to confirm the dialog.
        cancel_button (QPushButton): Button to cancel the dialog.
    Methods:
        __init__(self, parent=None): Initializes the dialog with optional parent.
        setup_ui(self): Sets up the UI components and their properties.
        create_layout(self): Creates and arranges the layout of the dialog.
        connect_signals(self): Connects signals and slots for interactivity.
    """
    def __init__(self, parent=None):
        """
        Initializes the LilyWalkDialog.

        Args:
            parent (QWidget, optional): The parent widget of this dialog. Defaults to None.

        Attributes:
            exlbl (QLabel): Label for notes section.
            lily_walk_note (QLineEdit): Input field for notes.
            exlbl2 (QLabel): Label for gait evaluation section.
            exlbl1 (QLabel): Label for behavior evaluation section.
            lily_gait (QSlider): Slider for gait evaluation.
            lily_gait_spinbox (QSpinBox): Spinbox for gait evaluation.
            lily_behavior (QSlider): Slider for behavior evaluation.
            lily_behavior_spinbox (QSpinBox): Spinbox for behavior evaluation.
            ok_button (QPushButton): Button to confirm the dialog.
            cancel_button (QPushButton): Button to cancel the dialog.
        """
        super().__init__(parent)
        self.resize(320,220)
        self.setWindowTitle("Lily Walk Details")
        self.exlbl = QLabel("Notes?")
        self.lily_walk_note = QLineEdit()
        self.exlbl2 = QLabel("How well did she seem to walk?")
        self.exlbl1 = QLabel("How did she behave?")
        self.lily_gait = QSlider(Qt.Orientation.Horizontal)
        self.lily_gait_spinbox = QSpinBox()
        self.lily_behavior = QSlider(Qt.Orientation.Horizontal)
        self.lily_behavior_spinbox = QSpinBox()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        self.setup_ui()
        self.create_layout()
        self.connect_signals()
        self.setStyleSheet(lily_styles)

    def setup_ui(self):                        
        """
        Sets up the UI components for the Lily Walk dialog.
        This method initializes the placeholder text for the notes field, 
        sets the range for the behavior and gait sliders and spinboxes.
        UI Components:
        - Notes field placeholder text set to "Notes".
        - Behavior slider and spinbox range set from 0 to 10.
        - Gait slider and spinbox range set from 0 to 10.
        """
        self.lily_walk_note.setPlaceholderText("Notes")
                
        self.lily_behavior.setRange(0, 10)
        self.lily_behavior_spinbox.setRange(0, 10)

        # Intensity slider and spinbox
        self.lily_gait.setRange(0, 10)
        self.lily_gait_spinbox.setRange(0, 10)

        # Buttons

    def create_layout(self):
        """
        Creates and sets the main layout for the Lily Walk Dialog UI.
        This method constructs the main layout using QVBoxLayout and adds various widgets
        and sub-layouts to it, including:
        - Lily Notes
        - Behavior Slider and Spinbox
        - Gait Slider and Spinbox
        - Buttons (OK and Cancel)
        The layout is then set as the main layout for the dialog.
        Widgets and layouts added:
        - self.exlbl: QLabel for Lily Notes
        - self.lily_walk_note: Widget for displaying Lily's walk notes
        - self.exlbl1: QLabel for Behavior Slider
        - self.lily_behavior: Slider for Lily's behavior
        - self.lily_behavior_spinbox: Spinbox for Lily's behavior
        - self.exlbl2: QLabel for Gait Slider
        - self.lily_gait: Slider for Lily's gait
        - self.lily_gait_spinbox: Spinbox for Lily's gait
        - self.ok_button: QPushButton for OK action
        - self.cancel_button: QPushButton for Cancel action
        """
        main_layout = QVBoxLayout()

        # Lily Notes
        main_layout.addWidget(self.exlbl)
        main_layout.addWidget(self.lily_walk_note)

        # Behavior Slider and Spinbox
        lily_walked_like_layout = QVBoxLayout()
        lily_walked_like_layout.addWidget(self.exlbl1)
        lily_walked_like_layout.addWidget(self.lily_behavior)
        lily_walked_like_layout.addWidget(self.lily_behavior_spinbox)
        main_layout.addLayout(lily_walked_like_layout)
        
        # Gait Slider and Spinbox
        lily_walked_like_layout2 = QVBoxLayout()
        lily_walked_like_layout2.addWidget(self.exlbl2)
        lily_walked_like_layout2.addWidget(self.lily_gait)
        lily_walked_like_layout2.addWidget(self.lily_gait_spinbox)
        main_layout.addLayout(lily_walked_like_layout2)

        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def connect_signals(self):
        """
        Connects the signals and slots for the UI elements.

        This method sets up the following connections:
        - Synchronizes the value of the effort slider with the effort spinbox.
        - Synchronizes the value of the effort spinbox with the effort slider.
        - Synchronizes the value of the intensity slider with the intensity spinbox.
        - Synchronizes the value of the intensity spinbox with the intensity slider.
        - Connects the OK button to the accept method.
        - Connects the Cancel button to the reject method.
        """
        # Synchronize effort slider and spinbox
        self.lily_behavior.valueChanged.connect(self.lily_behavior_spinbox.setValue)
        self.lily_behavior_spinbox.valueChanged.connect(self.lily_behavior.setValue)

        # Synchronize intensity slider and spinbox
        self.lily_gait.valueChanged.connect(self.lily_gait_spinbox.setValue)
        self.lily_gait_spinbox.valueChanged.connect(self.lily_gait.setValue)

        # Connect buttons
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
