# ----- IMPORTING REQUIRED MODULES ----- #

# Importing decouple to get environment variables.
from decouple import config

# Importing telegram bot api, customer filters, and utilities.
from telebot import TeleBot, custom_filters, util

# Importing the channel updater function, to update channel content.
from job_posts import channel_jobs_updater

# Importing partial from functools
from functools import partial

# Importing the database cleaning function.
from database import database_cleaner

# Importing chat handlers, filters and Scheduler.
from tgbot import (
    GroupMessageHandler,
    IsOwner,
    NotSpammer,
    OwnerMessageHandler,
    Scheduler,
    MyChatMember,
    allow_chat,
    SpamMiddleware,
)

# Importing commands.
from tgbot.commands import group_commands as group_cmd
from tgbot.commands import job_commands as job_cmd
from tgbot.commands import owner_commands as owner_cmd

# ----- GLOBAL VARIABLES ----- #

# Getting telegram bot token from .env file.
BOT_TOKEN = config("BOT_TOKEN")

# Getting channel name.
CHANNEL_ID = config("CHANNEL_ID")


# ----- INITIATING OBJECTS ----- #


# Creating the bot object. Increasing the number of threads, and using class based middlewares.
bot = TeleBot(BOT_TOKEN, num_threads=5, use_class_middlewares=True)

# Creating the owner chat handler object and passing the bot instance.
owner_msg_handler = OwnerMessageHandler(bot)
# Creating the group chat handler object and passing the bot instance.
group_msg_handler = GroupMessageHandler(bot)
# Creating the my chat member handler object and passing the bot instance.
my_chat_member_handler = MyChatMember(bot)


# ----- REGISTERING JOB COMMAND HANDLERS  ----- #


def job_commands(
    owner_handler: OwnerMessageHandler, group_handler: GroupMessageHandler
) -> None:
    """_summary_ : This function collects job commands.

    Parameters
    ----------
    owner_handler : OwnerMessageHandler
        _description_ : A messages handler object to register messages in private chat.
    group_handler : GroupMessageHandler
        _description_ A messages handler object to register messages in group chat.
    """
    # /ljobs command in 'Private chat' for bot owner
    owner_handler.message_handler(func=job_cmd.ljobs, commands=["ljobs"])

    # /ljobs command in 'Group chat', with admins filter
    group_handler.message_handler(
        func=job_cmd.ljobs,
        commands=["ljobs"],
        group_admins=True,
    )


# ----- REGISTERING OWNER COMMAND HANDLERS  ----- #


def owner_chat(chat_handler: OwnerMessageHandler) -> None:
    """_summary_ : This function collects the owner chat handlers.

    Parameters
    ----------
    owner_chat : OwnerMessageHandler
        _description_ : A messages handler object to register messages in private chat.
    """

    # /check command in 'Private chat' for bot owner
    chat_handler.message_handler(func=owner_cmd.check, commands=["check"])

    # /echo command in 'Private chat' for bot owner
    chat_handler.message_handler(func=owner_cmd.echo, commands=["echo"])

    # /help command in 'Private chat' for bot owner
    chat_handler.message_handler(func=owner_cmd.admin_help, commands=["help"])

    # /addgroup command in chat
    chat_handler.message_handler(
        func=owner_cmd.add_allow_group,
        commands=["addgroup"],
    )

    # /rmgroup command in chat
    chat_handler.message_handler(
        func=owner_cmd.rm_allow_group,
        commands=["rmgroup"],
    )

    # /getgroup command in chat
    chat_handler.message_handler(
        func=owner_cmd.get_allow_group,
        commands=["getgroup"],
    )


# ----- REGISTERING GROUP COMMAND HANDLERS  ----- #


def group_chat(chat_handler: GroupMessageHandler) -> None:
    """_summary_ : This function collects the group chat handlers.

    Parameters
    ----------
    group_chat : GroupMessageHandler
        _description_ : A messages handler object to register messages in group chat.
    """

    # /tips command in 'Group chat'.
    chat_handler.message_handler(func=group_cmd.tips, commands=["tips"])

    # /help command in 'Group chat'.
    chat_handler.message_handler(func=group_cmd.help, commands=["help"])

    # /source command in 'Group chat'.
    chat_handler.message_handler(func=group_cmd.source, commands=["source"])


# ----- REGISTERING MY CHAT MEMBER HANDLERS  ----- #


def my_chat_member(chat_handler: MyChatMember) -> None:
    """_summary_ : This function collects the bot's chat member handlers.

    Parameters
    ----------
    chat_handler : MyChatMember
        _description_ : A chat member handler to register bot chat.
    """
    # Handles the bot's allowed chat. 'the bot leaves if not in the allow list'.
    chat_handler.my_chat_handler(func=allow_chat)


# ----- SETTING SCHEDULES ----- #


def schedule() -> None:
    """This function collects the created schedules."""
    # Setting the channel_updater scheduler
    ## Every 7 days at 7:00 PM.
    channel_schedule = Scheduler(days_skipped=7, hour="19:00")
    ## Using 'partial' to pass the function with arguments without calling it.
    channel_schedule.set_schedule(partial(channel_jobs_updater, bot))

    # Setting the database_cleaner scheduler
    ## Every 60 minutes (an hour).
    database_cleaner_schedule = Scheduler(minutes=60)
    # Setting the callable function to the database_cleaner.
    database_cleaner_schedule.set_schedule(database_cleaner)

    # Running the channel_updater schedule.
    channel_schedule.run()
    # Running the database_cleaner_schedule schedule.
    database_cleaner_schedule.run()


# ----- SETTING CHAT HANDLERS ----- #


def chat_handlers() -> None:
    """This function collects all chat handlers."""

    # Adding the job commands chat handler for private | group chat.
    job_commands(owner_msg_handler, group_msg_handler)

    # Adding owner chat handlers.
    owner_chat(owner_msg_handler)

    # Adding group chat handlers.
    group_chat(group_msg_handler)

    # Adding my chat member handler..
    my_chat_member(my_chat_member_handler)


# ----- SETTING CHAT FILTERS ----- #


def chat_filters() -> None:
    """This function collects all chat filters."""

    # Adding group admin filters.
    bot.add_custom_filter(custom_filters.IsAdminFilter(bot))
    # Adding owner filter.
    bot.add_custom_filter(IsOwner())
    # Adding spam filter.
    bot.add_custom_filter(NotSpammer())


# ----- SETTING CHAT MIDDLEWARES ----- #


def middlewares() -> None:
    # Setting up the spam middleware.
    bot.setup_middleware(SpamMiddleware(bot=bot, limit=15))


# ----- MAIN FUNCTION CODE ----- #

# main function.
def main() -> None:
    """This function runs all collector functions."""
    # Adding schedule
    schedule()
    # Adding chat handlers.
    chat_handlers()
    # Adding filters
    chat_filters()
    # Setting up middlewares.
    middlewares()
    # Running the bot.
    bot.infinity_polling(allowed_updates=util.update_types)


# Running main.
main()
