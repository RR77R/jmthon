import heroku3
import os
import sys
import time

from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger

from jmthon.clients.session import H2, H3, H4, H5, Jmthon, RJMTHON
from jmthon.config import Config


StartTime = time.time()
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))


if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                level=INFO)


LOGS = getLogger(__name__)

bot = Jmthon
tbot = RJMTHON


if not Config.API_HASH:
    LOGS.warning(" تأكد من فار الايبي هاش اولا ")
    quit(1)


if not Config.APP_ID:
    LOGS.warning("تاكد من فار الايبي ايدي اولا")
    quit(1)


if not Config.BOT_TOKEN:
    LOGS.warning("تاكد من فار توكن البوت اولت")
    quit(1)    

if not Config.DB_URI:    
    LOGS.warning("تأكد من فار قاعده البيانات الخاصه بك اولا.")
    quit(1)


if not Config.JMTHON_SESSION:
    LOGS.warning("تاكد من فار سيشن جمثون اولا.")
    quit(1)


try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except Exception:
    HEROKU_APP = None


CMD_LIST = {}
CMD_HELP = {}
CMD_HELP_BOT = {}
CMD_INFO = {}
INT_PLUG = ""
LOAD_PLUG = {}
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
ISAFK = False
AFKREASON = None
SUDO_LIST = {}

#t.me/JMTHON