from PyQt6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QSpinBox, QSlider, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import Qt
# stylesheet
# ui setup
from ui.dialogs_lily.lily_ui import Ui_Dialog
# layout creation
# signal connections

class LilyWalkDialog(QDialog, Ui_Dialog):
    """
    LilyWalkDialog is a custom QDialog that provides a user interface for entering details about Lily's walk.

    Attributes:
        exlbl (QLabel): Label for the notes section.
        lily_walk_note (QLineEdit): Input field for notes.
        exlbl2 (QLabel): Label for the gait evaluation section.
        exlbl1 (QLabel): Label for the behavior evaluation section.
        lily_gait (QSlider): Slider for evaluating Lily's gait.
        lily_gait_spinbox (QSpinBox): Spinbox for displaying the value of the gait slider.
        lily_behavior (QSlider): Slider for evaluating Lily's behavior.
        lily_behavior_spinbox (QSpinBox): Spinbox for displaying the value of the behavior slider.
        ok_button (QPushButton): Button to confirm the dialog.
        cancel_button (QPushButton): Button to cancel the dialog.

    Methods:
        __init__(parent=None): Initializes the dialog, sets up the UI, creates the layout, connects signals, and applies the stylesheet.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Call the generated setup method
        self.initialize_widgets()
        self.resize(320, 220)
        self.setWindowTitle("Lily Walk Details")
        self.connect_signals()
        # stylesheet
    
    def initialize_widgets(self):
        """
        Initializes the widgets for the dialog.

        This method customizes the widgets and styles for the dialog. It sets up
        the stylesheets from an external file and correctly connects the button
        box to the instance methods for handling acceptance and rejection actions.

        Actions:
        - Sets the stylesheet for the dialog.
        - Connects the 'accepted' signal of the button box to the 'accept' method.
        - Connects the 'rejected' signal of the button box to the 'reject' method.
        """
        try:
            # Correctly connecting the button box to the instance methods
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)
        except Exception as e:
            logger.error(f"Error in constructicon of wefe_dialog : {e}", exc_info=True)
    
    def connect_signals(self):
        """
        Connects the signals and slots for the UI elements in the exercise dialog.
    
        This method synchronizes the values between sliders and spinboxes for effort and intensity,
        ensuring that changes in one are reflected in the other. It also connects the OK and Cancel
        buttons to their respective accept and reject actions.
        """
        # Synchronize effort slider and spinbox
        self.lily_behavior.valueChanged.connect(self.lily_behavior_spinbox.setValue)
        self.lily_behavior_spinbox.valueChanged.connect(self.lily_behavior.setValue)
        
        self.lily_gait.valueChanged.connect(self.lily_gait_spinbox.setValue)
        self.lily_gait_spinbox.valueChanged.connect(self.lily_gait.setValue)
