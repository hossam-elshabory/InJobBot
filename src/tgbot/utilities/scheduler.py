# ----- IMPORTING REQUIRED MODULES ----- #

# Importing time and threading to run the scheduled tasks on a different thread.
import threading
import time

# Importing Callable to type hinting.
from typing import Callable

# Importing the schedule package.
import schedule


class Scheduler:
    """This class creates schedules for updating channel content and cleaning the spammers list."""

    def __init__(
        self, hour: str = None, days_skipped: int = None, minutes: int = None
    ) -> None:
        """_summary_ : This function initiates the scheduler object.

        Parameters
        ----------
        hour : str
            _description_, by default None : The hour to execute the job 'function' at.
        days_skipped : int, optional
            _description_, by default None : Number of days to skip before executing the job 'function'.
        minutes : int, optional
            _description_, by default None : Run the job every ?? minutes.
        """
        self.days_skipped = days_skipped
        self.minutes = minutes
        self.hour = hour

    def set_schedule(self, func: Callable) -> None:
        """_summary_ : This Method set the callable function to execute on schedule.

        Parameters
        ----------
        func : Callable
            _description_ : The function 'job' to execute.
        mints : bool, optional
            _description_, by default False : optional argument for executing every x minutes 'for spam list cleaning'.
        """
        """
        Change before deployment to desired schedule time frame
        For more info check doc: https://schedule.readthedocs.io/en/stable/examples.html
        """
        # Checks if mints Arg is provided or not
        if self.minutes:
            # If self._minutes is not None, set job to be executed every x minute
            schedule.every(self.minutes).minutes.do(func)
        else:
            # If it's None execute the normal schedule for chanel job update
            schedule.every(self.days_skipped).days.at(self.hour).do(func)

    @staticmethod
    def runner() -> None:
        """This Method checks if there is a pending job jobs every 5 seconds."""
        # A while loop to keep checking for pending schedule jobs
        while True:
            # Running pending schedule jobs
            schedule.run_pending()
            # Sleeping for 5 seconds
            time.sleep(5)

    def run(self) -> None:
        """This Method runs the scheduler on a new thread."""
        # Running the schedule runner on a separate thread
        t1 = threading.Thread(target=self.runner)
        # Starting th thread
        t1.start()
