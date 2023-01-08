# ----- IMPORTING REQUIRED MODULES ----- #

# Importing the TeleBot object for type hinting
from telebot import TeleBot

# Importing the ChatMemberUpdated for type hinting
from telebot.types import ChatMemberUpdated

# Importing the GetGroupCommand to get the allowed group list from the database
from database import GetGroupCommand


def allow_chat(msg: ChatMemberUpdated, bot: TeleBot) -> None:
    """This function handles bot's action when added to new group chat."""

    # Getting the allow groups id's from the database.
    groups = GetGroupCommand().execute()
    # Parsing the id from the tuples [(-1233,), (-4567)].
    allow_list = [group[0] for group in groups]

    # Getting the bot's member statues.
    new = msg.new_chat_member

    # If the bot's member status is member (meaning bot was added to a group)
    ## and this group chat_id is not in the allow list; the bot's leaves the chat.
    if new.status == "member" and str(msg.chat.id) not in allow_list:
        # Bot's leaves the chat.
        bot.leave_chat(msg.chat.id)
