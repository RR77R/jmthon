import asyncio
import datetime
import importlib
import inspect
import logging
import math
import os
import re
import sys
import time
import traceback
from pathlib import Path
from time import gmtime, strftime

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator, InputMessagesFilterDocument

from jmthon import *
from jmthon.clients import *
from jmthon.helpers import *
from jmthon.config import *
from jmthon.utils import *

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from jmthon.config import Config
else:
    if os.path.exists("Config.py"):
        from Config import Development as Config


def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import jmthon.utils

        path = Path(f"jmthon/plugins/{shortname}.py")
        name = "jmthon.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("تم بنجاح تحميل " + shortname)
    else:
        import jmthon.utils

        path = Path(f"jmthon/plugins/{shortname}.py")
        name = "jmthon.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = Jmthon
        mod.H1 = Jmthon
        mod.H2 = H2
        mod.H3 = H3
        mod.H4 = H4
        mod.H5 = H5
        mod.Jmthon = Jmthon
        mod.JMTHON = JMTHON
        mod.tbot = JMTHON
        mod.tgbot = bot.tgbot
        mod.command = command
        mod.CmdHelp = CmdHelp
        mod.client_id = client_id
        mod.logger = logging.getLogger(shortname)
        sys.modules["uniborg.util"] = jmthon.utils
        mod.Config = Config
        mod.borg = bot
        mod.jmthon = bot
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_jmthon = delete_jmthon
        mod.eod = delete_jmthon
        mod.Var = Config
        mod.admin_cmd = admin_cmd
        mod.jmthon_cmd = jmthon_cmd
        mod.sudo_cmd = sudo_cmd
        sys.modules["userbot.utils"] = jmthon.utils
        sys.modules["userbot"] = jmthon
        sys.modules["userbot.events"] = jmthon
        spec.loader.exec_module(mod)
        sys.modules["jmthon.plugins." + shortname] = mod
        LOGS.info("تم بنجاح تحميل " + shortname)


def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"jmthon.plugins.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError


async def plug_channel(client, channel):
    if channel:
        LOGS.info("تم العثور على قناه الملفات.")
        LOGS.info("يتم تحميل ملفات الخارجيه.")
        plugs = await client.get_messages(channel, None, filter=InputMessagesFilterDocument)
        total = int(plugs.total)
        for plugins in range(total):
            plug_id = plugs[plugins].id
            plug_name = plugs[plugins].file.name
            if os.path.exists(f"jmthon/plugins/{plug_name}"):
                return
            downloaded_file_name = await client.download_media(
                await client.get_messages(channel, ids=plug_id),
                "jmthon/plugins/",
            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            try:
                load_module(shortname.replace(".py", ""))
            except Exception as e:
                LOGS.error(str(e))


# jmthon