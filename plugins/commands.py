#!/usr/bin/env python3
# Copyright (C) @vloggerdeven
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils import TG_SUCKS, FIX_TG_SUCKS
@Client.on_message(filters.command("start"))
async def start(bot, message):
    buttons = [
            [
                InlineKeyboardButton('SEARCH HERE', switch_inline_query_current_chat=""),
            ],
            [
                InlineKeyboardButton('UPDATES', url="https://t.me/dk_botx")
            ]
        ]
    if len(message.command) > 1 and  (message.command[1]).startswith("tgsucks"):
        _, vid_id = (message.command[1]).split("_", 1)
        await message.reply("Something went wrong and Blame Telegram for that :(\nI will be sending the trimmed video shortly")
        if TG_SUCKS.get(vid_id):
            video = TG_SUCKS.get(vid_id)
            await message.reply_video(video['file_id'], caption=video['caption'])
        else:
            FIX_TG_SUCKS[vid_id] = True
        return
    
    await message.reply(
        f"**HEY {message.from_user.mention},\nI am an Inline Youtube Trimmer Bot by @DK_BOTx .**\n__You can use me only via inline mode.__\n\nExample: `@YouTubeTrimbot vlogger deven | 1:25:1 1:26:6` or `@YouTubeTrimbot vlogger deven |",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_message(filters.command("help"))
async def help(bot, message):
    await start(bot, message)

@Client.on_message(filters.private & filters.text & ~filters.via_bot)
async def text_msgs(bot, message):
    buttons = [
            [
                InlineKeyboardButton('SEARCH INLINE', switch_inline_query_current_chat=message.text),
            ],
        ]
    await message.reply(
        "HEY , I CAN WORK ONLY VIA INLINE.",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
