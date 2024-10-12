from PyQt6.QtGui import QTextCharFormat, QFont, QTextCursor
from PyQt6.QtWidgets import QApplication, QTextEdit
from typing import Callable, Any
from formatters.text_format_setup import BaseTextFormatter
from utility.logger_setup import create_logger
logger = create_logger(__name__)


class UnderlineTextFormatter(BaseTextFormatter):
    """
    UnderlineTextFormatter is a class that extends BaseTextFormatter to provide functionality for underlining text.
    Methods:
        make_underline(fmt, current_format):
            Toggles the underline property of the font in the given format.
        apply():
            Applies the underline formatting to the current text format.
    """

    def make_underline(self, fmt, current_format):
        fmt.setFontUnderline(not current_format.font().underline())
    
    # This method can be used to directly apply this formatting
    def apply(self):
        self.apply_current_text_format(self.format_text)
