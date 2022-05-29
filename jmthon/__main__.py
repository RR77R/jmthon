import glob
import os
import sys

from pathlib import Path
from telethon import Button, TelegramClient
from telethon.utils import get_peer_id

from jmthon import LOGS, bot, tbot
from jmthon.clients.session import Rr77, H2, H3, H4, H5
from jmthon.config import Config
from jmthon.utils import join_it, load_module, logger_check, start_msg, update_sudo, plug_channel
from jmthon.version import __jmthon__ as jmthonver

hl = Config.HANDLER

JMTHON_PIC = "https://telegra.ph/file/d85083f6bb31ec14d912b.jpg"


async def jmthons(session=None, client=None, session_name="Main"):
    if session:
        LOGS.info(f"••• يتم تشغيل الحسابات [{session_name}] •••")
        try:
            await client.start()
            return 1
        except:
            LOGS.error(f" خطأ في {session_name} تأكد وحاول مجددا")
            return 0
    else:
        return 0


# Load plugins based on config UNLOAD
async def plug_load(path):
    files = glob.glob(path)
    for name in files:
        with open(name) as jmthon:
            path1 = Path(jmthon.name)
            shortname = path1.stem
            if shortname.replace(".py", "") in Config.UNLOAD:
                os.remove(Path(f"jmthon/plugins/{shortname}.py"))
            else:
                load_module(shortname.replace(".py", ""))      


# Final checks after startup
async def jmthon_is_on(total):
    await update_sudo()
    await logger_check(bot)
    await start_msg(tbot, JMTHON_PIC, jmthonver, total)
    await join_it(bot)
    await join_it(H2)
    await join_it(H3)
    await join_it(H4)
    await join_it(H5)


# jmthon starter...
async def start_jmthon():
    try:
        tbot_id = await tbot.get_me()
        Config.BOT_USERNAME = f"@{tbot_id.username}"
        bot.tgbot = tbot
        LOGS.info("••• يتم تشغيل جمثون •••")
        C1 = await jmthons(Config.JMTHON_SESSION, bot, "JMTHON_SESSION")
        C2 = await jmthons(Config.SESSION_2, H2, "SESSION_2")
        C3 = await jmthons(Config.SESSION_3, H3, "SESSION_3")
        C4 = await jmthons(Config.SESSION_4, H4, "SESSION_4")
        C5 = await jmthons(Config.SESSION_5, H5, "SESSION_5")
        await tbot.start()
        total = C1 + C2 + C3 + C4 + C5
        LOGS.info("••• اكتملت عمليه التنصيب •••")
        LOGS.info("••• يتم بدء تنزيل الملفات •••")
        await plug_load("jmthon/plugins/*.py")
        await plug_channel(bot, Config.PLUGIN_CHANNEL)
        LOGS.info("• تم تشغيل سورس جمثون بنجاح  •")
        LOGS.info("للحصول على اخر اخبار و التحديثات الخاصه بالسورس انضم الى القناه  @jmthon")
        LOGS.info(f"» مجموع الحسابات = {str(total)} «")
        await jmthon_is_on(total)
    except Exception as e:
        LOGS.error(f"{str(e)}")
        sys.exit()


bot.loop.run_until_complete(start_jmthon())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        bot.run_until_disconnected()
    except ConnectionError:
        pass


# jmthonbot
