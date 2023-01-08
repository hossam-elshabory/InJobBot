# ----- IMPORTING REQUIRED MODULES ----- #

# Importing the Telebot object for type hinting
# Importing the abstract base class and abstract method to create the chat handler interface
from abc import ABC, abstractmethod

# Importing Callable to type hinting
from typing import Callable

# Importing the TeleBot object
from telebot import TeleBot

# Defining the Message Handler base class
class MyChatHandler(ABC):
    """Abstract message handlers class"""

    # Bot instance
    bot: TeleBot

    @abstractmethod
    def my_chat_handler(self):
        """This method implements the register_my_chat_member_handler functionality"""
        # DOCS:https://pytba.readthedocs.io/en/latest/sync_version/index.html#telebot.TeleBot.register_my_chat_member_handler


class MyChatMember(MyChatHandler):
    """his class handles the bot chat member registration."""

    def __init__(self, bot: TeleBot) -> None:
        """_summary_ : This class register the bot chat member.

        Parameters
        ----------
        bot : TeleBot
            _description_ : Bot instance.

        Methods
        -------
        my_chat_handler()

        _parameters_
        ------------
            func : Callable
                _description_ : The function to be called.

        __Example__ :
        -------------
            >>> MyChatMember(bot).my_chat_handler(func=allowed_chat_func)
        """

        # Bot instance
        self.bot = bot

    def my_chat_handler(self, *, func: Callable) -> None:
        """_summary_ : This Method takes the function to be called on the bot chat member.

        Parameters
        ----------
        func : Callable
            _description_ : The function to be called.

        Example
        -------
            >>> MyChatMember(bot).my_chat_handler(func=allowed_chat_func)

        """
        self.bot.register_my_chat_member_handler(
            callback=func,  # The function that is going to be called.
            pass_bot=True,  # Passing the bot the function.
        )
