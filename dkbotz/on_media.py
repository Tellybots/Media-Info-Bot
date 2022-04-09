# (c) @DKBOTZHELP Or https://github.com/DKBOTZHELP

from datetime import datetime
from sys import version_info
from time import time
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message((filters.video | filters.audio | filters.document) & ~filters.channel & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""
**Should I Show File Information?**

""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Yes", callback_data="showFileInfo"),
              InlineKeyboardButton("No", callback_data="closeMessage")]]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(command(["ping", f"ping@dkbotz"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


#@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
#async def get_uptime(client: Client, message: Message):
#    current_time = datetime.utcnow()
#    uptime_sec = (current_time - START_TIME).total_seconds()
#    uptime = await _human_time_duration(int(uptime_sec))
#    await message.reply_text(
#        "🤖 Bot Status:\n"
#        f"• **Uptime:** `{uptime}`\n"
#        f"• **Start time:** `{START_TIME_ISO}`"
#    )
#
