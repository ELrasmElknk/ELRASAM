import os

from telethon import Button, events

from JE313P import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/21e89e713e2e7de5cc936.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@Elrasam7"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@JE313P.on(events.NewMessage(pattern="^/بنك"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/EL_RASA")]]
    await JE313P.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
