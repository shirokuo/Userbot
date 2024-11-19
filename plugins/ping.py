import asyncio
import os
import sys
import time
from . import (
    ATRA_COL,
    LOGS,
    OWNER_NAME,
    OWNER_ID,
    ULTROID_IMAGES,
    Button,
    Carbon,
    Telegraph,
    Var,
    allcmds,
    asst,
    bash,
    call_back,
    callback,
    def_logs,
    eor,
    get_string,
    heroku_logs,
    in_pattern,
    inline_pic,
    restart,
    shutdown,
    start_time,
    time_formatter,
    udB,
    ultroid_bot,
    ultroid_cmd,
    ultroid_version,
    updater,
)


@ultroid_cmd(pattern="Ping$", chats=[], type=["official", "assistant"])
async def _(event):
    start = time.time()
    x = await event.reply("Ping")
    end = round((time.time() - start) * 1000)
    uptime = time_formatter((time.time() - start_time) * 1000)
    await x.edit(get_string("kping").format(end, uptime))
