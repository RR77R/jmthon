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
    await event.edit("hi")
