import asyncio
import os

from userbot import ALIVE_NAME
from userbot.utils import lightning_cmd, sudo_cmd

PM_IMG = Config.ALIVE_PIC
version = "4.5"
python_version = "3.8.5"
catversion = "3.0"
ALIVE_MSG = Config.ALIVE_MSG or "✮ MY BOT IS RUNNING SUCCESFULLY ✮"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "  ✥ "

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝔅𝔩𝔞𝔠𝔨 𝔲𝔰𝔢𝔯𝔟𝔬𝔱"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)

# Thanks to Sipak bro and Raganork..
# animation Idea by @hopepsycho (Sipakisking)
# Made by @king_of_psycho ....and thanks to @hopepsycho for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/cfc422395273551a0b148.jpg"
file2 = "https://telegra.ph/file/11b72dc7b0c1483f4986e.jpg"
file3 = "https://telegra.ph/file/11b72dc7b0c1483f4986e.jpg"
file4 = "https://telegra.ph/file/11b72dc7b0c1483f4986e.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "** 𝔅𝔩𝔞𝔠𝔨 𝔲𝔰𝔢𝔯𝔟𝔬𝔱 𝙸𝚂 🅾🅽🅻🅸🅽🅴**\n\n"

pm_caption += "✘ About My System ✘\n\n"
pm_caption += "➾ **`ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ`** ☞ 1.17.5\n"
pm_caption += "➾ **`ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ`** ☞ [ᴊᴏɪɴ](https://t.me/kunjappansupportez)\n"
pm_caption += "➾ **`ʟɪᴄᴇɴꜱᴇ`**  ☞ [𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤](https://github.com/hopepsycho)\n"
pm_caption += "➾ **`ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ`** ☞ [𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤](https://github.com/hopepsycho/Black-userbot)\n\n"
pm_caption += "➾ **Spammer Go Away Im His Assitant"
pm_caption += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={ghanti})\n"


@borg.on(lightning_cmd(pattern=r"dalive"))
@borg.on(sudo_cmd(pattern=r"dalive", allow_sudo=True))
async def amireallyalive(yes):
    await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await yes.delete()

    """ For .dalive command, check if the bot is running.  """
    await borg.send_file(yes.chat_id, PM_IMG, caption=pm_caption)
    await yes.delete()
