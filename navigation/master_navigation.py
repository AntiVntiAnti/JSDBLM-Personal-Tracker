import utility.tracker_config as tkc
from utility.logger_setup import create_logger
logger = create_logger(__name__)
from typing import Any


def change_mainStack(mainStack: Any, index: int) -> None:
    """
    Changes the current index of the mainStack to the specified index.

    Args:
        mainStack (Any): The stack object whose current index is to be changed.
        index (int): The index to set as the current index of the mainStack.

    Returns:
        None

    Raises:
        Exception: If there is an error while changing the current index of the mainStack.
    """

    try:
        mainStack.setCurrentIndex(index)
    except Exception as e:
        logger.error(f"main stack Page Change Error: {e}", exc_info=True)


def change_alpha_stack_page(stack_alpha: Any, index: int) -> None:
    """
    Changes the current index of the given stack_alpha to the specified index.

    Args:
        stack_alpha (Any): The stack object whose current index is to be changed.
        index (int): The index to set as the current index of the stack_alpha.

    Returns:
        None

    Raises:
        Exception: If an error occurs while setting the current index, it logs the error.
    """

    try:
        stack_alpha.setCurrentIndex(index)
    except Exception as e:
        logger.error(f"Alpha Stack Page Change Error: {e}", exc_info=True)


def change_agenda_stack_page(agenda_stack: Any, index: int) -> None:
    """
    Changes the current page of the agenda stack to the specified index.
    Args:
        agenda_stack (Any): The agenda stack object that supports the setCurrentIndex method.
        index (int): The index of the page to switch to.
    Returns:
        None
    Raises:
        Exception: If an error occurs while changing the page, it logs the error with traceback.
    """
    
    try:
        agenda_stack.setCurrentIndex(index)
    except Exception as e:
        logger.error(f"Agenda Stack Page Change Error: {e}", exc_info=True)
