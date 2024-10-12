# cspr_ui.py
from PyQt6.QtWidgets import QDialog
from ui.dialogs_cspr.cspr_ui import Ui_Dialog  # Import the generated file
from ui.dialogs_cspr.static.cspr_style import stylesheet
import ui.dialogs_cspr.static.csprres
from utility.logger_setup import create_logger
logger = create_logger(__name__)
from ui.frameless_dialog_window import FramelessDialog


class CsprDialog(FramelessDialog, Ui_Dialog):
    """
    CsprDialog is a custom QDialog that integrates with the Ui_CsprDialog interface.
    Attributes:
        parent (QWidget): The parent widget of the dialog.
        stylesheet (str): The stylesheet to be applied to the dialog.
    Methods:
        __init__(self, parent=None):
            Initializes the CsprDialog, sets up the UI, initializes widgets, resizes the dialog, and connects signals.
        initialize_widgets(self):
            Customizes widgets and styles, sets up stylesheets, and connects button box signals to instance methods.
        connect_signals(self):
            Connects the valueChanged signals of sliders and spinboxes to synchronize their values.
    """
    
    def __init__(self, parent=None):
        """
        Initializes the CsprDialog class.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.

        This method sets up the UI, initializes the widgets, resizes the dialog,
        and connects the necessary signals.
        """
        try:
            super().__init__(parent)
            self.setupUi(self)  # Call the generated setup method
            self.initialize_widgets()
            self.setFixedSize(265, 380)
            self.connect_signals()
        except Exception as e:
            logger.error(f"Error occurred in cspr_dialog {e}", exc_info=True)
            
    def initialize_widgets(self):
        """
        Initializes and customizes the widgets in the dialog.

        This method sets up the stylesheets from an external file and connects
        the button box signals to the corresponding instance methods for handling
        acceptance and rejection actions.

        Actions:
            - Sets the stylesheet for the dialog.
            - Connects the 'accepted' signal of buttonBox_2 to the 'accept' method.
            - Connects the 'rejected' signal of buttonBox_2 to the 'reject' method.
        """
        try:
            # Here you can customize widgets, styles, etc.
            # Set up stylesheets from external file
            self.setStyleSheet(stylesheet)
            # Correctly connecting the button box to the instance methods
            self.buttonBox_2.accepted.connect(self.accept)
            self.buttonBox_2.rejected.connect(self.reject)
        except Exception as e:
            logger.error(f"Error occurred in cspr_dialog {e}", exc_info=True)
    
    def connect_signals(self):
        """
        Connects the signals and slots for the UI elements.

        This method sets up the connections between the sliders and spinboxes
        for the 'calm', 'stress', 'pain', and 'rage' levels. When the value of
        a slider changes, the corresponding spinbox is updated, and vice versa.

        Connections:
            - calm_slider <-> calm_spinbox
            - stress_slider <-> stress_spinbox
            - pain_slider <-> pain_spinbox
            - rage_slider <-> rage_spinbox
        """
        try:
            # Assuming these widgets are defined in the Designer file and accessed directly
            self.calm_slider.valueChanged.connect(self.calm_spinbox.setValue)
            self.calm_spinbox.valueChanged.connect(self.calm_slider.setValue)
            self.stress_slider.valueChanged.connect(self.stress_spinbox.setValue)
            self.stress_spinbox.valueChanged.connect(self.stress_slider.setValue)
            self.pain_slider.valueChanged.connect(self.pain_spinbox.setValue)
            self.pain_spinbox.valueChanged.connect(self.pain_slider.setValue)
            self.rage_slider.valueChanged.connect(self.rage_spinbox.setValue)
            self.rage_spinbox.valueChanged.connect(self.rage_slider.setValue)
        except Exception as e:
            logger.error(f"Error occurred in cspr_dialog {e}", exc_info=True)
