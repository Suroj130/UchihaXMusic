from pyrogram import Client, filters from random import randint

def generate_card(bin_input): if "x" not in bin_input: return "BIN must contain x for random digits."

# Generate random digits for 'x'
card_number = ""
for c in bin_input:
    if c == "x":
        card_number += str(randint(0, 9))
    else:
        card_number += c

mm = str(randint(1, 12)).zfill(2)
yyyy = str(randint(2025, 2030))
cvv = str(randint(100, 999))

return f"{card_number}|{mm}|{yyyy}|{cvv}"

@Client.on_message(filters.command("gen")) async def gen_card_handler(client, message): try: args = message.text.split(" ", 1) if len(args) < 2: await message.reply("Use: /gen 414720xxxxxxxxxx") return

bin_input = args[1].strip()
    generated = generate_card(bin_input)
    await message.reply(f"Generated Card:\n`{generated}`")

except Exception as e:
    await message.reply(f"Error: {str(e)}")

