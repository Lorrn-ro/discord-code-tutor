# Discord Code Tutor

A Discord bot that explains code using the OpenAI API. Type `!explain`
followed by a code snippet (or a coding question) in any channel the
bot can see, and it replies with a clear, step-by-step explanation.

## Setup

1. Install dependencies:
   pip3 install discord.py openai python-dotenv

2. Create a `.env` file in the project folder with:
   OPENAI_API_KEY=your-openai-key-here
   DISCORD_BOT_TOKEN=your-discord-bot-token-here

3. In the Discord Developer Portal, make sure "Message Content Intent"
   is enabled for your bot, and invite it to a server with the
   necessary permissions (View Channels, Send Messages, Read Message
   History).

## Usage

Run the bot:
   python3 bot.py

In Discord, type:
   !explain <paste your code or question here>

Long responses are automatically split into multiple messages to stay
under Discord's character limit.

## Notes

Requires your own OpenAI API key and Discord bot token. Never commit
your `.env` file — it's excluded via `.gitignore`.
