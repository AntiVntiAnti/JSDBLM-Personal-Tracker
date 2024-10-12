from PyQt6.QtCore import QSettings, QDate, QTime
from PyQt6.QtWidgets import QDateEdit, QTextEdit, QSlider, QSpinBox
import utility.tracker_config as tkc
from utility.logger_setup import create_logger
logger = create_logger(__name__)


class SettingsManagerLilysWidgets:
    """
    A class to manage the settings of Lily's widgets using QSettings.
    Methods
    -------
    __init__():
        Initializes the settings manager with the organization name and application name.
    save_lilys_widget_states(
        lily_notes: QTextEdit
        Saves the current states of Lily's widgets to the settings.
    restore_lilys_widget_states(
        lily_notes: QTextEdit
        Restores the states of Lily's widgets from the settings.
    """
    def __init__(self):
        """
        Initializes the settings manager for Lily's widgets.

        This constructor sets up the QSettings object with the organization name
        and application name specified in the tkc module.

        Attributes:
            settings (QSettings): The settings object for managing application settings.
        """
        self.settings = QSettings(tkc.ORGANIZATION_NAME, tkc.LILY_APP)
    
    def save_lilys_widget_states(

        self,
        lily_time_in_room_slider: QSlider,
        lily_mood_slider: QSlider,
        lily_mood_activity_slider: QSlider,
        lily_energy_slider: QSlider,
        lily_time_in_room: QSlider,
        lily_mood: QSpinBox,
        lily_activity: QSpinBox,
        lily_energy: QSpinBox,
        lily_notes: QTextEdit,
    ):
        """
        Saves the states of Lily's widgets to the settings.

        Args:
            lily_time_in_room_slider (QSlider): Slider for Lily's time in room.
            lily_mood_slider (QSlider): Slider for Lily's mood.
            lily_mood_activity_slider (QSlider): Slider for Lily's mood activity.
            lily_energy_slider (QSlider): Slider for Lily's energy.
            lily_time_in_room (QSlider): Slider for Lily's time in room.
            lily_mood (QSpinBox): SpinBox for Lily's mood.
            lily_activity (QSpinBox): SpinBox for Lily's activity.
            lily_energy (QSpinBox): SpinBox for Lily's energy.
            lily_notes (QTextEdit): TextEdit for Lily's notes.

        Raises:
            Exception: If saving any of the widget states fails.
        """
        try:
            self.settings.setValue('lily_time_in_room_slider', lily_time_in_room_slider.value())
            self.settings.setValue('lily_mood_slider', lily_mood_slider.value())
            self.settings.setValue('lily_mood_activity_slider', lily_mood_activity_slider.value())
            self.settings.setValue('lily_energy_slider', lily_energy_slider.value())
            self.settings.setValue('lily_time_in_room', lily_time_in_room.value())
            self.settings.setValue('lily_mood', lily_mood.value())
            self.settings.setValue('lily_activity', lily_activity.value())
            self.settings.setValue('lily_energy', lily_energy.value())
            self.settings.setValue('lily_notes', lily_notes.toHtml())
        except Exception as e:
            logger.error(f"Failed to save Tuesday's journal: {str(e)}")
    
    def restore_lilys_widget_states(        
        self,
        lily_time_in_room_slider: QSlider,
        lily_mood_slider: QSlider,
        lily_mood_activity_slider: QSlider,
        lily_energy_slider: QSlider,
        lily_time_in_room: QSlider,
        lily_mood: QSpinBox,
        lily_activity: QSpinBox,
        lily_energy: QSpinBox,
        lily_notes: QTextEdit, ):
        """
        Restores the state of Lily's widgets from saved settings.

        Parameters:
        self (object): The instance of the class containing the settings.
        lily_time_in_room_slider (QSlider): Slider for Lily's time in room.
        lily_mood_slider (QSlider): Slider for Lily's mood.
        lily_mood_activity_slider (QSlider): Slider for Lily's mood activity.
        lily_energy_slider (QSlider): Slider for Lily's energy.
        lily_time_in_room (QSlider): Slider for Lily's time in room.
        lily_mood (QSpinBox): SpinBox for Lily's mood.
        lily_activity (QSpinBox): SpinBox for Lily's activity.
        lily_energy (QSpinBox): SpinBox for Lily's energy.
        lily_notes (QTextEdit): TextEdit for Lily's notes.

        Raises:
        Exception: If there is an error restoring the widget states, it logs an error message.
        """
        try:
            lily_time_in_room_slider.setValue(self.settings.value('lily_time_in_room_slider',
                                                                  0,
                                                                  type=int))
            lily_mood_slider.setValue(self.settings.value('lily_mood_slider', 0, type=int))
            lily_mood_activity_slider.setValue(self.settings.value('lily_mood_activity_slider',
                                                                   0,
                                                                   type=int))
            lily_energy_slider.setValue(self.settings.value('lily_energy_slider', 0, type=int))
            lily_time_in_room.setValue(self.settings.value('lily_time_in_room', 0, type=int))
            lily_mood.setValue(self.settings.value('lily_mood', 0, type=int))
            lily_activity.setValue(self.settings.value('lily_activity', 0, type=int))
            lily_energy.setValue(self.settings.value('lily_energy', 0, type=int))
            lily_notes.setHtml(self.settings.value('lily_notes', "", type=str))
        except Exception as e:
            logger.error(f"Failed to restore Tuesday's journal: {str(e)}")
