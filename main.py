from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QStyleFactory
from ui.app import MainWindow
import sys
# from utility.logger_setup import logger
import ui.main_ui.res
import ui.main_ui.dialog_res
from ui.main_ui.jsdblm_stylesheet import mainStackStyle
from utility.logger_setup import create_logger
logger = create_logger(__name__)


def run_app():
    """
    Initializes and runs the main application.

    This function sets up the QApplication, applies the Fusion style, 
    initializes the main window with a fixed size, and starts the event loop.
    It also handles various exceptions that might occur during the execution.

    Exceptions:
        ValueError: If a value error occurs during execution.
        TypeError: If a type error occurs during execution.
        ImportError: If an import error occurs during execution.
        OSError: If an OS error occurs during execution.
        Exception: If any other unexpected error occurs during execution.
    """
    try:
        app = QApplication(sys.argv)
        app.setStyle(QStyleFactory.create("Fusion"))
        window = MainWindow()
        window.setStyleSheet(mainStackStyle)
        window.setFixedSize(400, 400)
        window.show()
        sys.exit(app.exec())
    except (ValueError, TypeError) as e:
        logger.error(f"Value or Type error occurred {e}", exc_info=True)
    except ImportError as e:
        logger.error(f"Import error occurred {e}", exc_info=True)
    except OSError as e:
        logger.error(f"OS error occurred {e}", exc_info=True)
    except Exception as e:
        logger.error(f"Unexpected error occurred {e}", exc_info=True)


if __name__ == '__main__':
    run_app()
