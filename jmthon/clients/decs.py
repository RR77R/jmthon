import inspect
import re

from pathlib import Path
from telethon import events

from .session import H2, H3, H4, H5
from jmthon import CMD_LIST, LOAD_PLUG, bot
from jmthon.config import Config
from jmthon.sql.gvar_sql import gvarstat


def jmthon_cmd(
    pattern: str = None,
    allow_sudo: bool = True,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    args["blacklist_chats"] = True
    black_list_chats = list(Config.BL_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    sudo_user = Config.SUDO_USERS

    if pattern is not None:
        global jmthon_reg
        global sudo_reg
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            jmthon_reg = sudo_reg = re.compile(pattern)
        else:
            jmthon_ = "\\" + Config.HANDLER
            sudo_ = "\\" + Config.SUDO_HANDLER
            jmthon_reg = re.compile(jmthon_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = jmthon_ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (jmthon_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
                cmd2 = (
                    (sudo_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd1)
            except BaseException:
                CMD_LIST.update({file_test: [cmd1]})


    def decorator(func):
        if not disable_edited:
            bot.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=jmthon_reg))
        bot.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=jmthon_reg))
        if allow_sudo:
            if not disable_edited:
                bot.add_event_handler(func, events.MessageEdited(**args, from_users=sudo_user, pattern=sudo_reg))
            bot.add_event_handler(func, events.NewMessage(**args, from_users=sudo_user, pattern=sudo_reg))
        if H2:
            if not disable_edited:
                H2.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=jmthon_reg))
            H2.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=jmthon_reg))
        if H3:
            if not disable_edited:
                H3.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=jmthon_reg))
            H3.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=jmthon_reg))
        if H4:
            if not disable_edited:
                H4.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=jmthon_reg))
            H4.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=jmthon_reg))
        if H5:
            if not disable_edited:
                H5.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=jmthon_reg))
            H5.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=jmthon_reg))
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception:
            LOAD_PLUG.update({file_test: [func]})
        return func

    return decorator


def jmthon_handler(
    **args,
):
    def decorator(func):
        bot.add_event_handler(func, events.NewMessage(**args, incoming=True))
        if H2:
            H2.add_event_handler(func, events.NewMessage(**args, incoming=True))
        if H3:
            H3.add_event_handler(func, events.NewMessage(**args, incoming=True))
        if H4:
            H4.add_event_handler(func, events.NewMessage(**args, incoming=True))
        if H5:
            H5.add_event_handler(func, events.NewMessage(**args, incoming=True))
        return func

    return decorator
