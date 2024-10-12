from PyQt6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QSpinBox, QSlider, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import Qt
from ui.dialogs_diet.diet_style import exer_dialog
from ui.dialogs_diet.ui_setup import setup_ui
from ui.dialogs_diet.layout_creation import create_layout
from ui.dialogs_diet.signal_connections import connect_signals


class DietDialog(QDialog):
    """
    DietDialog is a QDialog subclass that provides a user interface for inputting diet details.

    Attributes:
        food_eaten_lbl (QLabel): Label prompting the user to input what they ate.
        calories_lbl (QLabel): Label prompting the user to input the number of calories.
        food_eaten (QLineEdit): Input field for the user to enter the food they ate.
        calories (QSpinBox): Input field for the user to enter the number of calories.
        ok_button (QPushButton): Button to confirm the input.
        cancel_button (QPushButton): Button to cancel the input and close the dialog.

    Methods:
        __init__(self, parent=None): Initializes the dialog, sets up the UI, layout, and signal connections.
    """

    def __init__(self, parent=None):
        """
        Initializes the DietDialog.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.

        Attributes:
            food_eaten_lbl (QLabel): Label for the food eaten input.
            calories_lbl (QLabel): Label for the calories input.
            food_eaten (QLineEdit): Input field for the food eaten.
            calories (QSpinBox): Input field for the number of calories.
            ok_button (QPushButton): Button to confirm the input.
            cancel_button (QPushButton): Button to cancel the input.
        """
        super().__init__(parent)
        self.resize(200, 145)
        self.food_eaten_lbl = QLabel("What did you eat?")
        self.calories_lbl = QLabel("How Many Calories")
        self.food_eaten = QLineEdit()
        self.calories = QSpinBox()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        self.setWindowTitle("Diet Details")
        setup_ui(self)
        create_layout(self)
        connect_signals(self)
        self.setStyleSheet(exer_dialog)
