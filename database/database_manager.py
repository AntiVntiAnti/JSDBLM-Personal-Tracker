# from sexy_logger import logger
import sqlite3
import utility.tracker_config as tkc
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
import os
import shutil
from typing import List, Union
from utility.logger_setup import create_logger

logger = create_logger(__name__)

user_dir = os.path.expanduser('~')
db_path = os.path.join(os.getcwd(), tkc.DB_NAME)  # Database Name
target_db_path = os.path.join(user_dir, tkc.DB_NAME)  # Database Name


def initialize_database():
    """
    Initializes the database by copying an existing database file to the target path or creating a new one if it doesn't exist.
    The function performs the following steps:
    1. Checks if the target database path exists.
    2. If the target database path does not exist:
        a. Checks if the source database path exists.
        b. If the source database path exists, copies it to the target path.
        c. If the source database path does not exist, creates a new SQLite database at the target path.
    3. Logs an error if unable to create or copy the database.
    Exceptions:
        Logs any exceptions that occur during the database initialization process.
    Raises:
        Exception: If there is an error during the database initialization process.
    """
    
    try:
        if not os.path.exists(target_db_path):
            if os.path.exists(db_path):
                shutil.copy(db_path, target_db_path)
            else:
                db = QSqlDatabase.addDatabase('QSQLITE')
                db.setDatabaseName(target_db_path)
                if not db.open():
                    logger.error("Error: Unable to create database")
                db.close()
    except Exception as e:
        logger.error("Error: Unable to create database", str(e))


class DataManager:
    """
    DataManager is a class responsible for managing a SQLite database using PyQt's QSqlDatabase and QSqlQuery.

    Attributes:
        db (QSqlDatabase): The database connection.
        query (QSqlQuery): The SQL query object.

    Methods:
        __init__(db_name): Initializes the database manager.
        setup_tables(): Sets up all the necessary tables for the database.
        setup_lily_walk_table(): Sets up the 'lily_walk_table' in the database.
        setup_lily_walk_gait_table(): Sets up the 'lily_walk_gait_table' in the database.
        setup_lily_walk_behavior_table(): Sets up the 'lily_walk_behavior_table' in the database.
        setup_lily_walk_note_table(): Sets up the 'lily_walk_note_table' in the database.
        insert_into_lily_walk_table(date, time): Inserts a new record into the 'lily_walk_table'.
        insert_into_lily_walk_note_table(date, time, lily_walk_note): Inserts a new record into the 'lily_walk_note_table'.
        insert_into_lily_walk_gait_table(date, time, lily_gait): Inserts a new record into the 'lily_walk_gait_table'.
        insert_into_lily_walk_behavior_table(date, time, lily_behavior): Inserts a new record into the 'lily_walk_behavior_table'.
        lily_execute_insert(sql, bind_values, table_name): Executes an SQL insert statement with the provided bind values.
        setup_exercise_detail_table(): Sets up the exercise detail tables in the database.
        insert_into_exercise_type_table(date, time, exercise_type): Inserts a new record into the 'exercise_type_table'.
        insert_into_exercise_length_table(date, time, length): Inserts a new record into the 'exercise_length_table'.
        insert_into_exercise_effort_table(date, time, effort): Inserts a new record into the 'exercise_effort_table'.
        insert_into_exercise_intensity_table(date, time, intensity): Inserts a new record into the 'exercise_intensity_table'.
        _execute_insert(sql, bind_values, table_name): Executes an SQL insert statement with the provided bind values.
        setup_table_sunday(): Sets up the 'sunday_table' in the database.
        insert_into_sunday_table(sun_date, sun_note_one): Inserts a new record into the 'sunday_table'.
        setup_table_monday(): Sets up the 'monday_table' in the database.
        insert_into_monday_table(mon_date, mon_note_one): Inserts a new record into the 'monday_table'.
        setup_table_tuesday(): Sets up the 'tuesday_table' in the database.
        insert_into_tuesday_table(tues_date, tues_note_one): Inserts a new record into the 'tuesday_table'.
    """

    
    def __init__(self,
                 db_name=target_db_path):
        """
        Initializes the database manager.

        Args:
            db_name (str): The path to the database file. Defaults to target_db_path.

        Raises:
            Exception: If there is an error opening the database.

        Attributes:
            db (QSqlDatabase): The database connection.
            query (QSqlQuery): The SQL query object.

        Methods:
            setup_tables(): Sets up the necessary tables in the database.
        """
        
        try:
            self.db = QSqlDatabase.addDatabase('QSQLITE')
            self.db.setDatabaseName(db_name)
            
            if not self.db.open():
                logger.error("Error: Unable to open database")
            logger.debug("DB INITIALIZING")
            self.query = QSqlQuery()
            self.setup_tables()
        except Exception as e:
            logger.error(f"Error: Unable to open database {e}", exc_info=True)
    
    def setup_tables(self):
        """
        Sets up all the necessary tables for the database.

        This method initializes various tables required for tracking different
        aspects such as sleep, exercise, diet, hydration, and more. Each table
        is set up by calling its respective setup method.

        Tables initialized:
        - Sleep table
        - Total hours slept table
        - Woke up like table
        - Sleep quality table
        - Shower table
        - Exercise table
        - Teethbrush table
        - Diet table
        - Hydration table
        - Lily diet table
        - Lily mood table
        - Lily walk table
        - Lily walk gait table
        - Lily walk behavior table
        - Time in room table
        - Lily notes table
        - Lily walk note table
        - Wefe table
        - Into CSPR exam table
        - MMDMR table
        - Sunday table
        - Monday table
        - Tuesday table
        - Wednesday table
        - Thursday table
        - Friday table
        - Saturday table
        - Exercise detail table
        """
        self.setup_sleep_table()
        self.setup_total_hours_slept_table()
        self.setup_woke_up_like_table()
        self.setup_sleep_quality_table()
        self.setup_shower()
        self.setup_exercise()
        self.setup_teethbrush()
        self.setup_diet_table()
        self.setup_hydration_table()
        self.setup_lily_diet_table()
        self.setup_lily_mood_table()
        self.setup_lily_walk_table()
        self.setup_lily_walk_gait_table()
        self.setup_lily_walk_behavior_table()
        self.setup_time_in_room_table()
        self.setup_lily_notes_table()
        self.setup_lily_walk_note_table()
        self.setup_wefe_table()
        self.setup_into_cspr_exam()
        self.setup_mmdmr_table()
        self.setup_table_sunday()
        self.setup_table_monday()
        self.setup_table_tuesday()
        self.setup_table_wednesday()
        self.setup_table_thursday()
        self.setup_table_friday()
        self.setup_table_saturday()
        self.setup_exercise_detail_table()
    
    def setup_lily_walk_table(self) -> None:
        """
        Sets up the 'lily_walk_table' in the database if it does not already exist.

        The table includes the following columns:
        - id: INTEGER, primary key, auto-incremented
        - date: TEXT, stores the date of the walk
        - time: TEXT, stores the time of the walk

        Logs an error message if the table creation fails.
        """
        if not self.query.exec("""
               CREATE TABLE IF NOT EXISTS lily_walk_table (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   date TEXT,
                   time TEXT
                   )
           """):
            logger.error(f"Error creating table: lily_walk_table - {self.query.lastError().text()}")
    
    def setup_lily_walk_gait_table(self):
        """
        Creates the 'lily_walk_gait_table' in the database if it does not already exist.

        The table includes the following columns:
        - id: An integer primary key that auto-increments.
        - date: A text field to store the date.
        - time: A text field to store the time.
        - lily_gait: An integer field to store the lily gait data.

        Logs an error message if the table creation fails.
        """
        if not self.query.exec("""
               CREATE TABLE IF NOT EXISTS lily_walk_gait_table (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   date TEXT,
                   time TEXT,
                   lily_gait INTEGER
                   )
           """):
            logger.error(f"Error creating table: lily_walk_gait_table - {self.query.lastError().text()}")
    
    def setup_lily_walk_behavior_table(self):
        """
        Creates the 'lily_walk_behavior_table' in the database if it does not already exist.

        The table has the following columns:
        - id: INTEGER PRIMARY KEY AUTOINCREMENT
        - date: TEXT
        - time: TEXT
        - lily_behavior: INTEGER

        Logs an error if the table creation fails.
        """
        if not self.query.exec("""
               CREATE TABLE IF NOT EXISTS lily_walk_behavior_table (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   date TEXT,
                   time TEXT,
                   lily_behavior INTEGER
                   )
           """):
            logger.error(f"Error creating table: lily_walk_behavior_table - {self.query.lastError().text()}")
    
    def setup_lily_walk_note_table(self):
        """
        Creates the 'lily_walk_note_table' in the database if it does not already exist.

        The table has the following columns:
        - id: INTEGER, primary key, autoincrement
        - date: TEXT, the date of the note
        - time: TEXT, the time of the note
        - lily_walk_note: TEXT, the content of the note

        Logs an error message if the table creation fails.
        """
        if not self.query.exec("""
               CREATE TABLE IF NOT EXISTS lily_walk_note_table (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   date TEXT,
                   time TEXT,
                   lily_walk_note TEXT
                   )
           """):
            logger.error(f"Error creating table: lily_walk_note_table - {self.query.lastError().text()}")
    
    def insert_into_lily_walk_table(self,
                                    date: str,
                                    time: str) -> None:
        """
        Inserts a new record into the lily_walk_table.

        Args:
            date (str): The date of the lily walk in the format 'YYYY-MM-DD'.
            time (str): The time of the lily walk in the format 'HH:MM:SS'.

        Returns:
            None
        """
        sql = """INSERT INTO lily_walk_table (date, time) VALUES (?, ?)"""
        bind_values = [date, time]
        self.lily_execute_insert(sql, bind_values, "lily_walk_table")
    
    def insert_into_lily_walk_note_table(self,
                                         date: str,
                                         time: str,
                                         lily_walk_note: str
                                         ) -> None:
        """
        Inserts a new record into the lily_walk_note_table.

        Args:
            date (str): The date of the lily walk note.
            time (str): The time of the lily walk note.
            lily_walk_note (str): The content of the lily walk note.

        Returns:
            None
        """
        sql = """
            INSERT INTO lily_walk_note_table (date, time, lily_walk_note) VALUES (?, ?, ?)"""
        bind_values = [date, time, lily_walk_note]
        self.lily_execute_insert(sql, bind_values, "lily_walk_note_table")
    
    def insert_into_lily_walk_gait_table(self,
                                         date: str,
                                         time: str,
                                         lily_gait: int) -> None:
        """
        Inserts a new record into the lily_walk_gait_table.

        Args:
            date (str): The date of the record in 'YYYY-MM-DD' format.
            time (str): The time of the record in 'HH:MM:SS' format.
            lily_gait (int): The gait value to be inserted.

        Returns:
            None
        """
        sql = """INSERT INTO lily_walk_gait_table (date, time, lily_gait) VALUES (?, ?, ?)"""
        bind_values = [date, time, lily_gait]
        self.lily_execute_insert(sql, bind_values, "lily_walk_gait_table")
    
    def insert_into_lily_walk_behavior_table(self,
                                             date: str,
                                             time: str,
                                             lily_behavior: int) -> None:
        """
        Inserts a new record into the lily_walk_behavior_table.

        Args:
            date (str): The date of the behavior in 'YYYY-MM-DD' format.
            time (str): The time of the behavior in 'HH:MM:SS' format.
            lily_behavior (int): An integer representing the behavior.

        Returns:
            None
        """
        sql = """INSERT INTO lily_walk_behavior_table (date, time, lily_behavior) VALUES (?, ?, ?)"""
        bind_values = [date, time, lily_behavior]
        self.lily_execute_insert(sql, bind_values, "lily_walk_behavior_table")
    
    def lily_execute_insert(self,
                            sql: str,
                            bind_values: List[Union[str, int]],
                            table_name: str) -> None:
        """
        Executes an SQL insert statement with the provided bind values.

        Args:
            sql (str): The SQL insert statement with placeholders for bind values.
            bind_values (List[Union[str, int]]): A list of values to bind to the SQL statement.
            table_name (str): The name of the table where the data will be inserted.

        Raises:
            ValueError: If the number of placeholders in the SQL statement does not match the number of bind values.
            sqlite3.DatabaseError: If there is a database error during the execution of the insert statement.
            Exception: For any other unexpected errors during the execution.

        Logs:
            Error messages are logged if there are issues with the insertion process.
        """
        try:
            if sql.count('?') != len(bind_values):
                raise ValueError(f"Mismatch in bind values for {table_name}: expected {sql.count('?')}, got {len(bind_values)}.")
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if not self.query.exec():
                logger.error(f"Error inserting data into {table_name}: {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError in {table_name}: {e}")
        except sqlite3.DatabaseError as e:
            logger.error(f"Database error during data insertion into {table_name}: {e}",
                         exc_info=True)
        except Exception as e:
            logger.error(f"Unexpected error during data insertion into {table_name}: {e}",
                         exc_info=True)
    
    def setup_exercise_detail_table(self) -> None:
        """
        Sets up the exercise detail tables in the database if they do not already exist.

        This method creates the following tables:
        - exercise_type_table: Stores the type of exercise with columns for id, date, time, and exercise_type.
        - exercise_length_table: Stores the length of exercise with columns for id, date, time, and length.
        - exercise_effort_table: Stores the effort of exercise with columns for id, date, time, and effort.
        - exercise_intensity_table: Stores the intensity of exercise with columns for id, date, time, and intensity.

        Logs an error message if any table creation fails.
        """
        # Exercise Type Table
        if not self.query.exec("""
            CREATE TABLE IF NOT EXISTS exercise_type_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                time TEXT,
                exercise_type TEXT
            )
        """):
            logger.error(f"Error creating table: exercise_type_table - {self.query.lastError().text()}")
        
        # Exercise Length Table
        if not self.query.exec("""
            CREATE TABLE IF NOT EXISTS exercise_length_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                time TEXT,
                length INTEGER
            )
        """):
            logger.error(f"Error creating table: exercise_length_table - {self.query.lastError().text()}")
        
        # Exercise Effort Table
        if not self.query.exec("""
            CREATE TABLE IF NOT EXISTS exercise_effort_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                time TEXT,
                effort INTEGER
            )
        """):
            logger.error(f"Error creating table: exercise_effort_table - {self.query.lastError().text()}")
        
        # Exercise Intensity Table
        if not self.query.exec("""
            CREATE TABLE IF NOT EXISTS exercise_intensity_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                time TEXT,
                intensity INTEGER
            )
        """):
            logger.error(f"Error creating table: exercise_intensity_table - {self.query.lastError().text()}")
    
    def insert_into_exercise_type_table(self,
                                        date: str,
                                        time: str,
                                        exercise_type: str) -> None:
        """
        Inserts a new record into the exercise_type_table.

        Args:
            date (str): The date of the exercise in 'YYYY-MM-DD' format.
            time (str): The time of the exercise in 'HH:MM:SS' format.
            exercise_type (str): The type of exercise performed.

        Returns:
            None
        """
        sql = """INSERT INTO exercise_type_table (date, time, exercise_type) VALUES (?, ?, ?)"""
        bind_values = [date, time, exercise_type]
        self._execute_insert(sql, bind_values, "exercise_type_table")
    
    def insert_into_exercise_length_table(self,
                                          date: str,
                                          time: str,
                                          length: int) -> None:
        """
        Inserts a new record into the exercise_length_table.

        Args:
            date (str): The date of the exercise in 'YYYY-MM-DD' format.
            time (str): The time of the exercise in 'HH:MM:SS' format.
            length (int): The length of the exercise in minutes. Must be a non-negative integer.

        Returns:
            None

        Raises:
            ValueError: If the length is negative.
        """
        if length < 0:
            logger.error(f"Invalid length value: {length}")
            return
        sql = """INSERT INTO exercise_length_table (date, time, length) VALUES (?, ?, ?)"""
        bind_values = [date, time, length]
        self._execute_insert(sql, bind_values, "exercise_length_table")
    
    def insert_into_exercise_effort_table(self,
                                          date: str,
                                          time: str,
                                          effort: int) -> None:
        """
        Inserts a new record into the exercise_effort_table.

        Args:
            date (str): The date of the exercise effort in YYYY-MM-DD format.
            time (str): The time of the exercise effort in HH:MM:SS format.
            effort (int): The effort value of the exercise. Must be a non-negative integer.

        Returns:
            None

        Raises:
            ValueError: If the effort value is negative.
        """
        if effort < 0:
            logger.error(f"Invalid effort value: {effort}")
            return
        sql = """INSERT INTO exercise_effort_table (date, time, effort) VALUES (?, ?, ?)"""
        bind_values = [date, time, effort]
        self._execute_insert(sql, bind_values, "exercise_effort_table")
    
    def insert_into_exercise_intensity_table(self,
                                             date: str,
                                             time: str,
                                             intensity: int) -> None:
        """
        Inserts a new record into the exercise_intensity_table.

        Args:
            date (str): The date of the exercise in YYYY-MM-DD format.
            time (str): The time of the exercise in HH:MM:SS format.
            intensity (int): The intensity level of the exercise. Must be a non-negative integer.

        Returns:
            None

        Raises:
            ValueError: If the intensity is a negative value.
        """
        if intensity < 0:
            logger.error(f"Invalid intensity value: {intensity}")
            return
        sql = """INSERT INTO exercise_intensity_table (date, time, intensity) VALUES (?, ?, ?)"""
        bind_values = [date, time, intensity]
        self._execute_insert(sql, bind_values, "exercise_intensity_table")
    
    def _execute_insert(self,
                        sql: str,
                        bind_values: List[Union[str, int]],
                        table_name: str) -> None:
        """
        Executes an SQL insert statement with the provided bind values.

        Args:
            sql (str): The SQL insert statement with placeholders for bind values.
            bind_values (List[Union[str, int]]): The values to bind to the SQL statement.
            table_name (str): The name of the table where the data will be inserted.

        Raises:
            ValueError: If the number of placeholders in the SQL statement does not match the number of bind values.
            sqlite3.DatabaseError: If there is a database error during the execution of the insert statement.
            Exception: If an unexpected error occurs during the execution of the insert statement.

        Logs:
            Error messages are logged if there are issues with the insertion process.
        """
        try:
            if sql.count('?') != len(bind_values):
                raise ValueError(f"Mismatch in bind values for {table_name}: expected {sql.count('?')}, got {len(bind_values)}.")
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if not self.query.exec():
                logger.error(f"Error inserting data into {table_name}: {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError in {table_name}: {e}")
        except sqlite3.DatabaseError as e:
            logger.error(f"Database error during data insertion into {table_name}: {e}",
                         exc_info=True)
        except Exception as e:
            logger.error(f"Unexpected error during data insertion into {table_name}: {e}",
                         exc_info=True)
    
    def setup_table_sunday(self):
        """
        Sets up the 'sunday_table' in the database if it does not already exist.

        This method creates a table named 'sunday_table' with the following columns:
        - id: An integer primary key that auto-increments.
        - sun_date: A text field to store the date.
        - sun_note_one: A text field to store a note.

        If the table creation fails, an error message is logged.

        Returns:
            None
        """
        if not self.query.exec(f"""
                CREATE TABLE IF NOT EXISTS sunday_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sun_date TEXT,
                sun_note_one TEXT
                )"""):
            logger.error(f"Error creating table: sundays table", self.query.lastError().text())
    
    def insert_into_sunday_table(self,
                                 sun_date: str,
                                 sun_note_one: str) -> None:
        """
        Inserts a record into the 'sunday_table' with the provided date and note.
        Args:
            sun_date (str): The date to be inserted into the 'sunday_table'.
            sun_note_one (str): The note to be inserted into the 'sunday_table'.
        Raises:
            ValueError: If the number of placeholders in the SQL query does not match the number of bind values.
            Exception: If there is an error during the execution of the query.
        Logs:
            Error messages are logged if there is an issue with the insertion process.
        """
        
        sql: str = f"""INSERT INTO sunday_table(
                            sun_date,
                            sun_note_one) VALUES (?, ?)"""
        
        bind_values: List[Union[str, int]] = [sun_date, sun_note_one]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: sunday_table Expected {sql.count('?')}
                                        bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: sunday_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError sunday_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: sunday_table {e}", exc_info=True)
    
    def setup_table_monday(self):
        """
        Sets up the 'monday_table' in the database if it does not already exist.

        The table includes the following columns:
        - id: An integer primary key that autoincrements.
        - mon_date: A text field for the date.
        - mon_note_one: A text field for a note.

        Logs an error if the table creation fails.
        """
        if not self.query.exec(f"""
                CREATE TABLE IF NOT EXISTS monday_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mon_date TEXT,
                mon_note_one TEXT
                )"""):
            logger.error(f"Error creating table: mondays table", self.query.lastError().text())
    
    def insert_into_monday_table(self,
                                 mon_date: str,
                                 mon_note_one: str) -> None:
        """
        Inserts a new record into the monday_table in the database.

        Args:
            mon_date (str): The date to be inserted into the mon_date column.
            mon_note_one (str): The note to be inserted into the mon_note_one column.

        Raises:
            ValueError: If the number of placeholders in the SQL query does not match the number of bind values.
            Exception: If there is an error during the execution of the SQL query.

        Logs:
            Logs an error message if there is an issue with inserting data into the monday_table.
        """
        sql: str = f"""INSERT INTO monday_table(
                            mon_date,
                            mon_note_one) VALUES (?, ?)"""
        
        bind_values: List[Union[str, int]] = [mon_date, mon_note_one]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: monday_table Expected {sql.count('?')}
                                        bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: monday_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError monday_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: monday_table {e}", exc_info=True)
    
    def setup_table_tuesday(self):
        """
        Sets up the 'tuesday_table' in the database if it does not already exist.

        The table has the following columns:
        - id: An integer primary key that autoincrements.
        - tues_date: A text field to store the date.
        - tues_note_one: A text field to store a note.

        Logs an error if the table creation fails.
        """
        if not self.query.exec(f"""
                CREATE TABLE IF NOT EXISTS tuesday_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tues_date TEXT,
                tues_note_one TEXT
                )"""):
            logger.error(f"Error creating table: tuesdays table", self.query.lastError().text())
    
    def insert_into_tuesday_table(self,
                                  tues_date: str,
                                  tues_note_one: str) -> None:
        """
        Inserts a new record into the tuesday_table with the provided date and note.

        Args:
            tues_date (str): The date to be inserted into the tuesday_table.
            tues_note_one (str): The note to be inserted into the tuesday_table.

        Raises:
            ValueError: If the number of placeholders in the SQL query does not match the number of bind values.
            Exception: For any other exceptions that occur during the data insertion process.

        Logs:
            Error messages are logged if there is an issue with the SQL execution or if exceptions are raised.
        """
        sql: str = f"""INSERT INTO tuesday_table(
                            tues_date,
                            tues_note_one) VALUES (?, ?)"""
        
        bind_values: List[Union[str, int]] = [tues_date, tues_note_one]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: tuesday_table Expected {sql.count('?')}
                                        bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: tuesday_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError tuesday_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: tuesday_table {e}", exc_info=True)
    
    def setup_table_wednesday(self):
        """
        Sets up the 'wednesday_table' in the database if it doesn't already exist.

        Returns:
            None
        """
        if not self.query.exec(f"""
                CREATE TABLE IF NOT EXISTS wednesday_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                wed_date TEXT,
                wed_note_one TEXT
                )"""):
            logger.error(f"Error creating table: wednesday table", self.query.lastError().text())
    
    def insert_into_wednesday_table(self,
                                    wed_date: str,
                                    wed_note_one: str
                                    ) -> None:
        
        sql: str = f"""INSERT INTO wednesday_table(
                            wed_date,
                            wed_note_one) VALUES (?, ?)"""
        
        bind_values: List[Union[str, int]] = [wed_date, wed_note_one]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: wednesday_table Expected {sql.count('?')}
                                        bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: wednesday_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError wednesday_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: wednesday_table {e}", exc_info=True)
    
    def setup_table_thursday(self):
        """
        Sets up the 'thursday_table' in the database if it doesn't already exist.

        This method creates a table named 'thursday_table' with the following columns:
        - id: INTEGER PRIMARY KEY AUTOINCREMENT
        - thurs_date: TEXT
        - thurs_note_one: TEXT

        Returns:
        - None if the table is created successfully.
        - Logs an error message if there is an error creating the table.
        """
        if not self.query.exec(f"""
                CREATE TABLE IF NOT EXISTS thursday_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                thurs_date TEXT,
                thurs_note_one TEXT
                )"""):
            logger.error(f"Error creating table: thursday table", self.query.lastError().text())
    
    def insert_into_thursday_table(self,
                                   thurs_date: str,
                                   thurs_note_one: str
                                   ) -> None:
        
        sql: str = f"""INSERT INTO thursday_table(
                            thurs_date,
                            thurs_note_one) VALUES (?, ?)"""
        
        bind_values: List[Union[str, int]] = [thurs_date, thurs_note_one]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: thursday_table Expected {sql.count('?')}
                                        bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: thursday_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError thursday_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: thursday_table {e}", exc_info=True)
    
    def setup_table_friday(self):
        """
        Sets up the 'friday_table' in the database if it doesn't already exist.

        Returns:
            None
        """
        if not self.query.exec(f"""
                CREATE TABLE IF NOT EXISTS friday_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fri_date TEXT,
                fri_note_one TEXT
                )"""):
            logger.error(f"Error creating table: fridays table", self.query.lastError().text())
    
    def insert_into_friday_table(self,
                                 fri_date: str,
                                 fri_note_one: str
                                 ) -> None:
        
        sql: str = f"""INSERT INTO friday_table(
                            fri_date,
                            fri_note_one) VALUES (?, ?)"""
        
        bind_values: List[Union[str, int]] = [fri_date, fri_note_one]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: friday_table Expected {sql.count('?')}
                                        bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: friday_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError friday_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: friday_table {e}", exc_info=True)
    
    def setup_table_saturday(self):
        if not self.query.exec(f"""
                CREATE TABLE IF NOT EXISTS saturday_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sat_date TEXT,
                sat_note_one TEXT
                )"""):
            logger.error(f"Error creating table: saturdays table", self.query.lastError().text())
    
    def insert_into_saturday_table(self,
                                   sat_date: str,
                                   sat_note_one: str
                                   ) -> None:
        
        sql: str = f"""INSERT INTO saturday_table(
                            sat_date,
                            sat_note_one) VALUES (?, ?)"""
        
        bind_values: List[Union[str, int]] = [sat_date, sat_note_one]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: saturday_table Expected {sql.count('?')}
                                        bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: saturday_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError saturday_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: saturday_table {e}", exc_info=True)
    
    def setup_mmdmr_table(self) -> None:
        """
        Sets up the 'mmdmr_table' in the database if it doesn't already exist.

        This method creates a table named 'mmdmr_table' in the database with the following columns:
        - id: INTEGER (Primary Key, Autoincrement)
        - mmdmr_date: TEXT
        - mmdmr_time: TEXT
        - mood_slider: INTEGER
        - mania_slider: INTEGER
        - depression_slider: INTEGER
        - mixed_risk_slider: INTEGER

        If the table already exists, this method does nothing.

        Returns:
            None
        """
        if not self.query.exec(f"""
                                            CREATE TABLE IF NOT EXISTS mmdmr_table (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            mmdmr_date TEXT,
                                            mmdmr_time TEXT,
                                            mood_slider INTEGER,
                                            mania_slider INTEGER,
                                            depression_slider INTEGER,
                                            mixed_risk_slider INTEGER
                                            )"""):
            logger.error(f"Error creating table: mmdmr_table",
                         self.query.lastError().text())
    
    def insert_into_mmdmr_table(self,
                                mmdmr_date: int,
                                mmdmr_time: int,
                                mood_slider: int,
                                mania_slider: int,
                                depression_slider: int,
                                mixed_risk_slider: int) -> None:
        """
        Inserts data into the mmdmr_table.

        Args:
            mmdmr_date (int): The date of the mental_mental record.
            mmdmr_time (int): The time of the mental_mental record.
            mood_slider (int): The value of the mood slider.
            mania_slider (int): The value of the mania slider.
            depression_slider (int): The value of the depression slider.
            mixed_risk_slider (int): The value of the mixed risk slider.

        Returns:
            None

        Raises:
            ValueError: If the number of bind values does not match the number of placeholders in the SQL query.
            Exception: If there is an error during data insertion.

        """
        sql: str = f"""INSERT INTO mmdmr_table(
                            mmdmr_date,
                            mmdmr_time,
                            mood_slider,
                            mania_slider,
                            depression_slider,
                            mixed_risk_slider) VALUES (?, ?, ?, ?, ?, ?)"""
        
        bind_values: List[Union[str, int]] = [mmdmr_date, mmdmr_time,
                                              mood_slider, mania_slider, depression_slider,
                                              mixed_risk_slider]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: mmdmr_table Expected {sql.count('?')}
                                        bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: mmdmr_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError mmdmr_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: mmdmr_table {e}", exc_info=True)
    
    def setup_into_cspr_exam(self) -> None:
        if not self.query.exec(f"""
                                            CREATE TABLE IF NOT EXISTS cspr_table (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            cspr_date TEXT,
                                            cspr_time TEXT,
                                            calm_slider INTEGER,
                                            stress_slider INTEGER,
                                            pain_slider INTEGER,
                                            rage_slider INTEGER
                                            )"""):
            logger.error(f"Error creating table: cspr_table",
                         self.query.lastError().text())
    
    def insert_into_cspr_exam(self,
                              cspr_date: str,
                              cspr_time: str,
                              calm_slider: int,
                              stress_slider: int,
                              pain_slider: int,
                              rage_slider: int
                              ) -> None:
        
        sql: str = f"""INSERT INTO cspr_table(
                            cspr_date,
                            cspr_time,
                            calm_slider,
                            stress_slider,
                            pain_slider,
                            rage_slider) VALUES (?, ?, ?, ?, ?, ?)"""
        
        bind_values: List[Union[str, int]] = [cspr_date, cspr_time,
                                              calm_slider, stress_slider, pain_slider, rage_slider]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: cspr_table Expected {sql.count('?')}
                                        bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: cspr_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError cspr_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: cspr_table {e}", exc_info=True)
    
    def setup_wefe_table(self) -> None:
        if not self.query.exec(f"""
                                        CREATE TABLE IF NOT EXISTS wefe_table (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        wefe_date TEXT,
                                        wefe_time TEXT,
                                        wellbeing_slider INTEGER,
                                        excite_slider INTEGER,
                                        focus_slider INTEGER,
                                        energy_slider INTEGER
                                        )"""):
            logger.error(f"Error creating table: wefe_table",
                         self.query.lastError().text())
    
    def insert_into_wefe_table(self,
                               wefe_date: str,
                               wefe_time: str,
                               wellbeing_slider: int,
                               excite_slider: int,
                               focus_slider: int,
                               energy_slider: int
                               ) -> None:
        
        sql: str = f"""INSERT INTO wefe_table(
                        wefe_date,
                        wefe_time,
                        wellbeing_slider,
                        excite_slider,
                        focus_slider,
                        energy_slider
                        ) VALUES (?, ?, ?, ?, ?, ?)"""
        
        bind_values: List[Union[str, int]] = [wefe_date,
                                              wefe_time,
                                              wellbeing_slider,
                                              excite_slider,
                                              focus_slider,
                                              energy_slider]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: wefe_table Expected {sql.count('?')}
                                    bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: wefe_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError wefe_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: wefe_table {e}", exc_info=True)
    
    def setup_lily_notes_table(self) -> None:
        """
        Sets up the 'lily_notes_table' in the database if it doesn't already exist.

        This method creates a table named 'lily_notes_table' with the following columns:
        - id: INTEGER (Primary Key, Auto Increment)
        - lily_date: TEXT
        - lily_time: TEXT
        - lily_notes: TEXT

        Returns:
        - None if the table is created successfully.
        - Logs an error message if there's an error creating the table.
        """
        if not self.query.exec(f"""
                        CREATE TABLE IF NOT EXISTS lily_notes_table (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        lily_date TEXT,
                        lily_time TEXT,
                        lily_notes TEXT
                        )"""):
            logger.error(f"Error creating table: lily_notes_table", self.query.lastError().text())
    
    def insert_into_lily_notes_table(self,
                                     lily_date: str,
                                     lily_time: str,
                                     lily_notes: str) -> None:
        """
        Inserts a new record into the lily_notes_table.

        Args:
            lily_date (str): The date of the Lily note.
            lily_time (str): The time of the Lily note.
            lily_notes (str): The content of the Lily note.

        Raises:
            ValueError: If the number of bind values does not match the number of placeholders in the SQL query.

        Returns:
            None
        """
        sql: str = f"""INSERT INTO lily_notes_table(lily_date, lily_time, lily_notes) VALUES (?, ?, ?)"""
        bind_values: List[str] = [lily_date, lily_time, lily_notes]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: lily_notes_table Expected {sql.count('?')}
                            bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(f"Error inserting data: lily_notes_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError lily_notes_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: lily_notes_table {e}", exc_info=True)
        
        ##################################################################################################################
        # Lily Diet Table
        ##################################################################################################################
    
    def setup_time_in_room_table(self) -> None:
        """
        Sets up the 'lily_in_room_table' table in the database if it doesn't exist.

        This method creates the 'lily_in_room_table' table with the following columns:
        - id: INTEGER (Primary Key, Autoincrement)
        - lily_date: TEXT
        - lily_time: TEXT
        - time_in_room_slider: INTEGER

        Returns:
        None
        """
        if not self.query.exec(f"""
                        CREATE TABLE IF NOT EXISTS lily_in_room_table (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        lily_date TEXT,
                        lily_time TEXT,
                        time_in_room_slider INTEGER
                        )"""):
            logger.error(f"Error creating table: lily_in_room_table", self.query.lastError().text())
    
    def insert_into_time_in_room_table(self,
                                       lily_date: str,
                                       lily_time: str,
                                       time_in_room_slider: int) -> None:
        """
        Inserts a new record into the lily_in_room_table.

        Args:
            lily_date (str): The date of the record.
            lily_time (str): The time of the record.
            time_in_room_slider (int): The value of the time_in_room_slider.

        Raises:
            ValueError: If the number of bind values does not match the expected number of placeholders in the SQL query.

        Returns:
            None
        """
        sql: str = f"""INSERT INTO lily_in_room_table(lily_date, lily_time,
                                               time_in_room_slider) VALUES (?, ?, ?)"""
        bind_values: List[Union[str, int]] = [lily_date, lily_time, time_in_room_slider]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: lily_in_room_table Expected {sql.count('?')}
                            bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: lily_in_room_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError lily_in_room_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: lily_in_room_table {e}", exc_info=True)
        
        ##################################################################################################################
        # Lily Diet Table
        ##################################################################################################################
    
    def setup_lily_diet_table(self) -> None:
        """
        Sets up the 'lily_diet_table' in the database if it doesn't already exist.

        This method creates a table named 'lily_diet_table' with the following columns:
        - id: INTEGER (Primary Key, Auto Increment)
        - lily_date: TEXT
        - lily_time: TEXT

        Returns:
        None
        """
        if not self.query.exec(f"""
                        CREATE TABLE IF NOT EXISTS lily_diet_table (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        lily_date TEXT,
                        lily_time TEXT
                        )"""):
            logger.error(f"Error creating table: lily_diet_table", self.query.lastError().text())
    
    def insert_into_lily_diet_table(self,
                                    lily_date: str,
                                    lily_time: str) -> None:
        """
        Inserts a new record into the lily_diet_table.

        Args:
            lily_date (str): The date of the record.
            lily_time (str): The time of the record.

        Raises:
            ValueError: If the number of bind values does not match the expected number of placeholders in the SQL query.

        Returns:
        None
        """
        sql: str = f"""INSERT INTO lily_diet_table(lily_date, lily_time) VALUES (?, ?)"""
        bind_values: List[str] = [lily_date, lily_time]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: lily_eats_table Expected {sql.count('?')}
                            bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: lily_eats_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError lily_eats_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: lily_eats_table {e}", exc_info=True)
        
        ##################################################################################################################
        #       Lily MOOD table
        ##################################################################################################################
    
    def setup_lily_mood_table(self) -> None:
        """
        Sets up the 'lily_mood_table' in the database if it does not already exist.

        The table includes the following columns:
        - id: INTEGER, primary key, auto-incremented
        - lily_date: TEXT, the date associated with the mood entry
        - lily_time: TEXT, the time associated with the mood entry
        - lily_mood_slider: INTEGER, the mood level on a slider scale
        - lily_mood_activity_slider: INTEGER, the activity level on a slider scale
        - lily_energy_slider: INTEGER, the energy level on a slider scale

        Logs an error if the table creation fails.
        """
        if not self.query.exec(f"""
                        CREATE TABLE IF NOT EXISTS lily_mood_table (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        lily_date TEXT,
                        lily_time TEXT,
                        lily_mood_slider INTEGER,
                        lily_mood_activity_slider INTEGER,
                        lily_energy_slider INTEGER
                            )"""):
            logger.error(f"Error creating table: lily_mood_table", self.query.lastError().text())
    
    def insert_into_lily_mood_table(self,
                                    lily_date: str,
                                    lily_time: str,
                                    lily_mood_slider: int,
                                    lily_mood_activity_slider: int,
                                    lily_energy_slider: int) -> None:
        """
        Inserts a new record into the lily_mood_table.

        Args:
            lily_date (str): The date of the record.
            lily_time (str): The time of the record.
            lily_mood_slider (int): The mood slider value.
            lily_mood_activity_slider (int): The mood activity slider value.
            lily_energy_slider (int): The energy slider value.

        Raises:
            ValueError: If the number of bind values does not match the expected number in the SQL query.

        Returns:
        None
        """
        sql: str = f"""INSERT INTO lily_mood_table(
                lily_date, lily_time, lily_mood_slider, lily_mood_activity_slider, lily_energy_slider)
                VALUES (?, ?, ?, ?, ?)"""
        bind_values: List[Union[str, int]] = [lily_date, lily_time, lily_mood_slider,
                                              lily_mood_activity_slider, lily_energy_slider]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: lily_mood_table Expected
                            {sql.count('?')} bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: lily_mood_table - {self.query.lastError().text()}")
        except ValueError as ve:
            logger.error(f"ValueError lily_mood_table: {str(ve)}")
        except Exception as e:
            logger.error(f"Error during data insertion: lily_mood_table {e}", exc_info=True)
    
    def setup_mental_mental_table(self) -> None:
        """
        Sets up the 'mental_mental_table' in the database if it doesn't already exist.

        This method creates a table named 'mental_mental_table' in the database with the following columns:
        - id: INTEGER (Primary Key, Autoincrement)
        - mmdmr_date: TEXT
        - mmdmr_time: TEXT
        - mood_slider: INTEGER
        - mania_slider: INTEGER
        - depression_slider: INTEGER
        - mixed_risk_slider: INTEGER

        If the table already exists, this method does nothing.

        Returns:
            None
        """
        if not self.query.exec(f"""
                                    CREATE TABLE IF NOT EXISTS mental_mental_table (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    mmdmr_date TEXT,
                                    mmdmr_time TEXT,
                                    mood_slider INTEGER,
                                    mania_slider INTEGER,
                                    depression_slider INTEGER,
                                    mixed_risk_slider INTEGER
                                    )"""):
            logger.error(f"Error creating table: mental_mental_table",
                         self.query.lastError().text())
    
    def setup_diet_table(self):
        """
        Sets up the diet_table in the database if it does not already exist.

        The diet_table includes the following columns:
        - id: INTEGER PRIMARY KEY AUTOINCREMENT
        - diet_date: TEXT
        - diet_time: TEXT
        - food_eaten: TEXT
        - calories: INTEGER

        If the table creation fails, an error message is logged.

        Returns:
            None
        """
        if not self.query.exec(f"""
                        CREATE TABLE IF NOT EXISTS diet_table (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        diet_date TEXT,
                        diet_time TEXT,
                        food_eaten TEXT,
                        calories INTEGER
                        )"""):
            logger.error(f"Error creating table: diet_table", self.query.lastError().text())
    
    def insert_into_diet_table(self, diet_date, diet_time, food_eaten, calories):
        """
        Inserts a new record into the diet_table in the database.

        Args:
            diet_date (str): The date of the diet entry.
            diet_time (str): The time of the diet entry.
            food_eaten (str): The food item consumed.
            calories (int): The number of calories consumed.

        Raises:
            ValueError: If the number of bind values does not match the expected count.
            Exception: For any other errors that occur during data insertion.

        Logs:
            Error messages are logged if there is an issue with data insertion.
        """
        
        sql = f"""INSERT INTO diet_table(diet_date, diet_time, food_eaten, calories) VALUES
                (?, ?, ?, ?)"""
        
        bind_values = [diet_date, diet_time, food_eaten, calories]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"Mismatch: diet_table Expected {sql.count('?')} bind values, got "
                                 f"{len(bind_values)}.")
            if not self.query.exec():
                logger.error(f"Error inserting data: diet_table - {self.query.lastError().text()}")
        except ValueError as ve:
            logger.error(f"ValueError diet_table: {str(ve)}")
        except Exception as e:
            logger.error(f"Error during data insertion: diet_table", str(e))
    
    def setup_hydration_table(self):
        """
        Sets up the hydration_table in the database if it does not already exist.

        The hydration_table contains the following columns:
        - id: An integer primary key that auto-increments.
        - diet_date: A text field representing the date of the diet entry.
        - diet_time: A text field representing the time of the diet entry.
        - hydration: An integer representing the hydration level.

        If the table creation fails, an error is logged with the details of the failure.
        """
        if not self.query.exec(f"""
                        CREATE TABLE IF NOT EXISTS hydration_table (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        diet_date TEXT,
                        diet_time TEXT,
                        hydration INTEGER
                        )"""):
            logger.error(f"Error creating table: hydration_table", self.query.lastError().text())
        
        # database_manager.py
    
    def insert_into_hydration_table(self, diet_date, diet_time, hydration):
        """
        Inserts a new record into the hydration_table with the provided diet date, diet time, and hydration values.

        Args:
            diet_date (str): The date of the diet entry.
            diet_time (str): The time of the diet entry.
            hydration (float): The hydration value to be recorded.

        Raises:
            ValueError: If the number of bind values does not match the expected count.
            Exception: For any other errors that occur during the data insertion process.

        Logs:
            Error messages are logged if there are issues with the data insertion.
        """
        sql = """INSERT INTO hydration_table(diet_date, diet_time, hydration) VALUES (?, ?, ?)"""
        
        bind_values = [diet_date, diet_time, hydration]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"Mismatch: hydration_table Expected {sql.count('?')} bind values, got {len(bind_values)}.")
            if not self.query.exec():
                logger.error(f"Error inserting data: hydration_table - {self.query.lastError().text()}")
        except ValueError as ve:
            logger.error(f"ValueError hydration_table: {str(ve)}")
        except Exception as e:
            logger.error(f"Error during data insertion: hydration_table", str(e))
        
        # -:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-
        # SLEEP table
        # -:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-
    
    def setup_shower(self) -> None:
        """
        Sets up the 'shower_table' in the database if it does not already exist.

        The table includes the following columns:
        - id: An integer primary key that auto-increments.
        - basics_date: A text field to store the date.
        - basics_time: A text field to store the time.

        Logs an error if the table creation fails.
        """
        if not self.query.exec(f"""
                                CREATE TABLE IF NOT EXISTS shower_table (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                basics_date TEXT,
                                basics_time TEXT
                                )"""):
            logger.error(f"Error creating table: shower_table", self.query.lastError().text())
    
    def insert_into_shower_table(self, basics_date: str, basics_time: str,) -> None:
        """
        Inserts a new record into the shower_table with the provided date and time.

        Args:
            basics_date (str): The date to be inserted into the shower_table.
            basics_time (str): The time to be inserted into the shower_table.

        Raises:
            ValueError: If the number of placeholders in the SQL query does not match the number of bind values.
            Exception: If there is an error during the execution of the SQL query.

        Logs:
            Error messages are logged if there is an issue with the SQL execution or if a ValueError is raised.
        """
        sql: str = f"""INSERT INTO shower_table(basics_date, basics_time) VALUES (?, ?)"""
        
        bind_values: List[Union[str, bool]] = [basics_date, basics_time,
                                               ]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: shower_table Expected {sql.count('?')}
                            bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: shower_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError shower_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: shower_table {e}", exc_info=True)
    
    def setup_exercise(self) -> None:
        """
        Sets up the exercise table in the database if it does not already exist.

        This method executes a SQL command to create a table named 'exercise_table'
        with the following columns:
        - id: An integer primary key that auto-increments.
        - basics_date: A text field to store the date of the exercise.
        - basics_time: A text field to store the time of the exercise.

        If the table creation fails, an error message is logged.

        Returns:
            None
        """
        if not self.query.exec(f"""
                                CREATE TABLE IF NOT EXISTS exercise_table (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                basics_date TEXT,
                                basics_time TEXT
                                )"""):
            logger.error(f"Error creating table: exercise_table", self.query.lastError().text())
    
    def insert_into_exercise_table(self, basics_date: str, basics_time: str,) -> None:
        """
        Inserts a new record into the exercise_table with the provided date and time.

        Args:
            basics_date (str): The date of the exercise in 'YYYY-MM-DD' format.
            basics_time (str): The time of the exercise in 'HH:MM:SS' format.

        Raises:
            ValueError: If the number of placeholders in the SQL query does not match the number of bind values.
            Exception: For any other exceptions that occur during the execution of the query.

        Logs:
            Error messages are logged if there is an issue with the SQL execution or if an exception is raised.
        """
        
        sql: str = f"""INSERT INTO exercise_table(basics_date, basics_time) VALUES (?, ?)"""
        
        bind_values: List[Union[str, bool]] = [basics_date, basics_time,
                                               ]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: exercise_table Expected {sql.count('?')}
                            bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: exercise_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError exercise_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: exercise_table {e}", exc_info=True)
        
        # Teethbrushing Table
    
    def setup_teethbrush(self) -> None:
        """
        Sets up the tooth_table in the database if it does not already exist.

        This method creates a table named 'tooth_table' with the following columns:
        - id: INTEGER, primary key, auto-incremented
        - basics_date: TEXT
        - basics_time: TEXT

        If the table creation fails, an error is logged with the details of the failure.
        """
        if not self.query.exec(f"""
                                CREATE TABLE IF NOT EXISTS tooth_table (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                basics_date TEXT,
                                basics_time TEXT
                                )"""):
            logger.error(f"Error creating table: tooth_table", self.query.lastError().text())
    
    def insert_into_tooth_table(self,
                                basics_date: str,
                                basics_time: str) -> None:
        """
        Inserts a new record into the tooth_table with the provided date and time.

        Args:
            basics_date (str): The date to be inserted into the tooth_table.
            basics_time (str): The time to be inserted into the tooth_table.

        Raises:
            ValueError: If there is a mismatch between the number of placeholders in the SQL query and the number of bind values.
            Exception: For any other exceptions that occur during the execution of the query.

        Logs:
            Error messages are logged if there is an issue with the insertion process.
        """
        
        sql: str = f"""INSERT INTO tooth_table(basics_date, basics_time) VALUES (?, ?)"""
        
        bind_values: List[Union[str, bool]] = [basics_date, basics_time,
                                               ]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: tooth_table Expected {sql.count('?')}
                            bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: tooth_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError tooth_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: tooth_table {e}", exc_info=True)
    
    # SLEEP TIMES TABLE 
    def setup_sleep_table(self):
        """
        Sets up the sleep_table in the database if it does not already exist.

        The table includes the following columns:
        - id: INTEGER PRIMARY KEY AUTOINCREMENT
        - sleep_date: TEXT
        - time_asleep: TEXT
        - time_awake: TEXT

        If the table creation fails, an error message is logged.

        Returns:
            None
        """
        if not self.query.exec(f"""
                CREATE TABLE IF NOT EXISTS sleep_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sleep_date TEXT,
                time_asleep TEXT,
                time_awake TEXT
                )"""):
            logger.error(f"Error creating table: sleep_table", self.query.lastError().text())
    
    def insert_into_sleep_table(self, sleep_date, time_asleep, time_awake):
        """
        Inserts a record into the sleep_table with the provided sleep date, time asleep, and time awake.

        Args:
            sleep_date (str): The date of sleep in the format 'YYYY-MM-DD'.
            time_asleep (str): The time the user fell asleep in the format 'HH:MM:SS'.
            time_awake (str): The time the user woke up in the format 'HH:MM:SS'.

        Raises:
            ValueError: If the number of bind values does not match the number of placeholders in the SQL statement.
            Exception: For any other errors that occur during the execution of the query.

        Logs:
            Error messages are logged if there is an issue with the query execution or if a ValueError is raised.
        """
        sql = f"""INSERT INTO sleep_table(sleep_date, time_asleep, time_awake) VALUES (?, ?, ?)"""
        bind_values = [sleep_date, time_asleep, time_awake]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(
                    f"Mismatch: sleep_table Expected {sql.count('?')} bind values, got "
                    f"{len(bind_values)}.")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: sleep_table - {self.query.lastError().text()}")
        except ValueError as ve:
            logger.error(f"ValueError sleep_table: {str(ve)}")
        except Exception as e:
            logger.error(f"Error during data insertion: sleep_table", str(e))
    
    # -:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-
    # BASICS table
    # -:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-
    def setup_total_hours_slept_table(self):
        """
        Sets up the 'total_hours_slept_table' in the database if it does not already exist.

        The table includes the following columns:
        - id: An integer primary key that autoincrements.
        - sleep_date: A text field representing the date of sleep.
        - total_hours_slept: A text field representing the total hours slept.

        Logs an error message if the table creation fails.
        """
        if not self.query.exec(f"""
                CREATE TABLE IF NOT EXISTS total_hours_slept_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                sleep_date TEXT,
                total_hours_slept TEXT
                )"""):
            logger.error(f"Error creating table: total_hours_slept", self.query.lastError().text())
    
    def insert_into_total_hours_slept_table(self, sleep_date, total_hours_slept):
        """
        Inserts a record into the total_hours_slept_table with the provided sleep date and total hours slept.

        Args:
            sleep_date (str): The date of the sleep record.
            total_hours_slept (float): The total hours slept on the given date.

        Raises:
            ValueError: If the number of bind values does not match the number of placeholders in the SQL statement.
            Exception: If there is an error during the execution of the SQL statement.

        Logs:
            Logs an error message if there is an issue with the data insertion.
        """
        # Prepare the SQL statement
        sql = f"""INSERT INTO total_hours_slept_table(sleep_date, total_hours_slept) VALUES (?, ?)"""
        bind_values = [sleep_date, total_hours_slept]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(
                    f"Mismatch: total_hours_slept Expected {sql.count('?')} bind values, got "
                    f"{len(bind_values)}.")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: total_hours_slept - {self.query.lastError().text()}")
        except ValueError as ve:
            logger.error(f"ValueError total_hours_slept: {str(ve)}")
        except Exception as e:
            logger.error(f"Error during data insertion: total_hours_slept", str(e))
    
    def setup_woke_up_like_table(self):
        """
        Sets up the 'woke_up_like_table' in the database if it does not already exist.

        The table has the following columns:
        - id: INTEGER PRIMARY KEY AUTOINCREMENT
        - sleep_date: TEXT
        - woke_up_like: TEXT

        Logs an error if the table creation fails.
        """
        if not self.query.exec(f"""
                CREATE TABLE IF NOT EXISTS woke_up_like_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sleep_date TEXT,
                woke_up_like INTEGER
                )"""):
            logger.error(f"Error creating table: woke_up_like", self.query.lastError().text())
    
    def insert_woke_up_like_table(self, sleep_date: str, woke_up_like: int):
        """
        Inserts a record into the woke_up_like_table with the given sleep_date and woke_up_like values.

        Args:
            sleep_date (str): The date of sleep in the format 'YYYY-MM-DD'.
            woke_up_like (str): The description of how the person woke up.

        Raises:
            ValueError: If the number of bind values does not match the number of placeholders in the SQL statement.
            Exception: If there is an error during the execution of the SQL statement.

        Logs:
            Error messages are logged if there is an issue with the SQL execution or value binding.
        """
        # Prepare the SQL statement
        sql = f"""INSERT INTO woke_up_like_table(sleep_date, woke_up_like) VALUES (?, ?)"""
        bind_values = [sleep_date, woke_up_like]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(
                    f"Mismatch: woke_up_like Expected {sql.count('?')} bind values, got "
                    f"{len(bind_values)}.")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: woke_up_like - {self.query.lastError().text()}")
        except ValueError as ve:
            logger.error(f"ValueError woke_up_like: {str(ve)}")
        except Exception as e:
            logger.error(f"Error during data insertion: woke_up_like", str(e))
    
    def setup_sleep_quality_table(self):
        if not self.query.exec(f"""
                CREATE TABLE IF NOT EXISTS sleep_quality_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sleep_date TEXT,
                sleep_quality INTEGER
                )"""):
            logger.error(f"Error creating table: sleep_quality", self.query.lastError().text())
    
    def insert_into_sleep_quality_table(self,
                                        sleep_date,
                                        sleep_quality):
        # Prepare the SQL statement
        sql = f"""INSERT INTO sleep_quality_table(sleep_date, sleep_quality) VALUES (?, ?)"""
        bind_values = [sleep_date, sleep_quality]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(
                    f"Mismatch: sleep_quality Expected {sql.count('?')} bind values, got "
                    f"{len(bind_values)}.")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: sleep_quality - {self.query.lastError().text()}")
        except ValueError as ve:
            logger.error(f"ValueError sleep_quality: {str(ve)}")
        except Exception as e:
            logger.error(f"Error during data insertion: sleep_quality", str(e))


def close_database(self):
    try:
        logger.debug("if database is open")
        if self.db.isOpen():
            logger.debug("the database is closed successfully")
            self.db.close()
    except Exception as e:
        logger.exception(f"Error closing database: {e}")
