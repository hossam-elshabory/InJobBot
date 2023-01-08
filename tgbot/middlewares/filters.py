# ----- IMPORTING REQUIRED MODULES ----- #

# Importing decouple to get environment variables
from decouple import config

# Importing Customer filter to create admin filter
from telebot.custom_filters import SimpleCustomFilter

# Importing Message object to get user username from it
from telebot.types import Message

from database import GetUserCommand

# ----- GLOBAL VARIABLES ----- #

# Getting the username of the admin from .env file
OWNER = config("OWNER")


class IsOwner(SimpleCustomFilter):
    """Class will check whether the user is admin or creator in group or not."""

    # This key will be used in bot.py => register_message_handler function to check if the user is admin or not
    key = "owner"

    @staticmethod
    def check(msg: Message):
        # Check if the user username against the username in .env file
        return msg.from_user.username == OWNER


class NotSpammer(SimpleCustomFilter):
    """Class will check whether the user is in the spam list ot not."""

    # This key will be used in bot.py => register_message_handler function to check if the user is admin or not
    key: str = "spamfilter"

    @staticmethod
    def check(msg: Message):
        # Getting the user id from the message.
        user_id = str(msg.from_user.id)
        # Getting the user in the database.
        users = GetUserCommand().execute()
        # Extracting the users's id from the database.
        users_list = [user[0] for user in users]

        # Returning if the user is in the blocked users_list or not.
        return user_id not in users_list
