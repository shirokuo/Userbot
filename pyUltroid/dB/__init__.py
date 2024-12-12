from .. import run_as_module
import resources
if not run_as_module:
    from ..exceptions import RunningAsFunctionLibError

    raise RunningAsFunctionLibError(
        "You are running 'pyUltroid' as a functions lib, not as run module. You can't access this folder.."
    )

from .. import *
from . import *
DEVLIST = [
    719195224,  # @xditya
    1322549723,  # @danish_00
    1903729401,  # @its_buddhhu
    1303895686,  # @Sipak_OP
    611816596,  # @Arnab431
    1318486004,  # @sppidy
    803243487,  # @hellboi_atul
]

ULTROID_IMAGES = [
    f"https://graph.org/file/{_}.jpg"
    for _ in [
        "cad7038fe82e47f79c609"
        #"ec250c66268b62ee4ade6",
        #"3c25230ae30d246194eba",
        #"b01715a61b9e876c0d45d",
        #"4ceaf720a96a24527ecff",
        #"a96223b574f29f3f0d184",
        #"6e081d339a01cc6190393",
    ]
]

ALIVE_TEXT = [
        "Try taking a bath with Hydrochloric Acid instead of water.",
    "Try this: if you hold your breath underwater for an hour, you can hold it forever.",
    "Go Green! Stop breathing Oxygen.",
    "God is looking for you. You must go to meet him.",
    "give 100%. Now, let's donate your blood.",
    "Try jumping off a hundred story building but you can only do it once.",
    "You should donate your brain seeing as you never use it.",
    "Volunteer for targets in the shooting range.",
    "Headshots are fun. Get yourself one.",
    "You should try swimming with great white sharks.",
    "You should paint yourself red and run a bull marathon.",
    "You can stay underwater for the rest of your life without ever coming back up.",
    "How about you stop breathing for 1 day? That would be great.",
    "Try provoking a tiger when you're both in a cage.",
    "Have you tried shooting yourself 100m up using a cannon.",
    "You should try holding TNT in your mouth and lighting it.",
    "Try playing catch and throw with RDX it's fun.",
    "I heard phogine is poisonous but I guess you don't mind inhaling it for fun.",
    "Launch yourself into space while forgetting about oxygen on Earth.",
    "You should try playing snakes and ladders, with real snakes and no ladders.",
    "Dancing naked on some HT cables.",
    "Active Volcano is the best swimming pool for you.",
    "You should try taking a hot bath in a volcano.",
    "Try to spend one day in a coffin and it will be yours forever.",
    "Hit Uranium with slow-moving neutrons in front of you. This will be valuable experience.",
    "You could be the first person to step on the sun. Good luck.",
]
    
PING_IMAGES = [f"/resources/extras/ping_pic.mp4"]

stickers = [
    "CAADAQADeAIAAm_BZBQh8owdViocCAI",
    "CAADAQADegIAAm_BZBQ6j8GpKtnrSgI",
    "CAADAQADfAIAAm_BZBQpqC84n9JNXgI",
    "CAADAQADfgIAAm_BZBSxLmTyuHvlzgI",
    "CAADAQADgAIAAm_BZBQ3TZaueMkS-gI",
    "CAADAQADggIAAm_BZBTPcbJMorVVsQI",
    "CAADAQADhAIAAm_BZBR3lnMZRdsYxAI",
    "CAADAQADhgIAAm_BZBQGQRx4iaM4pQI",
    "CAADAQADiAIAAm_BZBRRF-cjJi_QywI",
    "CAADAQADigIAAm_BZBQQJwfzkqLM0wI",
    "CAADAQADjAIAAm_BZBQSl5GSAT0viwI",
    "CAADAQADjgIAAm_BZBQ2xU688gfHhQI",
    "CAADAQADkAIAAm_BZBRGuPNgVvkoHQI",
    "CAADAQADpgIAAm_BZBQAAZr0SJ5EKtQC",
    "CAADAQADkgIAAm_BZBTvuxuayqvjhgI",
    "CAADAQADlAIAAm_BZBSMZdWN2Yew1AI",
    "CAADAQADlQIAAm_BZBRXyadiwWGNkwI",
    "CAADAQADmAIAAm_BZBQDoB15A1jS1AI",
    "CAADAQADmgIAAm_BZBTnOLQ8_d72vgI",
    "CAADAQADmwIAAm_BZBTve1kgdG0Y5gI",
    "CAADAQADnAIAAm_BZBQUMyFiylJSqQI",
    "CAADAQADnQIAAm_BZBSMAe2V4pwhNgI",
    "CAADAQADngIAAm_BZBQ06D92QL_vywI",
    "CAADAQADnwIAAm_BZBRw7UAbr6vtEgI",
    "CAADAQADoAIAAm_BZBRkv9DnGPXh_wI",
    "CAADAQADoQIAAm_BZBQwI2NgQdyKlwI",
    "CAADAQADogIAAm_BZBRPHJF3XChVLgI",
    "CAADAQADowIAAm_BZBThpas7rZD6DAI",
    "CAADAQADpAIAAm_BZBQcC2DpZcCw1wI",
    "CAADAQADpQIAAm_BZBQKruTcEU4ntwI",
]


#@call_back("asupan")
async def asupan(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@xcryasupan", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(asupannya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan video asupan.**")
