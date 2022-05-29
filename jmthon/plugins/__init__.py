import datetime
import time

from jmthon import *
from jmthon.clients import *
from jmthon.config import Config
from jmthon.helpers import *
from jmthon.utils import *
from jmthon.random_strings import *
from jmthon.version import __jmthon__
from jmthon.sql.gvar_sql import gvarstat
from telethon import version

jmthon_logo = "./jmthon/resources/pics/jmthon_logo.jpg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
jmthon_ver = __jmthon__
tel_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

is_sudo = "True" if gvarstat("SUDO_USERS") else "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"


my_channel = Config.MY_CHANNEL or "JMTHON"
my_group = Config.MY_GROUP or "JMTHON_support"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/JMTHON"
jmthon_channel = f"[قناة السورس]({chnl_link})"
grp_link = "https://t.me/JMTHON_support"
jmthon_grp = f"[مجموعة السورس]({grp_link})"