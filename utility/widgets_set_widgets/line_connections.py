from typing import Union
# slider_spinbox_connections.py
from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QLineEdit, QTimeEdit
import utility.tracker_config as tkc
from utility.logger_setup import create_logger
logger = create_logger(__name__)


def line_edit_times(line_edit: Union[QLineEdit, str], time_edit: Union[QTimeEdit, QTime]) -> None:
    """
    Connects the textChanged signal of a QLineEdit to update the time of a QTimeEdit.

    This function checks if both line_edit and time_edit are not None and are instances of QLineEdit and QTimeEdit respectively.
    If so, it connects the textChanged signal of the line_edit to a lambda function that sets the time of the time_edit to the current time.

    Args:
        line_edit (Union[QLineEdit, str]): The QLineEdit widget or a string.
        time_edit (Union[QTimeEdit, QTime]): The QTimeEdit widget or a QTime object.

    Returns:
        None

    Raises:
        SpecificException: If an error occurs during the connection process.
    """

    try:
        if line_edit is not None and time_edit is not None:
            if isinstance(line_edit, QLineEdit) and isinstance(time_edit, QTimeEdit):
                line_edit.textChanged.connect(lambda: time_edit.setTime(QTime.currentTime()))
    except Exception as e:
        logger.error(f"Error in line_connections.py module : {e}")

