from PyQt6.QtWidgets import QDialog
from ui.dialogs_diet.diet_ui import Ui_Dialog  # Import the generated file
from utility.logger_setup import create_logger
logger = create_logger(__name__)
from ui.frameless_dialog_window import FramelessDialog

class DietDialog(FramelessDialog, Ui_Dialog):
    """
    DietDialog is a custom dialog class that inherits from FramelessDialog and Ui_Dialog.
    It initializes the dialog, sets up the UI, and connects the button box signals to 
    the corresponding instance methods.
    Methods:
        __init__(self, parent=None):
            Initializes the dialog with an optional parent widget. Logs any errors 
            that occur during initialization.
        initialize_widgets(self):
            Connects the accepted and rejected signals of the button box to the 
            corresponding instance methods. Logs any errors that occur during this process.
        Exception: If an error occurs during the initialization or widget setup, it is logged.
    
    """
    def __init__(self, parent=None):
        """
        Initializes the dialog.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.

        Raises:
            Exception: If an error occurs during the initialization, it is logged.
        """

        try:
            super().__init__(parent)
            self.setupUi(self)  # Call the generated setup method
            self.initialize_widgets()
            self.setFixedSize(180, 125)
        except Exception as e:
            logger.error(f"Error in constructicon of wefe_dialog : {e}", exc_info=True)
    
    def initialize_widgets(self):
        """
        Initializes the widgets for the dialog.

        This method connects the accepted and rejected signals of the button box
        to the corresponding instance methods. If an error occurs during this 
        process, it logs the error with detailed exception information.

        Raises:
            Exception: If there is an error connecting the button box signals.
        """

        try:
            # Correctly connecting the button box to the instance methods
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)
        except Exception as e:
            logger.error(f"Error in constructicon of wefe_dialog : {e}", exc_info=True)
    
