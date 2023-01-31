#Bu Kodlama @aykhan_s Və @B9SSD7 Tərəfindən Yazılıb Şəxsiləşdirmək Qadağandır Bu Meşajı Silmədən İşlət!
from config import Config
import secrets, os
import string
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from cryptography.fernet import Fernet
from mesajlar.komekci import random_line



api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
bot = Client('sehidmodulu', api_id, api_hash).start(bot_token=bot_token)
 
 


button = InlineKeyboardMarkup([
    [InlineKeyboardButton("🔄Dəyiş", callback_data="deyis")]
])

@bot.on_message(filters.command("sehid") & ~filters.edited)
async def commit(_, message):
    await message.reply_text((await random_line('mesajlar/txt/sehid.txt')), reply_markup=button)



@bot.on_callback_query(filters.regex("deyis"))
async def deyis(_, query: CallbackQuery):
    await query.edit_message_text((await random_line('mesajlar/txt/sehid.txt')), reply_markup=button)
