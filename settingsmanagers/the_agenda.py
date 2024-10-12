from PyQt6.QtCore import QSettings, QDate, QTime
from PyQt6.QtWidgets import QDateEdit, QTextEdit
import utility.tracker_config as tkc
from utility.logger_setup import create_logger
logger = create_logger(__name__)


class SettingsManagerJournal:
    """
    SettingsManagerJournal is responsible for saving and restoring journal settings for each day of the week.
    Methods:
        __init__():
            Initializes the SettingsManagerJournal with QSettings.
        save_journal(
            sat_note_one: QTextEdit
            Saves the journal settings for each day of the week.
                sun_date (QDateEdit): The QDateEdit widget for the Sunday date.
                sun_note_one (QTextEdit): The QTextEdit widget for the Sunday note.
                mon_date (QDateEdit): The QDateEdit widget for the Monday date.
                mon_note_one (QTextEdit): The QTextEdit widget for the Monday note.
                tues_date (QDateEdit): The QDateEdit widget for the Tuesday date.
                tues_note_one (QTextEdit): The QTextEdit widget for the Tuesday note.
                wed_date (QDateEdit): The QDateEdit widget for the Wednesday date.
                wed_note_one (QTextEdit): The QTextEdit widget for the Wednesday note.
                thurs_date (QDateEdit): The QDateEdit widget for the Thursday date.
                thurs_note_one (QTextEdit): The QTextEdit widget for the Thursday note.
                sat_date (QDateEdit): The QDateEdit widget for the Saturday date.
                sat_note_one (QTextEdit): The QTextEdit widget for the Saturday note.
        restore_journal(
            sat_note_one: QTextEdit
            Restores the journal settings for each day of the week.
                sun_date (QDateEdit): The QDateEdit widget for the Sunday date.
                sun_note_one (QTextEdit): The QTextEdit widget for the Sunday note.
                mon_date (QDateEdit): The QDateEdit widget for the Monday date.
                mon_note_one (QTextEdit): The QTextEdit widget for the Monday note.
                tues_date (QDateEdit): The QDateEdit widget for the Tuesday date.
                tues_note_one (QTextEdit): The QTextEdit widget for the Tuesday note.
                wed_date (QDateEdit): The QDateEdit widget for the Wednesday date.
                wed_note_one (QTextEdit): The QTextEdit widget for the Wednesday note.
                thurs_date (QDateEdit): The QDateEdit widget for the Thursday date.
                thurs_note_one (QTextEdit): The QTextEdit widget for the Thursday note.
                sat_date (QDateEdit): The QDateEdit widget for the Saturday date.
                sat_note_one (QTextEdit): The QTextEdit widget for the Saturday note.
    """
    def __init__(self):
        """
        Initializes the settings manager.

        This constructor sets up the QSettings object with the organization name
        and application name defined in the tkc module.

        Attributes:
            settings (QSettings): The settings object for managing application settings.
        """
        self.settings = QSettings(tkc.ORGANIZATION_NAME, tkc.APPLICATION_NAME)

    def save_journal(
        self,
        sun_date: QDateEdit,
        sun_note_one: QTextEdit,
        mon_date: QDateEdit,
        mon_note_one: QTextEdit,
        tues_date: QDateEdit,
        tues_note_one: QTextEdit,
        wed_date: QDateEdit,
        wed_note_one: QTextEdit,
        thurs_date: QDateEdit,
        thurs_note_one: QTextEdit,
        fri_date: QDateEdit,
        fri_note_one: QTextEdit,
        sat_date: QDateEdit,
        sat_note_one: QTextEdit,
    ):
        """
        Saves the journal settings for each day of the week.

            sun_date (QDateEdit): The QDateEdit widget for the Sunday date.
            sun_note_one (QTextEdit): The QTextEdit widget for the Sunday note.
            mon_date (QDateEdit): The QDateEdit widget for the Monday date.
            mon_note_one (QTextEdit): The QTextEdit widget for the Monday note.
            tues_date (QDateEdit): The QDateEdit widget for the Tuesday date.
            tues_note_one (QTextEdit): The QTextEdit widget for the Tuesday note.
            wed_date (QDateEdit): The QDateEdit widget for the Wednesday date.
            wed_note_one (QTextEdit): The QTextEdit widget for the Wednesday note.
            thurs_date (QDateEdit): The QDateEdit widget for the Thursday date.
            thurs_note_one (QTextEdit): The QTextEdit widget for the Thursday note.
            sat_date (QDateEdit): The QDateEdit widget for the Saturday date.
            sat_note_one (QTextEdit): The QTextEdit widget for the Saturday note.
        """
        try:
            self.settings.setValue('sun_date', sun_date.date())
            self.settings.setValue('sun_note_one', sun_note_one.toHtml())
            self.settings.setValue('mon_date', mon_date.date())
            self.settings.setValue('mon_note_one', mon_note_one.toHtml())
            self.settings.setValue('tues_date', tues_date.date())
            self.settings.setValue('tues_note_one', tues_note_one.toHtml())
            self.settings.setValue('wed_date', wed_date.date())
            self.settings.setValue('wed_note_one', wed_note_one.toHtml())
            self.settings.setValue('thurs_date', thurs_date.date())
            self.settings.setValue('thurs_note_one', thurs_note_one.toHtml())
            self.settings.setValue('fri_date', fri_date.date())
            self.settings.setValue('fri_note_one', fri_note_one.toHtml())
            self.settings.setValue('sat_date', sat_date.date())
            self.settings.setValue('sat_note_one', sat_note_one.toHtml())
        except Exception as e:
            logger.error(f"Error saving journal settings: {str(e)}")

    def restore_journal(        
        self,
        sun_date: QDateEdit,
        sun_note_one: QTextEdit,
        mon_date: QDateEdit,
        mon_note_one: QTextEdit,
        tues_date: QDateEdit,
        tues_note_one: QTextEdit,
        wed_date: QDateEdit,
        wed_note_one: QTextEdit,
        thurs_date: QDateEdit,
        thurs_note_one: QTextEdit,
        fri_date: QDateEdit,
        fri_note_one: QTextEdit,
        sat_date: QDateEdit,
        sat_note_one: QTextEdit,
    ):
        """
        Restores the journal entries for each day of the week from the settings.

        Parameters:
        self: The instance of the class.
        sun_date (QDateEdit): The date editor for Sunday.
        sun_note_one (QTextEdit): The text editor for the first note on Sunday.
        mon_date (QDateEdit): The date editor for Monday.
        mon_note_one (QTextEdit): The text editor for the first note on Monday.
        tues_date (QDateEdit): The date editor for Tuesday.
        tues_note_one (QTextEdit): The text editor for the first note on Tuesday.
        wed_date (QDateEdit): The date editor for Wednesday.
        wed_note_one (QTextEdit): The text editor for the first note on Wednesday.
        thurs_date (QDateEdit): The date editor for Thursday.
        thurs_note_one (QTextEdit): The text editor for the first note on Thursday.
        fri_date (QDateEdit): The date editor for Friday.
        fri_note_one (QTextEdit): The text editor for the first note on Friday.
        sat_date (QDateEdit): The date editor for Saturday.
        sat_note_one (QTextEdit): The text editor for the first note on Saturday.

        Raises:
        Exception: If there is an error restoring the journal settings, it logs the error.
        """
        try:
            sun_date.setDate(self.settings.value('sun_date', QDate.currentDate()))
            sun_note_one.setHtml(self.settings.value('sun_note_one', "", type=str))
            mon_date.setDate(self.settings.value('mon_date', QDate.currentDate()))
            mon_note_one.setHtml(self.settings.value('mon_note_one', "", type=str))
            tues_date.setDate(self.settings.value('tues_date', QDate.currentDate()))
            tues_note_one.setHtml(self.settings.value('tues_note_one', "", type=str))
            wed_date.setDate(self.settings.value('wed_date', QDate.currentDate()))
            wed_note_one.setHtml(self.settings.value('wed_note_one', "", type=str))
            thurs_date.setDate(self.settings.value('thurs_date', QDate.currentDate()))
            thurs_note_one.setHtml(self.settings.value('thurs_note_one', "", type=str))
            fri_date.setDate(self.settings.value('fri_date', QDate.currentDate()))
            fri_note_one.setHtml(self.settings.value('fri_note_one', "", type=str))
            sat_date.setDate(self.settings.value('sat_date', QDate.currentDate()))
            sat_note_one.setHtml(self.settings.value('sat_note_one', "", type=str))
        except Exception as e:
            logger.error(f"Error restoring journal settings: {str(e)}")
