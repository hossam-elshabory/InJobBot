# ----- IMPORTING REQUIRED MODULES ----- #

# Importing the keyboard objects.
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class InlineKeyboardCreator:
    """This class created inline keyboards."""

    def __init__(self, keyboard: dict[str, str], row_width: int = 1) -> None:
        """_summary_ : This class takes a dict mapping the keys to the button text and the values to the link the button directs to.

        Parameters
        ----------
        keyboard : dict[str, str]
            _description_ : A dict of {text:link}.
        row_width : int
            _description_, by default 1 : The width of the inline keyboard.
        """

        self.kb = keyboard
        self.width = row_width

    def create_kb(self) -> InlineKeyboardMarkup:
        """This Method create the inline keyboard object"""
        # Creating the inline keyboard markup instance, for the job links.
        kb = InlineKeyboardMarkup()

        # Setting up the row width.
        kb.row_width(self.width)

        # Looping over the dict and creating a keyboard for each key:value pair.
        for text, link in self.kb.items():
            kb.add(InlineKeyboardButton(text=text, link=link))

        # Returning the inlinekeyboard.
        return kb


def jobs_post_inline_kb(job_link: str) -> InlineKeyboardMarkup:
    """_summary_ : This function creates the inline keyboard markup for the job links.

    Parameters
    ----------
    job_link : str
        _description_ : job link URL.

    Returns
    -------
    InlineKeyboardMarkup
        _description_ : The inline keyboard markup for the job links.
    """

    # Creating the inline keyboard markup instance, for the job links.
    inline_kb = InlineKeyboardMarkup()

    # Setting the keyboard row width to 1; so the links will be displayed in one row.
    inline_kb.row_width = 1

    inline_kb.add(
        InlineKeyboardButton("👆 Click Here To Apply 👆", url=job_link),
    )

    # Returning the inline keyboard markup.
    return inline_kb
