from PyQt6 import QtSql
from PyQt6.QtWidgets import QAbstractItemView
from utility.logger_setup import create_logger
logger = create_logger(__name__)

# model_setup.py


def create_and_set_model(table_name: str, view_widget: QAbstractItemView) -> QtSql.QSqlTableModel:
    """
    Creates a QSqlTableModel, sets it to the specified table, and assigns it to the given view widget.

    Args:
        table_name (str): The name of the table to set in the model.
        view_widget (QAbstractItemView): The view widget to which the model will be assigned.

    Returns:
        QtSql.QSqlTableModel: The created and configured QSqlTableModel.

    Raises:
        RuntimeError: If there is an error selecting data from the specified table.
    """

    model = QtSql.QSqlTableModel()
    model.setTable(table_name)
    model.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnFieldChange)
    if not model.select():
        error_message = f"Error selecting data from table: {table_name}, {model.lastError().text()}"
        logger.error(error_message)
        raise RuntimeError(error_message)

    view_widget.setModel(model)
    return model
