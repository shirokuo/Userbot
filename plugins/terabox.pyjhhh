# Made by @chillyyyyyyyy
# Thumbnail issue fixed by @NeoMatrix90

from . import ultroid_cmd, eor
import requests
import os
import asyncio
from moviepy.editor import VideoFileClip
from telethon.tl.types import DocumentAttributeVideo

async def get_terabox_video_data(terabox_link):
    url = "https://teraboxdownload.com/api/get-data"
    headers = {
        "Host": "teraboxdownload.com",
        "Connection": "keep-alive",
        "Content-Length": "58",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-platform": '"Android"',
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Origin": "https://teraboxdownload.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://teraboxdownload.com/",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "gads=ID=fa05791ae6af7b1a:T=1720245887:RT=1720245887:S=ALNI_Mayh9QeGn5NFEOPQSPbfa6Wpe7w0A; gpi=UID=00000e755cffdaab:T=1720245887:RT=1720245887:S=ALNI_MaHSOyrwrCIvTdGkyUmB7LafPqQRw; __eoi=ID=7682214e5b4a5a9f:T=1720245887:RT=1720245887:S=AA-AfjYjpeFTC78Fr0svIhgWvt9M"
    }
    payload = {
        "url": terabox_link
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    if 'resolutions' in data[0]:
        return {
            'fast_download': data[0]['resolutions'].get('Fast Download'),
            'hd_video': data[0]['resolutions'].get('HD Video'),
            'thumbnail': data[0].get('thumbnail'),
            'title': data[0].get('title', 'video')
        }
    else:
        return None

async def download_file(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200 and response.content:
            with open(filename, 'wb') as file:
                file.write(response.content)
            return filename
        return None
    except Exception as e:
        print(f"Error downloading file: {e}")
        return None

async def get_video_metadata(filename):
    clip = VideoFileClip(filename)
    metadata = {
        'duration': clip.duration,
        'width': clip.w,
        'height': clip.h
    }
    clip.close()
    return metadata

@ultroid_cmd(pattern="terabox")
async def terabox(event):
    try:
        terabox_link = event.text.split(' ', 1)[1]
        status_message = await eor(event, "Fetching video link from Terabox...")

        video_data = await get_terabox_video_data(terabox_link)
        if not video_data:
            await status_message.edit("Failed to get the video link.")
            return

        fast_download = video_data['fast_download']
        hd_video = video_data['hd_video']
        title = video_data['title']
        thumbnail = video_data['thumbnail']

        await status_message.edit(f"Fast Download Link: {fast_download}\nHD Video Link: {hd_video}\nDownloading the video...")

        video_file = f"{title}.mp4"
        thumb_file = await download_file(thumbnail, "tera-thumb.jpg")

        download_success = await download_file(fast_download, video_file) or await download_file(hd_video, video_file)

        if not download_success:
            await status_message.edit("Failed to download the video from both links.")
            return

        await status_message.edit("Uploading the video...")

        metadata = await get_video_metadata(video_file)

        await event.client.send_file(
            event.chat_id,
            video_file,
            thumb=thumb_file,
            caption="Here is your video from Terabox!",
            attributes=[
                DocumentAttributeVideo(
                    duration=int(metadata.get('duration', 0)),
                    w=metadata.get('width', 0),
                    h=metadata.get('height', 0),
                    supports_streaming=True
                )
            ]
        )

        await asyncio.sleep(4)
        os.remove(video_file)
        os.remove(thumb_file)
        await status_message.delete()
    except Exception as e:
        await status_message.edit(f"An error occurred: {str(e)}")
