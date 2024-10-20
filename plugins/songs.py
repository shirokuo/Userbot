from pyUltroid.fns.ytdl import download_yt, get_yt_link
from . import get_string, requests, ultroid_cmd

@ultroid_cmd(
    pattern="s(ong|song|vsong|vsong) ?(.*)",
)
async def download_from_youtube_(event):
    ytd = {
        "prefer_ffmpeg": True,
        "addmetadata": True,
        "geo-bypass": True,
        "nocheckcertificate": True,
        "cookiefile": "cookies.txt",
    }
    opt = event.pattern_match.group(1).strip()
    xx = await event.eor(get_string("com_1"))
    
    if opt in ("ong", "vsong"):
        if opt == "ong":
            ytd["format"] = "bestaudio"
            ytd["outtmpl"] = "%(id)s.m4a"
        else:
            ytd["format"] = "best"
            ytd["outtmpl"] = "%(id)s.mp4"
            ytd["postprocessors"] = [{"key": "FFmpegMetadata"}]
        url = event.pattern_match.group(2)
        if not url:
            return await xx.eor(get_string("youtube_1" if opt == "ong" else "youtube_3"))
        try:
            requests.get(url)
        except BaseException:
            return await xx.eor(get_string("youtube_2" if opt == "ong" else "youtube_4")) 

    elif opt in ("song", "vsong"):
        if opt == "song":
            ytd["format"] = "bestaudio"
            ytd["outtmpl"] = "%(id)s.m4a"
        else:
            ytd["format"] = "best"
            ytd["outtmpl"] = "%(id)s.mp4"
            ytd["postprocessors"] = [{"key": "FFmpegMetadata"}]
        try:
            query = event.text.split(" ", 1)[1]
        except IndexError:
            return await xx.eor(get_string("youtube_5" if opt == "song" else "youtube_7"))
        url = get_yt_link(query)
        if not url:
            return await xx.edit(get_string("unspl_1"))
        await xx.eor(get_string("youtube_6" if opt == "song" else "youtube_8"))

    else:
        return
    await download_yt(xx, url, ytd)
