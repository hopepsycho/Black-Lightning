

import os
from telethon import events, Button, custom
from userbot.thunderconfig import Config

from userbot import ALIVE_NAME, bot 

currentversion = "2.1"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝐤𝐮𝐧𝐣𝐚𝐩𝐩𝐚𝐧"
ASSIS_PIC = os.environ.get("ASSIS_PIC", None)
if ASSIS_PIC is None:
     PM_IMG = "https://telegra.ph/file/cfc422395273551a0b148.jpg"
else:
     PM_IMG = ASSIS_PIC


pm_caption = " ►**ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += "► **SYSTEMS STATS**\n"
pm_caption += "► **Telethon Version:** `1.15.0` \n"
pm_caption += f"► **Assistant Version** : `{currentversion}`\n"
pm_caption += f"► **My Master** : {DEFAULTUSER} \n"
pm_caption += "► **License** : [GNU General Public License v3.0](https://github.com/hopepsycho/Black-userbot/blob/master/LICENSE)\n"
pm_caption += "► **Copyright** : [𝐊𝐔𝐍𝐉𝐀𝐏𝐏𝐀𝐍](GitHub.com/hopepsycho/Black-userbot)\n"
light = [[Button.url("✧Repos✧", "https://github.com/hopepsycho/Black-userbot"), Button.url("✧Support✧", "https://t.me/kunjappansupport")]]
light +=[[custom.Button.inline("✧Help✧", data="gibcmd")]]
@tgbot.on(events.NewMessage(pattern="^/alive" , func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption, buttons=light)
