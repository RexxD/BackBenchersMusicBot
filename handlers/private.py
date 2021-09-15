from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAELUCJhGiacm9ro5nAJXr_GlzPrpV3UgAACNwIAAkGdiFW9ustLyOBHoiAE")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I'm Private music of @TheRiZoeL For group's voice call. Developed by [ℝ𝚒ℤ𝚘𝚎𝕃](https://t.me/TheRiZoeL).

If you want to add this Bot in your group Contact @TheRiZoeL**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀ℝ𝚒ℤ𝚘𝚎𝕃", url="https://t.me/TheRiZoeL")
                  ],[ 
                    InlineKeyboardButton(
                        "ᴅɴʜxʜᴇʟʟ", url="https://t.me/DNHxHELL"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**RiZoeL Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "RiZoeL", url="https://t.me/RiZoeL")
                ]
            ]
        )
   )


RIZ_PIC = "https://telegra.ph/file/d9f9d87cf08142a8cafe2.jpg"
@Client.on_message(filters.command("alive") & ~filters.edited)
@sudo_users_only
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    if RIZ_PIC:
        RIZ_caption = f"ℝ𝚒ℤ𝚘𝚎𝕃𝕏𝕄𝚞𝕊𝚒𝚌 𝚒𝚣𝚣 𝔸𝕃𝕀𝕍𝔼\n\n"
        RIZ_caption += f"◑ ━━━━━ ▣ ━━━━━ ◐\n"
        RIZ_caption += f"➣ ʙᴏᴛ ᴠɪʀsɪᴏɴ : 1.0.2\n"
        RIZ_caption += f"➣ ᴄʀᴇᴀᴛᴏʀ : [ʀɪᴢᴏᴇʟ](https://t.me/TheRiZoeL)\n"
        RIZ_caption += f"➣ sᴜᴘᴘᴏʀᴛ : [ᴊᴏɪɴ](https://t.me/DNHxHELL)\n"
        RIZ_caption += f"➣ sᴛᴀʀᴛ ᴛɪᴍᴇ : `{START_TIME_ISO}`\n"
        RIZ_caption += f"➣ ᴜᴘᴛɪᴍᴇ : `{uptime}`\n"
        RIZ_caption += f"◑ ━━━━━ ▣ ━━━━━ ◐\n\n"
        await event.client.send_file(
            event.chat_id, RIZ_PIC, caption=RIZ_caption
        )
        await event.delete()
