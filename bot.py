import discord
from discord.ext import commands
import os
from openai import OpenAI
import asyncio
from dotenv import load_dotenv

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")


client = OpenAI(api_key=OPENAI_KEY)

intents = discord.Intents.default()
intents.message_content = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)
user_instructions = (
    "Type !explain followed by the questions about code you have. "
    "You can also paste the code you want the bot to explain for you."
)

@bot.event
async def on_ready():
    target_channel = bot.get_channel(1535669415926956163)
    if target_channel:
        await target_channel.send(f'Hey there. {user_instructions}')
    print(f"Bot logged in successfully as {bot.user}")

@bot.command()
async def explain(ctx, *, prompt: str = None):
    if not prompt:
        await ctx.send("Please provide some code or a question after `!explain`!")
        return

    try:
        developer_instruction = (
            "You are a world-class coding tutor and coding assistant. "
            "Your job is to explain the user's pasted code cleanly, making it easy to read, "
            "step-by-step, explaining what each piece of code does. "
            "Also answer any specific coding questions the 16-year-old has "
            "about the code or how it works."
        )

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "developer", "content": developer_instruction},
                {"role": "user", "content": prompt} # Clean prompt without "!explain"
            ]
        )
        
        # FIX: Changed choices[0] to dot notation to match OpenAI's syntax structure
        ai_response = response.choices[0].message.content
        if len(ai_response) >= 2000:
             for i in range(0, len(ai_response), 2000):
                chunk = ai_response[i : i + 2000]
                await ctx.send(chunk)
        else:
            await ctx.send(ai_response)
        
    except Exception as e:
        print(f"\n❌ An error occurred: {e}\n")
        await ctx.send("Sorry, I ran into an error trying to process that request.")

bot.run(DISCORD_TOKEN)
