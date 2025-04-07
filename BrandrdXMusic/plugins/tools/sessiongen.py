import asyncio
from pyrogram import Client, __version__ as ver

API_ID = input("\nআপনার API ID দিন:\n> ")
API_HASH = input("\nআপনার API HASH দিন:\n> ")

print("\n\nটেলিগ্রাম অ্যাকাউন্টের সাথে যুক্ত ফোন নম্বর দিন যখন জিজ্ঞাসা করা হবে।\n\n")

fallen = Client("Fallen", api_id=API_ID, api_hash=API_HASH, in_memory=True)

async def main():
    await fallen.start()
    sess = await fallen.export_session_string()
    txt = f"এটি আপনার Pyrogram {ver} স্ট্রিং সেশন\n\n<code>{sess}</code>\n\nএটি কারো সাথে শেয়ার করবেন না।\n@BRANDED_WORLD-এ যোগ দিতে ভুলবেন না।"
    await fallen.send_message("me", txt)
    print(f"এটি আপনার Pyrogram {ver} স্ট্রিং সেশন\n{sess}\nকপি করতে ডাবল ক্লিক করুন।")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())