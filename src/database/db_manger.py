# ----- IMPORTING REQUIRED MODULES ----- #

# Importing sqlite3 for database creation.
import sqlite3

# Importing Path for type hinting.
from pathlib import Path

# Importing Cursor for type hinting.
from sqlite3 import Cursor


class DatabaseManger:
    """This class manges the connection to the sqlite database."""

    def __init__(self, database_filename: Path) -> None:
        """_summary_ : Initializing a connection with the database.

        Parameters
        ----------
        database_filename : Path
            _description_ : A path to the database file to connect to, if doesn't exist, it will be created.
        """
        self.connection = sqlite3.connect(database_filename, check_same_thread=False)

    def __del__(self) -> None:
        """_summary_ : This method closes the connection with the database."""
        self.connection.close()

    def _execute(self, statement: str, values: tuple[str] = None) -> Cursor:
        """_summary_ : This method executes SQL statements and returns back a Cursor object containing the query result if any.

        Parameters
        ----------
        statement : str
            _description_ : The SQL statement to execute on the database.
        values : tuple[str], optional
            _description_, by default None : Tuples containing the values to replace the placeholders with to prevent sql injection.

        Returns
        -------
        Cursor
            _description_ : A Cursor object containing the result of the query.
        """
        # Opening a connection to the database using a context manger to automatically close when done
        with self.connection:
            # Create the cursor object
            cursor = self.connection.cursor()
            # Executing the received statement
            cursor.execute(statement, values or [])
            # Returning the cursor object to extract returned data if any
            return cursor

    def create_table(self, table_name: str, columns: dict[str, str]) -> None:
        """_summary_ : This method creates a table in the database if the table is note existing.

        Parameters
        ----------
        table_name : str
            _description_ : The name of the table to create.
        columns : dict[str, str]
            _description_ : A dict holding the columns names as a key and their types as the value

        """
        # Creating a list of column followed by their data types from the provided dict
        columns_with_types = [
            f"{column_name} {data_type}" for column_name, data_type in columns.items()
        ]

        # Executing the table creation SQL statement using the provided table name and columns names
        self._execute(
            f"""
                CREATE TABLE IF NOT EXISTS {table_name}
                ({", ".join(columns_with_types)});
            """
        )

    def add(self, table_name: str, data: dict[str, str]) -> None:
        """_summary_ : This method adds data into the database using the 'INSERT INTO' SQL statement.

        Parameters
        ----------
        table_name : str
            _description_ : Table name to perform the statement on.
        data : dict[str, str]
            _description_ : A dict of strings, specifying the columns names and the columns values to be added to the table.
        """
        # Creating placeholders for the provided data
        placeholders = ", ".join("?" * len(data))
        # Getting the columns names from the data: [dict] keys
        column_names = ", ".join(data.keys())
        # Getting the columns values from the data: [dict] values and storing them in a tuple to pass them to the _execute method
        column_values = tuple(data.values())

        # Executing the 'INSERT INTO' statement on the database, ignoring; if records already exists
        self._execute(
            f"""
            INSERT OR IGNORE INTO {table_name}
            ({column_names})
            VALUES ({placeholders})
            """,
            column_values,
        )

    def select(
        self, table_name: str, criteria: dict[str, str] = None, order_by: str = None
    ) -> Cursor:
        """_summary_: : This method selects data from the database using the 'SELECT' SQL statement and returns back  data.

        Parameters
        ----------
        table_name : str
            _description_ : Table name to perform the statement on.
        criteria : dict[str, str], optional
            _description_, by default None : The criteria to use as a filter on the SELECT statement, passed as a dict => {keys(criteria) : values(values)}
        order_by : str, optional
            _description_, by default None : A column name to sort the returned query by, will map to the ORDER BY {order_by}

        Returns
        -------
        Cursor
            _description_ : A Cursor object containing the data back from the database of any.
        """
        # Creating an empty dict if no criteria was provided
        criteria = criteria or {}

        # Creating the query 'SELECT' statement
        query = f"SELECT * FROM {table_name}"

        # If criteria was provided parse it and add placeholders for it
        if criteria:
            # Creating placeholders fro the provided criteria
            placeholders = [f"{column} = ?" for column in criteria.keys()]
            # Joining each statement with 'AND'
            select_criteria = " AND ".join(placeholders)
            # Adding the 'select_criteria' to the query after the 'WHERE' SQL statement
            query += f" WHERE {select_criteria}"

        # If order_by was provided adds in a 'ORDER BY' SQL statement to sort the data
        if order_by:
            # Adding the 'ORDER BY' statement to the query followed by the column name to sort by
            query += f" ORDER BY {order_by}"

        # Executing the query and passing the criteria values to the cursor and returning back the results
        return self._execute(query, tuple(criteria.values()))

    def update(
        self, table_name: str, criteria: dict[str, str], data: dict[str, str]
    ) -> None:
        """_summary_ : This method updates data in the database using the 'UPDATE' statement.

        Parameters
        ----------
        table_name : str
            _description_ : Table name to perform the statement on.
        criteria : dict[str, str]
            _description_ : The criteria to use as a filter on the UPDATE statement, passed as a dict => {keys(criteria) : values(values)}
        data : dict[str, str]
            _description_ : The actual data to update
        """
        # Creating placeholders for the update criteria
        placeholders = [f"{column} = ?" for column in criteria]
        # Joining the placeholders with the AND operator
        update_criteria = " AND ".join(placeholders)
        # Creating placeholders for the update data
        data_placeholders = ", ".join(f"{key} = ?" for key in data)
        # Creating two tuples holding the values to update and the new data to update them with
        values = tuple(data.values()) + tuple(criteria.values())
        # Executing the UPDATE statement
        self._execute(
            f"""
            UPDATE {table_name}
            SET {data_placeholders}
            WHERE {update_criteria};
            """,
            values,
        )

    def delete(self, table_name: str, criteria: dict[str, str]) -> None:
        """_summary_ : This method deletes data from the database using the 'DELETE' statement.

        Parameters
        ----------
        table_name : str
            _description_ : Table name to perform the statement on.
        criteria : dict[str, str]
            _description_ : The criteria to use as a filter on the DELETE statement, passed as a dict => {keys(criteria) : values(values)}
        """
        # Creating placeholders for the provided criteria
        placeholders = [
            f"{column} = ?" for column in criteria
        ]  #! add criteria.keys() if didn't work
        # Joining the created placeholders with AND operator
        delete_criteria = " AND ".join(placeholders)
        # Executing the DELETE statement
        self._execute(
            f"""
            DELETE FROM {table_name}
            WHERE {delete_criteria}
            """,
            tuple(criteria.values()),
        )
