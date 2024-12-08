from telethon import TelegramClient, events
import asyncio
from . import ultroid_bot, asst

@ultroid_bot.on(events.NewMessage(pattern="hello"))
async def start(event):
    await event.reply("Halo! Ketikkan @nama_botmu untuk mencari.")

@ultroid_bot.on(events.InlineQuery)
async def inline_handler(event):
    builder = event.builder
    results = []

    # Proses query pengguna di sini
    query = event.text.lower()
    if query == "hello":
        results.append(builder.article(
            title="Hello!",
            text="World!"
        ))

    await client.send_inline_bot_result(event.chat_id, results, query_id=event.id)

with client:
    client.loop.run_until_complete(client.start())
    client.run_until_disconnected()
    
