import random
import os
import logging
import asyncio
from telethon import Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import TelegramClient, events
from mesajlar.mesaj import salam, necesen, sagol, getdim, geldim, sesizKOLGE, ban, emoji1, emoji2, fed, niye, ne, hay, mal, can, balam, xos, hara, gel, gordum
from mesajlar.bot import yeni_user, info

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




# Yeni istifadəçi mesajı
@client.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(f"{random.choice(yeni_user)}")

client_start = b"\x42\x6F\x74\x20\x42\x61\xC5\x9F\x6C\x61\x64\xC4\xB1\x6C\x64\xC4\xB1\x2E\x2E\x2E\x0A\x4F\x77\x6E\x65\x72\x3A\x20\x61\x79\x6B\x68\x61\x6E\x5F\x73\x20\x7C\x20\x61\x79\x6B\x68\x61\x6E\x30\x32\x36\x0A\x74\x2E\x6D\x65\x2F\x52\x6F\x42\x6F\x74\x6C\x61\x72\x69\x6D\x54\x67"
@client.on(events.NewMessage(pattern='(?i)/xaosinfo+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(info)}")
 
@client.on(events.NewMessage(pattern='(?i)salam+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(salam)}")

@client.on(events.NewMessage(pattern='(?i)necəsən+'))
@client.on(events.NewMessage(pattern='(?i)necesen+'))
@client.on(events.NewMessage(pattern='(?i)nətərsən+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(necesen)}")

@client.on(events.NewMessage(pattern='(?i)sağol+'))
@client.on(events.NewMessage(pattern='(?i)sagol+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(sagol)}")

@client.on(events.NewMessage(pattern='(?i)getdim+'))
@client.on(events.NewMessage(pattern='(?i)gedim+'))
@client.on(events.NewMessage(pattern='(?i)gedirəm+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(getdim)}")

@client.on(events.NewMessage(pattern='(?i)gəldim+'))
@client.on(events.NewMessage(pattern='(?i)geldim+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(geldim)}")

@client.on(events.NewMessage(pattern='(?i)@sesizKOLGE+'))
@client.on(events.NewMessage(pattern='(?i)@MR_K4BUS_13+'))
@client.on(events.NewMessage(pattern='(?i)@Modelhs+'))
@client.on(events.NewMessage(pattern='(?i)@sanane_lann+'))
@client.on(events.NewMessage(pattern='(?i)@adsizm1_2+'))
@client.on(events.NewMessage(pattern='(?i)@NaraHva+'))
@client.on(events.NewMessage(pattern='(?i)@DAGLI_R_17+'))
@client.on(events.NewMessage(pattern='(?i)@lezgididee+'))
@client.on(events.NewMessage(pattern='(?i)@mmmdtly+'))
@client.on(events.NewMessage(pattern='(?i)@Cavkaa+'))
@client.on(events.NewMessage(pattern='(?i)KOLGE+'))
@client.on(events.NewMessage(pattern='(?i)KOLGƏ+'))
@client.on(events.NewMessage(pattern='(?i)kabus+'))
@client.on(events.NewMessage(pattern='(?i)niko+'))
@client.on(events.NewMessage(pattern='(?i)nara+'))
@client.on(events.NewMessage(pattern='(?i)@Geldim000+'))
@client.on(events.NewMessage(pattern='(?i)Emin+'))
@client.on(events.NewMessage(pattern='(?i)emın+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(sesizKOLGE)}")

@client.on(events.NewMessage(pattern='(?i)ban+'))
@client.on(events.NewMessage(pattern='(?i)kick+'))
@client.on(events.NewMessage(pattern='(?i)mute+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ban)}")
    
@client.on(events.NewMessage(pattern='(?i)🙄+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(emoji1)}")

@client.on(events.NewMessage(pattern='(?i)😂+'))
@client.on(events.NewMessage(pattern='(?i)🤣+'))
@client.on(events.NewMessage(pattern='(?i)😅+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(emoji2)}")

@client.on(events.NewMessage(pattern='(?i)xaos+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(fed)}")
 
@client.on(events.NewMessage(pattern='(?i)niye+'))
@client.on(events.NewMessage(pattern='(?i)nıye+'))
@client.on(events.NewMessage(pattern='(?i)niyə+'))
@client.on(events.NewMessage(pattern='(?i)nıyə+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(niye)}")

    
@client.on(events.NewMessage(pattern='(?i)ne+'))
@client.on(events.NewMessage(pattern='(?i)nə+'))
@client.on(events.NewMessage(pattern='(?i)what+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ne)}")
   
@client.on(events.NewMessage(pattern='(?i)hay+'))
@client.on(events.NewMessage(pattern='(?i)hiy+'))
@client.on(events.NewMessage(pattern='(?i)hııy+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(hay)}")
    
@client.on(events.NewMessage(pattern='(?i)mal+'))
@client.on(events.NewMessage(pattern='(?i)maal+'))
@client.on(events.NewMessage(pattern='(?i)qoyun+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(mal)}")
    
    
@client.on(events.NewMessage(pattern='(?i)can+'))
@client.on(events.NewMessage(pattern='(?i)haycan+'))
@client.on(events.NewMessage(pattern='(?i)uşş+'))
@client.on(events.NewMessage(pattern='(?i)uss+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(can)}")
    
    
@client.on(events.NewMessage(pattern='(?i)balam+'))
@client.on(events.NewMessage(pattern='(?i)quzum+'))
@client.on(events.NewMessage(pattern='(?i)❤+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(balam)}")
   
@client.on(events.NewMessage(pattern='(?i)xoş+'))
@client.on(events.NewMessage(pattern='(?i)xos+'))
@client.on(events.NewMessage(pattern='(?i)gününə+'))
@client.on(events.NewMessage(pattern='(?i)gününe+'))
@client.on(events.NewMessage(pattern='(?i)gunune+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(xos)}")
     
@client.on(events.NewMessage(pattern='(?i)hara+'))
@client.on(events.NewMessage(pattern='(?i)havaq+'))
@client.on(events.NewMessage(pattern='(?i)hansı+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(hara)}")
    
@client.on(events.NewMessage(pattern='(?i)gel+'))
@client.on(events.NewMessage(pattern='(?i)gəl+'))
@client.on(events.NewMessage(pattern='(?i)gelde+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(gel)}")
    
@client.on(events.NewMessage(pattern='(?i)gordum+'))
@client.on(events.NewMessage(pattern='(?i)gördüm+'))
@client.on(events.NewMessage(pattern='(?i)gördün+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(gordum)}")

######    TAĞ MODULU   #########    
    
    

    
    

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**⚡ Mən  𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ**\n**𝕏𝔸𝕆𝕊 Federasiyasının Rəsmi Tağ botuyam**\n**⚡ 𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ İlə Qrupunuzdakı Üyələri Etiket Edə Bilərəm**\n**Əmrlərlə Tanış Olmaq Üçün __ƏMRLƏR__ Butonuna Toxun**\n**ℹ Mənim Qruplarda Asan Və Sürətli İşləyə Bilməyim Üçün Mənə Qrupunuzda Sadə Adminlik Vermənizi Rica Edirem**",
                    buttons=(
                   
		      [Button.url('➕ ℚℝ𝕌ℙ𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Tagbot?startgroup=a')],
                      [Button.url('⚡ 𝕏𝔸𝕆𝕊 𝔽𝔹𝔸ℕ', f'https://t.me/XaosResmii')],
                      [Button.url('🇦🇿 𝕆𝕎ℕ𝔼ℝ 👨‍💻', f'https://t.me/sesizKOLGE')],
                      [Button.inline("⚙ Ə𝕄ℝ𝕃Ə𝕃", data="help")],
                    ),
                    link_preview=False
		   )

@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    await event.edit(f"**⚡ Mən  𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ**\n**𝕏𝔸𝕆𝕊 Federasiyasının Rəsmi Tağ botuyam**\n**⚡ 𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ İlə Qrupunuzdakı Üyələri Etiket Edə Bilərəm**\n**ℹƏmrlərlə Tanış Olmaq Üçün __ƏMRLƏR__ Butonuna Toxun**\n**ℹ Mənim Qruplarda Asan Və Sürətli İşləyə Bilməyim Üçün Mənə Qrupunuzda Sadə Adminlik Vermənizi Rica Edirem**", buttons=(
                      
                      [Button.url('➕ ℚℝ𝕌ℙ𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Tagbot?startgroup=a')],
                      [Button.url('⚡ 𝕏𝔸𝕆𝕊 𝔽𝔹𝔸ℕ', f'https://t.me/XaosResmii')],
                      [Button.url('🇦🇿 𝕆𝕎ℕ𝔼ℝ 👨‍💻', f'https://t.me/sesizKOLGE', "✔ ÖZƏLLİKLƏR", data="bot")],
                      [Button.inline("⚙ Ə𝕄ℝ𝕃Ə𝕃", data="help")],
                    ),
                    link_preview=False)

			     
@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):
    await event.edit(f"⚡ 𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ İn Əmrləri \n\n➪ /sehidler <səbəb> Şəhid Adları İlə Tağ Edər\n➪ /tag <səbəb> - 5-li Tağ Edər\n➪ /etag <səbəb> - Emoji İlə Tağ Edər\n➪ /btag <səbəb> - Bayraqlarla Tağ Edər\n➪ /mtag <səbəb>  Mafia Rolları İlı Tağ Edər\n➪ /rtag <səbəb> Rayon Və Şəhər Adları İlə Tağ Edər\n➪ /htag <səbəb> Heyvan Adları İlə Tağ Edər\n➪ /ttag <səbəb> - Tək Teək Tağ Edər\n➪ /admin <səbəb> - Adminləri Tağ Edər\n➪ /cancel - Tağ Prosesin Saxlayar\n➪ /start - Botu Başladar", buttons=(
                      [Button.url('➕ ℚℝ𝕌ℙ𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Tagbot?startgroup=a')],
	              [Button.inline("ℹ 𝕀ℕ𝔽𝕆", data="info")],
                      [Button.inline("🗑 𝔹𝔸𝔾𝕃𝔸", data="start")],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="info"))
async def handler(event):
    await event.edit(f"**Çox Özəllikli Tağ Botu Axtarmağa Çalışan Qrub Sahibləri  ⚡  𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ Bot Sizə Görə:\n\n☞︎︎︎ Şəhid Adları İlə Tağ Edər\n☞︎︎︎ 5-Li Tağ\n☞︎︎︎ Emojilərlə Tağ Edər\n☞︎︎︎ Heyvan Adları İlə Tağ Edər\n☞︎︎︎ Bayraqlarla Tağ Edər\n☞︎︎︎ Mafia Rolları İlə Tağ Edər\n☞︎︎︎ Rayon Və Şəhər Adları İlə Tağ Edər\n☞︎︎︎ Təkli Tağ\n☞︎︎︎ Yalnız Admimləri Tağ\n\n\nBelə Çox Özəllikli @XAOS_Tagbot 'u Qrupunuza Yönətici Olaraq Alıb Rahatlıqla , Tağ edə bilirsiz**\n\n**📢  QRUPDA ADMİNLİK MÜTLIQDİ**", buttons=(      
	              [Button.url('➕ ℚℝ𝕌ℙ𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Tagbot?startgroup=a')],
		      [Button.inline("⚙ 𝔼𝕊𝔸𝕊 𝕄𝔼𝕐ℕ𝕌", data="start")],
		    ),
                    link_preview=False)
                   
	
	

	
sehidler = "Qəzənfər Nəcəf Nurlan İnqilab Nicat Mirnəbi Məhəmməd Ramazan Telman Fazil Qələndər Nofəl İbrahim Habil Elşən Sabir Həsən Qər󠁧󠁢󠁷󠁬󠁳󠁿󠁧󠁢󠁷󠁬󠁳󠁿ib Ceyhun Mübariz Polad Cəbrayıl ".split(" ")


@client.on(events.NewMessage(pattern="^/sehidler ?(.*)"))
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


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	
	

seherler = "Ağcabədi Ağdam Ağdaş Ağdərə Ağıstafa Ağsu Astara Babək Bakı Balakən Beyləqan Bərdə Biləsuvar Cəbrayıl Cəlilabad Culfa Daşkəsən Dəliməmmədli Xocalı Füzuli Gədəbəy Gəncə Goranboy Göyçay Göygöl Göytəpə Hacıqabul Horadiz Xaçmaz Xankəndi Xocalı Xocavənd Xırdalan Xızı Xudat İmişli İsmayıllı Kəlbəcər Kürdəmir Qax Qazax Qəbələ Qobustan Qovlar Quba Qubadlı Qusar Laçın Lerik Lənkəran Liman Masallı Naftalan Naxçıvan Neftçala Oğuz Ordubad Saatlı Sabirabad Salyan Samux Siyəzən Sumqayıt Şuşa Şabran Şahbuz Şamaxı Şəki Şəmkir Şərur Şirvan Tərtər Tovuz Ucar Yardımlı Yevlax Zaqatala Zəngilan Zərdab󠁧󠁢󠁷󠁬󠁳󠁿󠁧󠁢󠁷󠁬󠁳󠁿".split(" ")


@client.on(events.NewMessage(pattern="^/rtag ?(.*)"))
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


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	
mafia = "👨‍🌾Vətəndaş 👨‍✈️Komissar Kattani 👨‍💼Çavuş 👨‍⚕️Doktor 🧟‍♀️Cadugar 🕵️Suiqəstçi 🧔Bomj 🦎Buqələmun 💂🏻Securıty 👳🏻‍♂️Satıcı 🙇🏻‍♂️Oğru 👷🏻‍♂️Mədənçi ⭐️General 🧝🏻‍♀️Şəhzadə 🎧DJ 🏦Bankir 🕴Don 🕺Mafia 👨‍⚖️Vəkil 🙍🏻‍♂️Məhbus 👨🏻‍🦱Dedektiv  🦦Köstəbək 👨🏻‍🎤Specialist 🔪Manyak 🤡Joker 👻Ruh 🧚🏻‍♀️Mələk 🦹🏻‍♂️BOSS 🥷Ninja 🥷SUPER Ninja 👨🏻‍🦲Dəli 🔮Reviver 💂Killer 🧛🏻‍♂️Vampir󠁧󠁢󠁷󠁬󠁳󠁿󠁧󠁢󠁷󠁬󠁳󠁿".split(" ")


@client.on(events.NewMessage(pattern="^/mtag ?(.*)"))
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


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	
bayrag = "🇦🇨 🇦🇩 🇦🇪 🇦🇫 🇦🇬 🇦🇮 🇦🇱 🇦🇴 🇦🇶 🇦🇷 🇦🇸 🇦🇹🇦🇺 🇦🇼 🇦🇽 🇦🇿 🇧🇦 🇧🇧 🇧🇩 🇧🇪 🇧🇫 🇧🇬 🇧🇭 🇧🇮🇧🇯 🇧🇱 🇧🇲 🇧🇳 🇧🇴 🇧🇶 🇧🇷 🇧🇸 🇧🇹 🇧🇻 🇧🇼 🇧🇾🇧🇿 🇨🇦 🇨🇨 🇨🇩 🇨🇫 🇨🇬 🇨🇭 🇨🇮 🇨🇰 🇨🇱 🇨🇲 🇨🇳🇨🇵 🇨🇷 🇨🇺 🇨🇻 🇨🇼 🇨🇽 🇨🇾 🇨🇿 🇩🇪 🇩🇬 🇩🇯 🇩🇰🇩🇲 🇩🇴 🇩🇿 🇪🇦 🇪🇨 🇪🇪 🇪🇬 🇪🇭 🇪🇷 🇪🇸 🇪🇹 🇪🇺🇫🇮 🇫🇯 🇫🇰 🇫🇲 🇫🇴 🇫🇷 🇬🇦 🇬🇧 🇬🇩 🇬🇪 🇬🇫 🇬🇬🇬🇭 🇬🇮 🇬🇱 🇬🇲 🇬🇳 🇬🇵 🇬🇶 🇬🇷 🇬🇸 🇬🇹 🇬🇺 🇬🇼🇬🇾 🇭🇰 🇭🇲 🇭🇳 🇭🇷 🇭🇹 🇭🇺 🇮🇨 🇮🇩 🇮🇪 🇮🇱 🇮🇲🇮🇳 🇮🇴 🇮🇶 🇮🇷 🇮🇸 🇮🇹 🇯🇪 🇯🇲 🇯🇴 🇯🇵 🇰🇪 🇰🇬🇰🇭 🇰🇮 🇰🇲 🇰🇳 🇰🇵 🇰🇷 🇰🇼 🇰🇾 🇰🇿 🇱🇦 🇱🇧 🇱🇨🇱🇮 🇱🇰 🇱🇷 🇱🇸 🇱🇹 🇱🇺 🇱🇻 🇱🇾 🇲🇦 🇲🇨 🇲🇩 🇲🇪🇲🇫 🇲🇬 🇲🇭 🇲🇰 🇲🇱 🇲🇲 🇲🇳 🇲🇴 🇲🇵 🇲🇶 🇲🇷 🇲🇸🇲🇹 🇲🇺 🇲🇻 🇲🇼 🇲🇽 🇲🇾 🇲🇿 🇳🇦 🇳🇨 🇳🇪 🇳🇫 🇳🇬🇳🇮 🇳🇱 🇳🇴 🇳🇵 🇳🇷 🇳🇺 🇳🇿 🇴🇲 🇵🇦 🇵🇪 🇵🇫 🇵🇬🇵🇭 🇵🇰 🇵🇱 🇵🇲 🇵🇳 🇵🇷 🇵🇸 🇵🇹 🇵🇼 🇵🇾 🇶🇦 🇷🇪🇷🇴 🇷🇸 🇷🇺 🇷🇼 🇸🇦 🇸🇧 🇸🇨 🇸🇩 🇸🇪 🇸🇬 🇸🇭 🇸🇮🇸🇯 🇸🇰 🇸🇱 🇸🇲 🇸🇳 🇸🇴 🇸🇷 🇸🇸 🇸🇹 🇸🇻 🇸🇽 🇸🇾🇸🇿 🇹🇦 🇹🇨 🇹🇩 🇹🇫 🇹🇬 🇹🇭 🇹🇯 🇹🇰 🇹🇱 🇹🇲 🇹🇳🇹🇴 🇹🇷 🇹🇹 🇹🇻 🇹🇼 🇹🇿 🇺🇦 🇺🇬 🇺🇲 🇺🇳 🇺🇸 🇺🇾🇺🇿 🇻🇦 🇻🇨 🇻🇪 🇻🇬 🇻🇮 🇻🇳 🇻🇺 🇼🇫 🇼🇸 🇽🇰 🇾🇪🇾🇹 🇿🇦 🇿🇲 🇿🇼 🏴󠁧󠁢󠁥󠁮󠁧󠁿 🏴󠁧󠁢󠁳󠁣󠁴󠁿 🏴󠁧󠁢󠁷󠁬󠁳󠁿󠁧󠁢󠁷󠁬󠁳󠁿".split(" ")


@client.on(events.NewMessage(pattern="^/btag ?(.*)"))
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


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	
	
emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")


@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
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


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)

	
	
heyvan = "Meymun🐵 İt🐕 At🐴 Tülkü🦊 Porsuq🐺 Pələng🦁 Çita🐆 Donuz🐷 İnək🐮 Öküz🐃 Zebra🦓 Maral🦌 Ceyran🦌 Qaban🐗 Mişoul🐀 Yarasa🦇 Xoruz🐓 Toyuq🐔 Cücə🐥 Göyərçin🕊 Sərçə🐦 Qartal🦅 Dinazavur🦖 Timsah🐊 Qurbağa🐸 Papuqayı🦜 Tovuzquşu🦚 Kərtənkələ🦎 Tısbağa🐢 İlan🐍 Balina🐬 Balıq🐟 İlbiz🐌 Kəpənək🦋 Qarışqa🐜 Arı🐝 Mikrob🦠 Virus🦠 Xərçəng🦂 Çəyirtkə🦗 Parabüzən🐞 Hörümçək🦂 Ördək🦆 Bayquş🦉 Hünduşqa🦃 Pinqivin🐧 Ayı🐻 Panda🐼".split(" ")
@client.on(events.NewMessage(pattern="^/htag ?(.*)"))
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


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
			
		
		
@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
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

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/ttag ?(.*)"))
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

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	
@client.on(events.NewMessage(pattern="^/admin ?(.*)"))
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
