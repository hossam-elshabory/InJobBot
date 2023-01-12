<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/FxL5qM0.jpg" alt="Bot logo"></a>
</p>

<h3 align="center">InJobHunter</h3>
<div align="center">

  [![Status](https://img.shields.io/badge/Status-Actice-brightgreen)]()
  [![Python version](https://img.shields.io/badge/Python-v3.11-blue)](https://www.python.org/)
  [![License](https://img.shields.io/badge/License-MIT-blue)]()


  [![BI & Data Jobs - Join Channel](https://img.shields.io/badge/BI_%26_Data_Jobs-Join_Channel-blue?style=for-the-badge&logo=Telegram)](https://t.me/bidajobs)

</div>

---

<p align="center"> 🤖 Weekly Posted Jobs Scrapped From LinkedIn.
    <br> 
</p>

- [🧐 About ](#-about-)
- [🎥 Demo ](#-demo-)
- [💭 How the bot works ](#-how-the-bot-works-)
- [🎈 Usage ](#-usage-)
  - [Quick Start Guide :](#quick-start-guide-)
  - [Prerequisites](#prerequisites)
- [🚀 Deploying your own bot ](#-deploying-your-own-bot-)
- [⛏️ Built Using ](#️-built-using-)
- [✍️ Authors ](#️-authors-)
- [🎉 Acknowledgements ](#-acknowledgements-)



## 🧐 About <a name = "about"></a>
This bot automates job searching by scrapping Jobs posted on LinkedIn from the previous week and sends it in a telegram channel on schedule or by demand using a command.

## 🎥 Demo <a name = "demo"></a>
![Working](images\example.gif)

## 💭 How the bot works <a name = "working"></a>

The bot scrapes this LinkedIn and fetches jobs postings details eg. (Job Title, Company, Location, Job_link) and parses it then posts it on a telegram channel with inline buttons below the post for applying.

The bot uses the **requests** library to make the HTTP request to LinkedIn and **BeautifulSoup** to parse the returned request and extract the job posting details from it.

The bot is written in Python 3.11, other dependencies are available in the requirements.txt

## 🎈 Usage <a name = "usage"></a>

### Quick Start Guide :

<br>

1. Create a bot using BotFather :

To use the bot, You first need to create a telegram bot using
the BotFather, you can follow this Wiki to do so [How to Create A Telegram Bot With BotFather]()

<br>

2. Create a *.env* file in the main directory and add your credentials : 

Create a *.env* file and put the `BOT_TOKEN` you got from the BotFather, and the `CHANNEL_ID` to the channel the bot will post it (channel must be public and bot must be an admin), and the `OWNER` *(The Owner's Username)*, as the blow image demonstrate.

![env example](images\env_file_example.png)

<br>

3. Run the bot :

```bash
python bot.py
```

***

### Prerequisites

You can install the project prerequisites using the requirements.txt file.
Navigate to the project directory and type the following command in the terminal :

```bash
pip install -r requirements.txt
```

## 🚀 Deploying your own bot <a name = "deployment"></a>
To see an example project on how to deploy your bot, please see my own configuration:

+ **Heroku**: https://github.com/kylelobo/Reddit-Bot#deploying_the_bot

## ⛏️ Built Using <a name = "built_using"></a>
+ [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/) - Python Telegram API Wrapper.
+ [requests](https://pypi.org/project/requests/) - Python HTTP library.
+ [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) - Python Screen-scraping library
+ [SQLite](https://www.sqlite.org/about.html) - SQL database engine.

## ✍️ Authors <a name = "authors"></a>
+ [@Hossam](https://github.com/hossam-elshabory) - Idea & Initial work.


## 🎉 Acknowledgements <a name = "acknowledgement"></a>
+ Database command pattern implementations.
  + [Practices of the python pro](https://www.amazon.com/Practices-Python-Pro-Dane-Hillard/dp/1617296082) - Book.
  + [Github REPO](https://github.com/daneah/practices-of-the-python-pro/tree/98bd0a1273d3a3d75f20069cc38d112ea09e6cec/ch10) - Actual code examples from the book. 
+ [How do I insert record only if the record doesn't exist?](https://dba.stackexchange.com/questions/189058/how-do-i-insert-record-only-if-the-record-doesnt-exist) - SQLite INSERT OR IGNORE INTO 
+ [pyTelegramBotAPI Telegram Group Chat](t.me/pyTelegramBotAPI) - Creating the bot.
