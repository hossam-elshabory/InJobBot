# ----- IMPORTING REQUIRED MODULES ----- #

# Importing protocol for commands interface creation
from typing import Protocol

# Importing the users database persistence layer implementation
from database.persistence import UsersDatabase

# Creating user database as an implementation of the IPersistanceLayer
persistence = UsersDatabase()

# Defining the command interface
class ICommand(Protocol):
    """This protocol abstracts the implementation of the predefined database commands classes"""

    def execute(self):
        """Implement the command execution"""


class AddUserCommand(ICommand):
    """The command adds a new user to the database using the INSERT INTO SQL statement."""

    def __init__(self, *, user_id: str, block_type: str) -> None:
        """_summary_ : This method gets the data to initiate the command to add a user to the database.

        Parameters
        ----------
        user_id : str
            _description_ : User's user_id.
        block_type : str
            _description_ : User's block type (temp | perm).
        """
        # Storing the user's id.
        self.user_id = user_id
        # Lowering the block time string, and stripping it from any leading|tailing space.
        self.block_type = (block_type.lower()).strip()

    def execute(self) -> None:
        """This method executes the 'INSERT INTO' statement."""
        # Calling the add_user method with the user's_id and his/her block type.
        persistence.add_user(self.user_id, self.block_type)
        return True, None


class GetUserCommand(ICommand):
    """This command sends a 'SELECT' query to the database returning with users in it."""

    def __init__(
        self, *, user_id: str = None, block_type: str = None, order_by="date_added"
    ) -> None:
        """_summary_ : This method gets the data to initiate the command to get user from database using user_id as a selection criteria and sort the results back using 'date_added' attribute (columns).

        Parameters
        ----------
        user_id : str, optional
            _description_ : User's user_id.
        order_by : str, optional
            _description_, by default "date_added" : The criteria in which to sort the returned query results.
        """
        # Setting the order_by criteria. By default will sort by date_added
        self.order_by = order_by
        # Setting the user's user_id
        self.user_id = user_id

        # Setting the user's block type
        self.block_type = block_type

    def execute(self) -> list:
        """This method executes the 'SELECT' statement."""
        # Calling the get_user method with user's id, block type, and the order by for sorting.
        return persistence.get_user(
            user_id=self.user_id, block_type=self.block_type, order_by=self.order_by
        )


class EditUserCommand(ICommand):
    """This command edits user's record in the database"""

    def __init__(self, *, user_id: str, block_type: str) -> None:
        """_summary_ : This method gets the data to initiate the command to update user's block_type (perm | temp) records in the database.

        Parameters
        ----------
        user_id : str
            _description_ : User's user_id.
        block_type : str
            _description_ : User's block type (temp | perm).
        """
        # Setting the user's user_id
        self.user_id = user_id
        # Setting the block type (temp | perm)
        self.block_type = block_type

    def execute(self):
        """This method executes the 'UPDATE' statement."""
        # Calling the edit method with the user's id and block type.
        persistence.edit(self.user_id, self.block_type)


class DeleteUserCommand(ICommand):
    """This command deletes user's record from the database."""

    def __init__(self, *, user_id: str) -> None:
        """_summary_ : This method gets the data to initiate the command to delete user from database.

        Parameters
        ----------
        user_id : str
            _description_ : User's user_id.
        """
        self.user_id = user_id

    def execute(self):
        """This method deletes the user from the database using the provided criteria."""
        # Calling the delete method with the user's id.
        persistence.delete(self.user_id)


class AddGroupToAllowListCommand(ICommand):
    """This command adds a group to the allow_list"""

    def __init__(self, *, group_id: str) -> None:
        """_summary_ : This method gets the data to initiate the command to add group to the bot's allow list.

        Parameters
        ----------
        group_id : str
            _description_ : The group_id to allow.
        """
        self.group_id = group_id

    def execute(self) -> None:
        """This method adds group"""
        # Calling the add_to_allow_list with the group's chat_id.
        persistence.add_to_allow_list(self.group_id)


class GetGroupCommand(ICommand):
    """This command sends a 'SELECT' query to the allow_list database returning with group in it."""

    def __init__(self, *, group_id: str = None, order_by="date_added") -> None:
        """_summary_ : This method gets the data to initiate the command to get user from database using group_id as a selection criteria and sort the results back using 'date_added' attribute (columns).

        Parameters
        ----------
        group_id : str
            _description_ : group_id.
        order_by : str, optional
            _description_, by default "date_added" : The criteria in which to sort the returned query results.
        """
        # Setting the order_by criteria. By default will sort by date_added
        self.order_by = order_by
        # Setting the user's group_id
        self.group_id = group_id

    def execute(self) -> list:
        """This method executes the 'SELECT' statement."""
        # Calling the get_group method with the group's chat_id.
        return persistence.get_group(group_id=self.group_id)


class DeleteGroupCommand(ICommand):
    """This command deletes Groups from the database."""

    def __init__(self, *, group_id: str) -> None:
        """_summary_ : This method gets the data to initiate the command to delete group from database.

        Parameters
        ----------
        user_id : str
            _description_ : Group's id.
        """
        self.group_id = group_id

    def execute(self):
        """This method deletes the user from the database using the provided criteria."""
        # Calling the delete_group method with the group's chat_id.
        persistence.delete_group(self.group_id)
