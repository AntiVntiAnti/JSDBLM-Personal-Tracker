from PyQt6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QSpinBox, QSlider, QPushButton, QVBoxLayout, QHBoxLayout,
    QTimeEdit, QDateEdit
)
from utility.logger_setup import create_logger

logger = create_logger(__name__)
from PyQt6.QtCore import Qt
# stylesheet
from ui.dialogs_sleep.exer_style import exer_dialog
# ui setup
from ui.dialogs_sleep.ui_setup import setup_ui
# layout creation
from ui.dialogs_sleep.layout_creation import create_layout
# signal connections
from ui.dialogs_sleep.signal_connections import connect_signals


class SleepDetailsDialog(QDialog):
    """
    SleepDetailsDialog is a QDialog subclass that provides a user interface for entering and displaying sleep details.
    Attributes:
        time_asleep_lbl (QLabel): Label for the time asleep input.
        time_asleep (QTimeEdit): Time edit widget for the time asleep input.
        time_awake_lbl (QLabel): Label for the time awake input.
        time_awake (QTimeEdit): Time edit widget for the time awake input.
        total_hours_lbl (QLabel): Label for the total hours slept display.
        total_hours_slept (QLineEdit): Line edit widget to display the total hours slept.
        sleep_quality_lbl (QLabel): Label for the sleep quality input.
        sleep_quality_slider (QSlider): Slider widget for the sleep quality input.
        sleep_quality (QSpinBox): Spin box widget for the sleep quality input.
        woke_up_lbl (QLabel): Label for the difficulty of waking up input.
        woke_up_like_slider (QSlider): Slider widget for the difficulty of waking up input.
        woke_up_like (QSpinBox): Spin box widget for the difficulty of waking up input.
        ok_button (QPushButton): Button to confirm the dialog.
        cancel_button (QPushButton): Button to cancel the dialog.
    Methods:
        __init__(self, parent=None):
            Initializes the SleepDetailsDialog with the given parent.
        calculate_total_hours_slept(self) -> None:
            Calculates the total hours slept based on the time asleep and time awake inputs.
            Updates the total_hours_slept line edit with the calculated value.
    """
    
    def __init__(self, parent=None):
        """
        Initializes the dialog for sleep details.
        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        Attributes:
            time_asleep_lbl (QLabel): Label for the time asleep input.
            time_asleep (QTimeEdit): Input for the time asleep.
            time_awake_lbl (QLabel): Label for the time awake input.
            time_awake (QTimeEdit): Input for the time awake.
            total_hours_lbl (QLabel): Label for the total hours slept input.
            total_hours_slept (QLineEdit): Input for the total hours slept.
            sleep_quality_lbl (QLabel): Label for the sleep quality input.
            sleep_quality_slider (QSlider): Slider for the sleep quality input.
            sleep_quality (QSpinBox): Spin box for the sleep quality input.
            woke_up_lbl (QLabel): Label for the difficulty of waking up input.
            woke_up_like_slider (QSlider): Slider for the difficulty of waking up input.
            woke_up_like (QSpinBox): Spin box for the difficulty of waking up input.
            ok_button (QPushButton): Button to confirm the dialog.
            cancel_button (QPushButton): Button to cancel the dialog.
        Methods:
            setup_ui(self): Sets up the user interface.
            create_layout(self): Creates the layout for the dialog.
            connect_signals(self): Connects the signals for the dialog.
            calculate_total_hours_slept(self): Calculates the total hours slept based on the time asleep and time awake.
        """
        try:
            super().__init__(parent)
            self.resize(245, 145)
            self.setWindowTitle("Sleep Details")
            self.setStyleSheet(exer_dialog)
            try:
                # Dialog Widgets
                self.time_asleep_lbl = QLabel("Time Asleep:")
                self.time_asleep = QTimeEdit()
                self.time_awake_lbl = QLabel("Time Awake:")
                self.time_awake = QTimeEdit()
                self.total_hours_lbl = QLabel("Total Hours Slept: ")
                self.total_hours_slept = QLineEdit()
                self.sleep_quality_lbl = QLabel("How well did I sleep?")
                self.sleep_quality_slider = QSlider(Qt.Orientation.Horizontal)
                self.sleep_quality = QSpinBox()
                self.woke_up_lbl = QLabel("How difficult was waking up?")
                self.woke_up_like_slider = QSlider(Qt.Orientation.Horizontal)
                self.woke_up_like = QSpinBox()
                self.ok_button = QPushButton("OK")
                self.cancel_button = QPushButton("Cancel")
                try:
                    # ui setup
                    setup_ui(self)
                    # layout creation
                    create_layout(self)
                    # signal connections
                    connect_signals(self)
                except Exception as e:
                    logger.error(f"Error occurred while setting up sleep dialog {e}")
            except Exception as e:
                logger.error(f"{e}")
            # Calculate total hours slept whenever time changes
            self.time_asleep.timeChanged.connect(self.calculate_total_hours_slept)
            self.time_awake.timeChanged.connect(self.calculate_total_hours_slept)
        except Exception as e:
            logger.error(f"{e}")
            
    def calculate_total_hours_slept(self) -> None:
        """
        Calculates the total hours slept based on the time asleep and time awake.
        This method retrieves the time asleep and time awake from the respective
        attributes, calculates the total duration of sleep in hours and minutes,
        and updates the `total_hours_slept` attribute and the corresponding UI
        element with the formatted result.
        Handles cases where the sleep duration spans past midnight.
        Raises:
            Exception: If an error occurs during the calculation, it is logged.
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
