import datetime
import random
import time

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from jmthon.sql.gvar_sql import gvarstat
from . import *

#-------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>• سورس جمثون يعمل بنجاح •</b></i>
<i><b>↼ المالك ⇀</i></b> : 『 <a href='tg://user?id={}'>{}</a> 』
╭──────────────
┣─ <b>» التيليثون ~</b> <i>{}</i>
┣─ <b>» جمثون ~</b> <i>{}</i>
┣─ <b>» الوقت ~</b> <i>{}</i>
┣─ <b>» البنك ~</b> <i>{}</i>
╰──────────────
<b><i>»»» <a href='https://t.me/jmthon'>[ ثناة السورس ]</a> «««</i></b>
"""

msg = """{}\n
<b><i>• حالة البوت / •</b></i>
<b>التيليثون ≈</b>  <i>{}</i>
<b>جمثون ≈</b>  <i>{}</i>
<b>الوقت ≈</b>  <i>{}</i>
"""
#-------------------------------------------------------------------------------

@jmthon_cmd(pattern="فحص$")
async def up(event):
    cid = await client_id(event)
    RAZAN, JMTHON_USER, jmthon_mention = cid[0], cid[1], cid[2]
    start = datetime.datetime.now()
    jasem = await eor(event, "- أنتظر قليلا")
    uptime = await get_time((time.time() - StartTime))
    a = gvarstat("ALIVE_PIC")
    pic_list = []
    if a:
        b = a.split(" ")
        if len(b) >= 1:
            for c in b:
                pic_list.append(c)
        PIC = random.choice(pic_list)
    else:
        PIC = "https://telegra.ph/file/d85083f6bb31ec14d912b.jpg"
    end = datetime.datetime.now()
    ling = (end - start).microseconds / 1000
    omk = ALIVE_TEMP.format(RAZAN, JMTHON_USER, tel_ver, jmthon_ver, uptime, ling)
    await event.client.send_file(event.chat_id, file=PIC, caption=omk, parse_mode="HTML")
    await jasem.delete()
