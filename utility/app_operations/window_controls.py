from typing import Any
from utility.logger_setup import create_logger
logger = create_logger(__name__)


class WindowController:
    """
    WindowController class provides methods to control the window state, such as minimizing and maximizing the window.
    Attributes:
        is_minimized (bool): Indicates whether the window is minimized.
        is_maximized (bool): Indicates whether the window is maximized.
    Methods:
        __init__():
            Initializes the WindowController with default states for minimized and maximized.
        toggle_minimize(window: Any) -> None:
            Toggles the minimized state of the given window. If the window is minimized, it will be restored to normal. 
            If it is not minimized, it will be minimized.
        toggle_maximize(window: Any) -> None:
            Toggles the maximized state of the given window. If the window is maximized, it will be restored to normal. 
            If it is not maximized, it will be maximized.
    """
    
    def __init__(self) -> None:
        """
        Initializes the window control settings.

        Attributes:
            is_minimized (bool): Indicates if the window is minimized.
            is_maximized (bool): Indicates if the window is maximized.
        """

        self.is_minimized: bool = False
        self.is_maximized: bool = False
    
    def toggle_minimize(self, window: Any) -> None:
        """
        Toggles the minimized state of the given window.

        If the window is currently minimized, it will be restored to its normal state.
        If the window is not minimized, it will be minimized.

        Args:
            window (Any): The window object to be toggled.

        Raises:
            Exception: Logs any exception that occurs during the operation.
        """

        try:
            if self.is_minimized:
                window.showNormal()
                self.is_minimized = False
            else:
                window.showMinimized()
                self.is_minimized = True
        except Exception as e:
            logger.error(f"{e}", exc_info=True)
    
    def toggle_maximize(self, window: Any) -> None:
        """
        Toggles the maximized state of the given window.

        If the window is currently maximized, it will be restored to its normal size.
        If the window is not maximized, it will be maximized.

        Args:
            window (Any): The window object to be toggled.

        Returns:
            None
        """

        if self.is_maximized:
            window.showNormal()
            self.is_maximized = False
        else:
            window.showMaximized()
            self.is_maximized = True
