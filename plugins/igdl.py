# Nimbus ~ UserBot
# Copyright (C) 2023 NimbusTheCloud
#
# This file is a part of < https://github.com/ufoptg/Nimbus/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/ufoptg/Nimbus/blob/main/LICENSE/>.
"""
 Commands Available
• `{i}instadl <Instagram link>`
   Download Instagram Media

• `{i}igdl <Instagram reel>`
   Download Instagram reel
"""

import os
import uuid
import ffmpeg
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeVideo
from pyUltroid.fns.misc import download_instagram_video
from . import eod, get_string, ultroid_bot, ultroid_cmd, LOGS


async def get_video_attributes(file_path):
    """Extract video attributes using ffmpeg."""
    try:
        probe = ffmpeg.probe(file_path)
        video_stream = next((stream for stream in probe["streams"] if stream["codec_type"] == "video"), None)
        if video_stream:
            return {
                "duration": str(int(float(video_stream["duration"]))),
                "width": str(int(video_stream["width"])),
                "height": str(int(video_stream["height"])),
                "mime_type": f'video/{video_stream["codec_name"]}',
                "title": os.path.basename(file_path),
            }
    except ffmpeg.Error as e:
        LOGS.error(f"FFmpeg error: {e.stderr}")
    return None

async def get_thumbnail(file_path, thumbnail_path):
    """Generate a video thumbnail using ffmpeg."""
    try:
        ffmpeg.input(file_path).output(thumbnail_path, vframes=1).run(capture_stdout=True, capture_stderr=True)
    except ffmpeg.Error as e:
        LOGS.error(f"Error extracting thumbnail: {e.stderr}")

async def get_gallery(msg_id):
    """Retrieve media gallery."""
    msgs = await ultroid_bot.get_messages(5210630997, ids=[*range(msg_id - 9, msg_id + 10)])
    return [msg for msg in msgs if msg and msg.grouped_id == msgs[9].grouped_id]

async def handle_instagram_download(event, command):
    """Handles media download from Instagram."""
    inp = event.pattern_match.group(1)
    chat = "@TopSaverBot"
    msg = await event.edit(get_string("com_1"))

    if not inp:
        await msg.eor("Please provide an Instagram link.", time=4)
        return

    try:
        async with event.client.conversation(chat) as conv:
            await event.client.send_message(chat, inp)
            response = await conv.wait_event(events.NewMessage(incoming=True, from_users=5210630997, func=lambda e: e.media))
            igmedia = response.media
            await event.client.send_read_acknowledge(conv.chat_id)

            media_tag = inp.split("/")[3]
            url_tags = {'p': 'Post', 'reel': 'Reel', 'stories': 'Story'}
            url = f"[{url_tags.get(media_tag, 'Media')}]({inp})"
            captions = get_string("instagram_1").format(url)

    except YouBlockedUserError:
        await msg.eor("Please unblock the bot you're trying to interact with.", time=4)
        return
    except Exception as error:
        LOGS.error(f"Error: {str(error)}")
        await msg.eor("No media found or an error occurred.", time=4)
        return

    unique_id = str(uuid.uuid4())
    ext = ".jpg" if hasattr(igmedia, "photo") else ".mp4" if hasattr(igmedia, "video") else None

    if not ext:
        await msg.eor("Unsupported media type.", time=4)
        return

    file_path = f"resources/downloads/{unique_id}{ext}"
    thumbnail_path = f"resources/downloads/{unique_id}.jpg"

    try:
        await event.client.download_media(igmedia, file=file_path)
        video_attributes = await get_video_attributes(file_path)
        await get_thumbnail(file_path, thumbnail_path)
    except Exception as download_error:
        LOGS.error(f"Download error: {download_error}")
        await msg.eor("Unable to download media.", time=4)
        return

    if video_attributes:
        captions += f"\nDuration: {video_attributes.get('duration', 'N/A')} seconds\nResolution: {video_attributes.get('width', 'N/A')}x{video_attributes.get('height', 'N/A')}"
        try:
            await event.client.send_file(
                event.chat_id,
                file=file_path,
                thumb=thumbnail_path,
                caption=captions,
                supports_streaming=True,
                force_document=False,
                attributes=[DocumentAttributeVideo(duration=int(video_attributes['duration']), w=int(video_attributes['width']), h=int(video_attributes['height']), supports_streaming=True)]
            )
        except Exception as send_error:
            LOGS.error(f"Send file error: {send_error}")
            await msg.eor("Unable to send media.", time=4)
        finally:
            os.remove(file_path)
            os.remove(thumbnail_path)
            await msg.delete()

@ultroid_cmd(pattern="instadl ?(.*)$")
async def instagram_instadl(event):
    """Download Instagram post or story."""
    await handle_instagram_download(event, "instadl")

@ultroid_cmd(pattern="igdl(?: |$)(.*)")
async def instagram_ig(event):
    """Download Instagram media using pyUltroid."""
    matched = event.pattern_match.group(1).strip()
    msg = await event.eor(get_string("udl_4"))

    if not matched:
        await msg.eor(get_string("udl_5"), time=5)
    else:
        try:
            filename = await download_instagram_video(matched, event)
            video_attributes = await get_video_attributes(filename)

            url = f"[Media]({matched})"
            captions = get_string("instagram_1").format(url)
            
            if video_attributes:
                captions += (
                    f"\nDuration: {video_attributes.get('duration', 'N/A')} seconds"
                    f"\nResolution: {video_attributes.get('width', 'N/A')}x{video_attributes.get('height', 'N/A')}"
                )

            await msg.eor(f"Uploading {filename}. . .")
            await event.client.send_file(
                event.chat_id,
                file=filename,
                caption=captions,
                supports_streaming=True,
                attributes=[
                    DocumentAttributeVideo(
                        duration=int(video_attributes.get("duration", 0)),
                        w=int(video_attributes.get("width", 0)),
                        h=int(video_attributes.get("height", 0)),
                        supports_streaming=True
                    )
                ]
            )
            os.remove(filename)
            await msg.delete()

        except Exception as e:
            LOGS.error(f"Error downloading Instagram video: {e}")
            await msg.eor("Unable to download the video.", time=4)

@ultroid_cmd(pattern="igdl(.*)$")
async def demn(ult):
    input = ult.pattern_match.group(1)
    chat = "@igdlxsajal_bot"
    await ult.edit("Please Wait")
    async with ult.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=5954491348))
            await ult.client.send_message(chat, f"{input}")
            response = await response
        except YouBlockedUserError:
            await ult.reply("Boss! Please Unblock @igdlxsajal_bot")    
            return
        x = response.text
        z = x.split("\n")[(len(x.split("\n")))-1]
        await ult.reply(input, file=response.media)

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
