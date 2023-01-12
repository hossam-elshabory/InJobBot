# ----- IMPORTING REQUIRED MODULES ----- #

# Importing telegram bot api
from telebot import TeleBot
from telebot.types import Message

# Importing the inline keyboard markup and button to create inline button for the job links
from tgbot import jobs_post_inline_kb


def send_job_posts(
    posts: list[dict], bot: TeleBot, msg: Message = None, channel_id: str = None
) -> None:
    """_summary_ : Loops over the provided job post list and send each post in a separate message.

    Parameters
    ----------
    posts : list[dict]
        _description_ : The list of job posts created by the telegram post creator.
    bot : TeleBot
        _description_
    msg : Message
        _description_ : The Message Object
    channel_id : str, optional
        _description_, by default None : The channel id.
    """

    # Looping over the posts list and sending each post to the user.
    for post in posts:
        bot.send_message(
            chat_id=channel_id or msg.chat.id,
            text=post["job_details"],
            reply_markup=jobs_post_inline_kb(post["job_link"]),
            parse_mode="Markdown",
        )
