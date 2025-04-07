import asyncio
from pyrogram import Client

api_id = int(input("Enter your API ID: "))
api_hash = input("Enter your API HASH: ")


async def main():
    async with Client("my_session", api_id=api_id, api_hash=api_hash) as app:
        session_string = await app.export_session_string()
        print("Your session string:")
        print(session_string)

asyncio.run(main())