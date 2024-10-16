from PyQt6.QtCore import QDate, QTime
from utility.logger_setup import create_logger
logger = create_logger(__name__)


def add_shower_data(main_window_instance,
                    widget_names,
                    db_insert_method):
    try:
        widget_methods = {
            widget_names['basics_date']: (None, 'date', "yyyy-MM-dd"),
            widget_names['basics_time']: (None, 'time', "hh:mm:ss"),
            
        }
        
        data_to_insert = []
        for widget_name, (widget_attr, method, format_type) in widget_methods.items():
            widget = getattr(main_window_instance, widget_name)
            value = getattr(widget, method)()
            if format_type:
                value = value.toString(format_type)
            data_to_insert.append(value)
        
        db_insert_method(*data_to_insert)
        reset_shower_data(main_window_instance, widget_names)
        logger.debug(f"{widget_names} committed succesfully")
    except Exception as e:
        logger.error(f"Error adding basics data: {e}", exc_info=True)


def reset_shower_data(main_window_instance,
                      widget_names):
    try:
        getattr(main_window_instance, widget_names['basics_date']).setDate(QDate.currentDate())
        getattr(main_window_instance, widget_names['basics_time']).setTime(QTime.currentTime())
        # Assuming there is a model for each day
        getattr(main_window_instance, widget_names['model']).select()
    except Exception as e:
        logger.error(f"Error resetting basics data: {e}", exc_info=True)
