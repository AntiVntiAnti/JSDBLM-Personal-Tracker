# utils.py or helpers.py
from PyQt6.QtCore import Qt
from utility.logger_setup import create_logger
logger = create_logger(__name__)


def apply_sorting(table_view, column_index):
    """
    Enable sorting on a QTableView and sort by the specified column in descending order.

    Args:
        table_view (QTableView): The table view to apply sorting to.
        column_index (int): The index of the column to sort by.
    """
    try:
        table_view.setSortingEnabled(True)
        table_view.sortByColumn(column_index, Qt.SortOrder.DescendingOrder)
    except Exception as e:
        logger.error(f"Error occurred when applying sort_table module - {e}", exc_info=True)
