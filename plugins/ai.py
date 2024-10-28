

import requests
from io import BytesIO
import asyncio
from RyuzakiLib import async_search
import asyncio
import json
import time
from . import ultroid_cmd
import google.generativeai as genai
import requests
from google.api_core.exceptions import InvalidArgument
from pyrogram import Client, filters
from pyrogram.types import Message 
from RyuzakiLib import FaceAI, FullStackDev, GeminiLatest, RendyDevChat


@ultroid_cmd(pattern="asko")        
async def chatgpt(client: Message):
    if len(message.command) > 1:
        prompt = message.text.split(maxsplit=1)[1]
    elif message.reply_to_message:
        prompt = message.reply_to_message.text
    else:
        return await message.reply_text("Give ask from CHATGPT-4O")
    try:
        messager = await chat_message(prompt)
        if len(messager) > 4096:
            with open("chat.txt", "w+", encoding="utf8") as out_file:
                out_file.write(messager)
            await message.reply_document(
                document="chat.txt",
                disable_notification=True
            )
            os.remove("chat.txt")
        else:
            await message.reply_text(messager, reply_to_message_id=ReplyCheck(message))
    except Exception as e:
        LOGS.error(str(e))
        return await message.reply_text(str(e))
