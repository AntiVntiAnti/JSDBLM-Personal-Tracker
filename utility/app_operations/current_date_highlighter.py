from PyQt6.QtWidgets import QDateEdit
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import QDate
from typing import Dict
import utility.tracker_config as tkc
from utility.logger_setup import create_logger
logger = create_logger(__name__)


class DateHighlighter:
    def __init__(self, date_widgets: Dict) -> None:
        """
        Initializes the CurrentDateHighlighter with the given date widgets.

        Args:
            date_widgets (Dict): A dictionary containing the date widgets to be highlighted.
        """
        self.date_widgets = date_widgets
        self.current_date = QDate.currentDate()
        self.update_date_styles()

    def update_date_styles(self) -> None:
        """
        This method iterates through the date widgets and applies a highlight
        to the widget if its date matches the current date. Otherwise, it 
        normalizes the widget's style.

        Raises:
            Exception: If an error occurs while updating the date styles, it 
            logs the error message.
        Updates the style of the QDateEdit widgets based on the current date.
        """
        try:
            for day, widget in self.date_widgets.items():
                if widget.date() == self.current_date:
                    self.highlight_current_date(widget)
                else:
                    self.normalize_date(widget)
        except Exception as e:
            logger.error(f"An error occurred while updating date styles: {e}")

    @staticmethod
    def highlight_current_date(widget: QDateEdit) -> None:
        """
        Highlights the current date in the given QDateEdit widget.

        This function sets the font and stylesheet of the provided QDateEdit widget
        to highlight the current date. If an error occurs during this process, it 
        logs the error message.

        Args:
            widget (QDateEdit): The QDateEdit widget to be highlighted.

        Raises:
            Exception: If an error occurs while setting the font or stylesheet.
        """

        try:
            font = QFont()
            widget.setFont(font)
            widget.setStyleSheet(tkc.COLOR)
        except Exception as e:
            logger.error(f"An error occurred while highlighting the current date: {e}")

    @staticmethod
    def normalize_date(widget: QDateEdit) -> None:
        """
        Resets the font and stylesheet of a QDateEdit widget to its default state.

        This function sets the font of the provided QDateEdit widget to non-bold and 
        applies a default stylesheet. If an error occurs during this process, it logs 
        the error message.

        Args:
            widget (QDateEdit): The QDateEdit widget to be normalized.

        Raises:
            Exception: If an error occurs while setting the font or stylesheet.
        """

        try:
            font = QFont()
            font.setBold(False)
            widget.setFont(font)
            widget.setStyleSheet(tkc.STYLESHEET)
        except Exception as e:
            logger.error(f"An error occurred while normalizing the date: {e}")
