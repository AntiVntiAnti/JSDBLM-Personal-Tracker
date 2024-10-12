from PyQt6.QtWidgets import QSlider, QSpinBox
import utility.tracker_config as tkc
from utility.logger_setup import create_logger
logger = create_logger(__name__)


def connect_slider_spinbox(slider: QSlider, spinbox: QSpinBox) -> None:
    """
    Connects a slider's valueChanged signal to a spinbox's setValue slot and vice versa.

    Parameters:
        slider (QSlider): The slider object.
        spinbox (QSpinBox): The spinbox object.

    Returns:
        None
    """
    try:
        if slider is not None and spinbox is not None:
            if isinstance(slider, QSlider) and isinstance(spinbox, QSpinBox):
                # Connect the slider's valueChanged signal to the spinbox's setValue slot
                slider.valueChanged.connect(spinbox.setValue)
                # Connect the spinbox's valueChanged signal to the slider's setValue slot
                spinbox.valueChanged.connect(slider.setValue)
                # Add logger to track the success or failure of the connection process
    except Exception as e:
        logger.error(f"Error connecting signals and slots: {e}")
