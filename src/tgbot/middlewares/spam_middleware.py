# Importing dataclass to create the middleware class and fields for default values.
from dataclasses import dataclass, field

# Importing decouple's config to get the owner's username from the .env file.
from decouple import config

# Importing telebot objects for middleware and type hinting.
from telebot import TeleBot
from telebot.handler_backends import BaseMiddleware, CancelUpdate
from telebot.types import Message

# Importing database commands.
from database.db_commands import AddUserCommand, GetUserCommand

OWNER = config("OWNER")


@dataclass(slots=True)
class SpamMiddleware(BaseMiddleware):
    """_summary_ : This Middleware handles users who spam commands."""

    # Bot instance.
    bot: TeleBot
    # The time limit between messages.
    limit: int
    # Chat update types to look for.
    update_types = ["message"]
    # Dict["user_id": "last date msg was sent"].
    last_time: dict[str, str] = field(default_factory=dict)
    # List of users in the block list database.
    _blocked_users: list = field(default_factory=list)

    @property
    def get_blocked_users(self) -> list:
        """_summary_: This property updates and returns back a list of strings of the blocked users.

        Returns
        -------
        _type_ : list
            _description_ : A list of strings of the blocked users.
        """
        # Querying the database for users.
        users = GetUserCommand().execute()
        # Extracting the users id's from the query result and returning it.
        self._blocked_users = [user[0] for user in users]
        # Returning back an updated list of the users in the database.
        return self._blocked_users

    @staticmethod
    def not_owner(msg: Message) -> bool:
        """_summary_ : This method returns if the user is the owner or not.

        Returns
        -------
        _type_ : bool
            _description_ : Returns True for NOT owner, False for IS owner.
        """
        # True if not Owner, False if Owner.
        return msg.from_user.username != OWNER

    def set_last_time(self, msg: Message) -> None:
        """_summary_ : This method sets user's message date to his id in last_time dict => dict['user_id': 'date of last message sent'].

        Parameters
        ----------
        msg : Message
            _description_ : TeleBot Message Object.
        """
        # Setting the last message date for the user.
        self.last_time[msg.from_user.id] = msg.date

    def is_spamming(self, msg: Message) -> bool:
        """_summary_ : Checks if the time between the last two sent messages by the user exceeds the limit.

        Returns
        -------
        _type_ : bool
            _description_ : Returns True if user is spamming above the limit, False if user is not spamming.
        """
        # True if more than the limit, False if less than the limit.
        return (msg.date - self.last_time[msg.from_user.id]) < self.limit

    def pre_process(self, msg: Message, data):
        """_summary_ : This method handles update requests in chat.

        Parameters
        ----------
        msg : Message
            _description_ : TeleBot Message Object.
        """
        # If the user is in the blocked users list from the database handler will skip.
        if str(msg.from_user.id) in self.get_blocked_users:

            # Cancelling handler
            return CancelUpdate()

        # If the user message starts with '/' AKA. command eg. /tip | /help.
        if msg.text[0] == "/":

            # If the user id is not in the last time dict; then add them.
            if msg.from_user.id not in self.last_time:
                # User is not in a dict, so lets add and cancel this condition.
                self.set_last_time(msg)
                # Exiting the conditional statement
                return

            # If the time between commands user's sent is more than the limit, user gets a warning and gets blocked.
            if self.is_spamming(msg) and self.not_owner(msg):

                # User is flooding, so sending a warning.
                self.bot.reply_to(
                    msg, "You have been blocked for an hour, for spamming too often."
                )

                # Adding the user to the database with a 'temp' block type.
                AddUserCommand(user_id=msg.from_user.id, block_type="temp").execute()

                # Canceling the update
                return CancelUpdate()

        # Adding the last time message data to the last_time dict.
        self.set_last_time(msg)

    def post_process(self, msg: Message, data, exception):
        pass
