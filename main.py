import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import raw
import random
from pyrogram import enums
from pyrogram.errors import BadRequest
from config import Config as C
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                            InlineKeyboardButton)
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
import pyrogram

from animations import *
app = Client("bot", C.API_ID, C.API_HASH, bot_token=C.TOKEN)

@app.on_message(filters.private &  filters.command(["start"]))
async def start(bot, message):
  await message.reply('https://t.me/miliservice')

list_of_animation = [
    'بکشش | kill him',
    'نیمه شعبان | colorfull',
    'سکس | sex',
    'شطرنج | chess',
    'رانندگی | driving',
    'پلیس | police',
    'ماه | moon',
    'منظومه شمسی | solar system',
    'جق | jerk off',
    'فحش کلمه ای | persian single swear words',
    'دوستت دارم | I love you ',
    'پروانه | butterfly',
    'مغزت | your brain',
    'شمارش معکوس | count down',
    'برقص | dance'
]

@app.on_inline_query()
async def answer(client, inline_query):
    results = []
    try:
        member = await app.get_chat_member(-1001848766738, inline_query.from_user.id)
        for i in list_of_animation:
            results.append(
                InlineQueryResultArticle(
                    title=i,id=i,
                    input_message_content=InputTextMessageContent(
                        i
                    ),
                    description='بزن روش',
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton(
                                i,
                                callback_data="i"
                            )]
                        ]
                    )
                )
            )
        await inline_query.answer(results,cache_time=1) 
    except:
        results.append(
           InlineQueryResultArticle(
                    title='هنوز عضو چنل نیستید برای عضویت کلیک کنید',url='https://t.me/miliservice',
                    input_message_content=InputTextMessageContent(
                        '''برای استفاده از این ربات 
ابتدا در چنل  https://t.me/miliservice
عضو شوید . '''
                    )))
        
        await inline_query.answer(results,cache_time=1) 
    



from collections import deque

@app.on_raw_update()
async def mmm(cl, up, us, ch):
 if type(up) == raw.types.UpdateBotInlineSend:
        
    try:
        if up.id=='دوستت دارم | I love you ': 
            

            m = ['‎🤍🤍🤍🤍🤍🤍🤍🤍🤍\n',
    '‎🤍🤍💚💚🤍💚💚🤍🤍\n',
    '‎🤍💚💚💚💚💚💚💚🤍\n',
    '‎🤍💚💚💚💚💚💚💚🤍\n',
    '‎🤍💚💚💚💚💚💚💚🤍\n',
    '‎🤍🤍💚💚💚💚💚🤍🤍\n',
    '‎🤍🤍🤍💚💚💚🤍🤍🤍\n',
    '‎🤍🤍🤍🤍💚🤍🤍🤍🤍\n',
    '‎🤍🤍🤍🤍🤍🤍🤍🤍🤍\n']
            text=''
            for i in m:
                text+=i
                try:
                    await cl.edit_inline_text(
                        pyrogram.utils.pack_inline_message_id(up.msg_id),text
                    )
                    await asyncio.sleep(0.2)
                except FloodWait as e:
                     await asyncio.sleep(e.value)    

            for i in ghalb:
                try:
                    await cl.edit_inline_text(
                        pyrogram.utils.pack_inline_message_id(up.msg_id),i
                    )
                    await asyncio.sleep(0.2)
                except FloodWait as e:
                     await asyncio.sleep(e.value)        

            await cl.edit_inline_text(
                    pyrogram.utils.pack_inline_message_id(up.msg_id),'دوستت دارم ❤️🥹'
                )    
        
        elif up.id=='نیمه شعبان | colorfull':
            # color fullllll
            deq = deque(list("🟥🟧🟨🟩🟦🟪🟫⬛⬜"))
            for _ in range(30):
              await asyncio.sleep(0.4)
              try:
                await cl.edit_inline_text(pyrogram.utils.pack_inline_message_id(up.msg_id),"".join(deq))
                deq.rotate(1)
              except FloodWait as e:
                     await asyncio.sleep(e.value)       
            
        elif up.id=='پروانه | butterfly':
            deq = deque(list("🦋✨🦋✨🦋✨🦋✨"))
            for _ in range(30):
              await asyncio.sleep(0.4)
              try:
                await cl.edit_inline_text(pyrogram.utils.pack_inline_message_id(up.msg_id),"".join(deq))
                deq.rotate(1)
              except FloodWait as e:
                   await asyncio.sleep(e.value)  
        
        elif up.id=='مغزت | your brain':
            animation_interval = 1
            animation_ttl = range(14)
            animation_chars = [
            "  \n🧠         <(^_^ <)🗑",
            "  \n🧠       <(^_^ <)  🗑",
            "  \n🧠     <(^_^ <)    🗑",
            "  \n🧠   <(^_^ <)      🗑",
            "  \n🧠 <(^_^ <)        🗑",
            "  \n🧠<(^_^ <)         🗑",
            "  \n(> ^_^)>🧠         🗑",
            "  \n  (> ^_^)>🧠       🗑",
            "  \n    (> ^_^)>🧠     🗑",
            "  \n      (> ^_^)>🧠   🗑",
            "  \n        (> ^_^)>🧠 🗑",
            "  \n          (> ^_^)>🧠🗑",
            "  \n           (> ^_^)>🗑",
            "  \n           <(^_^ <)🗑",
        ]
            for i in animation_ttl:

                await asyncio.sleep(animation_interval)
                try:
                  await cl.edit_inline_text(pyrogram.utils.pack_inline_message_id(up.msg_id),animation_chars[i % 14])
                except FloodWait as e:
                     await asyncio.sleep(e.value)      

        elif up.id=='پلیس | police':  
            animation_interval = 0.3
            animation_ttl = range(12) 
            for i in animation_ttl:
              await asyncio.sleep(animation_interval)
              try:
                await cl.edit_inline_text(pyrogram.utils.pack_inline_message_id(up.msg_id),police[i % 12])
              except FloodWait as e:
                   await asyncio.sleep(e.value)  

        elif up.id=='منظومه شمسی | solar system': 
            animation_interval = 0.1
            animation_ttl = range(80)   
            for i in animation_ttl:
              await asyncio.sleep(animation_interval)
              try:
                await cl.edit_inline_text(pyrogram.utils.pack_inline_message_id(up.msg_id),solar[i % 8])
              except FloodWait as e:
                     await asyncio.sleep(e.value)      
        
        elif up.id=='شمارش معکوس | count down':
            for i in count_down:
              try:
                await cl.edit_inline_text(pyrogram.utils.pack_inline_message_id(up.msg_id),i)
                await asyncio.sleep(1)
              except FloodWait as e:
                     await asyncio.sleep(e.value)      
            await cl.edit_inline_text(pyrogram.utils.pack_inline_message_id(up.msg_id),'بووم')  

        elif up.id=='ماه | moon':
            for i in moon:
                try:
                    await cl.edit_inline_text(pyrogram.utils.pack_inline_message_id(up.msg_id),i)
                    await asyncio.sleep(0.2)
                except FloodWait as e:
                     await asyncio.sleep(e.value)        

        elif up.id=='جق | jerk off':
            for i in jagh:
                try:
                    await cl.edit_inline_text(pyrogram.utils.pack_inline_message_id(up.msg_id),i)
                    await asyncio.sleep(0.2)
                except FloodWait as e:
                     await asyncio.sleep(e.value)        

        elif up.id=='فحش کلمه ای | persian single swear words':
            for i in swears[5:25]:
                try:
                    await cl.edit_inline_text(pyrogram.utils.pack_inline_message_id(up.msg_id),i)
                    await asyncio.sleep(0.6)
                except FloodWait as e:
                     await asyncio.sleep(e.value)        

        elif up.id=='سکس | sex':
            for i in sex:
                try:
                    await cl.edit_inline_text(pyrogram.utils.pack_inline_message_id(up.msg_id),i)
                    await asyncio.sleep(0.6)
                except FloodWait as e:
                     await asyncio.sleep(e.value)        

        elif up.id=='بکشش | kill him':  
            animation_interval = 0.7
            animation_ttl = range(12)
            animation_chars = [
            "بمیررر کسکشششش",
            f"\n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - \n _/﹋\_\n",
            f"\n\n_/﹋\_\n (҂`_´)\n  <,︻╦╤─ ҉ - -\n _/﹋\_\n",
            f"\n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - - -\n _/﹋\_\n",
            f"\n\n_/﹋\_\n (҂`_´)\n<,︻╦╤─ ҉ - -\n _/﹋\_\n",
            f"\n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - \n _/﹋\_\n",
            f"\n\n_/﹋\_\n (҂`_´)\n  <,︻╦╤─ ҉ - -\n _/﹋\_\n",
            f"\n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - - - \n _/﹋\_\n",
        ]
            for i in animation_ttl:
                await asyncio.sleep(animation_interval)
                try:
                  await cl.edit_inline_text(pyrogram.utils.pack_inline_message_id(up.msg_id),animation_chars[i % 8]) 
                except FloodWait as e:
                     await asyncio.sleep(e.value)      

        elif up.id=='رانندگی | driving': 
            animation_interval = 0.5
            animation_ttl = range(16) 
            for i in animation_ttl:
              await asyncio.sleep(animation_interval)
              try:
                await cl.edit_inline_text(pyrogram.utils.pack_inline_message_id(up.msg_id),driving[i % 16])   
              except FloodWait as e:
                     await asyncio.sleep(e.value)      
        
        elif up.id=='شطرنج | chess':   
            animation_interval = 0.3
            animation_ttl = range(28)  
            for i in animation_ttl:
              await asyncio.sleep(animation_interval)
              try:
                await cl.edit_inline_text(pyrogram.utils.pack_inline_message_id(up.msg_id),chess[i % 28])   
              except FloodWait as e:
                     await asyncio.sleep(e.value)       
        elif up.id=='برقص | dance':
            for i in dance:
              await asyncio.sleep(0.3)
              try:
                await cl.edit_inline_text(pyrogram.utils.pack_inline_message_id(up.msg_id),i)   
              except FloodWait as e:
                     await asyncio.sleep(e.value)      

    except:
        pass














      












  
if __name__ == '__main__':
    print('[Bot] : listening :)')
    app.run()