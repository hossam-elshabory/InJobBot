# Importing Abstract base class and abstractmethod to create the interface
from abc import ABC, abstractmethod

# Adding datetime and timezone to add the time the user was added to the database
from datetime import datetime

# Added the database manger (Receiver) to use it in the PersistanceLayer Implementation
from database.db_manger import DatabaseManger

# from db_manger import DatabaseManger


# Creating the Persistance Layer interface
class IPersistenceLayer(ABC):
    """An abstracted interface for the database controller"""

    @abstractmethod
    def add_user(self, data) -> None:
        raise NotImplementedError("Database Controller must implement a create method")

    @abstractmethod
    def add_to_allow_list(self, data) -> None:
        raise NotImplementedError("Database Controller must implement a create method")

    @abstractmethod
    def get_user(self, order_by: str = None) -> list:
        raise NotImplementedError("Database Controller must implement a get method")

    @abstractmethod
    def get_group(self, order_by: str = None) -> list:
        raise NotImplementedError("Database Controller must implement a get method")

    @abstractmethod
    def edit(self, id: str) -> None:
        raise NotImplementedError("Database Controller must implement a edit method")

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError("Database Controller must implement a delete method")


# Creating 'UsersDatabase' as an implementation of the IPersistanceLayer base class
class UsersDatabase(IPersistenceLayer):
    """This class sits between the database commands and the database manger class"""

    def __init__(self) -> None:
        """_summary_ : This creates the 2 tables 'users' and 'allow_list'"""
        # Table name to be created if not existing
        self.table_name = "bot_users"
        # Initiating the data base users
        self.db = DatabaseManger("bot_db.sqlite")

        # Creating the table 'bot_users' in the database
        self.db.create_table(
            self.table_name,
            {
                # "id": "integer primary key autoincrement",
                "user_id": "text primary key not null",
                "block_type": "text not null",
                "date_added": "text not null",
            },
        )
        # Creating the allowlist table
        self.db.create_table(
            "allow_list",
            {
                "group_id": "text primary key not null",
            },
        )

    def add_user(self, user_id: str, block_type: str) -> None:
        """_summary_ : This methods adds users to the database.

        Parameters
        ----------
        user_id : str
            _description_ : user id.
        block_type : str
            _description_ : 'perm' for permanently block | 'temp' fro temporary block
        """
        # Getting the current date to be added as an attribute to the user record
        date = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
        # Added the user to the database
        self.db.add(
            self.table_name,
            {"user_id": user_id, "block_type": block_type, "date_added": date},
        )

    def add_to_allow_list(self, group_id: str) -> None:
        """_summary_ : This methods adds users to the database.

        Parameters
        ----------
        group_id : str
            _description_ : group_id to allow
        """
        # Adds the user to the database
        self.db.add(
            "allow_list",
            {"group_id": group_id},
        )

    def get_user(
        self, user_id: str = None, block_type: str = None, order_by: str = None
    ) -> list:
        """_summary_ : This methods selects users from the database.

        Parameters
        ----------
        user_id : str, optional
            _description_, by default None : user_id to filter by.
        order_by : str, optional
            _description_, by default None : Column name to order the query result by, be default it will be order by the date added.

        Returns
        -------
        list
            _description_ : A list of tuples containing each records
        """
        # If a user_id and a block type were provided adds it to the select criteria.
        if block_type:
            select_criteria = {"block_type": block_type}
        else:
            # If no user_id was provided pass on an empty dict to the criteria parameter
            select_criteria = {"user_id": user_id} if user_id else None

        # Returning the list of records that fitted the query select criteria
        return self.db.select(
            self.table_name, criteria=select_criteria, order_by=order_by
        ).fetchall()

    def get_group(self, group_id: str = None, order_by: str = None) -> list:
        """_summary_ : This methods selects group from the database.

        Parameters
        ----------
        group_id : str, optional
            _description_, by default None : group_id to filter by.
        order_by : str, optional
            _description_, by default None : Column name to order the query result by, be default it will be order by the date added.

        Returns
        -------
        list
            _description_ : A list of tuples containing each records
        """
        # If no group_id was provided pass on an empty dict to the criteria parameter
        select_criteria = {"group_id": group_id} if group_id else None

        # Returning the list of records that fitted the query select criteria
        return self.db.select(
            "allow_list", criteria=select_criteria, order_by=order_by
        ).fetchall()

    def edit(self, user_id: str, block_type: str):
        """_summary_ : This method update the records in the database using the user user_id as a criteria.

        Parameters
        ----------
        user_id : str
            _description_ : user's user_id.
        block_type : str
            _description_ : The block type of the user perm for permanent | temp for temporary
        """
        # Sending the update statement to the database
        self.db.update(
            self.table_name, {"user_id": user_id}, {"block_type": block_type}
        )

    def delete(self, user_id: str):
        """_summary_ : This method deletes user from the database using his user_id as a criteria.

        Parameters
        ----------
        user_id : str
            _description_ : user's user_id.
        """
        # Deleting the user record using his user_id as a filter criteria
        self.db.delete(self.table_name, {"user_id": user_id})

    def delete_group(self, group_id: str):
        """_summary_ : This method deletes group from the database using his group_id as a criteria.

        Parameters
        ----------
        user_id : str
            _description_ : group's id.
        """
        # Deleting the user record using his user_id as a filter criteria
        self.db.delete("allow_list", {"group_id": group_id})
