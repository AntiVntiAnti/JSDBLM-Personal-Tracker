from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout


def create_layout(dialog):
    """
    Sets up the layout for the given dialog.
    This function creates a vertical layout and adds widgets for food eaten and calories.
    It also creates a horizontal layout for OK and Cancel buttons and adds it to the main layout.
    Args:
        dialog (QDialog): The dialog for which the layout is being created. It should have the following attributes:
            - food_eaten_lbl (QLabel): Label for the food eaten input.
            - food_eaten (QWidget): Widget for the food eaten input.
            - calories_lbl (QLabel): Label for the calories input.
            - calories (QWidget): Widget for the calories input.
            - ok_button (QPushButton): Button to confirm the action.
            - cancel_button (QPushButton): Button to cancel the action.
    """
    main_layout = QVBoxLayout()

    # Exercise type
    main_layout.addWidget(dialog.food_eaten_lbl)
    main_layout.addWidget(dialog.food_eaten)
    
    # Length of exercise
    main_layout.addWidget(dialog.calories_lbl)
    main_layout.addWidget(dialog.calories)

    # Buttons
    button_layout = QHBoxLayout()
    button_layout.addWidget(dialog.ok_button)
    button_layout.addWidget(dialog.cancel_button)
    main_layout.addLayout(button_layout)

    dialog.setLayout(main_layout)
