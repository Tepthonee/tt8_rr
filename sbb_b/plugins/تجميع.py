# t.me/Dar4k
# this file for https://github.com/thejmthon/sbb_b0

import asyncio
import requests
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import events
from sbb_b import sbb_b

@sbb_b.ar_cmd(pattern="تجميع$")
async def _(event):
        await event.edit("**- يجب عليك الاشتراك بقنوات البوت لتفادي الاخطاء اولا**")
        channel_entity = await sbb_b.get_entity("@t06bot")
        await sbb_b.send_message('@t06bot', '/start')
        await asyncio.sleep(10)
        msg0 = await sbb_b.get_messages('@t06bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(10)
        msg1 = await sbb_b.get_messages('@t06bot', limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(10)
            list = await sbb_b(GetHistoryRequest(peer=channel_entity, limit=1,offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await edit_or_reply(event, "**- لا توجد أي قنوات متاحة في البوت الان**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sbb_b(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sbb_b(ImportChatInviteRequest(bott))
                msg2 = await sbb_b.get_messages('@t06bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await edit_or_reply(event, "**- تم بنجاح الاشتراك في {chs} من القنوات**")
            except:
                await edit_or_reply(event, "**- لقد حدث خطأ ما يبدو أنه تم حظرك**")
                break
        await edit_or_reply(event, "**- تم بنجاح الانتهاء من تجميع النقاط**")
        
