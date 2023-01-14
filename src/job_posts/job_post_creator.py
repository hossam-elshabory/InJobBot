# ----- IMPORTING REQUIRED MODULES ----- #

# Importing abstract base class, abstract method.
from abc import ABC, abstractmethod

# Importing data class and field for default factory values.
from dataclasses import dataclass, field

# Importing Any for type hinting.
from typing import Any


# Creating the abstract base class for the post creator
class TgPost(ABC):
    """Abstract Telegram post creator class."""

    @abstractmethod
    def create_posts(self, data: Any):
        """This method loop over the data list[dict] and create a post."""


@dataclass(slots=True)
class TgJobPost(TgPost):
    """_summary_ : This data class creates posts from the scrapped data."""

    # This is the template that will be used to create the post.
    post_template: str = (
        "• *Job Title* : {} \n"
        "• *Company* : {} \n"
        "• *Location* : {} \n"
        "• *Job Link* : {} \n"
    )

    # This is a list that will hold the final posts.
    posts: list = field(default_factory=list)

    def create_posts(self, jobs_data: list[dict]) -> list[dict]:
        """_summary_ : This method loop over the jobs_data list and create a post for each job.

        Parameters
        ----------
        jobs_data : list[dict]
            _description_ : This is the list of jobs data that will be used to create the posts.

        Returns
        -------
        list[dict]
            _description_ : A list of dicts that contain 'job_details' and 'job_links' for each jobs.

        """
        # looping over the jobs data list[dict] and creating a [dict] for each job containing the 'job details' and the 'job links'.
        for job in jobs_data:

            # This is a dict that will hold the job details and the job links for each job.
            post = {
                # This key hold the job details formatted for posting using the post_template.
                "job_details": self.post_template.format(
                    job["job_title"],
                    job["job_company"],
                    job["job_location"],
                    # Grab the first apply link for and embed it inside 'APPLY HERE'
                    ## Using Markdown syntax => [Text](Link to embed).
                    f"[ LINK 🔗]({job['apply_link']})",
                ),
                # This key hold the list of apply links for this job.
                "job_link": job["apply_link"],
            }

            # Adding the formatted job into the 'self.posts' list of the class.
            self.posts.append(post)
            #! break <= Uncomment for testing.
