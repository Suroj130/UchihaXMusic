from BrandrdXMusic import app
from pyrogram import filters, enums
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from logging import getLogger
from BrandrdXMusic.utils.database import get_assistant
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageChops

def circle(pfp, size=(500, 500), brightness_factor=1.3):
    pfp = pfp.resize(size).convert("RGBA")
    pfp = ImageEnhance.Brightness(pfp).enhance(brightness_factor)
    mask = Image.new("L", (pfp.size[0]*3, pfp.size[1]*3), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, mask.size[0], mask.size[1]), fill=255)
    mask = mask.resize(pfp.size)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chatname, id, uname, brightness_factor=1.3):
    background = Image.open("BrandrdXMusic/assets/wel2.png")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp, brightness_factor=brightness_factor).resize((635, 635))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype("BrandrdXMusic/assets/font.ttf", size=70)
    draw.text((2999, 450), f'ID: {id}', fill=(255, 255, 255), font=font)
    background.paste(pfp, (255, 323), pfp)
    path = f"downloads/welcome#{id}.png"
    background.save(path)
    return path

# Example usage
welcomepic("file-JF6s4pWSJHCcEvdYFbNCBx", user="User123", chatname="MyChat", id=12345, uname="user123")

@app.on_message(filters.command("welcome") & ~filters.private)
async def auto_state(_, message):
    usage = "**ᴜsᴀɢᴇ:**\n**⦿ /welcome [on|off]**"
    chat_id = message.chat.id
    if len(message.command) == 1:
        return await message.reply_text(usage)

    user = await app.get_chat_member(chat_id, message.from_user.id)
    if user.status not in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
        return await message.reply("**sᴏʀʀʏ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴇɴᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ!**")

    state = message.text.split(None, 1)[1].strip().lower()
    A = await wlcm.find_one(chat_id)
    if state == "off":
        if A:
            await message.reply_text("**ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ !**")
        else:
            await wlcm.add_wlcm(chat_id)
            await message.reply_text(f"**ᴅɪsᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ** {message.chat.title}")
    elif state == "on":
        if not A:
            await message.reply_text("**ᴇɴᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ.**")
        else:
            await wlcm.rm_wlcm(chat_id)
            await message.reply_text(f"**ᴇɴᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ** {message.chat.title}")
    else:
        await message.reply_text(usage)

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_new_member(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    A = await wlcm.find_one(chat_id)
    if A:
        return

    if not member.new_chat_member or member.new_chat_member.status == "kicked":
        return

    user = member.new_chat_member.user
    count = await app.get_chat_members_count(chat_id)
    try:
        pic = await app.download_media(user.photo.big_file_id, file_name=f"pp{user.id}.png")
    except:
        pic = "BrandrdXMusic/assets/upic.png"

    try:
        welcomeimg = welcomepic(pic, user.first_name, member.chat.title, user.id, user.username)
        deep_link = f"tg://openmessage?user_id={user.id}"
        add_link = f"https://t.me/{app.username}?startgroup=true"

        temp.MELCOW[f"welcome-{chat_id}"] = await app.send_photo(
            chat_id,
            photo=welcomeimg,
            caption=f"""
**❅────✦ ᴡᴇʟᴄᴏᴍᴇ ✦────❅**  
  
▰▰▰▰▰▰▰▰▰▰▰▰▰  
**➻ ɴᴀᴍᴇ »** {user.mention}
**➻ ɪᴅ »** `{user.id}`
**➻ ᴜ_ɴᴀᴍᴇ »** @{user.username}
**➻ ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs »** {count}
▰▰▰▰▰▰▰▰▰▰▰▰▰  
  
**❅─────✧❅✦❅✧─────❅**
""",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("๏ ᴠɪᴇᴡ ɴᴇᴡ ᴍᴇᴍʙᴇʀ ๏", url=deep_link)],
                [InlineKeyboardButton("๏ ᴋɪᴅɴᴀᴘ ᴍᴇ ๏", url=add_link)],
            ])
        )
    except Exception as e:
        LOGGER.error(e)