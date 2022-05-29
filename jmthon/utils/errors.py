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
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from jmthon import *
from jmthon.helpers import *
from jmthon.config import Config


# this shit handles errors
def errors_handler(func):
    async def wrapper(errors):
        try:
            await func(errors)
        except BaseException:

            date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            new = {
                'error': str(sys.exc_info()[1]),
                'date': datetime.datetime.now()
            }

            text = "**تقرير خطأ سورس جمثون**\n\n"

            link = "[هنا](https://t.me/JMTHON_Support)"
            text += "يمكنك الابلاغ عن المشكله اذا كنت تريد"
            text += f"- فقط قم بتوجيه الرسالة الى {link}.\n"

            ftext = "\nDisclaimer:\nThis file is uploaded ONLY here,"
            ftext += "\nwe logged only fact of error and date,"
            ftext += "\nwe respect your privacy,"
            ftext += "\nyou may not report this error if you've"
            ftext += "\nany confidential data here, no one will see your data\n\n"

            ftext += "--------BEGIN JMTHON TRACEBACK LOG--------"
            ftext += "\nDate: " + date
            ftext += "\nGroup ID: " + str(errors.chat_id)
            ftext += "\nSender ID: " + str(errors.sender_id)
            ftext += "\n\nEvent Trigger:\n"
            ftext += str(errors.text)
            ftext += "\n\nTraceback info:\n"
            ftext += str(traceback.format_exc())
            ftext += "\n\nError text:\n"
            ftext += str(sys.exc_info()[1])
            ftext += "\n\n--------END JMTHON TRACEBACK LOG--------"

            command = "git log --pretty=format:\"%an: %s\" -5"

            ftext += "\n\n\nLast 5 commits:\n"

            process = await asyncio.create_subprocess_shell(
                command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE)
            stdout, stderr = await process.communicate()
            result = str(stdout.decode().strip()) \
                + str(stderr.decode().strip())

            ftext += result

    return wrapper

# jmthon
