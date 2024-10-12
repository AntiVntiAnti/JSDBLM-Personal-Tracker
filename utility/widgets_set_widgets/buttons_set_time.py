from typing import Optional
from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QPushButton, QTimeEdit
import utility.tracker_config as tkc
from utility.logger_setup import create_logger
logger = create_logger(__name__)


def btn_times(app_btns: Optional[QPushButton], times_edit: Optional[QTimeEdit]) -> bool:
    """
    Connects a QPushButton to a QTimeEdit widget to set the current time when the button is clicked.

    Args:
        app_btns (Optional[QPushButton]): The button that will trigger the time setting.
        times_edit (Optional[QTimeEdit]): The time edit widget that will be set to the current time.

    Returns:
        bool: True if the connection was successful, False otherwise.

    Raises:
        Exception: Logs an error if the connection fails.
    """

    try:
        if app_btns is None or not isinstance(app_btns, QPushButton) or times_edit is None or not isinstance(
            times_edit,
            QTimeEdit
                ):
            return False
        app_btns.clicked.connect(lambda: times_edit.setTime(QTime.currentTime()))
        return True
    except Exception as e:
        logger.error(f"{app_btns} unable to set {times_edit}, {type(e).__name__}: {str(e)}", exc_info=True)
        return False
