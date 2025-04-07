from pyrogram import Client, filters
from pyrogram.types import Message
import random

@Client.on_message(filters.command("gen") & filters.private)
async def card_generator(_, message: Message):
    try:
        args = message.text.split(" ", 1)[1]
        bin_code, month, year, cvv = args.split("|")
        bin_code = bin_code.strip()

        cards = []
        for _ in range(10):
            card = bin_code
            while "x" in card:
                card = card.replace("x", str(random.randint(0, 9)), 1)
            cards.append(f"{card}|{month}|{year}|{cvv}")

        reply_text = "**Generated Cards:**\n" + "\n".join(cards)
        await message.reply(reply_text)
    except:
        await message.reply("**Usage:**\n/gen 414720xxxxxxxxxx|12|2026|cvv", quote=True)