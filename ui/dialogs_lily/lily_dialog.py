
from PyQt6.QtWidgets import QDialog, QSlider, QSpinBox
from ui.dialogs_lily.lily_ui import Ui_LilyDialog  # Import the generated file
from utility.logger_setup import create_logger
logger = create_logger(__name__)
from ui.frameless_dialog_window import FramelessDialog


class LilyWalkDialog(FramelessDialog, Ui_LilyDialog):
    
    """LilyWalkDialog is a custom dialog class that inherits from FramelessDialog and Ui_LilyDialog.
    It provides a user interface for adjusting Lily's behavior and gait through sliders.
    Methods:
        __init__(self, parent=None):
            Initializes the dialog, sets up the UI, and initializes the widgets.
            Args:
                parent (QWidget, optional): The parent widget. Defaults to None.
                Exception: If there is an error during the construction of the dialog,
                initialize_widgets(self):
                """
    
    
    def __init__(self, parent=None):
        """
        Initializes the LilyDialog class.
        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        Raises:
            Exception: If there is an error during the initialization process, it will be logged.
        """        
        try:
            super().__init__(parent)
            self.setupUi(self)  # Call the generated setup method
            self.initialize_widgets()
            self.setFixedSize(325, 175)
        except Exception as e:
            logger.error(f"Error in constructicon of wefe_dialog : {e}", exc_info=True)
    
    def initialize_widgets(self):
        """
        Initializes the widgets and connects their signals to the appropriate slots.
        This method sets up the connections between the sliders and their corresponding
        value display widgets, ensuring that changes in one are reflected in the other.
        It also connects the button box's accepted and rejected signals to the instance's
        accept and reject methods, respectively.
        Raises:
            Exception: If there is an error during the initialization of the widgets,
                       it logs the error with detailed information.
        """
        try:
            self.lily_behavior_slider.valueChanged.connect(self.lily_behavior.setValue)
            self.lily_behavior.valueChanged.connect(self.lily_behavior_slider.setValue)
            
            self.lily_gait_slider.valueChanged.connect(self.lily_gait.setValue)
            self.lily_gait.valueChanged.connect(self.lily_gait_slider.setValue)
            # Correctly connecting the button box to the instance methods
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)
        except Exception as e:
            logger.error(f"Error in constructicon of wefe_dialog : {e}", exc_info=True)
    
