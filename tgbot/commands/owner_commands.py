# ----- IMPORTING REQUIRED MODULES ----- #

# Importing random to randomly choose a reply from the helper messages dict.
import random

# Importing telegram bot API.
from telebot import TeleBot, util

# Importing telegram API Message object.
from telebot.types import Message

# Importing database commands.
from database import (
    AddGroupToAllowListCommand,
    DeleteGroupCommand,
    GetGroupCommand,
)

# Importing helper messages.
from tgbot.utilities import msgs


# ----- DEFINING INTERFACES ----- #


# Command Functions Protocol.
def command_name(msg: Message, bot: TeleBot) -> None:
    """Implement command"""
    pass


# ----- OWNER OF BOT COMMANDS ----- #


def check(msg: Message, bot: TeleBot) -> None:
    """This function handles the '/check' command."""
    # Replying to the /check command with random choice message from the helper messages dict.
    bot.reply_to(message=msg, text=random.choice(msgs.get("check")))


def echo(msg: Message, bot: TeleBot) -> None:
    """This function handles the '/echo' command."""
    # Replying to the '/echo' command with the message sent.
    bot.reply_to(message=msg, text=f"you just said {msg.text}")


def admin_help(msg: Message, bot: TeleBot) -> None:
    """This function handles the /helpadmin command."""
    bot.reply_to(message=msg, text=msgs.get("help_admins"), parse_mode="markdown")


# ----- GROUP ALLOW LIST CONTROL COMMANDS ----- #


def add_allow_group(msg: Message, bot: TeleBot) -> None:
    """This function handles the /addgroup command."""

    # Getting the group id argument after the command.
    group_id = util.extract_arguments(msg.text)

    # Executing the add group command.
    AddGroupToAllowListCommand(group_id=group_id).execute()

    # Replying to the owner command.
    bot.reply_to(
        message=msg,
        text=f"Added *{group_id}* to the groups allowlist",
        parse_mode="markdown",
    )


def rm_allow_group(msg: Message, bot: TeleBot) -> None:
    """This function handles the /rmgroup command."""

    # Getting the group id argument after the command
    group_id = util.extract_arguments(msg.text)

    # Executing the remove group command
    DeleteGroupCommand(group_id=group_id).execute()

    # Replying to the owner command
    bot.reply_to(
        message=msg,
        text=f"Removed *{group_id}* from the groups allowlist",
        parse_mode="markdown",
    )


def get_allow_group(msg: Message, bot: TeleBot) -> None:
    """This function handles the /getgroups command."""

    # If an argument was given after the command strip it of white space and run query.
    ## with the group id
    if group_id := util.extract_arguments(msg.text).strip():
        # Running the getgroup query with the given id.
        groups = GetGroupCommand(group_id=group_id).execute()
    else:
        # Running the getgroup query, returning all groups in database.
        groups = GetGroupCommand().execute()

    # Extracting the group ids from the query result.
    message = [f"*id:*  {group[0]}" for group in groups]

    # Formatting the message by joining all groups with new line break for readability.
    msg_formatted = "*Groups in the allowlist*: \n \n" + "\n".join(message)

    # Replying to the command with groups id.
    bot.reply_to(message=msg, text=msg_formatted, parse_mode="markdown")
