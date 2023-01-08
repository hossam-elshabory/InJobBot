# ----- IMPORTING REQUIRED MODULES ----- #

# Importing re for regex.
import re

# Importing telegram bot API.
from telebot import TeleBot, util

# Importing telegram API Message object.
from telebot.types import Message

# Importing jobs factory function to create scrap jobs => create job posts.
from job_posts.job_post_factory import jobs_factory

# Importing job posts sender function to loop over created job data and send each with inline keyboard.
from job_posts.job_post_sender import send_job_posts


# ----- DEFINING INTERFACES  ----- #


# Command Functions Protocol
def command_name(msg: Message, bot: TeleBot) -> None:
    """Implement command."""
    pass


# ----- HELPER FUNCTIONS ----- #


def param_validator(parameter: str) -> bool:
    """_summary_ : This function takes in the job command parameter and validates it.

    Parameters
    ----------
    parameter : str
        _description_ : The parameter extracted from the message.

    Returns
    -------
    bool
        _description_ : True if is valid, False it not.
    """
    # Compiling the command valid pattern.
    pattern = re.compile(r"\D+,\D+")

    # lowering the param case and removing spaces.
    params = parameter.lower().replace(" ", "")

    # Checking if passed parameters is valid of not, and returning the result as a bool True | False.
    return bool(re.search(pattern, params))


# ----- JOBS COMMANDS ----- #


def ljobs(msg: Message, bot: TeleBot) -> None:
    """This function handles the '/ljobs' command."""

    # If search were provided:
    # 1- Strip space for string if any.
    # 2- check if the parameters were passed in valid format.
    # 3- If parameters are valid pass them to the scrapper, if not send a message to user.
    if search_params := util.extract_arguments(msg.text).strip():
        # If the parameters are not in valid format send message to user and exit function.
        if not param_validator(search_params):
            bot.reply_to(
                message=msg,
                text=f"*{msg.text}* is not a valid search pattern.\nplease follow this pattern * /ljob job title, location *",
                parse_mode="markdown",
            )
            # Exit function.
            return
        # Splitting the parameters with the ',' and converting them into a tuple.
        search_params = tuple(search_params.split(","))

        # Passing the new search params to create the jobs using the jobs factory function.
        jobs = jobs_factory(search_params)
    else:
        # Creating the jobs using the jobs factory functions.
        jobs = jobs_factory()

    # Looping over the list of created posts and sending each one in a message in chat with 2 inline kb.
    send_job_posts(posts=jobs, bot=bot, msg=msg)
