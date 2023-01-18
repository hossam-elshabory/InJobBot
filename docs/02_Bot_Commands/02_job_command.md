# The job command

## The Code Behind The Command

The core functionality and implementation behind the `/ljobs` command is handled by the `job_posts` modules. 

When the `/ljobs` command is called the `job_post_factory.py` module calls the `job_scrapper.py` module to send a request to LinkedIn jobs with the provided search parameters (job title, location) or the default search parameters ^^*BI Data Analyst, Egypt.*^^ if none was provided. 

Then the returned data is passed to the `TgJobPost` data class in the `job_post_creator.py` module to further parse and format the job data to make it ready for being sent in telegram chat using the `send_job_posts` function in the `job_post_sender.py` module.

****

### The `job_post_factory.py` module

??? abstract "Click to view the `job_post_factory.py` module"
    ::: src.job_posts.job_post_factory


The `job_post_factory` is the factory that handles creating the job posts process, from scrapping and parsing the data, formatting it for telegram messages, to sending it in chat. 

!!! question "How does it work"
    1. It calls the scrapper class `LinkedinScrapper` from the `job_scrapper.py` module.
    2. Passes the returned data from the `LinkedinScrapper` class to the `TgJobPost` class in the `job_post_creator.py` module to extract jobs information and format it for telegram. 
    3. It uses the `send_job_posts` function from the `job_post_sender.py` module to send each created post as a separate message in the telegram chat.

****

### The `job_scrapper.py` module

The `job_scrapper` module contains the `LinkedinScrapper` data class which scrapes and collects job posts, parses, and formats them. 

The `LinkedinScrapper` uses the [requests library](https://pypi.org/project/requests/) to send the request to LinkedIn, and [BeautifulSoap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse the HTML response. 

??? abstract "Click to view the `LinkedinScrapper` data class"
    ::: src.job_posts.job_scrapper.LinkedinScrapper

****

### The `job_post_creator.py` module

The `job_post_creator.py` module contains the `TgJobPost` data class which takes in a dictionary of lists ==(*created by the `LinkedinScrapper` data class*)== containing the **job title**, **company**, **location**, and **job post link**. 

It creates a dictionary of two key:value paris for each job post as the following: `{job_details:str, job_link: str}`.

``` py title="job_post_creator.py" linenums="51" hl_lines="7 8 9 10 13 16"
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
```

!!! note ""
    • The ==**job_details**==: contains the job information as a string.

    • The ==**job_link**==: contains the job post URL on linkedin.

??? abstract "Click to view the `TgJobPost` data class"
    ::: src.job_posts.job_post_creator.TgJobPost

****

### The `job_post_sender.py` module

This module has only one simple function, `send_job_posts`  which takes in the dictionary of list containing the *job details* and *job link* key, value pairs ==*(Created by the [`TgJobPost`](#the-job_post_creatorpy-module) data class)*== and sends each one in a separate message, with the *job_details* as the message body, and the *job_link* as an ^^inline keyboard button^^ directing to the job apply link. 

??? abstract "Click to view the `send_job_posts` function"
    ::: src.job_posts.job_post_sender.send_job_posts

The `send_job_posts` function uses the `jobs_post_inline_kb` function from the keyboards module folder to create the inline keyboard.

??? abstract "Click to view the `jobs_post_inline_kb` function"
    ::: src.tgbot.keyboards.inline.inline_keyboards.jobs_post_inline_kb

****

## Using The Command

The `ljobs` command can be used alone or with arguments *(search parameters)* to scrap LinkedIn jobs for last week posted jobs returning each job in a separate message with the job information and the job link for applying. 

****

### Default Search

If the `/ljobs` command was sent in chat without any ^^arguments or search parameters^^ it will default to searching for ^^BI Data Analyst^^ Roles in ^^Egypt^^ like in the following GIF.

!!! example ""
    <figure markdown>
    ![ljob_command](../assets/bot_commands/job_command.gif){width="500"}
    <figcaption>/ljobs command.</figcaption>
    </figure>

****

### Searching With Arguments

The `/ljob` command also supports custom job search by providing search parameters after the command in chat following the `job title, location` pattern | format as demonstrated in the following GIF.

!!! example ""
    <figure markdown>
    ![ljob_command](../assets/bot_commands/job_command_arg.gif){width="500"}
    <figcaption>/ljobs command with parameters.</figcaption>
    </figure>

!!! warning "Please note that"
    If you don't follow the `job title, location` pattern the bot will through an error telling you
    that this is an invalid search pattern, specifying the correct one to follow.

****

### Search Format | Pattern

The `/ljob` command uses python's [Regex library](https://pypi.org/project/regex/) to verify the provided search parameters using `param_validator` function in the `job_commands.py` module.

The `param_validator` function does the validation using the following pattern.

``` py title="param_validator function"
# Compiling the command valid pattern.
pattern = re.compile(r"\D+,\D+")
```

??? abstract "Click to view the `param_validator` function"
    ::: src.tgbot.commands.job_commands.param_validator


Here's a live example of the bot's behavior when provided with invalid parameters.  

!!! example ""
    <figure markdown>
    ![ljob_command](../assets/bot_commands/job_command_format.gif){width="500"}
    <figcaption>/ljobs command pattern validator.</figcaption>
    </figure>
