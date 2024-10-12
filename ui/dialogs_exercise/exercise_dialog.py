from PyQt6.QtWidgets import QDialog
from ui.dialogs_exercise.exercise_ui import Ui_Dialog  # Import the generated file
from utility.logger_setup import create_logger
logger = create_logger(__name__)
from ui.frameless_dialog_window import FramelessDialog

class ExerciseDetailsDialog(FramelessDialog, Ui_Dialog):
    """   
    ExerciseDetailsDialog is a custom dialog class that inherits from FramelessDialog and Ui_Dialog.
    It provides a user interface for displaying and interacting with exercise details.
    Methods:
        __init__(self, parent=None):
            Initializes the ExerciseDetailsDialog.
        initialize_widgets(self):
                Exception: If there is an error during the initialization of the widgets, it is logged.
    """
    def __init__(self, parent=None):
        """
        Initializes the ExerciseDialog.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.

        Raises:
            Exception: If an error occurs during initialization, it is logged.
        """

        try:
            super().__init__(parent)
            self.setupUi(self)  # Call the generated setup method
            self.initialize_widgets()
            self.setFixedSize(225, 245)
            # Calculate total hours slept whenever time changes
        except Exception as e:
            logger.error(f"Error in constructicon of exercise_dialog : {e}", exc_info=True)
    
    def initialize_widgets(self):
        """
        Initializes the widgets and connects their signals to the appropriate slots.
        This method sets up the following connections:
        - Synchronizes the value of the effort slider and spinbox.
        - Synchronizes the value of the intensity slider and spinbox.
        - Connects the accepted and rejected signals of the button box to the corresponding instance methods.
        If an exception occurs during the initialization, it logs an error message with the exception details.
        Raises:
            Exception: If there is an error during the initialization of the widgets.
        """
        try:
            self.effort_slider.valueChanged.connect(self.effort_spinbox.setValue)
            self.effort_spinbox.valueChanged.connect(self.effort_slider.setValue)
            
            # Synchronize intensity slider and spinbox
            self.intensity_slider.valueChanged.connect(self.intensity_spinbox.setValue)
            self.intensity_spinbox.valueChanged.connect(self.intensity_slider.setValue)
            
            # Correctly connecting the button box to the instance methods
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)
            
        except Exception as e:
            logger.error(f"Error in constructicon of exercise_self : {e}", exc_info=True)
    
