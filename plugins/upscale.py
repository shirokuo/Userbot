import cv2
import subprocess
from tqdm import tqdm
import sys
import argparse
import os
import base64
import requests
from . import LOGS, con

try:
    import cv2
except ImportError:
    LOGS.error(f"{file}: OpenCv not Installed.")

import numpy as np

try:
    from PIL import Image
except ImportError:
    Image = None
    LOGS.info(f"{file}: PIL  not Installed.")
from telegraph import upload_file as upf
from telethon.errors.rpcerrorlist import (
    ChatSendMediaForbiddenError,
    MessageDeleteForbiddenError,
)

from . import (
    Redis,
    async_searcher,
    download_file,
    get_string,
    requests,
    udB,
    ultroid_cmd,
)


@ultroid_cmd(pattern="upscale$")
async def enhance_image(event):
    reply_message = await event.get_reply_message()
    if not (reply_message and (reply_message.photo or reply_message.sticker)):
        return await event.eor("Reply to a photo")

    msg = await event.eor("Upscaling image...")
    image = await reply_message.download_media()

    # Read image file into binary data
    with open(image, 'rb') as f:
        image_data = f.read()

    # Encode binary image data to base64
    encoded_image = base64.b64encode(image_data).decode('utf-8')

    # Construct the JSON payload
    payload = {
        "resize_mode": 0,
        "show_extras_results": True,
        "gfpgan_visibility": 0,
        "codeformer_visibility": 0,
        "codeformer_weight": 1,
        "upscaling_resize": 2,
        "upscaler_1": "4xUltrasharpV10",
        "upscaler_2": "R-ESRGAN 4x+",
        "upscale_first": False,
        "image": encoded_image
    }

    # Set up headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic cGljYXRvYXBpOko3XnMxazYqaTJA"
    }

    # Send the POST request
    response = requests.post('http://110.93.223.194:5670/sdapi/v1/extra-single-image', json=payload, headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        # Extract enhanced image data from response
        response_data = response.json()
        enhanced_image_base64 = response_data.get('image')

        # Decode base64 image data
        enhanced_image_binary = base64.b64decode(enhanced_image_base64)

        # Save the enhanced image to a file
        enhanced_image_path = 'upscale_image.jpg'
        with open(enhanced_image_path, 'wb') as img_file:
            img_file.write(enhanced_image_binary)

        # Upload enhanced image both as a file and as a photo
        await event.client.send_file(event.chat_id, enhanced_image_path, reply_to=reply_message)
        await event.client.send_file(event.chat_id, enhanced_image_path, force_document=True, reply_to=reply_message)

        # Clean up files
        os.remove(enhanced_image_path)
        os.remove(image)

        await msg.delete()
    else:
        await msg.edit("Failed to upscale image.")


import cv2
import subprocess
from tqdm import tqdm
import sys
import argparse


@ultroid_cmd(pattern="vupscale$")
async def scale_video(sourcevideopath, upscaledvideopath, scalingresolution):
    videosourcename = sourcevideopath
    sourcevideo = cv2.VideoCapture(videosourcename)
    destvideo = "Upscaled_Video.mp4"
    sourcefps = sourcevideo.get(cv2.CAP_PROP_FPS)
    totalframes = int(sourcevideo.get(cv2.CAP_PROP_FRAME_COUNT))
    format = cv2.VideoWriter_fourcc(*'mp4v')
    newresolution = scalingresolution
    scaledvideo = cv2.VideoWriter(destvideo, format, sourcefps, newresolution)
    print("")
    print("Rescaling...........")
    print("")
    pbar = tqdm(total=totalframes)
    while True:
        ret, frame = sourcevideo.read()
        if ret == True:
            b = cv2.resize(frame,newresolution,fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
            scaledvideo.write(b)
            pbar.update(1)
        else:
            pbar.close()
            break
    sourcevideo.release()
    scaledvideo.release()
    cv2.destroyAllWindows()
    p = subprocess.Popen("ffprobe -show_streams -print_format json " + sourcevideopath, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    streams = p.communicate()[0]
    streams = streams.decode('utf-8')
    if 'audio' in streams.lower():
        print("")
        print("Extracting audio from source video.........")
        print("")
        subprocess.call("ffmpeg -i " + sourcevideopath + " sourceaudio.mp3", shell=True)
        print("")
        print("Merging source audio and upscaled video.........")
        print("")
        subprocess.call("ffmpeg -i " + destvideo + " -i sourceaudio.mp3 -map 0:0 -map 1:0 " + upscaledvideopath, shell=True)
    else:
        print("")
        print("No audio stream found.........")
        print("")

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-i', type=str,
                    metavar='Source video path', required=True,
                    help='Path to source file.')
parser.add_argument('-o', type=str,
                    metavar='Scaled video path', required=True,
                    help='Path to scaled file.')
parser.add_argument('-r', type=int, nargs='+',
                    metavar='Desired video resolution', required=True,
                    help='Desired video output resolution.')
args = parser.parse_args()

if not args.i and not i:
    raise Exception('Missing -i Input option')
if not args.o and not o:
    raise Exception('Missing -o Output option')
if not args.r and not r:
    raise Exception('Missing -r Resolution option')

scale_video(args.i, args.o, tuple(args.r))
