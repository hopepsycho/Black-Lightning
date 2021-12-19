# Credits by @Hackintush

import asyncio
import time

from telethon.errors import FloodWaitError
from telethon.tl import functions

from uniborg.util import edit_or_reply, sudo_cmd

from userbot import bot as cipherx 
from userbot.utils import admin_cmd as cipherx_on_cmd 
from userbot import ALIVE_NAME, CMD_HELP

DEL_TIME_OUT = 60
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "вℓα¢к 𝒖𝒔𝒆𝒓𝒃𝒐𝒕"

@cipherx.on(cipherx_on_cmd(pattern="cipher"))
@cipherx.on(sudo_cmd(pattern="cipher", allow_sudo=True))
async def _(event):
    sed = await edit_or_reply(event, "`ᴋᴜɴᴊᴀᴘᴘᴀɴ ɪs ᴀʟɪᴠᴇ ᴏɴʟɪɴᴇ...`")
    if event.fwd_from:
        return
    while True:
        dictionary = {
            "0": "₀",
            "1": "₁",
            "2": "₂",
            "3": "₃",
            "4": "₄",
            "5": "₅",
            "6": "₆",
            "7": "₇",
            "8": "₈",
            "9": "₉",
        }
        HM = time.strftime("%H . %M")
        for key, value in dictionary.items():
            HM = HM.replace(key, value)
        name = f"{DEFAULTUSER} {HM}"
        logger.info(name)

        try:
            await borg(
                functions.account.UpdateProfileRequest(
                    first_name=name
                )
            )

        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)

        await asyncio.sleep(DEL_TIME_OUT)
    await sed.edit("**вℓα¢к 𝒖𝒔𝒆𝒓𝒃𝒐𝒕 ᴀʟɪᴠᴇ ᴏɴ ɪs ᴏɴʟɪɴᴇ**")


CMD_HELP.update(
    {
        "timeprofile": "**TimeProfile**\
\n\n**Syntax : **`.cipher`\
\n**Usage :** Change Profile Name With Current Time"
    }
)
