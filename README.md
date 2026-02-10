###🤖 Multi-Platform GitHub Repo Auto Poster

Telegram + Discord | Powered by Python

This project automatically fetches high-quality trending GitHub repositories and posts them to Telegram and Discord channels with rich formatting and preview images.

Built by @akarshxs

🚀 Features

🔍 Fetches GitHub repos using advanced topic streams

🎯 Filters:

⭐ Stars > 300

📅 Recently updated

🖼️ Sends GitHub OpenGraph preview images

📢 Auto-posts to:

Telegram Channel

Discord Channel

♻️ Avoids reposting same repositories

🧠 Smart random selection from:

AI / ML / LLM

Cybersecurity / Hacking

Blockchain / Crypto

Web / Dev / Cloud

Bots / Automation / Discord

Game / XR / Metaverse

🧩 Tech Stack

Python 3.10+

requests

telebot (pyTelegramBotAPI)

discord.py

asyncio

📁 Project Structure
├── main.py
├── posted.json     # Stores already posted repo IDs
├── README.md

⚙️ Setup & Installation
1️⃣ Clone the Repo
git clone https://github.com/akarshxs/github-repo-poster-bot.git
cd github-repo-poster-bot

2️⃣ Install Requirements
pip install requests pyTelegramBotAPI discord.py

3️⃣ Configure Tokens

Edit in main.py:

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TARGET_TG_CHANNEL = "@your_channel"

DISCORD_BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN"
DISCORD_CHANNEL_ID = 123456789012345678

GITHUB_TOKEN = "YOUR_GITHUB_PAT"


⚠️ Never expose real tokens in public repos. Use .env or environment variables in production.

▶️ Run the Bot
python main.py


You should see:

[DISCORD] Logged in as ...
[BOT] Multi-Platform GitHub Repo Poster Running...

📸 What It Posts

Each post includes:

Repo Name

Stream Category

Language

⭐ Stars & Forks

Description

GitHub Link

Preview Image

🛡️ Safety Notes

Don’t commit real API keys.

Use rate limits responsibly.

Follow GitHub, Telegram & Discord ToS.

👤 Author

Akarsh Tripathi
🔗 GitHub → https://github.com/akarshxs

💬 Discord / Telegram Bot Dev | AI | Automation | Cybersecurity

🌟 Support

If you like this project:

⭐ Star the repo
🍴 Fork it
🧠 Contribute ideas
📣 Share it
