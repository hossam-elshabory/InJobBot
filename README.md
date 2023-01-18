<p align="center">
  <a href="" rel="noopener">
 <img width=300px height=300px src="src\images\bot_logo.png" alt="Bot logo"></a>
</p>
 
<h3 align="center">InJobBot</h3>
<div align="center">

  ![Status - Active](https://img.shields.io/badge/Status-Active-2ea44f?logo=Cachet&logoColor=green)
  ![Maintained - Yes](https://img.shields.io/badge/Maintained-Yes-2ea44f)
  ![Python - >=3.11](https://img.shields.io/badge/Python->=3.11-blue?logo=Python)
  ![LICENSE - MIT](https://img.shields.io/badge/LICENSE-MIT-yellow)

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
  ![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

  [![InJoBot - Join Telegram Channel](https://img.shields.io/badge/InJoBot-Join_Telegram_Channel-blue?style=for-the-badge&logo=telegram)](https://t.me/itsinjobbot)

</div>

---

# [📄 Official Documentation]() <!-- omit from toc -->

<p align="center"> 🤖 Weekly Posted LinkedIn Jobs In Your Telegram. 🤖
    <br> 
</p>

- [🧐 About ](#-about-)
- [🎥 Demo ](#-demo-)
- [💭 How the bot works ](#-how-the-bot-works-)
- [🎈 Usage ](#-usage-)
  - [Quick Start Guide :](#quick-start-guide-)
- [🚀 Deploying your own bot ](#-deploying-your-own-bot-)
- [⛏️ Built Using ](#️-built-using-)
- [✍️ Authors ](#️-authors-)
- [✅ Todo ](#-todo-)
- [🎉 Acknowledgements ](#-acknowledgements-)

## 🧐 About <a name = "about"></a>
InJobBot automates job searching by scrapping Jobs posted on LinkedIn from the previous week and sends it in a telegram channel on schedule or by demand using a command in chat.

## 🎥 Demo <a name = "demo"></a>
<p align="center">
  <a href="" rel="noopener">
 <img width=500px height=500px src="src\images\example.gif" alt="Working"></a>
</p>

## 💭 How the bot works <a name = "working"></a>

The bot scrapes LinkedIn jobs page and fetches job postings details eg. (Job Title, Company, Location, Job_link) and parses it then sends it in chat with inline buttons below the post for applying.

The bot uses the **requests** library to make the HTTP request to LinkedIn and **BeautifulSoup** to parse the returned request content and extract the job posting details from it.

The bot is written in Python 3.11, other dependencies are available in the requirements.txt

## 🎈 Usage <a name = "usage"></a>

### Quick Start Guide :

<br>

1. Create a bot using BotFather :

To use the bot, You first need to create a telegram bot using
the BotFather, you can follow this Wiki to do so [How to Create A Telegram Bot With BotFather]()

<br>

2. Create a *.env* file in the main directory and add your credentials : 

Create a *.env* file and put the `BOT_TOKEN` you got from the BotFather, and the `CHANNEL_ID` to the channel the bot will post it (channel must be public and **<ins>bot must be an admin</ins>**), and the `OWNER` *(The Owner's Username)*, as the blow image demonstrate.

![env example](src\images\env_file_example.png)

<br>

3. Install prerequisites using the requirements.txt file.
Navigate to the project directory and type the following command in the terminal :

```bash
pip install -r requirements.txt
```

<br>

4. Run the bot :

```bash
python bot.py
```
<br>

5. Type `/help` in chat to view available commands

<p align="center">
  <a href="" rel="noopener">
 <img width=500px height=500px src="src\images\help_command_owner.gif" alt="help command"></a>
</p>

> 🛑View the [documentations]() for more details about the bot's commands and how to add your own.
***

## 🚀 Deploying your own bot <a name = "deployment"></a>
You can deploy the bot after configuring it to any cloud hosting service, it's just like deploying a web app to the cloud.

You can follow this tutorial to host your bot on [Pythonanywhere.](https://www.pythonanywhere.com)
  - https://youtu.be/TOlNSunbfc8

> ⚠ Make sure to install the dependencies on the cloud using `pip install -r requirements.txt` first before running the bot.

## ⛏️ Built Using <a name = "built_using"></a>
+ [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/) - Python Telegram API Wrapper.
+ [requests](https://pypi.org/project/requests/) - Python HTTP library.
+ [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) - Python Screen-scraping library
+ [SQLite](https://www.sqlite.org/about.html) - SQL database engine.

## ✍️ Authors <a name = "authors"></a>
+ [@Hossam](https://github.com/hossam-elshabory) - Idea & Initial work.

## ✅ Todo <a name = "TODO"></a>
- [ ] Make the scrapper asynchronous using [httpx.](https://www.python-httpx.org)
- [ ] Implement [AsyncTeleBot.](https://pytba.readthedocs.io/en/latest/async_version/index.html)
- [ ] Improve the database tables's schema.
- [ ] Improve the Group's allow list commands.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
+ Database command pattern implementations.
  + [Practices of the python pro](https://www.amazon.com/Practices-Python-Pro-Dane-Hillard/dp/1617296082) - Book.
  + [Github REPO](https://github.com/daneah/practices-of-the-python-pro/tree/98bd0a1273d3a3d75f20069cc38d112ea09e6cec/ch10) - Actual code examples from the book. 
+ [How do I insert record only if the record doesn't exist?](https://dba.stackexchange.com/questions/189058/how-do-i-insert-record-only-if-the-record-doesnt-exist) - SQLite INSERT OR IGNORE INTO 
+ [pyTelegramBotAPI Telegram Group Chat](t.me/pyTelegramBotAPI) - Creating the bot.