from typing import List
from PyQt6.QtWidgets import QLineEdit
from utility.logger_setup import create_logger
logger = create_logger(__name__)


def calculate_calories(calories_values: List[int], total_calories_widget: QLineEdit) -> None:
    """
    Calculate the total calories from a list of calorie values and update a QLineEdit widget with the result.

    Args:
        calories_values (List[int]): A list of integer values representing individual calorie counts.
        total_calories_widget (QLineEdit): A QLineEdit widget where the total calorie count will be displayed.

    Returns:
        None

    Raises:
        Exception: If an error occurs during the calculation or updating the widget, it will be logged.
    """
    try:
        total_calories = sum(calories_values)

        # Update the total_calories_widget with the total
        total_calories_widget.setText(str(total_calories))
    except Exception as e:
        logger.error(f"An error occurred while calculating calories: {e}")
