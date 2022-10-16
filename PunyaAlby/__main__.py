# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de
# t.me/ruangdiskusikami & t.me/ruangprojects 

import importlib

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from PunyaAlby import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bots
from PunyaAlby.helpers.misc import heroku

MSG_ON = """
**ALBY-PYROBOT DIAKTIFKAN**📍
      (\︵/) 
　⫺( •ᆺ•)⫹ 
┏━∪ ━━━━━━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alby` **untuk Mengecheck Bot**
┗━━━━━━━━━
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("ruangdiskusikami")
            await bot.join_chat("ruangprojects")
            await bot.join_chat("PYROALBY")
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
            LOGGER("PunyaAlby").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("PunyaAlby").info(f"ALBY-PYROBOT v{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("PunyaAlby").info("Starting ALBY-PYROBOT")
    install()
    heroku()
    LOOP.run_until_complete(main())
