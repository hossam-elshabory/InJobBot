# The Help And Tips Commands

## The Owner Help Command

If you are the owner of the bot you can send a `/help` command in the private chat with the bot or in a group a bot is in, and the bot will reply with a message containing all the commands you as an (Owner) can use.

!!! example ""
    !!! example ""
    <figure markdown>
    ![ljob_command](../assets/bot_commands/help_command_owner.gif){width="500"}
    <figcaption>owner's /help command.</figcaption>
    </figure>

!!! note 
    The reply to the `/help` command will differ to group admins and normal group members.
    Only the bot's owner set in the [bot configuration .env file](../01_Tutorial%20-%20User%20Guide/03_configuring_bot.md) will get the command list help message.

****

## Editing The Help and Tips Message

You can edit the help and tips message sent to group members in the `chat_helper.py` module located in ==*src/tgbot/utilities/chat_helper.py*.==

``` py title="chat_helper.py" linenums="7" hl_lines="1 5"
    "help": [
        "I search linkedin for *Jobs💼* posted last week and send them in chat.\nI also have some tips for you, send me a /tips command to view them.",
        "I can tell you what *Jobs 💼* posted on linkedin last week.\nYou can send me a /tips command to view some tips.",
    ],
    "tips": [
        "Landing a job could be challenging if you are not well prepared, so, here are some tips:\n\n🔰 _Follow this guide to setup your GitHub profile_. [HERE](https://www.sitepoint.com/github-profile-readme/)\n🔰 Follow this guide to setup your LinkedIn profile. [HERE](https://www.linkedin.com/business/talent/blog/product-tips/linkedin-profile-summaries-that-we-love-and-how-to-boost-your-own)",
        "Finding a job might be difficult if you are not properly prepared, so here are some pointers.\n\n🔰 _Setup your GitHub profile by following this tutorial_. [HERE](https://www.sitepoint.com/github-profile-readme/)\n🔰 To set up your LinkedIn profile, follow this tutorial.[HERE](https://www.linkedin.com/business/talent/blog/product-tips/linkedin-profile-summaries-that-we-love-and-how-to-boost-your-own)",
    ]
```
