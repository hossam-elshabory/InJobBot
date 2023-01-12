# ----- IMPORTING REQUIRED MODULES ----- #

# Importing datetime and timedelta to for time calculations.
from datetime import datetime, timedelta

# Importing the needed database commands
from database import DeleteUserCommand, GetUserCommand


def more_than_hour(time_added: str) -> bool:
    """_summary_ : This function checks if the temporary banned users has been banned for more than an hour and remove them from the block list.

        Parameters
        ----------
        time_added : str
            _description_ : The time the user was added to the block list.
    `
        Returns
        -------
        bool
            _description_ : True if the time_added was more than 1 hour, and False if less than an hour.
    """

    # Predefining the time formate existing in the database.
    time_format = "%Y/%m/%d, %H:%M:%S"

    # Getting the time string from the func parameter and and converting it back to a datetime object.
    time_added_formatted = datetime.strptime(time_added, time_format)

    # Getting the current time, and setting the timedelta difference to an hour.
    current_time, diff = datetime.now(), timedelta(
        hours=1
    )  #! timedelta(minutes=1) <= for testing

    # Calculating the timedelta between the current time and the time the user was blocked
    ## Starting with the 'current_time' because it will always be bigger (in the future).
    delta = current_time - time_added_formatted

    # Checking if the timedelta (diff. between now, and block time) is more than the defined timedelta (1 hour).
    return delta > diff


def database_cleaner() -> None:
    """This function cleans the spammers database."""

    # Querying the user's in the database who are temporary blocked.
    temp_blocked_users = GetUserCommand(block_type="temp").execute()

    # Getting the users id's in the temp_blocked_users if they have been blocked for more than 1 hour.
    users_id = [user[0] for user in temp_blocked_users if more_than_hour(user[2])]

    # Looping over the user's returned list and removing them from the blocked list.
    for user in users_id:
        # Calling the delete user command on the users blocked more than 1 hour.
        DeleteUserCommand(user_id=user).execute()
