import logging
import os
import sys

import utility.tracker_config as tkc

LOG_DIRECTORY = tkc.PRINGLES
# LOG_FILE = 'TESTJAN23MAIN.txt'


log_directory = os.path.join(os.path.expanduser('~'), tkc.PRINGLES)

# Create the directory if it doesn't exist
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Path to your log file
log_file = os.path.join(log_directory, tkc.LOG_FILE)

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt=tkc.DATEFORMAT,
                    filename=log_file,
                    filemode=tkc.FILE_MODE)

# Create the directory if it doesn't exist
LOG_DIRECTORY = 'logsDialogs'
log_directory = os.path.join(os.path.expanduser('~'), LOG_DIRECTORY)

if not os.path.exists(log_directory):
    os.makedirs(log_directory)


def create_logger(module_name):
    """
    Creates and configures a logger for the specified module.
    Args:
        module_name (str): The name of the module for which the logger is being created.
    Returns:
        logging.Logger: Configured logger instance for the specified module.
    """
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    file_handler = logging.FileHandler(os.path.join(log_directory, f'{module_name}.log'))
    file_handler.setFormatter(formatter)
    
    # stream_handler = logging.StreamHandler(sys.stdout)
    # stream_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    # logger.addHandler(stream_handler)
    
    return logger
