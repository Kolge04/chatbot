import random
import os
import logging
import asyncio
from os import remove
from time import time
from telethon import Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import ChannelParticipantsBots
from telethon.tl.functions.users import GetFullUserRequest
from telethon import TelegramClient, events
from mesajlar.mesaj import taım, azz, enn, trrr, russ, fra
from mesajlar.bot import yeni_user, ınfom

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)


api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

tekli_calisan = []

anlik_calisan = []

grup_sayi = []

user_sayi = []

anlik_calisan = []
######  START####

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
  await event.reply(f"**👋 Salam {ad}\nMən  𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ**\n**𝕏𝔸𝕆𝕊 Federasiyasının Rəsmi Tağ botuyam**\n**⚡ 𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ İlə Qrupunuzdakı Üyələri Etiket Edə Bilərəm**\n**Əmrlərlə Tanış Olmaq Üçün __ƏMRLƏR__ Butonuna Toxun**\n**ℹ Mənim Qruplarda Asan Və Sürətli İşləyə Bilməyim Üçün Mənə Qrupunuzda Sadə Adminlik Vermənizi Rica Edirem**",
                    buttons=(
			    
		      [Button.url('➕ ℚℝ𝕌ℙ𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Tagbot?startgroup=a')],
                      [Button.url('⚡ 𝕏𝔸𝕆𝕊 𝔽𝔹𝔸ℕ', f'https://t.me/XaosResmii')],
                      [Button.url('🇦🇿 𝕆𝕎ℕ𝔼ℝ 👨‍💻', f'https://t.me/sesizKOLGE')],
                      [Button.inline("⚙ Ə𝕄ℝ𝕃Əℝ", data="help")],
                    ),
                    link_preview=False
		   )

@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
    await event.edit(f"**👋 Salam {ad}\n ⚡Mən  𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ**\n**𝕏𝔸𝕆𝕊 Federasiyasının Rəsmi Tağ botuyam**\n**⚡ 𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ İlə Qrupunuzdakı Üyələri Etiket Edə Bilərəm**\n**ℹƏmrlərlə Tanış Olmaq Üçün __ƏMRLƏR__ Butonuna Toxun**\n**ℹ Mənim Qruplarda Asan Və Sürətli İşləyə Bilməyim Üçün Mənə Qrupunuzda Sadə Adminlik Vermənizi Rica Edirem**", buttons=(
                      
                      [Button.url('➕ ℚℝ𝕌ℙ𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Tagbot?startgroup=a')],
                      [Button.url('⚡ 𝕏𝔸𝕆𝕊 𝔽𝔹𝔸ℕ', f'https://t.me/XaosResmii')],
                      [Button.url('🇦🇿 𝕆𝕎ℕ𝔼ℝ 👨‍💻', f'https://t.me/sesizKOLGE')],	             
                      [Button.inline("⚙ Ə𝕄ℝ𝕃Əℝ", data="help")],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):
    await event.edit(f"⚡ 𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ İn Əmrləri \n\n➪ /sehidler <səbəb> Şəhid Adları İlə Tağ Edər\n➪ /tag <səbəb> - 5-li Tağ Edər\n➪ /etag <səbəb> - Emoji İlə Tağ Edər\n➪ /btag <səbəb> - Bayraqlarla Tağ Edər\n➪ /mtag <səbəb>  Mafia Rolları İlı Tağ Edər\n➪ /rtag <səbəb> Rayon Və Şəhər Adları İlə Tağ Edər\n➪ /htag <səbəb> Heyvan Adları İlə Tağ Edər\n➪ /ttag <səbəb> - Tək Teək Tağ Edər\n➪ /admin <səbəb> - Adminləri Tağ Edər\n➪ /cancel - Tağ Prosesin Saxlayar\n➪ /id - Qrup və Sizin İD i verər\n➪ /tema - Bir Birindən Maraqlı Temalar Atar\n➪ /pin - İsdənilən Bir Mesajı Sabitləyər\n➪ /unpin - Sabitlənmiş Mesajı Silər\n➪ /start - Botu Başladar\n\nℹ Botu /, !, ., @ Simvollarla İsdifadə Edə Bilərsiz!", buttons=(
                      [Button.url('➕ ℚℝ𝕌ℙ𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Tagbot?startgroup=a')],
	              [Button.inline("ℹ 𝕀ℕ𝔽𝕆", data="info")],
                      [Button.inline("🗑 𝔹𝔸𝔾𝕃𝔸", data="start")],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="info"))
async def handler(event):
    await event.edit(f"**Çox Özəllikli Tağ Botu Axtarmağa Çalışan Qrub Sahibləri  ⚡  𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ Bot Sizə Görə:\n\n☞︎︎︎ Şəhid Adları İlə Tağ Edər\n☞︎︎︎ 5-Li Tağ\n☞︎︎︎ Emojilərlə Tağ Edər\n☞︎︎︎ Heyvan Adları İlə Tağ Edər\n☞︎︎︎ Bayraqlarla Tağ Edər\n☞︎︎︎ Mafia Rolları İlə Tağ Edər\n☞︎︎︎ Rayon Və Şəhər Adları İlə Tağ Edər\n☞︎︎︎ Təkli Tağ\n☞︎︎︎ Yalnız Admimləri Tağ\n☞︎︎︎ Maraqlı Temalar\n☞︎︎︎ Qrup Və Öz İD Niz\n☞︎︎︎ İstənilən Mesajı Sabitləyin\n☞︎︎︎ İstənilən Mesaji Sabitdən Silin\n\n\nBelə Çox Özəllikli @XAOS_Tagbot 'u Qrupunuza Yönətici Olaraq Alıb Rahatlıqla , Tağ edə bilirsiz**\nℹ Botu /, !, ., @ Simvollarla İsdifadə Edə Bilərsiz!\n**📢  QRUPDA ADMİNLİK MÜTLIQDİ**", buttons=(      
	              [Button.url('➕ ℚℝ𝕌ℙ𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Tagbot?startgroup=a')],
		      [Button.inline("⚙ 𝔼𝕊𝔸𝕊 𝕄𝔼𝕐ℕ𝕌", data="start")],
		    ),
                    link_preview=False)
                   


@client.on(events.NewMessage(pattern="^.stat ?(.*)"))
async def start(event):
  await event.reply(f"📊 [𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ](https://t.me/XAOS_Tagbot) İstatiska", buttons=(
                      [
                       Button.inline("📊 İstatiska", data="stats")
                      ],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="stats"))
async def handler(event):
    await event.edit(f"📊 [𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ](https://t.me/XAOS_Tagbot) Un  İstatiskası\n\n📋 Toplam Qrup: `{len(grup_sayi)}`\n📈 Aktuv Qruplar: `{len(anlik_calisan)}`\n👤 İsdifadəçi Sayı: `{len(user_sayi)}`", buttons=(
	                [
                       Button.inline("♻️ YENİLƏ", data="stats")
                      ],
                    ),
                    link_preview=False)
	      

#---------------‐------------------‐-------

      #####İD PY 🆔️🆔️
	

		

@client.on(events.NewMessage(pattern="^.id ?(.*)"))
async def id(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_id = previous_message.sender_id
        chat_id = event.chat_id
        if event.is_private:
            return await event.reply(f"**🆔️ id:** `{user_id}`\n**📎 link:-** [Toxun 👆](tg://settings)")
        else:
            return await event.reply(f"**👤 Sən**\n**🆔️ id:-** `{user_id}`\n**📎 link:-** [Toxun 👆](tg://settings)\n\n**👥 GRUP**\n**🆔️ id:** `{chat_id}`")


#@edalet_22 terefindən @RoBotlarimTg üçün yazilib silmədən istifadə edin
    else:
        user_id = event.sender_id 
        chat_id = event.chat_id
        if event.is_private:
            return await event.reply(f"**🆔️ id:** `{user_id}`\n**📎 link:-** [Toxun 👆](tg://settings)")
        else:
            return await event.reply(f"**👤 Sən**\n**🆔️ id:-** `{user_id}`\n**📎 link:-** [Toxun 👆](tg://settings)\n\n**👥 GRUP**\n**🆔️ id:** `{chat_id}`")
    
  #----------------------------------------


####  banda ###

#Bu kodda olan • By @EdaletRoBot yazisini silen gelib mene Ata deyer
@client.on(events.NewMessage(pattern="^.banda ?(.*)"))
async def banda(event):
    if not event.is_group:
        return await event.reply("Bu əmr qruplar üçün etibarlıdır!")
    info = await event.client.get_entity(event.chat_id)
    title = info.title if info.title else "This chat"
    mentions = f'**{title}** qrupunda olan silinmiş hesaplar:\n'
    deleted = 0
    async for user in event.client.iter_participants(event.chat_id):
        if user.deleted:
            mentions += f"\nSilinmiş hesap `{user.id}`"
            deleted += 1
            await event.client.kick_participant(event.chat_id, user.id)
    mentions += f"\nSilinmiş hesaplar` = {deleted}`\n\n__• By @EdaletRoBot__"
    await event.reply(mentions)
    

   ##  PİN  UNPİN ✴
SAHIB = 5663585448
	
@client.on(events.NewMessage(pattern="^.pin ?(.*)"))
async def pin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("Bir mesajı cavablayın")
        await event.reply("Pinləndi")
        await event.client.pin_message(event.chat_id, event.reply_to_msg_id, notify=True)
    else:
        await event.reply("Sən sahib deyilsən pinləməyə çalışma")
 
#Bu kodu @edalet_22 tərəfindən @RoBotlarimTg kanalı üçün yazılmışdır (bu messagı silməyin!!!!!!)
@client.on(events.NewMessage(pattern="^.unpin ?(.*)"))
async def unpin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("Bir pinlənən mesajı cavablayın")
        await event.reply("Pinlənmiş mesaj qaldırıldı")
        await event.client.unpin_message(event.chat_id)
    else:
        await event.reply("Sən sahib deyilsən unpinləməyə çalışma")
 #------------------------------------'xxxxxxxxxxxxxxx

#   #########Yeni istifadəçi mesajı⬇️  ##########

@client.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(f"{random.choice(yeni_user)}")

@client.on(events.ChatAction)
async def handler(event):
    if event.user_left:
        await event.reply(f"Səni tanimaq gözəl idi❗")
#---------------------------------------‐-----------------

#    #######CHAT MESAJLAR⬇️  #########

client_start = b"\x42\x6F\x74\x20\x42\x61\xC5\x9F\x6C\x61\x64\xC4\xB1\x6C\x64\xC4\xB1\x2E\x2E\x2E\x0A\x4F\x77\x6E\x65\x72\x3A\x20\x61\x79\x6B\x68\x61\x6E\x5F\x73\x20\x7C\x20\x61\x79\x6B\x68\x61\x6E\x30\x32\x36\x0A\x74\x2E\x6D\x65\x2F\x52\x6F\x42\x6F\x74\x6C\x61\x72\x69\x6D\x54\x67" 

@client.on(events.NewMessage(pattern='(?i)/ınfo+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ınfom)}")

@client.on(events.callbackquery.CallbackQuery(data="tema"))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.respond(f"{random.choice(taım)}",
		      
		      buttons=(
			   
                      [Button.inline("♻️ DƏYİŞ", data="tema")],
                    ),
                    link_preview=False
		   )


@client.on(events.NewMessage(pattern='(?i)/tema+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.respond(f"{random.choice(taım)}",
		      buttons=(
			   
                      [Button.inline("♻️ DƏYİŞ", data="tema")],
                    ),
                    link_preview=False
		   )



@client.on(events.NewMessage(pattern='(?i)/aze+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(azz)}")
 
@client.on(events.NewMessage(pattern='(?i)/rus+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(russ)}")
 
@client.on(events.NewMessage(pattern='(?i)/eng+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(enn)}")
 
@client.on(events.NewMessage(pattern='(?i)/tr+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(trrr)}")
 
@client.on(events.NewMessage(pattern='(?i)/fr+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(fra)}")
 #------------‐--------------------------------------------

#OYUNN  ⬇️
	
	

                  
######    TAĞ MODULU⬇️   #########  
	

	
sehidler = "Qəzənfər Nəcəf Nurlan İnqilab Nicat Mirnəbi Məhəmməd Ramazan Telman Fazil Qələndər Nofəl İbrahim Habil Elşən Sabir Həsən Qər󠁧󠁢󠁷󠁬󠁳󠁿󠁧󠁢󠁷󠁬󠁳󠁿ib Ceyhun Mübariz Polad Cəbrayıl ".split(" ")

@client.on(events.NewMessage(pattern="^.sehidler ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qurup və kanallar üçün keçərlidi. ❗**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmr sadəcə adminlər istifadə edə bilər 〽️**")
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("❌ Keçmiş Mesajlar Üçün Tağ Edə Bilmərəm..")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("❌ İstifadəçiləri Çağırmağım Üçün Bir Səbəb Yoxdur ")
  else:
    return await event.respond("🗣 İstifadəçiləri Tağ Edə Bilməyim Üçün Bir Səbəb Yazın...!")
  
	
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"🥀 [{random.choice(sehidler)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Tag Prosesi Uğurla dayandırıldı")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"🥀 [{random.choice(sehidler)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Tag Prosesi Uğurla Dayandırıldı")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	
	

seherler = "Ağcabədi Ağdam Ağdaş Ağdərə Ağıstafa Ağsu Astara Babək Bakı Balakən Beyləqan Bərdə Biləsuvar Cəbrayıl Cəlilabad Culfa Daşkəsən Dəliməmmədli Xocalı Füzuli Gədəbəy Gəncə Goranboy Göyçay Göygöl Göytəpə Hacıqabul Horadiz Xaçmaz Xankəndi Xocalı Xocavənd Xırdalan Xızı Xudat İmişli İsmayıllı Kəlbəcər Kürdəmir Qax Qazax Qəbələ Qobustan Qovlar Quba Qubadlı Qusar Laçın Lerik Lənkəran Liman Masallı Naftalan Naxçıvan Neftçala Oğuz Ordubad Saatlı Sabirabad Salyan Samux Siyəzən Sumqayıt Şuşa Şabran Şahbuz Şamaxı Şəki Şəmkir Şərur Şirvan Tərtər Tovuz Ucar Yardımlı Yevlax Zaqatala Zəngilan Zərdab󠁧󠁢󠁷󠁬󠁳󠁿󠁧󠁢󠁷󠁬󠁳󠁿".split(" ")


@client.on(events.NewMessage(pattern="^.rtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qurup və kanallar üçün keçərlidi ❗**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmr sadəcə adminlər istifadə edə bilər 〽️**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Keçmiş mesajlar üçün tag edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("❌ İstifadəçiləri çağırmağım üçün bir səbəb yoxdur ")
  else:
    return await event.respond("**🗣 İstifadəçiləri çağırmağım üçün bir səbəb yazın...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➪ [{random.choice(seherler)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tag prosesini dayandırdınız ✅**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➪ [{random.choice(seherler)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Tag prosesi uğurla dayandırıldı ✅\n\n**Buda sizin reklamınız ola bilər @sesizKOLGE**✅")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	
mafia = "👨‍🌾Vətəndaş 👨‍✈️Komissar Kattani 👨‍💼Çavuş 👨‍⚕️Doktor 🧟‍♀️Cadugar 🕵️Suiqəstçi 🧔Bomj 🦎Buqələmun 💂🏻Securıty 👳🏻‍♂️Satıcı 🙇🏻‍♂️Oğru 👷🏻‍♂️Mədənçi ⭐️General 🧝🏻‍♀️Şəhzadə 🎧DJ 🏦Bankir 🕴Don 🕺Mafia 👨‍⚖️Vəkil 🙍🏻‍♂️Məhbus 👨🏻‍🦱Dedektiv  🦦Köstəbək 👨🏻‍🎤Specialist 🔪Manyak 🤡Joker 👻Ruh 🧚🏻‍♀️Mələk 🦹🏻‍♂️BOSS 🥷Ninja 🥷SUPER Ninja 👨🏻‍🦲Dəli 🔮Reviver 💂Killer 🧛🏻‍♂️Vampir󠁧󠁢󠁷󠁬󠁳󠁿󠁧󠁢󠁷󠁬󠁳󠁿".split(" ")


@client.on(events.NewMessage(pattern="^.mtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qurup və kanallar üçün keçərlidi ❗**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmr sadəcə adminlər istifadə edə bilər 〽️**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Keçmiş mesajlar üçün tag edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("❌ İstifadəçiləri çağırmağım üçün bir səbəb yoxdur ")
  else:
    return await event.respond("**🗣 İstifadəçiləri çağırmağım üçün bir səbəb yazın...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➪ [{random.choice(mafia)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tag prosesini dayandırdınız ✅**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➪ [{random.choice(mafia)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Tag prosesi uğurla dayandırıldı ✅\n\n**Buda sizin reklamınız ola bilər  @sesizKOLGE**✅")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	
bayrag = "🇦🇨 🇦🇩 🇦🇪 🇦🇫 🇦🇬 🇦🇮 🇦🇱 🇦🇴 🇦🇶 🇦🇷 🇦🇸 🇦🇹🇦🇺 🇦🇼 🇦🇽 🇦🇿 🇧🇦 🇧🇧 🇧🇩 🇧🇪 🇧🇫 🇧🇬 🇧🇭 🇧🇮🇧🇯 🇧🇱 🇧🇲 🇧🇳 🇧🇴 🇧🇶 🇧🇷 🇧🇸 🇧🇹 🇧🇻 🇧🇼 🇧🇾🇧🇿 🇨🇦 🇨🇨 🇨🇩 🇨🇫 🇨🇬 🇨🇭 🇨🇮 🇨🇰 🇨🇱 🇨🇲 🇨🇳🇨🇵 🇨🇷 🇨🇺 🇨🇻 🇨🇼 🇨🇽 🇨🇾 🇨🇿 🇩🇪 🇩🇬 🇩🇯 🇩🇰🇩🇲 🇩🇴 🇩🇿 🇪🇦 🇪🇨 🇪🇪 🇪🇬 🇪🇭 🇪🇷 🇪🇸 🇪🇹 🇪🇺🇫🇮 🇫🇯 🇫🇰 🇫🇲 🇫🇴 🇫🇷 🇬🇦 🇬🇧 🇬🇩 🇬🇪 🇬🇫 🇬🇬🇬🇭 🇬🇮 🇬🇱 🇬🇲 🇬🇳 🇬🇵 🇬🇶 🇬🇷 🇬🇸 🇬🇹 🇬🇺 🇬🇼🇬🇾 🇭🇰 🇭🇲 🇭🇳 🇭🇷 🇭🇹 🇭🇺 🇮🇨 🇮🇩 🇮🇪 🇮🇱 🇮🇲🇮🇳 🇮🇴 🇮🇶 🇮🇷 🇮🇸 🇮🇹 🇯🇪 🇯🇲 🇯🇴 🇯🇵 🇰🇪 🇰🇬🇰🇭 🇰🇮 🇰🇲 🇰🇳 🇰🇵 🇰🇷 🇰🇼 🇰🇾 🇰🇿 🇱🇦 🇱🇧 🇱🇨🇱🇮 🇱🇰 🇱🇷 🇱🇸 🇱🇹 🇱🇺 🇱🇻 🇱🇾 🇲🇦 🇲🇨 🇲🇩 🇲🇪🇲🇫 🇲🇬 🇲🇭 🇲🇰 🇲🇱 🇲🇲 🇲🇳 🇲🇴 🇲🇵 🇲🇶 🇲🇷 🇲🇸🇲🇹 🇲🇺 🇲🇻 🇲🇼 🇲🇽 🇲🇾 🇲🇿 🇳🇦 🇳🇨 🇳🇪 🇳🇫 🇳🇬🇳🇮 🇳🇱 🇳🇴 🇳🇵 🇳🇷 🇳🇺 🇳🇿 🇴🇲 🇵🇦 🇵🇪 🇵🇫 🇵🇬🇵🇭 🇵🇰 🇵🇱 🇵🇲 🇵🇳 🇵🇷 🇵🇸 🇵🇹 🇵🇼 🇵🇾 🇶🇦 🇷🇪🇷🇴 🇷🇸 🇷🇺 🇷🇼 🇸🇦 🇸🇧 🇸🇨 🇸🇩 🇸🇪 🇸🇬 🇸🇭 🇸🇮🇸🇯 🇸🇰 🇸🇱 🇸🇲 🇸🇳 🇸🇴 🇸🇷 🇸🇸 🇸🇹 🇸🇻 🇸🇽 🇸🇾🇸🇿 🇹🇦 🇹🇨 🇹🇩 🇹🇫 🇹🇬 🇹🇭 🇹🇯 🇹🇰 🇹🇱 🇹🇲 🇹🇳🇹🇴 🇹🇷 🇹🇹 🇹🇻 🇹🇼 🇹🇿 🇺🇦 🇺🇬 🇺🇲 🇺🇳 🇺🇸 🇺🇾🇺🇿 🇻🇦 🇻🇨 🇻🇪 🇻🇬 🇻🇮 🇻🇳 🇻🇺 🇼🇫 🇼🇸 🇽🇰 🇾🇪🇾🇹 🇿🇦 🇿🇲 🇿🇼 🏴󠁧󠁢󠁥󠁮󠁧󠁿 🏴󠁧󠁢󠁳󠁣󠁴󠁿 🏴󠁧󠁢󠁷󠁬󠁳󠁿󠁧󠁢󠁷󠁬󠁳󠁿".split(" ")


@client.on(events.NewMessage(pattern="^.btag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("⛔ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidir..")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("⛔ Bu Əmrdən Sadəcə Adminlər İsdifadə Edə Bilər..")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("❌ Keçmiş mesajlar üçün tag edə bilmərəm")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("❌ İstifadəçiləri Çağırmağım Üçün Bir Səbəb Yoxdur ")
  else:
    return await event.respond("❌ İstifadəçiləri Tağ Edə Bilməyim Üçün Bir Səbəb Yazın..")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Tağ Prosesi Uğurla Dayandırıldı")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Tag Prosesi Uğurla Dayandırıldı")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
	
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	
	
emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")


@client.on(events.NewMessage(pattern="^.etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("⛔ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidir..")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("⛔ Bu Əmr Sadəcə Adminlər İsdifadə Edə Bilər..")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Keçmiş Mesajlar Üçün Tağ Edə Bilmərəm")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("❌ İstifadəçiləri Çağırmağım Üçün Bir Səbəb Yoxdur")
  else:
    return await event.respond("❌ İstifadəçiləri Tağ Edə Bilməyim Üçün Bir Səbəb Yazın...")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Tag Prosesi Uğurla Dayandırıldı")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Tag Prosesi Uğurla Dayandırıldı")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

	
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)

	
	
heyvan = "Meymun🐵 İt🐕 At🐴 Tülkü🦊 Porsuq🐺 Pələng🦁 Çita🐆 Donuz🐷 İnək🐮 Öküz🐃 Zebra🦓 Maral🦌 Ceyran🦌 Qaban🐗 Mişoul🐀 Yarasa🦇 Xoruz🐓 Toyuq🐔 Cücə🐥 Göyərçin🕊 Sərçə🐦 Qartal🦅 Dinazavur🦖 Timsah🐊 Qurbağa🐸 Papuqayı🦜 Tovuzquşu🦚 Kərtənkələ🦎 Tısbağa🐢 İlan🐍 Balina🐬 Balıq🐟 İlbiz🐌 Kəpənək🦋 Qarışqa🐜 Arı🐝 Mikrob🦠 Virus🦠 Xərçəng🦂 Çəyirtkə🦗 Parabüzən🐞 Hörümçək🦂 Ördək🦆 Bayquş🦉 Hünduşqa🦃 Pinqivin🐧 Ayı🐻 Panda🐼".split(" ")
@client.on(events.NewMessage(pattern="^.htag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**⛔ Bu əmr qurup və kanallar üçün keçərlidi**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmr sadəcə adminlər istifadə edə bilər 〽️**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Keçmiş mesajlar üçün tag edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("❌ İstifadəçiləri çağırmağım üçün bir səbəb yoxdur ")
  else:
    return await event.respond("**🗣 İstifadəçiləri çağırmağım üçün bir səbəb yazın...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➪ [{random.choice(heyvan)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tag prosesini dayandırdınız ✅**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➪ [{random.choice(heyvan)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Tag prosesi uğurla dayandırıldı ✅\n\n**Buda sizin reklamınız ola bilər @sesizKOLGE**✅")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
			
	
@client.on(events.NewMessage(pattern="^.tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("⛔ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidir")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("⛔ Bu Əmrdən Sadəcə Adminlər İsdifadə Edə Bilər..")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("❌ Keçmiş Mesajlar Üçün Tağ Edə Bilmərəm")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("❌ İstifadəçiləri Çağırmağım Üçün Bir Səbəb Yoxdur")
  else:
    return await event.respond("🗣 İstifadəçiləri Tağ Edə Bilməyim Üçün Bir Səbəb Yazın...!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➪ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Tag Prosesi Uğurla Dayandırıldı")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➪ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Tag Prosesi Uğurla Dayandırıldı")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^.ttag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("⛔ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidir")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("⛔ Bu Əmrdən Sadəcə Adminlər İsdifadə Edə Bilər")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("❌ Keçmiş Mesajlar Üçün Tağ Edə Bilmərəm")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("❌ İstifadəçiləri Çağırmağım Üçün Bir Səbəb Yoxdur")
  else:
    return await event.respond("🗣 İstifadəçiləri Tağ Edə Bilməyim Üçün Birr Səbəb Yazın...!")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**📢 [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("✅ Tag Prosesi Uğurla Dayandırıldı")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"📢 [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("✅ Tag Prosesi Uğurla Dayandırıldı")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^.admin ?(.*)"))
async def tag_admin(event):
    chat = await event.get_input_chat()
    text = "♕︎ Qrup Adminlərinin Siyahısı ♕︎\n"
    async for x in event.client.iter_participants(chat, 100, filter=ChannelParticipantsAdmins):
        text += f" \n ➪ [{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        await event.client.send_message(event.chat_id, text, reply_to=event.reply_to_msg_id)
    else:
        await event.reply(text)
    raise StopPropagation

   

client_run = client_start.decode("utf8")
print(">> Chat bot işləyir ♿ <<")
print(f"{client_run}")
client.run_until_disconnected()
