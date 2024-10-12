from PyQt6.QtWidgets import QSlider, QLabel
import utility.tracker_config as tkc
from utility.logger_setup import create_logger
logger = create_logger(__name__)


def connect_label_to_slider(slider: QSlider, label: QLabel) -> None:
    """
    Connects a QSlider's valueChanged signal to a QLabel's setValue slot.

    This function ensures that the QLabel updates its value whenever the QSlider's value changes.

    Args:
        slider (QSlider): The slider whose value changes will trigger the label update.
        label (QLabel): The label that will display the slider's value.

    Raises:
        Exception: If there is an error connecting the signals and slots, it will be logged.
    """

    try:
        if slider is not None and label is not None:
            if isinstance(slider, QSlider) and isinstance(label, QLabel):
                # Connect the slider's valueChanged signal to the label's setValue slot
                slider.valueChanged.connect(label.setValue)
    except Exception as e:
        logger.error(f"Error connecting signals and slots: {e}")
