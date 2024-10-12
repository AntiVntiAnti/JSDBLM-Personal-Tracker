from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout


def create_layout(dialog):
    """
    Creates and sets the layout for the exercise dialog.

    This method initializes and arranges the widgets in a vertical layout.
    It includes the following sections:
    - Exercise type input
    - Length of exercise input
    - Effort input with a slider and spinbox
    - Intensity input with a slider and spinbox
    - OK and Cancel buttons

    The layout is set to the main layout of the dialog.
    """
    main_layout = QVBoxLayout()

    # Exercise type
    main_layout.addWidget(dialog.exlbl)
    main_layout.addWidget(dialog.exercise_type_input)

    # Length of exercise
    main_layout.addWidget(dialog.exlbl1)
    main_layout.addWidget(dialog.length_of_exercise)

    # Effort
    main_layout.addWidget(dialog.exlbl2)
    effort_layout = QHBoxLayout()
    effort_layout.addWidget(dialog.effort_slider)
    effort_layout.addWidget(dialog.effort_spinbox)
    main_layout.addLayout(effort_layout)

    # Intensity
    main_layout.addWidget(dialog.exlbl3)
    intensity_layout = QHBoxLayout()
    intensity_layout.addWidget(dialog.intensity_slider)
    intensity_layout.addWidget(dialog.intensity_spinbox)
    main_layout.addLayout(intensity_layout)

    # Buttons
    button_layout = QHBoxLayout()
    button_layout.addWidget(dialog.ok_button)
    button_layout.addWidget(dialog.cancel_button)
    main_layout.addLayout(button_layout)

    dialog.setLayout(main_layout)
