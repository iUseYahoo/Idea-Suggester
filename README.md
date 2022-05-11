# Idea-Suggester
This website allows users to send ideas/suggestions to your discord server and database.

# What is this repoository?
- This repository is a website which interacts with its API to send a suggestion to a discord server. The API (Server) will also add the users IP to a 'logged_users' table inside the database, This IP will be hashed in md5, This is to prevent abuse of the API (Spamming suggestions).

# Downloads and Requirements
### Discord Requirement(s)
- [Discord Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) - (REQUIRED)

### Software Requirements
- [Python](https://www.python.org/downloads/) - (REQUIRED)
- [SQLite DB Browser](https://sqlitebrowser.org/dl/) - (OPTIONAL, If you want to add more words to the database.)

# Python Package Requirements
- [Flask](https://pypi.org/project/Flask/) - (REQUIRED)

# Setup
- 1. Open [config.json](https://github.com/iUseYahoo/Idea-Suggester/blob/main/api/config.json) and set a port and webhook.
- 2. Open [scripts.js at line 4](https://github.com/iUseYahoo/Idea-Suggester/blob/main/scripts.js#L4) and change the IP and Port to the IP you will be using and the port.

# Notes
- The API does not store your IP in an unhashed version or sends the unhashed version to any spaces.
- I hope you like my trash web development skills (Mainly my CSS).
