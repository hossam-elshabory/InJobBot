# ----- IMPORTING REQUIRED MODULES ----- #

# Importing random to randomly choose a reply from the helper messages dict.
import random

# Importing telegram bot API.
from telebot import TeleBot

# Importing telegram API Message object.
from telebot.types import Message

# Importing helper messages.
from tgbot.utilities.chat_helper import msgs


# Command Functions Protocol.
def command_name(msg: Message, bot: TeleBot) -> None:
    """Implement command."""
    pass


# ----- COMMANDS ----- #


def help(msg: Message, bot: TeleBot) -> None:
    """This function handles the /help command."""
    bot.reply_to(
        message=msg,
        text=random.choice(msgs.get("help")),
        disable_web_page_preview=True,
        parse_mode="markdown",
    )


def tips(msg: Message, bot: TeleBot) -> None:
    """This function handles the /tips command."""
    bot.reply_to(
        message=msg,
        text=random.choice(msgs.get("tips")),
        disable_web_page_preview=True,
        parse_mode="markdown",
    )


def source(msg: Message, bot: TeleBot) -> None:
    """This function handles the /source command."""
    bot.reply_to(
        message=msg,
        text=random.choice(msgs.get("source")),
        parse_mode="markdown",
    )
