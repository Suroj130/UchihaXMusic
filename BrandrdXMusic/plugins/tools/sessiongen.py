from pyrogram import Client

api_id = int(input("Enter your API ID: "))
api_hash = input("Enter your API HASH: ")

with Client("my_session", api_id=api_id, api_hash=api_hash) as app:
    print("Your session string:")
    print(app.export_session_string())