
import random
from pyrogram import Client, filters

def generate_card(bin_format):
    card = ""
    for char in bin_format:
        if char == "x":
            card += str(random.randint(0, 9))
        else:
            card += char
    return card

@Client.on_message(filters.command("gen"))
async def card_generator(_, message):
    if len(message.command) < 2:
        return await message.reply("Usage: `/gen 414720xxxxxxxxxx|12|2026|cvv`", quote=True)

    try:
        bin_input = message.text.split(None, 1)[1]
        bin_split = bin_input.split("|")
        if len(bin_split) != 4:
            return await message.reply("Invalid format. Use: `/gen 414720xxxxxxxxxx|12|2026|cvv`", quote=True)

        bin_format, month, year, cvv = bin_split
        result = ""
        for _ in range(10):  # generate 10 cards
            card = generate_card(bin_format)
            result += f"{card}|{month}|{year}|{cvv}\n"

        await message.reply(f"Generated Cards:\n`{result}`", quote=True)
    except Exception as e:
        await message.reply(f"Error: {str(e)}", quote=True)
