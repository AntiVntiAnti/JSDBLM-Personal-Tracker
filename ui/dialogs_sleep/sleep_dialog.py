from PyQt6.QtWidgets import QDialog
from ui.dialogs_sleep.sleep_ui import Ui_Dialog  # Import the generated file
from utility.logger_setup import create_logger
logger = create_logger(__name__)
from ui.frameless_dialog_window import FramelessDialog


class SleepDialog(FramelessDialog, Ui_Dialog):
    """
    SleepDialog class provides a dialog interface for tracking sleep patterns.
    Attributes:
        total_hrs_slept (str): A string representing the total hours slept in HH:mm format.
    Methods:
        __init__(parent=None):
            Initializes the SleepDialog instance, sets up the UI, initializes widgets, and connects signals.
        initialize_widgets():
            Initializes and connects the widgets within the dialog.
        calculate_total_hours_slept() -> None:
            Calculates the total hours slept based on the time asleep and time awake, and updates the UI.
    """
    def __init__(self, parent=None):
        """
        Initializes the SleepDialog class.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.

        Initializes the UI components, sets the fixed size of the dialog,
        and connects the timeChanged signals of the time_asleep and time_awake
        widgets to the calculate_total_hours_slept method.

        Raises:
            Exception: If an error occurs during initialization, it is logged.
        """

        try:
            super().__init__(parent)
            self.setupUi(self)  # Call the generated setup method
            self.initialize_widgets()
            self.setFixedSize(345, 200)
            # Calculate total hours slept whenever time changes
            self.time_asleep.timeChanged.connect(self.calculate_total_hours_slept)
            self.time_awake.timeChanged.connect(self.calculate_total_hours_slept)
        except Exception as e:
            logger.error(f"Error in constructicon of sleep_dialog : {e}", exc_info=True)
    
    def initialize_widgets(self):
        """
        Initializes the widgets and connects their signals to the appropriate slots.
        This method sets up the connections between the sliders and their corresponding
        value displays, ensuring that changes in one are reflected in the other. It also
        connects the accept and reject signals of the button box to the respective instance
        methods.
        Raises:
            Exception: If there is an error during the initialization of the widgets, it
            logs the error with detailed information.
        """
        try:
            self.sleep_quality_slider.valueChanged.connect(self.sleep_quality.setValue)
            self.sleep_quality.valueChanged.connect(self.sleep_quality_slider.setValue)
            self.woke_up_like_slider.valueChanged.connect(self.woke_up_like.setValue)
            self.woke_up_like.valueChanged.connect(self.woke_up_like_slider.setValue)
            # Correctly connecting the button box to the instance methods
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)
            
        except Exception as e:
            logger.error(f"Error in constructicon of sleep_dialog : {e}", exc_info=True)
    
    def calculate_total_hours_slept(self) -> None:
        """
        Calculates the total hours slept based on the time asleep and time awake.
        This method retrieves the time asleep and time awake, converts them to total minutes since the start of the day,
        calculates the difference in minutes, and handles cases where the time spans past midnight. The result is then
        converted back to hours and minutes and formatted as a string in HH:mm format. The formatted string is set to
        the `total_hours_slept` attribute and updated in the corresponding lineEdit.
        Raises:
            Exception: If an error occurs during the calculation, it logs the error with detailed information.
        """
        try:
            time_asleep = self.time_asleep.time()
            time_awake = self.time_awake.time()
            
            # Convert time to total minutes since the start of the day
            minutes_asleep = (time_asleep.hour() * 60 + time_asleep.minute())
            minutes_awake = (time_awake.hour() * 60 + time_awake.minute())
            
            # Calculate the difference in minutes
            total_minutes = minutes_awake - minutes_asleep
            
            # Handle case where the time spans past midnight
            if total_minutes < 0:
                total_minutes += (24 * 60)  # Add 24 hours worth of minutes
            
            # Convert back to hours and minutes
            hours = total_minutes // 60
            minutes = total_minutes % 60
            
            # Create the total_hours_slept string in HH:mm format
            self.total_hrs_slept = f"{hours:02}:{minutes:02}"
            
            # Update the lineEdit with the total hours slept
            self.total_hours_slept.setText(self.total_hrs_slept)
        
        except Exception as e:
            logger.error(f"Error occurred while calculating total hours slept: {e}", exc_info=True)
