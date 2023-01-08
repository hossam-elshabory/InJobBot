# ----- IMPORTING REQUIRED MODULES ----- #

# Importing the Telebot object for type hinting
# Importing the abstract base class and abstract method to create the chat handler interface
from abc import ABC, abstractmethod

# Importing Callable to type hinting
from typing import Callable

# Importing the TeleBot object
from telebot import TeleBot

# Defining the Message Handler base class
class MessageHandler(ABC):
    """Abstract message handlers class"""

    # Bot instance
    bot: TeleBot

    @abstractmethod
    def message_handler(self):
        """This method implements the register_message_handler functionality"""


class OwnerMessageHandler(MessageHandler):
    """This class handles the messages | commands registration for the owner chat"""

    def __init__(self, bot: TeleBot) -> None:
        """_summary_ : This class register the owner commands and handles his/her messages.

        Parameters
        ----------
        bot : _type_ : TeleBot
            _description_ : bot instance.

        Methods
        -------
        register_message_handler()
            _summary_ : This Method takes in a function and a list of commands, and calls the function when these command are sent in the 'Private chat' from the bot owner.

            __parameters__
            --------------
            func : Callable
                _description_ : The function to be called.
            commands : list[str]
                _description_ : a list of strings specifying the commands for the bot listens for.

            __Example__
            -----------
                >>>  OwnerMessageHandler.message_handler(func=start, commands=['start'])
                >>>  OwnerMessageHandler.message_handler(func=start, commands=['start'], kwargs={command: AddUser()})

        """
        # Bot instance
        self.bot = bot

    def message_handler(self, *, func: Callable, commands: list[str]) -> None:
        """_summary_ : This Method takes in a function and a list of commands, and calls the function when these command are sent in the 'Private chat' from the bot owner.
        Parameters
        ----------
        func : Callable
            _description_ : The function to be called.
        commands : list[str]
            _description_ : a list of strings specifying the commands for the bot listens for.

        Example
        -------
            >>>  OwnerMessageHandler.message_handler(func=start, commands=['start'])
        """
        # Registering the command.
        self.bot.register_message_handler(
            callback=func,  # Command function name from the 'command.py' module.
            commands=commands,  # Command call name in chat.
            pass_bot=True,  # Passing the bot instance into the function.
            owner=True,  # Adding the filter for owner key.
        )


class GroupMessageHandler(MessageHandler):
    """This class handles the messages | commands registration for the group chat."""

    def __init__(self, bot: TeleBot) -> None:
        """_summary_ : This class register the group commands.

        Parameters
        ----------
        bot : _type_ : TeleBot
            _description_ : bot instance.

        Methods
        -------
        register_message_handler()
            _summary_ : This Method takes in a function and a list of commands, and calls the function when these command are sent in the 'Group chat' from members.

            __parameters__
            --------------
            func : Callable
                _description_ : The function to be called.
            commands : list[str]
                _description_ : a list of strings specifying the commands for the bot listens for.
            kwargs : dict, optional
                _description_, by default None : Any key word arguments to pass to the function called.


            __Example__
            -----------
                >>>  GroupMessageHandler.message_handler(func=answerfaq, commands=['faq'])
                >>>  GroupMessageHandler.message_handler(func=answerfaq, commands=['faq'], group_admins=False, spammers_list=spammers)
        """
        # Bot instance
        self.bot = bot

    def message_handler(
        self,
        *,
        func: Callable,
        commands: list[str],
        group_admins: bool = None,
    ):
        """_summary_ : This Method takes in a function and a list of commands, and calls the function when these command are sent in the 'Group chat' from group members.

        Parameters
        ----------
        func : Callable
            _description_ : The function to be called when the command is sent.
        commands : list[str]
            _description_ : A list of strings specifying the commands for the bot listens for.
        group_admins : bool, optional
            _description_, by default False : True for group admins only commands, false for all chat members.

        Example
        -------
            >>>  GroupMessageHandler.register_message_handler(func=answerfaq, commands=['faq'])
            >>>  GroupMessageHandler.register_message_handler(func=answerfaq, commands=['faq'], group_admins=True)
        """
        # Registering the command.
        self.bot.register_message_handler(
            callback=func,  # Command function name from the 'command.py' module.
            commands=commands,  # Command call name in chat.
            chat_types=[
                "group",
                "supergroup",
            ],  # Specifying chat type for this command.
            pass_bot=True,  # Passing the bot instance into the function.
            is_chat_admin=group_admins,  # Check wether user is admin in chat or not.
            spamfilter=True,  # Adding the Not spam filter.
        )
