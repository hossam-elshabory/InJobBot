# ----- IMPORTING REQUIRED MODULES ----- #

# Importing decouple to grab the channel id from the .env file.
from decouple import config

# Importing TeleBot for Type hinting.
from telebot import TeleBot

# Importing the telegram job post dataclass.
from .job_post_creator import TgJobPost

# Importing the scrapper
from .job_scrapper import LinkedinScrapper

# Importing the send_job_posts function to send posts.
from .job_post_sender import send_job_posts


# Getting the CHANNEL_ID for channel_update from the .env file.
CHANNEL_ID = config("CHANNEL_ID")


def job_scrapper(
    scrapper: LinkedinScrapper, search_params: tuple[str, str] = None
) -> list[dict]:
    """_summary_ : This function creates the linkedin scrapper object and retrieves the formatted data.

    Parameters
    ----------
    scrapper : LinkedinScrapper
        _description_ : The linkedin scrapper object.

    Returns
    -------
    list[dict]
        _description_ : A list of dicts containing the scrapped jobs data for linkedin.
    """
    # Creating the scrapper object.
    scrapper = scrapper()

    # If search parameters were provided unpack them and pass them to the scrapper object.
    if search_params:
        # Setting up the search parameters tuple(job title, location).
        scrapper.set_search_params(*search_params)

    # Starting the scrapping process
    scrapper.scrape_jobs()

    # Retuning the formatted_data attribute contain the scraped formatted data from linkedin.
    return scrapper.formatted_data


def post_creator(data: list[dict], creator: TgJobPost) -> list[dict]:
    """_summary_ : This function creates the telegram job post creator objects to create job posts for the telegram channel.

    Parameters
    ----------
    data : list[dict]
        _description_ : A list of dict containing the jobs data.
    creator : TgJobPost
        _description_ : The telegram job posts creator object.

    Returns
    -------
    list[dict]
        _description_: A list of dict containing the formatted posts ready to send to telegram chat.
    """

    # Creating the telegram job post creator object
    creator = creator()

    # Creating the job post using the 'create_post()' method
    creator.create_posts(data)

    # Retuning the created posts stored in the 'TgJobPost.posts' attribute
    return creator.posts


def jobs_factory(search_params: tuple[str, str] = None) -> list[dict]:
    """_summary_ : This function creates the scrapper object and the post creator objects.

    Returns
    -------
    list[dict]
        _description_ : A list of dict containing the formatted posts ready to send to telegram chat.
    """
    # If search parameters were passed as an argument pass them into the scrapper.
    if search_params:
        # Passing the scrapper to the job_scrapper function with the search parameters if provided.
        jobs = job_scrapper(scrapper=LinkedinScrapper, search_params=search_params)
    else:
        # If no search parameters were provided, only pass the scrapper (will scrap for the default values)
        jobs = job_scrapper(scrapper=LinkedinScrapper)

    # Returning the created posts.
    return post_creator(data=jobs, creator=TgJobPost)


# Job updater function, this function will be called by the schedule to update the job postings in channel
def channel_jobs_updater(bot: TeleBot) -> None:
    """_summary_ : This function updates the job posting in the channel using the CHANNEL_ID variable from .env file

    Parameters
    ----------
    bot : TeleBot
        _description_ : bot instance
    """
    # Creating jobs using the jobs factory
    jobs = jobs_factory()
    # Sending jobs to the channel
    send_job_posts(jobs, bot, channel_id=CHANNEL_ID)
