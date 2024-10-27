

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



@ultroid_cmd(pattern="askold")
async def chatgpt_old(e):
    reply = await e.get_reply_message()
    if not query:
        if reply and reply.text:
            query = reply.message
    if not query:
        return await e.eor("Give a Question to ask from ChatGPT")
    not_pro = await e.eor("Generating answer...")
    payloads = {"query": query}
    try:
        response = await async_search(
            "",
            post=True,
            json=payloads,
            re_json=True,
            headers = {"Content-Type": "application/json"},
        )
        response = response["randydev"].get("message")
        if len(response + query) < 4080:
            to_edit = (
                f"Query:\n~ {query}\n\nChatGPT:\n~ {response}"
            )
            return await not_pro.edit(to_edit, parse_mode="html")
        with BytesIO(response.encode()) as file:
            file.name = "gpt_response.txt"
            await e.client.send_file(
                e.chat_id,
                file,
                caption=f"{query[:1020]}",
                reply_to=e.reply_to_msg_id
            )
        await not_pro.try_delete()
    except Exception as exc:
        LOGS.exception(exc)
        await not_pro.edit(f"Ran into an Error: \n{exc}" )
        
        
@ultroid_cmd(pattern="asko")        
async def chatgpt(client: Client, message: Message):
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
