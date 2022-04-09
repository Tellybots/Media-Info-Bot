# (c) @DKBOTZHELP Or https://github.com/DKBOTZHELP

from pyrogram import types
from dkbotz.file_info import (
    get_media_file_name,
    get_media_file_size,
    get_file_type,
    get_file_attr
)
from dkbotz.humanbytes import humanbytes


@Client.on_callback_query()
async def cb_handlers(c: Client, cb: "types.CallbackQuery"):
    if cb.data == "showFileInfo":
        replied_m = cb.message.reply_to_message
        _file_name = get_media_file_name(replied_m)
        text = f"**File Name:** `{_file_name}`\n\n" \
               f"**File Extension:** `{_file_name.rsplit('.', 1)[-1].upper()}`\n\n" \
               f"**File Type:** `{get_file_type(replied_m).upper()}`\n\n" \
               f"**File Size:** `{humanbytes(get_media_file_size(replied_m))}`\n\n" \
               f"**File MimeType:** `{get_file_attr(replied_m).mime_type}`"
        await cb.message.edit(
            text=text,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=types.InlineKeyboardMarkup(
                [[types.InlineKeyboardButton("Close Message", callback_data="closeMessage")]]
            )
        )
    elif cb.data == "closeMessage":
        await cb.message.delete(True)
