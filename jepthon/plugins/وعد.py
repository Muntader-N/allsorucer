import asyncio

from telethon.errors import FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetHistoryRequest, ImportChatInviteRequest

from jepthon import jepiq

@jepiq.ar_cmd(pattern="بخشيش وعد (.*)")
async def baqshis(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await jepiq.send_message(chat, "بخشيش")
        await asyncio.sleep(605)


@jepiq.ar_cmd(pattern="راتب وعد (.*)")
async def ratb(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await jepiq.send_message(chat, "راتب")
        await asyncio.sleep(605)


# none
@jepiq.ar_cmd(pattern="كلمات وعد (.*)")
async def waorwaad(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await jepiq.send_message(chat, "كلمات")
        await asyncio.sleep(0.5)
        masg = await jepiq.get_messages(chat, limit=1)
        masg = masg[0].message
        masg = ("".join(masg.split(maxsplit=3)[3:])).split(" ", 2)
        if len(masg) == 2:
            msg = masg[0]
            await jepiq.send_message(chat, msg)
        else:
            msg = masg[0] + " " + masg[1]
            await jepiq.send_message(chat, msg)


@jepiq.ar_cmd(pattern="استثمار وعد (.*)")
async def _(event):
    await event.edit(
        "**- تم تفعيل الاستثمار ببوت وعد بنجاح لأيقافه ارسل \n`.استثمار وعد 1`"
    )
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await jepiq.send_message(chat, "فلوسي")
        await asyncio.sleep(0.5)
        masg = await jepiq.get_messages(chat, limit=1)
        masg = masg[0].message
        masg = ("".join(masg.split(maxsplit=2)[2:])).split(" ", 2)
        msg = masg[0]
        if int(msg) > 500000000:
            await jepiq.send_message(chat, f"استثمار {msg}")
            await asyncio.sleep(10)
            mssag2 = await jepiq.get_messages(chat, limit=1)
            await mssag2[0].click(text="اي ✅")
        else:
            await jepiq.send_message(chat, f"استثمار {msg}")
        await asyncio.sleep(1210)
