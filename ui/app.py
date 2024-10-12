import datetime
from typing import List, Tuple, Any

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import QDate, QSettings, QTime, Qt, QByteArray, QDateTime
from PyQt6.QtGui import QCloseEvent
from PyQt6.QtWidgets import (
    QApplication,
    QTextEdit,
    QPushButton,
    QDialog,
    QFormLayout,
    QLineEdit,
    QMessageBox, )
from PyQt6.QtPrintSupport import QPrintDialog

from ui.main_ui.gui import Ui_MainWindow
# TRACKER CONFIG FILE TKC
import utility.tracker_config as tkc
# LOGGING
from utility.logger_setup import create_logger

logger = create_logger(__name__)
# NAVIGATION
from navigation.master_navigation import (
    change_mainStack, change_alpha_stack_page,
    change_agenda_stack_page, )

# UTILITY
from utility.app_operations.diet_calc import calculate_calories
from utility.app_operations.save_generic import TextEditSaver
from utility.widgets_set_widgets.slider_spinbox_connections import connect_slider_spinbox
from utility.app_operations.frameless_window import FramelessWindow
from utility.app_operations.window_controls import WindowController
from utility.app_operations.current_date_highlighter import DateHighlighter
from utility.widgets_set_widgets.line_connections import line_edit_times
from utility.widgets_set_widgets.slider_timers import connect_slider_timeedits
from utility.widgets_set_widgets.buttons_set_time import btn_times
from utility.app_operations.show_hide import toggle_views
from utility.widgets_set_widgets.buttons_set_time import btn_times

# Database Manager
from database.database_manager import DataManager
# Delete Records setup
from database.database_utility.delete_records import delete_selected_rows
# setup Models
from database.database_utility.model_setup import create_and_set_model
# add basics data
from database.add_data.basics_mod.basics_shower import add_shower_data
from database.add_data.basics_mod.basics_exercise import add_exercise_data
from database.add_data.basics_mod.basics_teethbrushing import add_teethbrush_data
# add diet data
from database.add_data.diet_mod.diet_hydration import add_hydration_data
from database.add_data.diet_mod.diet import add_diet_data
# add Lily data
from database.add_data.lily_mod.lily_walk_notes import add_lily_walk_notes
from database.add_data.lily_mod.lily_diet import add_lily_diet_data
from database.add_data.lily_mod.lily_walks import add_lily_walk_data
from database.add_data.lily_mod.lily_time_in_room import add_time_in_room_data
from database.add_data.lily_mod.lily_mood import add_lily_mood_data
from database.add_data.lily_mod.lily_notes import add_lily_note_data
# add sleep data
from database.add_data.sleep_mod.sleep_quality import add_sleep_quality_data
from database.add_data.sleep_mod.sleep_total_hours_slept import add_total_hours_slept_data
from database.add_data.sleep_mod.sleep_woke_up_like import add_woke_up_like_data
from database.add_data.sleep_mod.sleep import add_sleep_data
# add mental data
from database.add_data.mental.wefe import add_wefe_data
from database.add_data.mental.mmdmr import add_mentalsolo_data
from database.add_data.mental.cspr import add_cspr_data
# add agenda days sorted below
from database.add_data.agenda.sunday import agenda_data_sunday
from database.add_data.agenda.monday import agenda_data_monday
from database.add_data.agenda.tuesday import agenda_data_tuesday
from database.add_data.agenda.wednesday import agenda_data_wednesday
from database.add_data.agenda.thursday import agenda_data_thursday
from database.add_data.agenda.friday import agenda_data_friday
from database.add_data.agenda.saturday import agenda_data_saturday
# QSettings modules for lilys mood and time in room as well as for
# the Agenda
from settingsmanagers.lilys_widgets import SettingsManagerLilysWidgets
from settingsmanagers.the_agenda import SettingsManagerJournal
# Formatters
from formatters.colors.highlight import HighlightColorFormatter
from formatters.colors.color_text import ColorTextFormatter
from formatters.general.bold import BoldTextFormatter
from formatters.general.italic import ItalicTextFormatter
from formatters.general.superscript import SuperScriptTextFormatter
from formatters.general.subscript import SubScriptTextFormatter
from formatters.general.decrease_size import DecreaseFontSizeFormatter
from formatters.general.increase_size import IncreaseFontSizeFormatter
from formatters.general.strikethrough import StrikeTextFormatter
from formatters.general.underline import UnderlineTextFormatter
from formatters.alignment.right_align import RightAlignFormatter
from formatters.alignment.center_align import CenterAlignFormatter
from formatters.alignment.justify_align import JustifyAlignFormatter
from formatters.alignment.left_align import LeftAlignFormatter

from ui.dialogs_lily.lily_dialog import LilyWalkDialog
from ui.dialogs_exercise.exercise_dialog import ExerciseDetailsDialog
from ui.dialogs_diet.neudiet_dialog import DietDialog
from ui.dialogs_sleep.sleep_dialog import SleepDialog
from ui.dialogs_mmdmr.mmdmr_dialog import MmdmrDialog
from ui.dialogs_wefe.wefe_dialog import WefeDialog
from ui.dialogs_cspr.cspr_dialog import CsprDialog


class TableInputDialog(QDialog):
    """
    Dialog window for inputting table dimensions.

    This dialog allows the user to input the amount rows and columns for a table.

    Attributes:
        rows_input (QLineEdit): Input field for the amount rows.
        columns_input (QLineEdit): Input field for the amount columns.
        ok_button (QPushButton): OK button for accepting the input.
        cancel_button (QPushButton): Cancel button for rejecting the input.
    """
    
    def __init__(self,
                 parent=None):
        super().__init__(parent)
        self.setWindowTitle('Table Dimensions')
        layout = QFormLayout(self)
        
        # Input fields for rows and columns
        self.rows_input = QLineEdit(self)
        self.columns_input = QLineEdit(self)
        layout.addRow('Rows:', self.rows_input)
        layout.addRow('Columns:', self.columns_input)
        
        # OK and Cancel buttons
        self.ok_button = QPushButton('OK', self)
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button = QPushButton('Cancel', self)
        self.cancel_button.clicked.connect(self.reject)
        layout.addRow(self.ok_button, self.cancel_button)
    
    def get_dimensions(self):
        """
        Get the dimensions entered by the user.

        Returns:
            tuple: A tuple containing the amount rows and columns entered by the user.
        """
        return self.rows_input.text(), self.columns_input.text()


class MainWindow(FramelessWindow, QtWidgets.QMainWindow, Ui_MainWindow):
    """
    MainWindow class represents the main application window and its components.

    This class inherits from FramelessWindow, QtWidgets.QMainWindow, and Ui_MainWindow, and is responsible for initializing
    and managing the main application window, its models, widgets, and various functionalities.

    Attributes:
        sat_model (None): Model for Saturday data.
        fri_model (None): Model for Friday data.
        wed_model (None): Model for Wednesday data.
        thurs_model (None): Model for Thursday data.
        mon_model (None): Model for Monday data.
        tues_model (None): Model for Tuesday data.
        sun_model (None): Model for Sunday data.
        date_widgets (None): Widgets for date selection.
        date_highlighter (None): Highlighter for dates.
        day_buttons (None): Buttons for day selection.
        mmdmr_model (None): Model for MMDMR data.
        cspr_model (None): Model for CSPR data.
        wefe_model (None): Model for WEFE data.
        context_menu (None): Context menu for the application.
        yoga_model (None): Model for yoga data.
        tooth_model (None): Model for tooth brushing data.
        shower_model (None): Model for shower data.
        hydration_model (None): Model for hydration data.
        diet_model (None): Model for diet data.
        lily_walk_note_model (None): Model for Lily's walk notes.
        lily_notes_model (None): Model for Lily's notes.
        time_in_room_model (None): Model for time spent in room.
        lily_walk_model (None): Model for Lily's walk data.
        lily_mood_model (None): Model for Lily's mood data.
        lily_diet_model (None): Model for Lily's diet data.
        btn_times (None): Button times.
        sleep_quality_model (None): Model for sleep quality data.
        woke_up_like_model (None): Model for "woke up like" data.
        sleep_model (None): Model for sleep data.
        total_hours_slept_model (None): Model for total hours slept data.
        total_hrs_slept (None): Total hours slept.
        basics_model (None): Model for basic data.
        settings (QSettings): Settings for the window/frame visibility.
        journal_settings_manager (SettingsManagerJournal): Manager for journal settings.
        settings_manager_lilys_widgets (SettingsManagerLilysWidgets): Manager for Lily's widget settings.
        ui (Ui_MainWindow): User interface for the main window.
        window_controller (WindowController): Controller for window operations.
        db_manager (DataManager): Manager for database operations.
        text_formatter_bold (BoldTextFormatter): Formatter for bold text.
        text_formatter_color (ColorTextFormatter): Formatter for colored text.
        text_formatter_decrease_font_size (DecreaseFontSizeFormatter): Formatter for decreasing font size.
        text_formatter_highlight (HighlightColorFormatter): Formatter for highlighting text.
        text_formatter_increase_font (IncreaseFontSizeFormatter): Formatter for increasing font size.
        text_formatter_italic (ItalicTextFormatter): Formatter for italic text.
        text_formatter_strikethrough (StrikeTextFormatter): Formatter for strikethrough text.
        text_formatter_subscript (SubScriptTextFormatter): Formatter for subscript text.
        text_formatter_superscript (SuperScriptTextFormatter): Formatter for superscript text.
        text_formatter_underline (UnderlineTextFormatter): Formatter for underlined text.
        TextFormatCenter (CenterAlignFormatter): Formatter for center alignment.
        TextFormatRightAlign (RightAlignFormatter): Formatter for right alignment.
        TextFormatAlignLeft (LeftAlignFormatter): Formatter for left alignment.
        TextFormatJustify (JustifyAlignFormatter): Formatter for justified alignment.
        text_edit_saver (TextEditSaver): Saver for text edits.

    Methods:
        switch_page_view_setup: Sets up the page view.
        switch_page_agenda_view_setup: Sets up the agenda view.
        setup_models: Sets up the models.
        restore_state: Restores the state of the application.
        app_operations: Performs application operations.
        commits_setup: Sets up commit operations.
        delete_actions: Sets up delete actions.
        sort_tables_by_date_desc: Sorts tables by date in descending order.
        agendas_navigation: Sets up agenda navigation.
        using_actions_checks_buttons: Sets up actions, checks, and buttons.
        setup_formatting_actions: Sets up formatting actions.
        open_to_date: Opens the application to a specific date.
        highlight_current_date: Highlights the current date.
        restore_visibility_state: Restores the visibility state.
        auto_date_time_widgets: Sets up auto date and time widgets.
        init_basics_tracker: Initializes the basics tracker.
        init_hydration_tracker: Initializes the hydration tracker.
        slider_set_spinbox: Sets up the slider and spinbox.
        init_exercise_tracker: Initializes the exercise tracker.
        init_lily_walk_commit: Initializes the Lily walk commit.
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initializes the main application window and its components.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            sat_model (None): Model for Saturday data.
            fri_model (None): Model for Friday data.
            wed_model (None): Model for Wednesday data.
            thurs_model (None): Model for Thursday data.
            mon_model (None): Model for Monday data.
            tues_model (None): Model for Tuesday data.
            sun_model (None): Model for Sunday data.
            date_widgets (None): Widgets for date selection.
            date_highlighter (None): Highlighter for dates.
            day_buttons (None): Buttons for day selection.
            mmdmr_model (None): Model for MMDMR data.
            cspr_model (None): Model for CSPR data.
            wefe_model (None): Model for WEFE data.
            context_menu (None): Context menu for the application.
            yoga_model (None): Model for yoga data.
            tooth_model (None): Model for tooth brushing data.
            shower_model (None): Model for shower data.
            hydration_model (None): Model for hydration data.
            diet_model (None): Model for diet data.
            lily_walk_note_model (None): Model for Lily's walk notes.
            lily_notes_model (None): Model for Lily's notes.
            time_in_room_model (None): Model for time spent in room.
            lily_walk_model (None): Model for Lily's walk data.
            lily_mood_model (None): Model for Lily's mood data.
            lily_diet_model (None): Model for Lily's diet data.
            btn_times (None): Button times.
            sleep_quality_model (None): Model for sleep quality data.
            woke_up_like_model (None): Model for "woke up like" data.
            sleep_model (None): Model for sleep data.
            total_hours_slept_model (None): Model for total hours slept data.
            total_hrs_slept (None): Total hours slept.
            basics_model (None): Model for basic data.
            settings (QSettings): Settings for the window/frame visibility.
            journal_settings_manager (SettingsManagerJournal): Manager for journal settings.
            settings_manager_lilys_widgets (SettingsManagerLilysWidgets): Manager for Lily's widget settings.
            ui (Ui_MainWindow): UI setup for the main window.
            window_controller (WindowController): Controller for window operations.
            db_manager (DataManager): Manager for database operations.
            text_formatter_bold (BoldTextFormatter): Formatter for bold text.
            text_formatter_color (ColorTextFormatter): Formatter for colored text.
            text_formatter_decrease_font_size (DecreaseFontSizeFormatter): Formatter for decreasing font size.
            text_formatter_highlight (HighlightColorFormatter): Formatter for highlighting text.
            text_formatter_increase_font (IncreaseFontSizeFormatter): Formatter for increasing font size.
            text_formatter_italic (ItalicTextFormatter): Formatter for italic text.
            text_formatter_strikethrough (StrikeTextFormatter): Formatter for strikethrough text.
            text_formatter_subscript (SubScriptTextFormatter): Formatter for subscript text.
            text_formatter_superscript (SuperScriptTextFormatter): Formatter for superscript text.
            text_formatter_underline (UnderlineTextFormatter): Formatter for underlined text.
            TextFormatCenter (CenterAlignFormatter): Formatter for center alignment.
            TextFormatRightAlign (RightAlignFormatter): Formatter for right alignment.
            TextFormatAlignLeft (LeftAlignFormatter): Formatter for left alignment.
            TextFormatJustify (JustifyAlignFormatter): Formatter for justified alignment.
            text_edit_saver (TextEditSaver): Saver for text edits.

        Methods:
            switch_page_view_setup: Sets up the page view.
            switch_page_agenda_view_setup: Sets up the agenda view.
            setup_models: Initializes the models.
            restore_state: Restores the previous state.
            app_operations: Performs application operations.
            commits_setup: Sets up commit actions.
            delete_actions: Sets up delete actions.
            sort_tables_by_date_desc: Sorts tables by date in descending order.
            agendas_navigation: Sets up agenda navigation.
            using_actions_checks_buttons: Sets up action checks for buttons.
            setup_formatting_actions: Sets up formatting actions.
            open_to_date: Opens the application to a specific date.
            highlight_current_date: Highlights the current date.
            restore_visibility_state: Restores the visibility state.
            auto_date_time_widgets: Sets up auto date and time widgets.
            init_basics_tracker: Initializes the basics tracker.
            init_hydration_tracker: Initializes the hydration tracker.
            slider_set_spinbox: Sets up the slider and spinbox.
            init_exercise_tracker: Initializes the exercise tracker.
            init_lily_walk_commit: Initializes the Lily walk commit.
            init_diet_tracker: Initializes the diet tracker.
        """       
        super().__init__(*args, **kwargs)
        self.sat_model = None
        self.fri_model = None
        self.wed_model = None
        self.thurs_model = None
        self.mon_model = None
        self.tues_model = None
        self.sun_model = None
        self.date_widgets = None
        self.date_highlighter = None
        self.day_buttons = None
        self.mmdmr_model = None
        self.cspr_model = None
        self.wefe_model = None
        self.context_menu = None
        self.yoga_model = None
        self.tooth_model = None
        self.shower_model = None
        self.hydration_model = None
        self.diet_model = None
        self.lily_walk_note_model = None
        self.lily_notes_model = None
        self.time_in_room_model = None
        self.lily_walk_model = None
        self.lily_mood_model = None
        self.lily_diet_model = None
        self.btn_times = None
        self.sleep_quality_model = None
        self.woke_up_like_model = None
        self.sleep_model = None
        self.total_hours_slept_model = None
        self.total_hrs_slept = None
        self.basics_model = None
        # Settings for the Window//Frame Visibility
        self.settings = QSettings(tkc.ORGANIZATION_NAME, tkc.APPLICATION_NAME)
        # Settings for sun_date, sun_note_one || mon || tues || wed || thurs || fri || sat
        self.journal_settings_manager = SettingsManagerJournal()
        # LILYS time_in_room_slider || mood || energy || activity level sliders
        self.settings_manager_lilys_widgets = SettingsManagerLilysWidgets()
        # Formatting general
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.window_controller = WindowController()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.db_manager = DataManager()
        self.text_formatter_bold = BoldTextFormatter()
        self.text_formatter_color = ColorTextFormatter()
        self.text_formatter_decrease_font_size = DecreaseFontSizeFormatter()
        self.text_formatter_highlight = HighlightColorFormatter()
        self.text_formatter_increase_font = IncreaseFontSizeFormatter()
        self.text_formatter_italic = ItalicTextFormatter()
        self.text_formatter_strikethrough = StrikeTextFormatter()
        self.text_formatter_subscript = SubScriptTextFormatter()
        self.text_formatter_superscript = SuperScriptTextFormatter()
        self.text_formatter_underline = UnderlineTextFormatter()
        # setup alignment formatters
        self.TextFormatCenter = CenterAlignFormatter()
        self.TextFormatRightAlign = RightAlignFormatter()
        self.TextFormatAlignLeft = LeftAlignFormatter()
        self.TextFormatJustify = JustifyAlignFormatter()
        # How we know what Journal to save :D
        self.text_edit_saver = TextEditSaver()
        # setup UI
        self.restore_state()
        self.restore_visibility_state()
        self.setup_models()
        self.switch_page_agenda_view_setup()
        self.switch_page_view_setup()
        self.app_operations()
        self.commits_setup()
        self.delete_actions()
        self.sort_tables_by_date_desc()
        self.agendas_navigation()
        self.using_actions_checks_buttons()
        self.setup_formatting_actions()
        self.open_to_date()
        self.highlight_current_date()
        self.auto_date_time_widgets()
        self.slider_set_spinbox()
    
    def sort_tables_by_date_desc(self):
        """
        Sorts multiple table views by date in descending order.

        This method iterates over a predefined list of table views and sorts each one
        by the date column in descending order. The date column index is specified
        within the method and should be adjusted to match the correct column index
        for the date in your tables.

        Attributes:
            table_views (list): A list of table view objects to be sorted.
            date_column_index (int): The index of the date column to sort by.

        Note:
            Ensure that the `Qt` module is imported and available in the scope where
            this method is used.
        """

        table_views = [self.wefe_table, self.cspr_table, self.mmdmr_table,
                       self.sleep_table, self.total_hours_slept_table,
                       self.woke_up_like_table, self.sleep_quality_table, self.shower_table,
                       self.tooth_table, self.yoga_table, self.diet_table,
                       self.hydration_table, self.lily_diet_table, self.lily_mood_table,
                       self.lily_walk_table, self.time_in_room_table, self.lily_notes_table,
                       self.exercise_intensity_table,
                       self.exercise_effort_table,
                       self.exercise_length_table,
                       self.exercise_type_table, self.lily_walk_note_table,
                       self.lily_walk_behavior_table, self.lily_walk_gait_table,]
        
        # Column index for the date column
        date_column_index = 1  # Adjust this to the correct column index for your date column
        for table_view in table_views:
            table_view.setSortingEnabled(True)
            table_view.sortByColumn(date_column_index, Qt.SortOrder.DescendingOrder)
    
    def commits_setup(self):
        """
        Sets up various data points by calling multiple methods to add specific types of data.

        This method initializes the following data:
        - CSPR data
        - Diet data
        - Lily's diet data
        - Lily's mood data
        - Lily's notes data
        - Lily's time in room data
        - MMDMR data
        - Sleep data
        - Sleep quality data
        - WEFE data
        - Woke up like data
        - Total hours data
        - Sunday data
        - Monday data
        - Tuesday data
        - Wednesday data
        - Thursday data
        - Friday data
        - Saturday data

        Note: Some data points related to Lily's walk are currently commented out.
        """
        
        # self.add_diet_data()
        self.add_lily_diet_data()
        self.add_lily_mood_data()
        self.add_lily_notes_data()
        self.add_lily_time_in_room_data()
        self.init_mmdmr_tracker()
        self.init_cspr_tracker()
        self.init_wefe_tracker()
        self.add_sunday_data()
        self.add_monday_data()
        self.add_tuesday_data()
        self.add_wednesday_data()
        self.add_thursday_data()
        self.add_friday_data()
        self.add_saturday_data()
        self.init_sleep_commit()
        self.init_exercise_tracker()
        self.init_lily_walk_commit()
        self.init_diet_tracker()
        self.init_basics_tracker()
        self.init_hydration_tracker()
    
    ##########################################################################################
    # APP-OPERATIONS setup
    ##########################################################################################
    def app_operations(self):
        """
        Performs the necessary operations for setting up the application.

        This method connects the triggered signals of various actions to their respective slots,
        connects the currentChanged signal of the agendaStack to the on_page_changed slot, and
        sets up other UI-related functionalities.

        Actions connected:
        - actionInjectDate: Connects to the inject_date method.
        - actionInjectTime: Connects to the inject_time method.
        - actionSave: Connects to the save_current_text method.
        - actionPrint: Connects to the print_current_textedit method.
        - actionInjectTable: Connects to the inject_table method.
        - actionToggleWeekBar: Connects to a lambda function that toggles the visibility of the week_frame.
        - actionExit: Connects to the close_app method.

        AgendaStack:
        - Connects the currentChanged signal to the on_page_changed slot.

        Raises:
            Exception: If an error occurs while setting up the app_operations.
        """
        try:
            self.actionInjectDate.triggered.connect(self.inject_date)
            self.actionInjectTime.triggered.connect(self.inject_time)
            self.actionSave.triggered.connect(self.save_current_text)
            self.actionPrint.triggered.connect(self.print_current_textedit)
            self.agendaStack.currentChanged.connect(self.on_page_changed)
            self.actionInjectTable.triggered.connect(self.inject_table)
            self.actionToggleWeekBar.triggered.connect(lambda: toggle_views(self.week_frame))
            
            self.actionExit.triggered.connect(self.close_app)
        except Exception as e:
            logger.error(f"Error in app_operation block : {e}", exc_info=True)
    
    def on_page_changed(self,
                        index):
        """
        Callback method triggered when the page is changed in the UI.

        Args:
            index (int): The index of the new page.
        """
        try:
            self.settings.setValue("lastPageIndex", index)
        except Exception as e:
            logger.error(f"An error occurred in on_page_changed {e}", exc_info=True)
    
    def close_app(self):
        """
        Closes the application.
        """
        self.close()
    
    def save_visibility_state(self,
                              key,
                              state):
        """
        Save the visibility state of a widget.

        Parameters:
            key (str): The key to identify the widget.
            state (bool): The visibility state of the widget.

        Returns:
            None
        """
        settings = QSettings(tkc.ORGANIZATION_NAME, tkc.APPLICATION_NAME)
        settings.setValue(key, state)
    
    def restore_visibility_state(self):
        """
        Restores the visibility state of various UI elements based on the saved settings.

        The visibility state of the following UI elements will be restored:
        - week_frame

        The visibility state is retrieved from the saved settings using QSettings.

        Returns:
            None
        """
        
        self.week_frame.setVisible(
            self.settings.value(
                'week_frame',
                False,
                type=bool
            )
        )
    
    #########################################################################
    # highlight_current_date DATE MAPPING METHOD
    #########################################################################
    def highlight_current_date(self) -> None:
        """
        Highlights the current date in the date widgets.

        This method initializes a dictionary of date widgets and creates a DateHighlighter object
        to highlight the current date in the UI.

        Raises:
            Exception: If an error occurs while highlighting the current date.

        Returns:
            None
        """
        try:
            self.date_widgets = {
                "sun_date": self.sun_date,
                "mon_date": self.mon_date,
                "tues_date": self.tues_date,
                "wed_date": self.wed_date,
                "thurs_date": self.thurs_date,
                "fri_date": self.fri_date,
                "sat_date": self.sat_date,
            }
            self.date_highlighter = DateHighlighter(self.date_widgets)
        except Exception as e:
            logger.exception(f"Error occurred when using highlight_current_date {e}",
                             exc_info=True)
    
    ##########################################################################
    # FORMATTER ACTIONS
    ##########################################################################
    def setup_formatting_actions(self) -> None:
        """
        Sets up the formatting and alignment actions for text editing.

        This method connects various text formatting and alignment actions to their respective handlers and methods.
        It uses helper functions to establish these connections and logs the process.

        Actions include:
        - Text formatting (bold, italic, highlight, color, underline, strikethrough, font size increase/decrease, subscript, superscript)
        - Text alignment (center, right, left, justify)

        If an AttributeError occurs during the setup, it is logged as an error.

        Raises:
            AttributeError: If there is an issue with accessing attributes during the setup.
        """
        try:
            logger.debug("Setting up formatting actions...")
            
            # Helper function to connect actions for text formatting
            def connect_text_format_action(action_,
                                           handler_,
                                           method_):
                """
                Connects a text format action to a handler_ method.

                This function connects the `triggered` signal of the given `action` to a lambda function
                that calls the `apply_current_text_format` method of the `handler_` with the specified `method`.

                Args:
                    action_ (QAction): The action whose `triggered` signal is to be connected.
                    handler_ (object): The object that contains the `apply_current_text_format` method.
                    method_ (str): The method name or identifier to be passed to
                    `apply_current_text_format`.

                Returns:
                    None
                """
                action_.triggered.connect(lambda: handler_.apply_current_text_format(method_))
            
            # Helper function to connect actions for text alignment
            def connect_text_alignment_action(action_,
                                              handler_,
                                              method_):
                """
                Connects a text alignment action to a handler_ method.

                Args:
                    action_ (QAction): The action that triggers the text alignment.
                    handler_ (object): The handler_ object that contains the method to apply the text alignment.
                    method_ (str): The method name to be called on the handler_ to apply the text alignment.

                Returns:
                    None
                """
                action_.triggered.connect(lambda: handler_.apply_current_text_alignment(method_))
            
            # Mapping of actions to their respective handlers and methods
            text_format_actions = [
                (
                    self.actionTextBold,
                    self.text_formatter_bold,
                    self.text_formatter_bold.make_bold
                ),
                (
                    self.actionTextItalic,
                    self.text_formatter_italic,
                    self.text_formatter_italic.make_italic
                ),
                (
                    self.actionTextHighlight,
                    self.text_formatter_highlight,
                    self.text_formatter_highlight.format_text
                ),
                (
                    self.actionTextColor,
                    self.text_formatter_color,
                    self.text_formatter_color.font_color
                ),
                (
                    self.actionTextUnderline,
                    self.text_formatter_underline,
                    self.text_formatter_underline.make_underline
                ),
                (
                    self.actionTextStrike,
                    self.text_formatter_strikethrough,
                    self.text_formatter_strikethrough.make_strikethrough
                ),
                (
                    self.actionTextIncrease,
                    self.text_formatter_increase_font,
                    self.text_formatter_increase_font.increase_font_size
                ),
                (
                    self.actionTextDecrease,
                    self.text_formatter_decrease_font_size,
                    self.text_formatter_decrease_font_size.decrease_font_size
                ),
                (
                    self.actionTextSubscript,
                    self.text_formatter_subscript,
                    self.text_formatter_subscript.make_subscript
                ),
                (
                    self.actionTextSuperScript,
                    self.text_formatter_superscript,
                    self.text_formatter_superscript.make_superscript
                )
            ]
            
            # Apply text formatting connections
            for action, handler, method in text_format_actions:
                connect_text_format_action(action, handler, method)
            
            # Mapping of alignment actions
            alignment_actions = [
                (
                    self.actionTextAlignCenter,
                    self.TextFormatCenter,
                    self.TextFormatCenter.center_text
                ),
                (
                    self.actionTextAlignRight,
                    self.TextFormatRightAlign,
                    self.TextFormatRightAlign.right_align_text
                ),
                (
                    self.actionTextAlignLeft,
                    self.TextFormatAlignLeft,
                    self.TextFormatAlignLeft.left_align_text
                ),
                (
                    self.actionTextAlignJustify,
                    self.TextFormatJustify,
                    self.TextFormatJustify.justify_text
                )
            ]
            
            # Apply text alignment connections
            for action, handler, method in alignment_actions:
                connect_text_alignment_action(action, handler, method)
            
            logger.debug("Formatting actions set up successfully.")
        except AttributeError as e:
            logger.error(f"Attribute Error format actions {e}", exc_info=True)
    
    #########################################################################
    # Agenda_stack will open to current day in the Journal Mod
    #########################################################################
    def open_to_date(self):
        """
        Opens the agenda module to the current date.

        This method sets the current day in the agenda and agenda data stacks, maps the buttons
        to the current day,
        and checks the corresponding day buttons.

        Raises:
            AttributeError: If an attribute error occurs when setting up actions.

        """
        try:
            current_day = datetime.datetime.today().weekday()
            # Adjust the value to match your setup
            if current_day == 6:  # if today is Sunday
                current_day = 0
            else:
                current_day += 1  # shift other days by +1
            self.agenda_journal_stack.setCurrentIndex(current_day)
            self.agenda_data_stack.setCurrentIndex(current_day)
            self.map_buttons_to_days()
            self.day_buttons[current_day].setChecked(True)
        
        except AttributeError as e:
            logger.exception(f"Error occurred when setting up actions:{e}", exc_info=True)
    
    #########################################################################
    # map_buttons_to_days
    #########################################################################
    def map_buttons_to_days(self) -> None:
        """
        Maps buttons to days.

        This method maps the day buttons to their corresponding days of the week.
        It creates a dictionary where the keys represent the day index (0-6) and the values
        represent the corresponding button object.

        Returns:
            None
        """
        try:
            self.day_buttons = {
                0: self.sun_journal_nav_btn, 1: self.mon_journal_nav_btn,
                2: self.tues_journal_nav_btn, 3: self.wed_journal_nav_btn,
                4: self.thurs_journal_nav_btn, 5: self.fri_journal_nav_btn,
                6: self.sat_journal_nav_btn,
            }
        
        except Exception as e:
            logger.error(f"An error in the map_buttons_to_days check it out! {e}",
                         exc_info=True)
    
    #########################################################################
    # Save CURRENT text setup to save[export] the current working Textedit
    #########################################################################
    def save_current_text(self) -> None:
        """
        Save the current text by updating the current text edit and then
        saving the current text edit.

        Raises:
            Exception: If there is an error while saving the current text.
        """
        try:
            self.update_current_text_edit()
            self.text_edit_saver.save_current_text()
        except Exception as e:
            logger.error(f"Error saving current text: {e}", exc_info=True)
    
    def inject_table(self):
        """
        Opens a dialog to input table dimensions and inserts an HTML table into the focused QTextEdit widget.

        Raises:
            Exception: If an error occurs during the table injection process.
        """
        try:
            dialog = TableInputDialog(self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                rows, columns = map(int, dialog.get_dimensions())
                html = self.generate_table_html(rows, columns)
                focused_widget = QApplication.instance().focusWidget()
                if focused_widget and isinstance(focused_widget, QTextEdit):
                    text_edit = focused_widget
                    cursor = text_edit.textCursor()
                    cursor.insertHtml(html)
        except Exception as e:
            logger.error(f"{e}", exc_info=True)
    
    def inject_time(self):
        """
        Injects the current time into the focused QTextEdit widget.

        This method retrieves the currently focused widget and checks if it is an instance of QTextEdit.
        If it is, the current time is get and inserted into the QTextEdit widget using HTML formatting.

        Raises:
            Exception: If an error occurs during the injection process.

        """
        try:
            focused_widget = QApplication.instance().focusWidget()
            if isinstance(focused_widget, QTextEdit):
                text_edit = focused_widget
                current_time = QDateTime.currentDateTime().toString("h:mm AP")
                cursor = text_edit.textCursor()
                cursor.insertHtml(f"""
                                <strong><sup>it.is</sup></strong>{current_time}
                                """)
        except Exception as e:
            logger.error(f"{e}", exc_info=True)
    
    def inject_date(self):
        """
        Injects text into the currently focused QTextEdit widget.

        This method retrieves the currently focused widget using QApplication.instance().focusWidget().
        If the focused widget is an instance of QTextEdit, it retrieves the text edit object and inserts
        the predefined text from the tkc.COURSEWORK variable at the current cursor position.

        Raises:
            Exception: If any error occurs during the injection process.

        """
        try:
            focused_widget = QApplication.instance().focusWidget()
            if isinstance(focused_widget, QTextEdit):
                text_edit = focused_widget
                current_date = QDate.currentDate().toString("MMM dd, yyyy")
                cursor = text_edit.textCursor()
                cursor.insertHtml(f"""
                                    <h3 style="font:12pt 'Helvetica-Neue'; letter-spacing:2px;">{current_date}</h3>
                                    """)
        except Exception as e:
            logger.error(f"{e}", exc_info=True)
    
    def generate_table_html(self,
                            rows,
                            columns):
        """
        Generate an HTML table with the specified amount rows and columns.

        Args:
            rows (int): The several rows in the table.
            columns (int): The number of columns in the table.

        Returns:
            str: The HTML code for the generated table.

        Raises:
            Exception: If an error occurs while generating the table.

        """
        try:
            table_html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-REFACTOR NOTES 8-30">
            <title>Day at a Glance</title>
            <style>
                td {
                    border: 1px solid rgba(111,111,111, 0.34);
                    text-align: left;
                    padding:4px;
                }
            </style>
            </head>
            <body>
            """
            # table_html += f'Table of {rows} rows x {columns} columns'
            table_html += '<table>'
            for _ in range(rows):
                table_html += '<tr>'
                for _ in range(columns):
                    table_html += '<td></td>'
                table_html += '</tr>'
            table_html += '</table>'
            return table_html
        except Exception as e:
            logger.error(f"{e}")
    
    #########################################################################
    # Print support
    #########################################################################
    def update_current_text_edit(self):
        """
        Updates the current text edit.

        This method is responsible for updating the current text edit widget in the main window.
        It retrieves the currently focused widget using QApplication.instance().focusWidget() and
        checks if it is an instance of QTextEdit.
        If it is, it sets the current text edit using self.text_edit_saver.set_current_text_edit(
        focused_widget).
        Finally, it logs the update operation with the widget name.

        Raises:
            Exception: If there is an error updating the current text edit.
        """
        try:
            focused_widget = QApplication.instance().focusWidget()
            
            if isinstance(focused_widget, QTextEdit):
                self.text_edit_saver.set_current_text_edit(focused_widget)
                widget_name = (focused_widget.objectName() or "Unnamed QTextEdit")
                
                logger.debug(f"Current text edit updated for {widget_name}")
        except Exception as e:
            logger.error(f"Error updating current text edit: {e}", exc_info=True)
    
    #########################################################################
    # print_current_textedit support
    #########################################################################
    @staticmethod
    def print_current_textedit():
        """
        A method to print the content of the current QTextEdit widget,
        including logging the name of the QTextEdit being printed.

        This method retrieves the currently focused widget and checks if it is
        an instance of QTextEdit. If it is, it retrieves the widget's object name
        or uses a placeholder if the object name is not set. It then logs a debug
        message indicating that the current text edit is being printed for the
        specific widget.

        It creates a QPrintDialog to allow the user to select a printer and
        configure print settings. If the dialog is accepted, it prints the content
        of the focused QTextEdit widget using the selected printer. Finally, it
        logs a debug message indicating that the current text edit has been
        successfully printed.

        If any exception occurs during the process, an error message is logged
        along with the exception details.

        Raises:
            Exception: If an error occurs while printing the current text edit.
        """
        try:
            focused_widget = QApplication.instance().focusWidget()
            if isinstance(focused_widget, QTextEdit):
                # Attempt to retrieve the widget's object name, or use a
                # placeholder
                widget_name = (focused_widget.objectName() or "Unnamed QTextEdit")
                logger.debug(f"Printing current text edit for {widget_name}")
                
                dlg = QPrintDialog()
                if dlg.exec():
                    focused_widget.print(dlg.printer())
                    logger.debug(f"""Current text edit printed for
                                {widget_name}""")
        except Exception as e:
            logger.error(f"Error printing current text edit: {e}", exc_info=True)
    
    #########################################################################
    # Actions Check Buttons
    #########################################################################
    def using_actions_checks_buttons(self):
        """
        Connects each action to its corresponding button.

        This method creates a dictionary mapping action triggers to their corresponding buttons.
        It then loops through the dictionary and connects each action to its button using the
        `triggered` signal. When an action is triggered, the corresponding button will be checked.

        Returns:
            None
        """
        try:
            # A dictionary mapping action triggers to their corresponding button.
            action_to_button = {
                self.actionViewJournalSun: self.sun_journal_nav_btn,
                self.actionViewJournalMon: self.mon_journal_nav_btn,
                self.actionViewJournalTues: self.tues_journal_nav_btn,
                self.actionViewJournalWed: self.wed_journal_nav_btn,
                self.actionViewJournalThurs: self.thurs_journal_nav_btn,
                self.actionViewJournalFri: self.fri_journal_nav_btn,
                self.actionViewJournalSat: self.sat_journal_nav_btn,
            }
            
            # Loop through the dictionary and connect each action to its button.
            for action, button in action_to_button.items():
                action.triggered.connect(lambda checked,
                                                b=button: b.setChecked(True))
        except Exception as e:
            logger.error(f"An error occurred when using actions checks buttons {e}",
                         exc_info=True)
    
    #############################################################################################
    # Agenda Journal Navigation
    #############################################################################################
    def agendas_navigation(self):
        """
        Sets up the agenda navigation for the journal.

        This method connects actions and buttons to stack page indices for the agenda journal.
        It also sets up the pain rate sliders and connects them to the update_pain_sliders
        method.

        Raises:
            Exception: If an error occurs during the setup process.
        """
        try:
            # Mapping actions and buttons to stack page indices for the agenda journal
            action_to_page = {
                self.actionViewJournalSun: 0,
                self.actionViewJournalMon: 1,
                self.actionViewJournalTues: 2,
                self.actionViewJournalWed: 3,
                self.actionViewJournalThurs: 4,
                self.actionViewJournalFri: 5,
                self.actionViewJournalSat: 6,
            }
            
            agenda_navigation_btn = {
                self.sun_journal_nav_btn: 0,
                self.mon_journal_nav_btn: 1,
                self.tues_journal_nav_btn: 2,
                self.wed_journal_nav_btn: 3,
                self.thurs_journal_nav_btn: 4,
                self.fri_journal_nav_btn: 5,
                self.sat_journal_nav_btn: 6,
            }
            
            action_to_data_page = {
                self.actionViewJournalSun: 0,
                self.actionViewJournalMon: 1,
                self.actionViewJournalTues: 2,
                self.actionViewJournalWed: 3,
                self.actionViewJournalThurs: 4,
                self.actionViewJournalFri: 5,
                self.actionViewJournalSat: 6
            }
            
            alpha_stack_navigation_actions = {
                self.action_input_view_agenda: 0,
                self.action_data_view_agenda: 1,
            }
            mainStackNavvy = {
                self.action_input_view_agenda: 0,
                self.actionBDSInput: 1,
                self.actionShowDietPage: 2,
                self.actionShowBasicsPage: 3,
                self.actionLilysPage: 4,
                self.actionMentalModsView: 5,
                self.actionViewDataCollection: 6,
            }
            
            try:
                # Main Stack Navigation
                for action, page in alpha_stack_navigation_actions.items():
                    action.triggered.connect(
                        lambda _,
                               p=page: change_alpha_stack_page(self.agendaStack, p))
            except Exception as e:
                logger.error(f"An error occurred when setting up stack navigation {e}",
                             exc_info=True)
            
            # ACTIONS to change pages in the agenda module
            for action, page in action_to_page.items():
                action.triggered.connect(
                    lambda _,
                           p=page: change_agenda_stack_page(self.agenda_journal_stack, p))
            
            # BUTTONS for Agenda's SideBar
            for button, page in agenda_navigation_btn.items():
                button.clicked.connect(
                    lambda _,
                           p=page: change_agenda_stack_page(self.agenda_journal_stack, p))
            
            for button, page in agenda_navigation_btn.items():
                button.clicked.connect(
                    lambda _,
                           p=page: change_agenda_stack_page(self.agenda_data_stack, p)
                )
            
            # ACTION for DATA page
            for action, page in action_to_data_page.items():
                action.triggered.connect(
                    lambda _,
                           p=page: change_agenda_stack_page(self.agenda_data_stack, p))
            try:
                # Mapping actions and buttons to stack page indices for the agenda journal
                
                # Main Stack Navigation
                for action, page in mainStackNavvy.items():
                    action.triggered.connect(
                        lambda _,
                               p=page: change_mainStack(self.mainStack, p))
            
            except Exception as e:
                logger.error(f"An error has occurred: {e}", exc_info=True)
        
        except Exception as e:
            logger.error(f"An error has occurred: Navigation \n : {e}", exc_info=True)
    
    #########################################################################
    # UPDATE TIME support
    #########################################################################
    @staticmethod
    def update_time(state,
                    time_label):
        """
        Update the time displayed on the time_label widget based on the given state.

        Parameters:
        - state (int): The state of the time_label widget. If state is 2, the time_label will be
        updated.
        - time_label (QLabel): The QLabel widget to update with the current time.

        Returns:
        None

        Raises:
        None
        """
        try:
            if state == 2:  # checked state
                current_time = QTime.currentTime()
                time_label.setTime(current_time)
        except Exception as e:
            logger.error(f"Error updating time. {e}", exc_info=True)
    
    # ////////////////////////////////////////////////////////////////////////////////////////
    # SLIDER UPDATES SPINBOX/VICE VERSA SETUP
    # ////////////////////////////////////////////////////////////////////////////////////////
    def slider_set_spinbox(self):
        """
        Connects sliders to their corresponding spinboxes.

        This method establishes a connection between sliders and spinboxes
        by mapping each slider to its corresponding spinbox. It then calls
        the `connect_slider_spinbox` function to establish the connection.

        Returns:
            None
        """
        connect_slider_to_spinbox = {
            self.lily_time_in_room_slider: self.lily_time_in_room,
            self.lily_mood_slider: self.lily_mood,
            self.lily_mood_activity_slider: self.lily_activity,
            self.lily_energy_slider: self.lily_energy,
        }
        
        for slider, spinbox in connect_slider_to_spinbox.items():
            connect_slider_spinbox(slider, spinbox)
    
    # ##########################################################################################
    # ##########################################################################################
    #           SWITCH_PAGE i.e., custom setFixedSize per page in mainStack/agendaStack/etc.
    # ##########################################################################################
    # ##########################################################################################
    def switch_page2(self,
                     page_widget,
                     width,
                     height):
        """
        Switches the current page in the agenda stack to the specified widget and sets the window size.

        Args:
            page_widget (QWidget): The widget to switch to.
            width (int): The width to set for the window.
            height (int): The height to set for the window.

        Raises:
            Exception: If an error occurs while switching the page or setting the window size.
        """
        try:
            self.agendaStack.setCurrentWidget(page_widget)
            self.setFixedSize(width, height)
        except Exception as e:
            logger.error(f"{e}", exc_info=True)
    
    def switch_to_agenda_page(self):
        """
        Switches the current view to the agenda input page.

        This method attempts to switch the current page to the agenda input page
        with specified width and height. If an exception occurs during the switch,
        it logs the error with traceback information.

        Raises:
            Exception: If an error occurs during the page switch.
        """
        try:
            self.switch_page2(
                self.agendaInputPage,
                width=400,
                height=400
            )
        except Exception as e:
            logger.error(f"{e}", exc_info=True)
    
    def switch_agenda_size_large(self):
        """
        Switches the agenda input page to a large size.

        This method attempts to switch the current page to the agenda input page
        with specified width and height dimensions. If an exception occurs during
        this process, it logs the error with detailed exception information.

        Raises:
            Exception: If an error occurs while switching the page.
        """
        try:
            self.switch_page2(
                self.agendaInputPage,
                width=540,
                height=680
            )
        except Exception as e:
            logger.error(f"{e}", exc_info=True)
    
    def switch_agenda_size_medium(self):
        """
        Switches the agenda input page to medium size.

        This method changes the dimensions of the agenda input page to a width of 480 pixels and a height of 360 pixels.

        Returns:
            None
        """
        self.switch_page2(
            self.agendaInputPage,
            width=480,
            height=360
        )
    
    def switch_agenda_size_small(self):
        """
        Switches the agenda input page to a small size.

        This method changes the dimensions of the agenda input page to a width of 360 pixels and a height of 480 pixels.

        Returns:
            None
        """
        self.switch_page2(
            self.agendaInputPage,
            width=360,
            height=480
        )
    
    def switch_to_agenda_data_page(self):
        """
        Switches the current view to the agenda data page.

        This method changes the current page to the agendaJournsDataViewPage
        with specified width and height dimensions.

        Returns:
            None
        """
        self.switch_page2(
            self.agendaJournsDataViewPage,
            width=400,
            height=600
        )
    
    # SWITCH PAGE basic
    def switch_page(self,
                    page_widget,
                    width,
                    height):
        """
        Switches the current page in the main stack and sets the fixed size of the window.

        Args:
            page_widget (QWidget): The widget to switch to.
            width (int): The width to set for the window.
            height (int): The height to set for the window.

        Raises:
            Exception: If an error occurs while switching the page or setting the window size.
        """
        try:
            self.mainStack.setCurrentWidget(page_widget)
            self.setFixedSize(width, height)
        except Exception as e:
            logger.error(f"{e}", exc_info=True)
    
    def switch_bds_page(self):
        """
        Switches the current view to the BDS page with specified dimensions.

        This method changes the current page to the BDS (presumably a specific
        page in the application) and sets its width and height to 290 and 155
        respectively.

        Returns:
            None
        """
        self.switch_page(
            self.bds_page,
            width=300,
            height=120
        )
    
    def switch_diet_page(self):
        """
        Switches the current view to the diet page.

        This method changes the displayed page to the diet page with specified
        dimensions for width and height.

        Returns:
            None
        """
        self.switch_page(
            self.dietPage,
            width=290,
            height=165
        )
    
    def switch_ste_page(self):
        """
        Switches the current page to the STEPage with specified dimensions.

        This method changes the current page to the STEPage and sets the width
        and height of the new page to 290 and 100 respectively.
        """
        self.switch_page(
            self.STEPage,
            width=290,
            height=100
        )
    
    def switch_lilys_mod(self):
        """
        Switches the current page to Lily's mod page with specified dimensions.

        This method changes the current page to the Lily's mod page and sets the
        window dimensions to a width of 290 and a height of 320.
        """
        self.switch_page(
            self.lilys_mod,
            width=290,
            height=250
        )
    
    def switch_mental(self):
        """
        Switches the current view to the mentalPage.

        This method changes the current page to the mentalPage with specified
        width and height dimensions.

        Returns:
            None
        """
        self.switch_page(
            self.mentalPage,
            width=240,
            height=115
        )
    
    def switch_data_page(self):
        """
        Switches the current view to the data stack page.

        This method changes the current page to the data stack page with a specified
        width and height.

        Parameters:
        None

        Returns:
        None
        """
        self.switch_page(
            self.dataStackPage,
            width=980,
            height=640,
        )
    
    def switch_page_agenda_view_setup(self):
        """
        Sets up the agenda view switch actions by connecting UI actions to their respective handler methods.

        This method creates a dictionary mapping UI actions to their corresponding handler methods and
        connects each action's `triggered` signal to the appropriate handler. If an exception occurs
        during this process, it logs the error with traceback information.

        Raises:
            Exception: If an error occurs while setting up the agenda view switch actions.
        """
        try:
            agenda_switch = {
                self.action_input_view_agenda: self.switch_to_agenda_page,
                self.action_data_view_agenda: self.switch_to_agenda_data_page,
                self.actionAgendaLarge: self.switch_agenda_size_large,
                self.actionAgendaMedium: self.switch_agenda_size_medium,
                self.actionAgendaSmall: self.switch_agenda_size_small
            }
            
            for action, switchpage in agenda_switch.items():
                action.triggered.connect(switchpage)
        except Exception as e:
            logger.error(f"{e}", exc_info=True)
    
    def switch_page_view_setup(self):
        """
        Sets up the page view switching mechanism for the application.

        This method maps various actions to their corresponding page switch functions
        and connects the action's triggered signal to the appropriate function. If an
        exception occurs during this process, it logs the error.

        Actions and their corresponding switch functions:
        - self.actionBDSInput: self.switch_bds_page
        - self.actionLilysPage: self.switch_lilys_mod
        - self.actionShowDietPage: self.switch_diet_page
        - self.actionShowBasicsPage: self.switch_ste_page
        - self.actionViewDataCollection: self.switch_data_page
        - self.actionMentalModsView: self.switch_mental

        Exceptions:
            Logs any exceptions that occur during the setup process.
        """
        try:
            view_switch = {
                self.actionBDSInput: self.switch_bds_page,
                self.actionLilysPage: self.switch_lilys_mod,
                self.actionShowDietPage: self.switch_diet_page,
                self.actionShowBasicsPage: self.switch_ste_page,
                self.actionViewDataCollection: self.switch_data_page,
                self.actionMentalModsView: self.switch_mental,
            }
            
            for action, switchview in view_switch.items():
                action.triggered.connect(switchview)
        
        except Exception as e:
            logger.error(f"{e}")
    
    # ##########################################################################################
    #    AUTO DATE TIMEs
    # ##########################################################################################
    def auto_date_time_widgets(self):
        """
        Automatically sets the current date and time for specified widgets.

        This method updates the date and time for a predefined list of date and
        time widgets to the current date and time. It handles any exceptions
        that may occur during the process and logs the error.

        Widgets updated:
        - Date widgets: mmdmr_date, wefe_date, cspr_date, diet_date, sleep_date,
          basics_date, lily_date
        - Time widgets: mmdmr_time, wefe_time, cspr_time, diet_time, sleep_time,
          basics_time, lily_time

        Exceptions:
        - Logs any exceptions that occur during the update process.
        """
        try:
            widget_date_edit = [
                self.mmdmr_date,
                self.wefe_date,
                self.cspr_date,
                self.diet_date,
                self.sleep_date,
                self.basics_date,
                self.lily_date,
            ]
            
            widget_time_edit = [
                self.mmdmr_time,
                self.wefe_time,
                self.cspr_time,
                self.diet_time,
                self.sleep_time,
                self.basics_time,
                self.lily_time,
            ]
            
            for widget in widget_date_edit:
                widget.setDate(QDate.currentDate())
            
            for widget in widget_time_edit:
                widget.setTime(QTime.currentTime())
        except Exception as e:
            logger.error(f"{e}")
    
    def commits_set_times(self):
        """
        Sets the times for various buttons in the UI.

        The times are stored in a dictionary where the keys are the buttons and the values are the corresponding times.
        The buttons and times are connected using the `btn_times` dictionary.

        Example:
            self.btn_times = {
                self.shower_c: self.basics_time,
                self.add_exercise_data: self.basics_time,
                self.add_teethbrushing_data: self.basics_time,
            }

        The lineEdits are then connected to the centralized function `btn_times` using a for loop.

        Returns:
            None
        """
        self.btn_times = {
            self.shower_c: self.basics_time,
            self.add_exercise_data: self.basics_time,
            self.add_teethbrushing_data: self.basics_time,
        }
        
        # Connect lineEdits to the centralized function
        for app_btns, times_edit in self.btn_times.items():
            btn_times(app_btns, times_edit)
    
    # ##########################################################################################
    #           COMMITS COMMITS COMMITS COMMITS COMMITS COMMITS COMMITS COMMITS COMMITS
    # ##########################################################################################
    def add_sunday_data(self):
        """
        Adds Sunday data to the application.

        This method connects the 'triggered' signal of the actionSunday QAction to the
        agenda_data_sunday function. The function is called with the necessary arguments
        when the signal is emitted.

        Returns:
            None

        Raises:
            Logs an error if there is an exception while connecting the signal.
        """
        try:
            self.actionSunday.triggered.connect(lambda: agenda_data_sunday(self, {
                "sun_date": "sun_date", "sun_note_one": "sun_note_one", "model": "sun_model",
            },
                                                                           self.db_manager.insert_into_sunday_table))
        except Exception as e:
            logger.error(f"Unable to commit Sunday's Journ, sunday forfeits!{e}", exc_info=True)
    
    def add_monday_data(self):
        """
        Connects the Monday action trigger to the agenda_data_monday function.

        This method sets up a connection between the Monday action trigger and the
        agenda_data_monday function, passing in specific parameters and a database
        insertion method. If an exception occurs during this process, it logs an
        error message.

        Parameters:
        None

        Returns:
        None

        Raises:
        Exception: If there is an issue with committing Monday's data.
        """
        try:
            self.actionMonday.triggered.connect(lambda: agenda_data_monday(self, {
                "mon_date": "mon_date", "mon_note_one": "mon_note_one", "model": "mon_model",
            },
                                                                           self.db_manager.insert_into_monday_table, ))
        except Exception as e:
            logger.error(f"Unable to commit Monday's Journ, monday forfeits! {e}",
                         exc_info=True)
    
    def add_tuesday_data(self):
        """
        Adds Tuesday data to the agenda.

        This method connects the 'triggered' signal of the 'actionTuesday' action to a lambda function
        that calls 'agenda_data_tuesday' with the necessary parameters and inserts the data into the
        Tuesday table in the database.

        Parameters:
        None

        Raises:
        Exception: If an error occurs during the connection or data insertion process, it logs the error.
        """
        try:
            self.actionTuesday.triggered.connect(lambda: agenda_data_tuesday(self, {
                "tues_date": "tues_date", "tues_note_one": "tues_note_one",
                "model": "tues_model",
            }, self.db_manager.insert_into_tuesday_table))
        except Exception as e:
            logger.error(f"An Error has occurred {e}", exc_info=True)
    
    def add_wednesday_data(self):
        """
        Connects the Wednesday action trigger to the agenda_data_wednesday function.

        This method sets up a connection between the Wednesday action trigger and the
        agenda_data_wednesday function. When the Wednesday action is triggered, it
        passes a dictionary containing Wednesday-specific data to the function and
        calls the insert_into_wednesday_table method of the db_manager to insert the
        data into the Wednesday table.

        Raises:
            Exception: Logs an error message if an exception occurs during the connection setup.
        """
        try:
            self.actionWednesday.triggered.connect(lambda: agenda_data_wednesday(self, {
                "wed_date": "wed_date", "wed_note_one": "wed_note_one", "model": "wed_model",
            }, self.db_manager.insert_into_wednesday_table, ))
        except Exception as e:
            logger.error(f"An Error has occurred {e}", exc_info=True)
    
    def add_thursday_data(self):
        """
        Connects the Thursday action trigger to the agenda_data_thursday function.

        This method sets up a connection between the Thursday action trigger and the
        agenda_data_thursday function. When the Thursday action is triggered, it will
        call the agenda_data_thursday function with the specified parameters and
        insert the data into the Thursday table in the database.

        Raises:
            Exception: If an error occurs during the connection setup, it logs the error.
        """
        try:
            self.actionThursday.triggered.connect(lambda: agenda_data_thursday(self, {
                "thurs_date": "thurs_date", "thurs_note_one": "thurs_note_one",
                "model": "thurs_model",
            }, self.db_manager.insert_into_thursday_table, ))
        except Exception as e:
            logger.error(f"An Error has occurred {e}", exc_info=True)
    
    def add_friday_data(self):
        """
        Connects the 'actionFriday' trigger to the 'agenda_data_friday' function, which inserts data into the Friday table.

        This method sets up a connection between the 'actionFriday' trigger and a lambda function that calls
        'agenda_data_friday' with specific parameters. The lambda function passes a dictionary containing
        keys 'fri_date', 'fri_note_one', and 'model' to 'agenda_data_friday', along with the 'insert_into_friday_table'
        method from 'db_manager'.

        If an exception occurs during this process, it is logged as an error with the exception information.

        Raises:
            Exception: If an error occurs during the connection or execution of the lambda function.
        """
        try:
            self.actionFriday.triggered.connect(lambda: agenda_data_friday(self, {
                "fri_date": "fri_date", "fri_note_one": "fri_note_one", "model": "fri_model",
            }, self.db_manager.insert_into_friday_table, ))
        except Exception as e:
            logger.error(f"An Error has occurred {e}", exc_info=True)
    
    def add_saturday_data(self):
        """
        Connects the Saturday action trigger to the agenda_data_saturday function.

        This method sets up a connection between the Saturday action trigger and the
        agenda_data_saturday function. When the Saturday action is triggered, it
        passes specific data to the agenda_data_saturday function and calls the
        insert_into_saturday_table method of the db_manager to insert the data into
        the Saturday table.

        Returns:
            None

        Raises:
            Exception: If an error occurs during the connection or data insertion,
                       it logs the error with detailed information.
        """
        try:
            self.actionSaturday.triggered.connect(lambda: agenda_data_saturday(self, {
                "sat_date": "sat_date", "sat_note_one": "sat_note_one", "model": "sat_model",
            }, self.db_manager.insert_into_saturday_table, ))
        except Exception as e:
            logger.error(f"An Error has occurred {e}", exc_info=True)
    
    def init_sleep_commit(self):
        """
        Initializes the sleep tracker dialog by connecting the sleep dialog button
        to the commit_sleep_data method. Handles any exceptions that occur during
        the initialization process and logs an error message if an exception is raised.
        Raises:
            Exception: If an error occurs during the initialization of the sleep tracker dialog.
        """
        
        try:
            self.sleep_dialog_btn.clicked.connect(
                lambda: self.commit_sleep_data()
            )
            # Other buttons...
        except Exception as e:
            logger.error(f"Error initializing sleep tracker dialog: {e}", exc_info=True)
    
    def commit_sleep_data(self):
        """
        Commits sleep data from the SleepDialog to the database.
        This method creates an instance of SleepDialog and, if the dialog is accepted,
        retrieves the sleep data entered by the user. It then inserts this data into the 
        appropriate tables in the database and updates the corresponding models.
        The following data is committed:
        - Sleep date
        - Time asleep
        - Time awake
        - Total hours slept
        - Sleep quality
        - Woke up feeling like
        If the dialog is canceled, a log entry is made indicating the cancellation.
        In case of any exceptions during the process, an error is logged with the exception details.
        Raises:
            Exception: If there is an error committing the sleep data.
        """
        
        try:
            dialog = SleepDialog(self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                sleep_date = QDate.currentDate().toString("yyyy-MM-dd")
                time_asleep = dialog.time_asleep.time()
                time_awake = dialog.time_awake.time()
                total_hours_slept = dialog.total_hours_slept.text()
                sleep_quality = dialog.sleep_quality.value()
                woke_up_like = dialog.woke_up_like.value()
                
                self.db_manager.insert_into_sleep_table(sleep_date, time_awake, time_asleep)
                self.sleep_model.select()
                logger.info("sleep details recorded successfully.")
                self.db_manager.insert_into_total_hours_slept_table(sleep_date, total_hours_slept)
                self.total_hours_slept_model.select()
                self.db_manager.insert_woke_up_like_table(sleep_date, woke_up_like)
                self.woke_up_like_model.select()
                self.db_manager.insert_into_sleep_quality_table(sleep_date, sleep_quality)
                self.sleep_quality_model.select()
            else:
                logger.info("sleep details input was canceled.")
        except Exception as e:
            logger.error(f"Error committing sleep data: {e}", exc_info=True)
            
    def init_diet_tracker(self):
        """
        Initializes the diet tracker by connecting UI buttons to their respective functions.

        This method sets up the necessary connections for the diet tracker functionality.
        Specifically, it connects the `open_diet_dialog` button to the `commit_diet` method.
        Additional button connections can be added in the same manner.

        Raises:
            Exception: If there is an error during the initialization of the diet tracker buttons,
                       it logs the error with detailed exception information.
        """
        try:
            self.open_diet_dialog.clicked.connect(
                lambda: self.commit_diet()
            )
            # Other buttons...
        except Exception as e:
            logger.error(f"Error initializing diet tracker buttons: {e}", exc_info=True)

    def commit_diet(self):
        """
        Opens a dialog for the user to input diet details and commits the data to the database if accepted.

        The method performs the following steps:
        1. Opens the DietDialog for user input.
        2. If the dialog is accepted, retrieves the current date and time, food eaten, and calories.
        3. Inserts the retrieved data into the diet table in the database.
        4. Logs the successful recording of diet details and refreshes the diet model.
        5. If the dialog is canceled, logs the cancellation.
        6. Catches and logs any exceptions that occur during the process.

        Raises:
            Exception: If an error occurs while committing the diet data.
        """
        try:
            # Open the diet Details Dialog
            dialog = DietDialog(self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                diet_date = QDate.currentDate().toString("yyyy-MM-dd")
                diet_time = QTime.currentTime().toString("hh:mm:ss")
                food_eaten = dialog.food_eaten.text()
                calories = dialog.calories.value()
                self.db_manager.insert_into_diet_table(diet_date, diet_time, food_eaten, calories)
                logger.info(f"diet Committed {diet_time}, on {diet_date}")
                self.diet_model.select()
                logger.info("diet details recorded successfully.")
            else:
                logger.info("diet details input was canceled.")
        except Exception as e:
            logger.error(f"Error committing diet data: {e}", exc_info=True)
            
    def init_hydration_tracker(self):
        """
        Initializes the hydration tracker buttons.

        This method connects the click events of the hydration tracker buttons
        to the `commit_hydration` method with the corresponding hydration amount.

        Raises:
            Exception: If there is an error initializing the hydration tracker buttons.

        """
        try:
            self.eight_ounce_cup.clicked.connect(
                lambda: self.commit_hydration(8)
            )
            self.sixteen_ounce_cup.clicked.connect(
                lambda: self.commit_hydration(16)
            )
            self.twenty_four_ounce_cup.clicked.connect(
                lambda: self.commit_hydration(24)
            )
            self.thirty_two_ounce_cup.clicked.connect(
                lambda: self.commit_hydration(32)
            )
        except Exception as e:
            logger.error(f"Error initializing hydration tracker buttons: {e}", exc_info=True)
    
    def commit_hydration(self,
                         amount):
        """
        Commits the hydration data to the database.

        Args:
            amount (int): The amount of water in ounces.

        Raises:
            Exception: If an error occurs while committing the hydration data.

        Returns:
            None
        """
        try:
            date = QDate.currentDate().toString("yyyy-MM-dd")
            time = QTime.currentTime().toString("hh:mm:ss")
            self.db_manager.insert_into_hydration_table(date, time, amount)
            logger.info(f"Committed {amount} oz of water at {date} {time}")
            self.hydration_model.select()
        except Exception as e:
            logger.error(f"Error committing hydration data: {e}", exc_info=True)
    
    def init_basics_tracker(self):
        """
        Initializes the basic tracker buttons and connects them to their respective commit functions.

        This method sets up the click event handlers for the exercise, shower, and teeth brushing
        tracker buttons. When a button is clicked, the corresponding commit function is called.

        Raises:
            Exception: If there is an error during the initialization of the tracker buttons,
                       it logs the error with detailed exception information.
        """
        try:
            self.shower_commit.clicked.connect(
                lambda: self.commit_shower()
            )
            self.teeth_commit.clicked.connect(
                lambda: self.commit_teethbrushed()
            )
        except Exception as e:
            logger.error(f"Error initializing exercise tracker buttons: {e}", exc_info=True)
    
    def init_exercise_tracker(self):
        """
        Initializes the exercise tracker by connecting the exercise commit button
        to its corresponding handler. This method sets up the necessary signal-slot
        connections for the exercise tracking functionality.

        Raises:
            Exception: If there is an error during the initialization of the exercise
                       tracker buttons, it logs the error with detailed exception info.
        """
        try:
            self.exercise_commit.clicked.connect(
                lambda: self.commit_exercise()
            )
            # Other buttons...
        except Exception as e:
            logger.error(f"Error initializing exercise tracker buttons: {e}", exc_info=True)
    
    def commit_exercise(self):
        """
        Commits the current exercise data to the database and opens the Exercise Details Dialog for additional input.

        This method performs the following steps:
        1. Retrieves the current date and time.
        2. Inserts the date and time into the exercise table.
        3. Logs the exercise commitment.
        4. Refreshes the yoga model.
        5. Opens the Exercise Details Dialog for user input.
        6. If the dialog is accepted, retrieves additional exercise details (type, length, effort, intensity).
        7. Inserts the additional details into their respective tables.
        8. Refreshes the respective models.
        9. Logs the successful recording of exercise details.
        10. If the dialog is canceled, logs the cancellation.

        If any exception occurs during the process, it logs the error with the exception information.

        Raises:
            Exception: If an error occurs while committing exercise data.
        """
        try:
            dialog = ExerciseDetailsDialog(self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                date = QDate.currentDate().toString("yyyy-MM-dd")
                time = QTime.currentTime().toString("hh:mm:ss")
                self.db_manager.insert_into_exercise_table(date, time)
                logger.info(f"Exercise Committed {time}, on {date}")
                self.yoga_model.select()
                exercise_type = dialog.exercise_type_input.text()
                length_of_exercise = dialog.length_of_exercise.value()
                effort = dialog.effort_spinbox.value()
                intensity = dialog.intensity_spinbox.value()
                
                # Insert data into respective tables
                self.db_manager.insert_into_exercise_type_table(date, time, exercise_type)
                self.exercise_type_model.select()
                self.db_manager.insert_into_exercise_length_table(date, time, length_of_exercise)
                self.exercise_length_model.select()
                self.db_manager.insert_into_exercise_effort_table(date, time, effort)
                self.exercise_effort_model.select()
                self.db_manager.insert_into_exercise_intensity_table(date, time, intensity)
                self.exercise_intensity_model.select()
                
                logger.info("Exercise details recorded successfully.")
            else:
                logger.info("Exercise details input was canceled.")
        except Exception as e:
            logger.error(f"Error committing exercise data: {e}", exc_info=True)
    
    def init_lily_walk_commit(self):
        """
        Initializes the lily walk commit button by connecting its click event to the 
        commit_lily_walk_data method. This method sets up the necessary event handlers 
        for the lily walk button and handles any exceptions that may occur during the 
        initialization process.

        Raises:
            Exception: If an error occurs during the initialization of the lily walk 
            commit button, it logs the error with detailed information.
        """
        try:
            self.lily_walk_btn.clicked.connect(
                lambda: self.commit_lily_walk_data()
            )
            # Other buttons...
        except Exception as e:
            logger.error(f"Error initializing exercise tracker buttons: {e}", exc_info=True)
            
    def commit_lily_walk_data(self):
        """
        Commits the lily walk data to the database and handles the exercise details dialog.

        This method performs the following steps:
        1. Gets the current date and time.
        2. Inserts the date and time into the lily walk table.
        3. Logs the commit action.
        4. Refreshes the lily walk model.
        5. Opens the LilyWalkDialog for additional exercise details.
        6. If the dialog is accepted, retrieves the exercise details (note, gait, behavior)
            and inserts them into their respective tables.
        7. Refreshes the respective models for gait, behavior, and note.
        8. Logs the success of recording exercise details.
        9. If the dialog is canceled, logs the cancellation.
        10. Handles and logs any exceptions that occur during the process.

        Raises:
            Exception: If an error occurs while committing lily_walks data.
        """
        try:
            dialog = LilyWalkDialog(self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                date = QDate.currentDate().toString("yyyy-MM-dd")
                time = QTime.currentTime().toString("hh:mm:ss")
                self.db_manager.insert_into_lily_walk_table(date, time)
                logger.info(f"Exercise Committed {time}, on {date}")
                self.lily_walk_model.select()
                lily_walk_note = dialog.lily_walk_note.text()
                lily_gait = dialog.lily_gait.value()
                lily_behavior = dialog.lily_behavior.value()
                
                self.db_manager.insert_into_lily_walk_gait_table(date, time, lily_gait)
                self.lily_walk_gait_model.select()
                self.db_manager.insert_into_lily_walk_behavior_table(date, time, lily_behavior)
                self.lily_walk_behavior_model.select()
                self.db_manager.insert_into_lily_walk_note_table(date, time, lily_walk_note)
                self.lily_walk_note_model.select()
                
                logger.info("Lily Walk details recorded successfully.")
            else:
                logger.info("Lily Walk details input was canceled.")
        except Exception as e:
            logger.error(f"Error committing Lily Walk data: {e}", exc_info=True)
    
    def commit_shower(self):
        """
        Commits the current date and time to the shower table in the database.

        This method retrieves the current date and time, inserts them into the
        shower table using the db_manager, and updates the shower_model. If an
        error occurs during the process, it logs the error.

        Raises:
            Exception: If there is an error committing the shower data.
        """
        try:
            date = QDate.currentDate().toString("yyyy-MM-dd")
            time = QTime.currentTime().toString("hh:mm:ss")
            self.db_manager.insert_into_shower_table(date, time)
            logger.info(f"shower Committed {time}, on {date}")
            self.shower_model.select()
        except Exception as e:
            logger.error(f"Error committing shower data: {e}", exc_info=True)
    
    def commit_teethbrushed(self):
        """
        Commits the current date and time to the tooth brushing database table.

        This method retrieves the current date and time, formats them, and inserts
        the data into the tooth brushing table using the database manager. It also
        logs the operation and refreshes the tooth model to reflect the new data.

        If an error occurs during the operation, it logs the error with detailed
        exception information.

        Raises:
            Exception: If there is an error committing the data to the database.
        """
        try:
            date = QDate.currentDate().toString("yyyy-MM-dd")
            time = QTime.currentTime().toString("hh:mm:ss")
            self.db_manager.insert_into_tooth_table(date, time)
            logger.info(f"teethbrushed Committed {time}, on {date}")
            self.tooth_model.select()
        except Exception as e:
            logger.error(f"Error committing teethbrushed data: {e}", exc_info=True)
    
    def add_lily_diet_data(self):
        """
        Connects the `lily_ate_check` button click event to the `add_lily_diet_data` function.

        The `add_lily_diet_data` function is called with the following parameters:
        - `self`: The current instance of the class.
        - A dictionary containing the data to be passed to the `add_lily_diet_data` function:
            - "lily_date": The value of the "lily_date" attribute.
            - "lily_time": The value of the "lily_time" attribute.
            - "model": The value of the "lily_diet_model" attribute.
        - `self.db_manager.insert_into_lily_diet_table`: The function to be called when the button is clicked.

        Raises:
            Exception: If an error occurs during the execution of the method.

        """
        try:
            date = QDate.currentDate().toString('yyyy-MM-dd')
            time = QTime.currentTime().toString('hh:mm:ss')
            self.lily_ate_check.clicked.connect(lambda: add_lily_diet_data(self, {
                "lily_date": "lily_date", "lily_time": "lily_time",
                "model": "lily_diet_model",
            }, self.db_manager.insert_into_lily_diet_table, ))
        except Exception as e:
            logger.error(f"An Error has occurred {e}", exc_info=True)
    
    def add_lily_mood_data(self):
        """
        Connects the 'commit_mood' action to the 'add_lily_mood_data' function and passes the necessary data to it.

        This method connects the 'commit_mood' action to the 'add_lily_mood_data' function, which is responsible for inserting
        Lily's mood data into the database. It sets up the necessary data and connects the action to the function using a lambda
        function. The lambda function passes the required data and the function to be called when the action is triggered.

        Parameters:
            self (MainWindow): The instance of the main window.

        Returns:
            None
        """
        try:
            date = QDate.currentDate().toString('yyyy-MM-dd')
            time = QTime.currentTime().toString('hh:mm:ss')
            self.actionCommitLilyMood.triggered.connect(lambda: add_lily_mood_data(self, {
                "lily_date": "lily_date",
                "lily_time": "lily_time",
                "lily_mood_slider": "lily_mood_slider",
                "lily_energy_slider": "lily_energy_slider",
                "lily_mood_activity_slider": "lily_mood_activity_slider",
                "model": "lily_mood_model",
            }, self.db_manager.insert_into_lily_mood_table, ))
        except Exception as e:
            logger.error(f"An Error has occurred {e}", exc_info=True)
    
    def add_lily_notes_data(self):
        """
        Connects the 'commit_lily_notes' action to the 'add_lily_note_data' function.

        This method connects the 'commit_lily_notes' action to the 'add_lily_note_data' function,
        passing the necessary parameters. It handles any exceptions that occur and logs an error message.

        Parameters:
        - self: The instance of the main window.

        Returns:
        - None
        """
        try:
            date = QDate.currentDate().toString('yyyy-MM-dd')
            time = QTime.currentTime().toString('hh:mm:ss')
            self.lily_note_commit_btn.clicked.connect(lambda: add_lily_note_data(self, {
                "lily_date": "lily_date", "lily_time": "lily_time",
                "lily_notes": "lily_notes",
                "model": "lily_notes_model",
            }, self.db_manager.insert_into_lily_notes_table, ))
        except Exception as e:
            logger.error(f"An Error has occurred {e}", exc_info=True)

    def add_lily_time_in_room_data(self):
        """
        Connects the 'commit_room_time' action to the 'add_time_in_room_data' function,
        passing the necessary parameters and inserting the data into the time in room table.

        Raises:
            Exception: If an error occurs during the commit process.

        """
        try:
            date = QDate.currentDate().toString('yyyy-MM-dd')
            time = QTime.currentTime().toString('hh:mm:ss')
            self.actionCommitLilysTimeInRoom.triggered.connect(lambda: add_time_in_room_data(self, {
                "lily_date": "lily_date", "lily_time": "lily_time", "lily_time_in_room_slider":
                    "lily_time_in_room_slider", "model": "time_in_room_model"
            }, self.db_manager.insert_into_time_in_room_table))
        except Exception as e:
            logger.error(f"Error occurring during in_room commit main_window.py loc. {e}",
                         exc_info=True)
    
    def init_mmdmr_tracker(self):
        """
        Initializes the MMDMR tracker by connecting the show_mmdmr_dailog_btn click event
        to the commit_mmdmr method. Logs an error if the initialization fails.

        Raises:
            Exception: If there is an error during the connection of the button click event.
        """
        try:
            self.show_mmdmr_dailog_btn.clicked.connect(
                lambda: self.commit_mmdmr()
            )
        except Exception as e:
            logger.error(f"Error initializing mmdmr tracker buttons: {e}", exc_info=True)
    
    def commit_mmdmr(self):
        """
        Opens the MmdmrDialog for user input and commits the data to the database if accepted.
        This method performs the following steps:
        1. Opens the MmdmrDialog for user input.
        2. If the dialog is accepted, retrieves the current date and time.
        3. Collects values from the mood, mania, depression, and mixed risk sliders.
        4. Inserts the collected data into the mmdmr table in the database.
        5. Refreshes the mmdmr model to reflect the new data.
        6. Logs the success or cancellation of the data input.
        If an exception occurs during the process, it logs an error message with the exception details.
        Raises:
            Exception: If there is an error committing the mmdmr data.
        """
        try:
            # Open the mmdmr Details Dialog
            dialog = MmdmrDialog(self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                mmdmr_date = QDate.currentDate().toString("yyyy-MM-dd")
                mmdmr_time = QTime.currentTime().toString("hh:mm:ss")
                mood_slider = dialog.mood_slider.value()
                mania_slider = dialog.mania_slider.value()
                depression_slider = dialog.depression_slider.value()
                mixed_risk_slider = dialog.mixed_risk_slider.value()
                
                # Insert data into respective tables
                self.db_manager.insert_into_mmdmr_table(mmdmr_date,
                                                        mmdmr_time,
                                                        mood_slider,
                                                        mania_slider,
                                                        depression_slider,
                                                        mixed_risk_slider)
                self.mmdmr_model.select()
                logger.info("mmdmr details recorded successfully.")
            else:
                logger.info("mmdmr details input was canceled.")
        except Exception as e:
            logger.error(f"Error committing mmdmr data: {e}", exc_info=True)
    
    def init_cspr_tracker(self):
        """
        Initializes the CSPR tracker by connecting the `show_cspr_dialog_btn` button
        to the `commit_cspr` method. If an exception occurs during the initialization,
        it logs an error message with the exception details.

        Raises:
            Exception: If an error occurs during the connection of the button.
        """
        try:
            self.show_cspr_dialog_btn.clicked.connect(
                lambda: self.commit_cspr()
            )
        except Exception as e:
            logger.error(f"Error initializing cspr tracker buttons: {e}", exc_info=True)
    
    def commit_cspr(self):
        """
        Commits the CSPR (Calm, Stress, Pain, Rage) data to the database.
        This method opens a dialog to collect CSPR details from the user. If the user accepts the dialog,
        it retrieves the current date and time, as well as the values from the sliders in the dialog.
        It then inserts this data into the database and updates the model. If the user cancels the dialog,
        it logs the cancellation. Any exceptions encountered during the process are logged as errors.
        Raises:
            Exception: If there is an error committing the CSPR data.
        """
        try:
            
            # Open the cspr Details Dialog
            dialog = CsprDialog(self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                cspr_date = QDate.currentDate().toString("yyyy-MM-dd")
                cspr_time = QTime.currentTime().toString("hh:mm:ss")
                calm_slider = dialog.calm_slider.value()
                stress_slider = dialog.stress_slider.value()
                pain_slider = dialog.pain_slider.value()
                rage_slider = dialog.rage_slider.value()
                
                # Insert data into respective tables
                self.db_manager.insert_into_cspr_exam(cspr_date,
                                                       cspr_time,
                                                       calm_slider,
                                                       stress_slider,
                                                       pain_slider,
                                                       rage_slider)
                self.cspr_model.select()
                logger.info("cspr details recorded successfully.")
            else:
                logger.info("cspr details input was canceled.")
        except Exception as e:
            logger.error(f"Error committing cspr data: {e}", exc_info=True)
    
    def init_wefe_tracker(self):
        """
        Initializes the WEFE tracker by connecting the show_wefe_dialog_btn click event
        to the commit_wefe method. Logs an error if initialization fails.

        Raises:
            Exception: If there is an error during the initialization of the WEFE tracker buttons.
        """
        try:
            self.show_wefe_dialog_btn.clicked.connect(
                lambda: self.commit_wefe()
            )
        except Exception as e:
            logger.error(f"Error initializing wefe tracker buttons: {e}", exc_info=True)
    
    def commit_wefe(self):
        """
        Commits the WEFE (Wellbeing, Excitement, Focus, Energy) data from the dialog to the database.
        This method opens a dialog for the user to input WEFE data. If the user accepts the dialog,
        it retrieves the current date and time, as well as the values from the sliders in the dialog.
        It then inserts this data into the WEFE table in the database and updates the model.
        If the dialog is canceled, it logs that the input was canceled.
        Raises:
            Exception: If there is an error committing the WEFE data, it logs the error with traceback information.
        """
        try:
            dialog: object = WefeDialog(self)
            if dialog.exec() == dialog.DialogCode.Accepted:
                wefe_date = QDate.currentDate().toString("yyyy-MM-dd")
                wefe_time = QTime.currentTime().toString("hh:mm:ss")
                wellbeing_slider = dialog.wellbeing_slider.value()
                excite_slider = dialog.excite_slider.value()
                focus_slider = dialog.focus_slider.value()
                energy_slider = dialog.energy_slider.value()
                
                # Insert data into respective tables
                self.db_manager.insert_into_wefe_table(wefe_date,
                                                       wefe_time,
                                                       wellbeing_slider,
                                                       excite_slider,
                                                       focus_slider,
                                                       energy_slider)
                self.wefe_model.select()
                logger.info("wefe details recorded successfully.")
            else:
                logger.info("wefe details input was canceled.")
        except Exception as e:
            logger.error(f"Error committing wefe data: {e}", exc_info=True)
    
    def setup_models(self) -> None:
        """
        Sets up models for various tables by creating and assigning them to attributes.

        This method iterates over a predefined list of tuples, where each tuple contains:
        - The name of the table.
        - The table view.
        - The attribute name for the model.

        For each tuple, it attempts to create a model using the `create_and_set_model` function
        and assigns it to the corresponding attribute. If an error occurs during model creation,
        it logs the error with the table name.

        Raises:
            Exception: If there is an error during model creation, it will be logged.
        """
        try:
            model_setup_info = [
                (
                    "wefe_table",
                    self.wefe_table,
                    "wefe_model"
                ),
                (
                    "cspr_table",
                    self.cspr_table,
                    "cspr_model"
                ),
                (
                    "mmdmr_table",
                    self.mmdmr_table,
                    "mmdmr_model"
                ),
                (
                    "sleep_table",
                    self.sleep_table,
                    "sleep_model"
                ),
                (
                    "total_hours_slept_table",
                    self.total_hours_slept_table,
                    "total_hours_slept_model"
                ),
                (
                    "woke_up_like_table",
                    self.woke_up_like_table,
                    "woke_up_like_model"
                ),
                (
                    "sleep_quality_table",
                    self.sleep_quality_table,
                    "sleep_quality_model"
                ),
                (
                    "shower_table",
                    self.shower_table,
                    "shower_model"
                ),
                (
                    "tooth_table",
                    self.tooth_table,
                    "tooth_model"
                ),
                (
                    "exercise_table",
                    self.yoga_table,
                    "yoga_model"
                ),
                (
                    "diet_table",
                    self.diet_table,
                    "diet_model"
                ),
                (
                    "hydration_table",
                    self.hydration_table,
                    "hydration_model"
                ),
                (
                    "lily_diet_table",
                    self.lily_diet_table,
                    "lily_diet_model"
                ),
                (
                    "lily_mood_table",
                    self.lily_mood_table,
                    "lily_mood_model"
                ),
                (
                    "lily_walk_table",
                    self.lily_walk_table,
                    "lily_walk_model"
                ),
                (
                    "lily_walk_gait_table",
                    self.lily_walk_gait_table,
                    "lily_walk_gait_model"
                ),
                (
                    "lily_walk_behavior_table",
                    self.lily_walk_behavior_table,
                    "lily_walk_behavior_model"
                    
                ),
                (
                    "lily_in_room_table",
                    self.time_in_room_table,
                    "time_in_room_model"
                ),
                (
                    "lily_walk_note_table",
                    self.lily_walk_note_table,
                    "lily_walk_note_model"
                ),
                (
                    "lily_notes_table",
                    self.lily_notes_table,
                    "lily_notes_model"
                ),
                (
                    "sunday_table",
                    self.sun_table,
                    "sun_model"
                ),
                (
                    "monday_table",
                    self.mon_table,
                    "mon_model"
                ),
                (
                    "tuesday_table",
                    self.tues_table,
                    "tues_model"
                ),
                (
                    "wednesday_table",
                    self.wed_table,
                    "wed_model"
                ),
                (
                    "thursday_table",
                    self.thurs_table,
                    "thurs_model"
                ),
                (
                    "friday_table",
                    self.fri_table,
                    "fri_model"
                ),
                (
                    "saturday_table",
                    self.sat_table,
                    "sat_model"
                ),
                (
                    "exercise_intensity_table",
                    self.exercise_intensity_table,
                    "exercise_intensity_model"
                ),
                (
                    "exercise_effort_table",
                    self.exercise_effort_table,
                    "exercise_effort_model"
                ),
                (
                    "exercise_length_table",
                    self.exercise_length_table,
                    "exercise_length_model"
                ),
                (
                    "exercise_type_table",
                    self.exercise_type_table,
                    "exercise_type_model"
                ),
            
            ]
            for table_name, table_view, model_attr in model_setup_info:
                try:
                    setattr(self, model_attr, create_and_set_model(table_name, table_view))
                except Exception as e:
                    logger.error(f"Error setting up model for {table_name}: {e}", exc_info=True)
    
        except Exception as e:
            logger.error(f"Error setting up models: {e}", exc_info=True)
            
    # /////////////////////////////////////////////////////////////////////////////////////////////
    # DELETE button CONNECTION
    # /////////////////////////////////////////////////////////////////////////////////////////////
    def connect_entity_to_delete_data(self,entity,table_name,model_id):
        def connect_entity_to_delete_data(self, entity, table_name, model_id):
            """
            Connects an entity (action or button) to a function that deletes selected rows from a specified table.

            This method checks if the entity has either a 'triggered' or 'clicked' signal and connects it to the 
            delete_selected_rows function. If the entity does not have these attributes, a ValueError is raised.

            Args:
                entity (QAction or QPushButton): The entity to connect, which should be either an action or a button.
                table_name (str): The name of the table from which rows will be deleted.
                model_id (int): The ID of the model associated with the table.

            Raises:
                ValueError: If the entity does not have 'triggered' or 'clicked' attributes.
                Exception: If any other error occurs during the connection setup, it will be logged.
            """
        try:
            # Use a single lambda function to handle the connection for both actions and buttons.
            if hasattr(entity, 'triggered') or hasattr(entity, 'clicked'):
                signal = entity.triggered if hasattr(entity, 'triggered') else entity.clicked
                signal.connect(lambda: delete_selected_rows(self, table_name, model_id))
            else:
                raise ValueError("Entity must be an action or a button.")
        except Exception as e:
            logger.error(f'Error occurred when setting up delete connections: {e}', exc_info=True)
        
    def delete_actions(self) -> None:
        """
        Sets up delete actions for various modules.

        This method iterates over a predefined list of module names, constructs corresponding
        table and model names, and connects delete actions to these entities if the action
        exists.

        Raises:
            Exception: If an error occurs during the setup of delete connections, it logs the
                       error with detailed information.
        """
        try:
            modules = ["sun",
                       "mon",
                       "tues",
                       "wed",
                       "thurs",
                       "fri",
                       "sat",
                       "wefe",
                       "cspr",
                       "mmdmr",
                       "sleep",
                       "total_hours_slept",
                       "woke_up_like",
                       "sleep_quality",
                       "shower",
                       "tooth",
                       "yoga",
                       "diet",
                       "hydration",
                       "lily_diet",
                       "lily_mood",
                       "time_in_room",
                       "lily_walk",
                       "lily_walk_gait",
                       "lily_walk_behavior",
                       "lily_walk_note",
                       "lily_notes",
                       "exercise_intensity",
                       "exercise_effort",
                       "exercise_length",
                       "exercise_type"
                       ]
            for module in modules:
                table_name = f"{module}_table"  # Use `module`, not `modules`
                model_name = f"{module}_model"  # Same here
                
                # Setup for buttons, if they exist
                action_name = "actionDelete"
                if hasattr(self, action_name):
                    action = getattr(self, action_name)
                    self.connect_entity_to_delete_data(action, table_name, model_name)
        except Exception as e:
            logger.error(f'Error occurred when setting up delete connections: {e}', exc_info=True)
    
    def save_state(self):
        """
        Saves the state of the main window.

        This method saves the values of various sliders, inputs, and other UI elements
        as well as the window geometry and state to the application settings.

        Raises:
            Exception: If there is an error while saving the state.

        """
        try:
            self.journal_settings_manager.save_journal(
                self.sun_date,
                self.sun_note_one,
                self.mon_date,
                self.mon_note_one,
                self.tues_date,
                self.tues_note_one,
                self.wed_date,
                self.wed_note_one,
                self.thurs_date,
                self.thurs_note_one,
                self.fri_date,
                self.fri_note_one,
                self.sat_date,
                self.sat_note_one,
            )
            
            self.settings_manager_lilys_widgets.save_lilys_widget_states(
                self.lily_time_in_room_slider,
                self.lily_mood_slider,
                self.lily_mood_activity_slider,
                self.lily_energy_slider,
                self.lily_time_in_room,
                self.lily_mood,
                self.lily_activity,
                self.lily_energy,
                self.lily_notes,
            )
            
            self.settings.setValue(
                "geometry",
                self.saveGeometry())
            
            self.settings.setValue(
                "windowState",
                self.saveState())
        
        except Exception as e:
            logger.error(f"Geometry not good fail. {e}", exc_info=True)
    
    def restore_state(self) -> None:
        """
        Restores the state of the main window by retrieving values from the settings.

        This method restores the values of various sliders, text fields, and window geometry
        from the settings. If an error occurs during the restoration process, it is logged
        with the corresponding exception.

        Returns:
            None
        """
        try:
            self.journal_settings_manager.restore_journal(
                self.sun_date,
                self.sun_note_one,
                self.mon_date,
                self.mon_note_one,
                self.tues_date,
                self.tues_note_one,
                self.wed_date,
                self.wed_note_one,
                self.thurs_date,
                self.thurs_note_one,
                self.fri_date,
                self.fri_note_one,
                self.sat_date,
                self.sat_note_one,
            )
            self.settings_manager_lilys_widgets.restore_lilys_widget_states(
                self.lily_time_in_room_slider,
                self.lily_mood_slider,
                self.lily_mood_activity_slider,
                self.lily_energy_slider,
                self.lily_time_in_room,
                self.lily_mood,
                self.lily_activity,
                self.lily_energy,
                self.lily_notes,
            )
            # restore window geometry state
            self.restoreGeometry(
                self.settings.value("geometry", QByteArray()))
            
            self.restoreState(
                self.settings.value("windowState", QByteArray()))
        except Exception as e:
            logger.error(f"Error restoring WINDOW STATE {e}", exc_info=True)
    
    def closeEvent(self,
                   event: QCloseEvent) -> None:
        """
        Event handler for the close event of the main window.

        This method is called when the user tries to close the main window.
        It saves the state of the application before closing.

        Args:
            event (QCloseEvent): The close event object.

        Returns:
            None
        """
        try:
            try:
                self.save_visibility_state(
                    'week_frame',
                    self.week_frame.isVisible()
                )
            except Exception as e:
                logger.error(f"Error saving visibility state for week_frame: {e}", exc_info=True)
            try:
                self.save_state()
            except Exception as e:
                logger.error(f"{e}")
        except Exception as e:
            logger.error(f"error saving state during closure: {e}", exc_info=True)
