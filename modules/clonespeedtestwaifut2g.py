# Ported From DarkCobra Originally By UNIBORG
#
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}test`
    Test Your Server Speed.

"""
import html

from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from . import ultroid_cmd

from datetime import datetime

import speedtest

from . import *


@ultroid_cmd(pattern="test ?(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    as_document = None
    if input_str == "image":
        as_document = False
    elif input_str == "file":
        as_document = True
    xx = await event.eor("`Calculating ur Ultroid Server Speed. Please wait!`")
    start = datetime.now()
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    end = datetime.now()
    ms = (end - start).seconds
    response = s.results.dict()
    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    i_s_p = client_infos.get("isp")
    i_s_p_rating = client_infos.get("isprating")
    reply_msg_id = event.message.id
    if event.reply_to_msg_id:
        reply_msg_id = event.reply_to_msg_id
    try:
        response = s.results.share()
        speedtest_image = response
        if as_document is None:
            await xx.edit(
                """`Ultroid Server Speed in {} sec`

`Download: {}`
`Upload: {}`
`Ping: {}`
`Internet Service Provider: {}`
`ISP Rating: {}`""".format(
                    ms,
                    humanbytes(download_speed),
                    humanbytes(upload_speed),
                    ping_time,
                    i_s_p,
                    i_s_p_rating,
                )
            )
        else:
            await event.client.send_file(
                event.chat_id,
                speedtest_image,
                caption="**SpeedTest** completed in {} seconds".format(ms),
                force_document=as_document,
                reply_to=reply_msg_id,
                allow_cache=False,
            )
            await event.delete()
    except Exception as exc:  # dc
        await xx.edit(
            """**SpeedTest** completed in {} seconds
Download: {}
Upload: {}
Ping: {}


__With the Following ERRORs__
{}""".format(
                ms,
                humanbytes(download_speed),
                humanbytes(upload_speed),
                ping_time,
                str(exc),
            )
)


import re

from . import *

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+",
)


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, "", inputString)


@ultroid_cmd(
    pattern="waifu ?(.*)",
)
async def waifu(animu):
    xx = await eor(animu, get_string("com_1"))
    # """Creates random anime sticker!"""
    text = animu.pattern_match.group(1)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            await xx.edit(get_string("sts_1"))
            return
    waifus = [32, 33, 37, 40, 41, 42, 58, 20]
    finalcall = "#" + (str(random.choice(waifus)))
    sticcers = await animu.client.inline_query(
        "stickerizerbot",
        f"{finalcall}{(deEmojify(text))}",
    )
    await sticcers[0].click(
        animu.chat_id,
        reply_to=animu.reply_to_msg_id,
        silent=bool(animu.is_reply),
        hide_via=True,
    )
    await xx.delete()


import os
import random

import emoji
from telethon.utils import get_input_document

from . import *

chat = "text2gifBot"


def remove_emoji(string):
    return emoji.get_emoji_regexp().sub("", string)


@ultroid_cmd(pattern="t2g ?(.*)")
async def t2g(e):
    eris = await e.eor("`...`")
    input_args = e.pattern_match.group(1)
    if not input_args:
        input_args = "No Text was Given :(("
    args = remove_emoji(input_args)
    try:
        t2g = await e.client.inline_query(chat, args)
        doc = t2g[random.randrange(0, len(t2g) - 1)]
        try:
            file = await doc.download_media()
            done = await e.client.send_file(
                e.chat_id, file=file, reply_to=e.reply_to_msg_id
            )
            os.remove(file)
        except AttributeError:
            # for files, without write Method
            done = await doc.click(e.chat_id, reply_to=e.reply_to_msg_id)
        await eris.delete()
    except Exception as fn:
        return await eod(eris, f"**ERROR** : `{fn}`")
    await cleargif(done)


async def cleargif(gif_):
    try:
        await ultroid(
            functions.messages.SaveGifRequest(
                id=get_input_document(gif_),
                unsave=True,
            )
        )
    except Exception as E:
        LOGS.info(E)
      
@ultroid_cmd(pattern="clone ?(.*)", fullsudo=True)
async def _(event):
    eve = await event.eor("`Processing...`")
    reply_message = await event.get_reply_message()
    whoiam = await event.client(GetFullUserRequest(ultroid_bot.uid))
    if whoiam.full_user.about:
        mybio = str(ultroid_bot.me.id) + "01"
        udB.set_key(f"{mybio}", whoiam.full_user.about)  # saving bio for revert
    udB.set_key(f"{ultroid_bot.uid}02", whoiam.users[0].first_name)
    if whoiam.users[0].last_name:
        udB.set_key(f"{ultroid_bot.uid}03", whoiam.users[0].last_name)
    replied_user, error_i_a = await get_full_user(event)
    if replied_user is None:
        await eve.edit(str(error_i_a))
        return
    user_id = replied_user.users[0].id
    profile_pic = await event.client.download_profile_photo(user_id)
    first_name = html.escape(replied_user.users[0].first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.users[0].last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮"
    user_bio = replied_user.full_user.about
    await event.client(UpdateProfileRequest(first_name=first_name))
    await event.client(UpdateProfileRequest(last_name=last_name))
    await event.client(UpdateProfileRequest(about=user_bio))
    if profile_pic:
        file = await event.client.upload_file(profile_pic)
        await event.client(UploadProfilePhotoRequest(file))
    await eve.delete()
    await event.client.send_message(
        event.chat_id, f"**I am `{first_name}` from now...**", reply_to=reply_message
    )


@ultroid_cmd(pattern="revert$")
async def _(event):
    name = OWNER_NAME
    ok = ""
    mybio = str(ultroid_bot.me.id) + "01"
    bio = "Error : Bio Lost"
    chc = udB.get_key(mybio)
    if chc:
        bio = chc
    fname = udB.get_key(f"{ultroid_bot.uid}02")
    lname = udB.get_key(f"{ultroid_bot.uid}03")
    if fname:
        name = fname
    if lname:
        ok = lname
    n = 1
    client = event.client
    await client(
        DeletePhotosRequest(await event.client.get_profile_photos("me", limit=n))
    )
    await client(UpdateProfileRequest(about=bio))
    await client(UpdateProfileRequest(first_name=name))
    await client(UpdateProfileRequest(last_name=ok))
    await event.eor("Succesfully reverted to your account back !")
    udB.del_key(f"{ultroid_bot.uid}01")
    udB.del_key(f"{ultroid_bot.uid}02")
    udB.del_key(f"{ultroid_bot.uid}03")


async def get_full_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.forward.sender_id
                    or previous_message.forward.channel_id
                )
            )
            return replied_user, None
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        return replied_user, None
    else:
        input_str = None
        try:
            input_str = event.pattern_match.group(1)
        except IndexError as e:
            return None, e
        if event.message.entities is not None:
            mention_entity = event.message.entities
            probable_user_mention_entity = mention_entity[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            try:
                user_object = await event.client.get_entity(input_str)
                user_id = user_object.id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
        elif event.is_private:
            try:
                user_id = event.chat_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
        else:
            try:
                user_object = await event.client.get_entity(int(input_str))
                user_id = user_object.id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
