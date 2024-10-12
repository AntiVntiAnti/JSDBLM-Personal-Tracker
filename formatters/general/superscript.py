from PyQt6.QtGui import QTextCharFormat, QFont, QTextCursor
from PyQt6.QtWidgets import QApplication, QTextEdit
from utility.logger_setup import create_logger
logger = create_logger(__name__)
from typing import Callable, Any
from formatters.text_format_setup import BaseTextFormatter


class SuperScriptTextFormatter(BaseTextFormatter):
    """
    SuperScriptTextFormatter is a class that extends BaseTextFormatter to provide functionality for formatting text as superscript.
    Methods:
        make_superscript(fmt, current_format):
            Sets the vertical alignment of the given format to superscript.
        apply():
            Applies the current text format using the superscript formatting.
    """

    def make_superscript(self, fmt, current_format):
        # Set the vertical alignment to Subscript for the format
        fmt.setVerticalAlignment(QTextCharFormat.VerticalAlignment.AlignSuperScript)
    
    # This method can be used to directly apply this formatting
    def apply(self):
        self.apply_current_text_format(self.format_text)
