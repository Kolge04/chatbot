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
    await event.edit(f"📊 [𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ](https://t.me/XAOS_Tagbot) Un  İstatiskası\n\n📋 Toplam Qrup: `{len(grup_sayi)}`\n📈 Aktuv Qruplar: `{len(anlik_calisan)}`\n👤 İsdifadəçi Sayı: `{len(user_sayi)}`")
	              
                     
	    
	                

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
@client.on(events.NewMessage(pattern="^.stag ?(.*)"))
async def mentionall(event):
    await event.reply("🤔 **USERLƏRİ NECƏ TAG EDİM** ❓",
		      buttons=(
		      [Button.inline("🇦🇿 AZƏRBAYCAN CA", data="aze")],
                      [Button.inline("🇹🇷 TÜRK CƏ", data="tr")],
                    ),
                    link_preview=False
		   )
asoz = (
"Mən boşalan qədəhlərin deyil sənsizliyin sərxoşuyam.",
"Salam,xanım, necəsiniz? Allah sizə hərşey verib, bir mənim nömrəmdən başqa",
"Salam xanım Nərimanovda qalıram burdan xoşunuza necə gələ bilərəm?", 
"Xanım mən sizə gəlim sən anama gəlin gəl",
"Dünyanın ən gözəl hissi sənin şəxsidə yazmaq bəhanəndi",
"Gəl səninlə natural ədəd kimi olaq. Başlanğıcımız olsun, sonumuz olmasın",
"Bir səs eşidirsən? Bu sənin üçün atan qəlbimin səsidir",
"Könlüm qəmi neylər dilin nəğmələr söylər təki mənə bircə kəlmə sevirəm de..",
"Yeni ilə son günlər qalıb 'Staliçni' salatı bir yerdə yeyib AzTv-yə baxarıq🫂",
"Səni elə sevərəm ki, sənən başqa dünyada adam olub olmadığını yoxlayarsan",
"Şəxsidə 'Sizə sözüm var' bəhanəsi ilə yazıb qəlbinizə daxil ola bilərəm?",
"Yağış yağdı, Sən isə bal",
"Bəzi insanlar yağışı hiss edər, digərləri isə sadəcə islanar",
"Unutma; Hər gələn sevməz.. Və heç bir sevgili getməz",
"Heç bir ruhun ağrısı sənin dərdindən az deyil",
"Mən hər şeyi sınayıram; amma bacardığımı edirəm.",
"Sevgi bir qadının həyatının bütün hekayəsidir və bir kişinin yeganə macərasıdır.",
"Xoşbəxtlik ilk növbədə bədən sağlamlığındadır.",
"Nə qədər yaşadığımız deyil, necə yaşadığımızdır",
"Yer göy qurşağı, ağıl prizma, varlıq isə ağ şüadır.",
"Hara getdiyinizi bilmirsinizsə, hansı tərəfə getdiyinizin əhəmiyyəti yoxdur.",
"Həyatın ən qiymətli vaxtıdır. Kimə hədiyyə etdiyinizə diqqət edin.",
"Evin bütün pəncərələrini sındırıb, sonra qapını döyə bilməzsən.",
"Xoşbəxtlik yaşadığın həyat tərzində deyil, həyata baxış tərzindədir.",
"Unutma; Hər gələn sevməz.. Və heç bir sevgili getməz.",
"Bu həyatda yarım nəfəs. Sevgidən başqa heç nə planlaşdırma...",
"Hər kəsə içindəki yaxşılar qədər yaxşı bir həyat arzulayıram.",
"Gözəlliyi gözəl edən ədəbdir, ədəb isə gözəlliyi sevmək üçün səbəbdir!",
"Qızılgülün ətri qızılgül verənin əlində qalır",
"Axtardığın şey səni axtarandır.",
"Hətta bir quş da göydə qanad çırpar.",
"Könül almağı bilməyənlərə həyat əmanət deyil.",
"Dürüst olmaqdan qorxma, ən çox itirəcəyiniz yanlış insanlar olacaq.",
"İnsan ağac deyil, qırılanda səs çıxararsan.",
"Öyrənmək həyatın yeganə sübutudur.",
"Dünya əhalisi artdıqca insanların sayı azalır.",
"Layiq olmadığını düşündüyünüz insanlara əsla həqiqəti deməyin.",
"Çox şükür ki, göy hələ heç bir pul kisəsinə sığmır.",
"Özün ol. Artıq hamı götürüb.",
"Zərər çəkdim, boğazımdakı düyünləri uddum.",
"O qədər gözəl gülümsəyirdi ki, sevməsəydim boşuna olardı.",
"Onun sevdiyi men deyilem. Bunun ağrısını sizə deyə bilmərəm.",
"Onun sevdiyi men deyilem. Bunun ağrısını sizə deyə bilmərəm.",
"Zamanla hər şeyə alışırsan, amma bitmir.",
"Əgər həqiqəti deyirsənsə, heç nəyi xatırlamağa ehtiyac yoxdur.",
"Həqiqəti ilk söyləyən siz olun... Əks halda kimsə sizin yerinizə mütləq həqiqəti söyləyəcək.",
"Kişilər daha güclü ola bilər, amma qadınlar dözümlüdürlər.",
"Ağrı üçün heç bir resept yoxdur",
"Ardınca getməyə cəsarətiniz varsa, bütün arzular gerçəkləşə bilər.",
"Bu gizli sevgidir, heç kimə dərdlərimi deyə bilmərəm.",
"Sizcə sevgi hər şeyi bağışlayır?",
"Mənə də, sənə də siqaret lazımdır",
"Mən səndən xüsusi birini tanımırdım",
"Bir gün sevgi bitər, xatirələr qalır",
"Sevmək nə qədər uzun bir sözdür!",
"Hatırladığım en unutulası şeysin.",
"Birlikdə gülmək üçün darıxdığım insanlar var.",
"Xoşbəxtliyi səndə tapan sənindir, üstəlik qonaq.",
"Çox sev, amma bəyənmirsənsə məcbur etmə!",
"O qədər gözəl gülürdü ki, sevməsəm ziyan olacaqdı.",
"və insan insana yoldaş olmalı yaralarını sağalatmalı",
"Məzarlıq, əsəb uğruna peşman olanlarla dolu",
"Eşq külək kimidir görməzsən ama hiss edə bilərsən.",
"tərəzi var ölçü var , hərşeyin bir vaxtı var",
"Yanıltmasın səni masum baxışlar, bəzılarını şeytan ayaqdə alqışlar...",
"həyat sabahı gözləyəcək qədər uzun deyil",
"Yaxşılar əsla itirməz , itirilir.",
"görməzden gəldiyin sevgiyə möhtac qalman diləyiylə",
"Kaşki ağıl vermək yerinə hüzur versəniz",
"Heç bilmədiyim o qoxunu çox özləyirəm",
"𝑌𝑎𝑥𝑠‌𝚤 𝑜𝑙𝑎𝑛 𝑖𝑡𝑖𝑟𝑠𝑒𝑑𝑒 𝑞𝑎𝑧𝑎𝑛ı𝑟",
"𝐴ş𝑖𝑞 𝑜𝑙𝑚𝑎𝑞 𝑔𝑜‌𝑧ə𝑙 𝑏𝑖𝑟 ş𝑒𝑦 𝑎𝑚𝑎 𝑠𝑎𝑑ə𝑐ə 𝑠ənə",
"𝐻𝑒𝑐‌𝑘𝑖𝑚 ℎ𝑒𝑐‌𝑘𝑖𝑚𝑖 𝑖𝑡𝑖𝑟𝑚𝑒𝑧 𝑔𝑖𝑑ə𝑛 𝑏𝑎ş𝑞𝑎𝑠ı𝑛ı 𝑡𝑎𝑝𝑎𝑟, 𝑞𝑎𝑙𝑎𝑛 𝑜‌𝑧𝑢‌𝑛𝑢‌",
"Ç𝑜𝑥 ö𝑛ə𝑚𝑠ə𝑑𝑖𝑘 𝑖şə 𝑦𝑎𝑟𝑎𝑚𝑎𝑑ı 𝑎𝑟𝑡𝚤𝑞 𝑏𝑜ş𝑣𝑒𝑟𝑖𝑟𝑖𝑘",
"Ö𝑚𝑟ü𝑛ü𝑧ü 𝑠𝑢𝑠𝑑𝑢𝑞𝑙𝑎𝑟𝚤𝑛𝚤𝑧𝚤 𝑒𝑠‌𝑖𝑑𝑒𝑛 𝑏𝑖𝑟𝑖𝑦𝑙ə 𝑘𝑒ç𝑖𝑟𝑖𝑛",
"𝐺ö𝑛𝑙ü𝑛ü𝑧ə 𝑎𝑙𝑑ığı𝑛ı𝑧 𝑔ö𝑛𝑙ü𝑛ü𝑧ü 𝑎𝑙𝑚𝑎𝑔‌ı 𝑏𝑖𝑙𝑠𝑖𝑛",
"𝑆ə𝑛 ç𝑜𝑥 𝑠𝑒𝑣 𝑑𝑒 𝑏𝑢𝑟𝑎𝑥ı𝑏 𝑔𝑖𝑑ə𝑛 𝑦𝑎𝑟 𝑢𝑡𝑎𝑛𝑠ı𝑛",
"𝑌𝑎𝑥𝑠‌𝚤 𝑜𝑙𝑎𝑛 𝑖𝑡𝑖𝑟𝑠ə𝑑ə 𝑞𝑎𝑧𝑎𝑛ı𝑟",
"𝑆𝑎𝑣𝑎ş𝑚𝑎𝑦ı 𝑏𝑢𝑟𝑎𝑥𝚤𝑟𝑎𝑚 𝑏𝑢𝑛𝑢 𝑣𝑒𝑑𝑎 𝑠𝑎𝑦",
"𝑁ə 𝑖ç𝑖𝑚𝑑ə𝑘𝑖 𝑘𝑢‌𝑐‌ə𝑙ə𝑟ə 𝑠ığ𝑎𝑏𝑖𝑙𝑑𝑖𝑚 𝑁ə 𝑑ə 𝑐‌𝑜‌𝑙𝑑ə𝑘𝑖 𝑑ü𝑛𝑦𝑎𝑦𝑎", 
"𝐴𝑟𝑡ı𝑞 ℎ𝑒ç𝑏𝑖𝑟 ş𝑒𝑦 ə𝑣𝑣ə𝑙𝑘𝑖 𝑘𝑖𝑚𝑖 𝑑𝑒𝑦𝑖𝑙 𝐵𝑢𝑛𝑎 𝑚ə𝑛𝑑ə 𝑑𝑎𝑥𝑖𝑙ə𝑚", 
"𝐴ş𝑖𝑞 𝑜𝑙𝑚𝑎𝑞 𝑔𝑜‌𝑧𝑒𝑙 𝑏𝑖𝑟 ş𝑒𝑦 𝑎𝑚𝑎 𝑠𝑎𝑑ə𝑐ə 𝑠ə𝑛ə", 
"İ𝑛𝑠𝑎𝑛 𝑎𝑛𝑙𝑎𝑑ığı 𝑣𝑒 𝑎𝑛𝑙𝑎şı𝑙𝑑ığı 𝑖𝑛𝑠𝑎𝑛𝑑𝑎 ç𝑖çə𝑘 𝑎ç𝑎𝑟",
"𝑌𝑎𝑥𝑠‌𝚤𝑦𝑎𝑚 𝑑𝑒𝑠ə𝑚 𝑖𝑛𝑎𝑛𝑎𝑐𝑎𝑞, 𝑜 𝑘ə𝑑ə𝑟 𝑥ə𝑏ə𝑟𝑠𝑖𝑧 𝑚ə𝑛𝑑ə𝑛", 
"𝐸𝑙ə 𝑔𝑜‌𝑧ə𝑙 𝑏𝑎𝑥𝑡ı 𝑘𝑖 𝑞ə𝑙𝑏𝑖 𝑑ə 𝑔ü𝑙üşü 𝑞ə𝑑ə𝑟 𝑔𝑜‌𝑧ə𝑙 𝑠𝑎𝑛𝑚ış𝑡ı𝑚",
"𝑀ə𝑠𝑎𝑓ə𝑙ə𝑟 𝑈𝑚𝑟𝑢𝑚𝑑𝑎 𝐷𝑒𝑦𝑖𝑙, İç𝑖𝑚𝑑ə 𝐸𝑛 𝐺ü𝑧ə𝑙 𝑌𝑒𝑟𝑑ə𝑠ə𝑛",
"İ𝑛𝑠𝑎𝑛 𝑏ə𝑧ə𝑛 𝑏𝑜‌𝑦ü𝑘 𝑥ə𝑦𝑎𝑙𝑙𝑎𝑟𝚤𝑛𝚤 𝑘𝑖ç𝑖𝑘 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑙𝑎 𝑧𝑖𝑦𝑎𝑛 𝑒𝑑ə𝑟",
"𝐻𝑒𝑐‌𝑘𝑖𝑚 ℎ𝑒𝑐‌𝑘𝑖𝑚𝑖 𝑖𝑡𝑖𝑟𝑚ə𝑧 𝑔𝑒𝑑ə𝑛 𝑏𝑎ş𝑞𝑎𝑠ı𝑛ı 𝑡𝑎𝑝𝑎𝑟 𝑞𝑎𝑙𝑎𝑛 𝑜‌𝑧𝑢‌𝑛𝑢‌",
"Ç𝑜𝑥 ö𝑛ə𝑚𝑠ə𝑑𝑖𝑘 𝑖şə 𝑦𝑎𝑟𝑎𝑚𝑎𝑑ı 𝑎𝑟𝑡ı𝑞 𝑏𝑜ş𝑣𝑒𝑟𝑖𝑟𝑖𝑘", 
"𝐵𝑖𝑟 ç𝑖ç𝑒𝑘𝑙𝑒 𝑔ü𝑙𝑒𝑟 𝑞𝑎𝑑ı𝑛 𝑏𝑖𝑟 𝑙𝑎𝑓𝑙𝑎 ℎü𝑧ü𝑛",
"𝐻ə𝑟 ş𝑒𝑦𝑖 𝑏𝑖𝑙ə𝑛 𝑑𝑒𝑦𝑖𝑙 𝑞ı𝑦𝑚ə𝑡 𝑏𝑖𝑙ə𝑛 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟 𝑜𝑙𝑠𝑢𝑛 ℎə𝑦𝑎𝑡ı𝑛ı𝑧𝑑𝑎",
"𝑉𝑒𝑟𝑖𝑙ə𝑛 𝑑ə𝑦ə𝑟𝑖𝑛 𝑛𝑎𝑛𝑘𝑜𝑟𝑢 𝑜𝑙𝑚𝑎𝑦ı𝑛 𝑔𝑒𝑟𝑖𝑠𝑖 ℎə𝑙𝑙𝑜𝑙𝑢𝑟",
"𝑀ə𝑠𝑎𝑓ə 𝑖𝑦𝑖𝑑𝑖𝑟 𝑁ə ℎə𝑑𝑑𝑖𝑛𝑖 𝑎ş𝑎𝑛 𝑜𝑙𝑢𝑟 𝑛ə 𝑑ə 𝑐𝑎𝑛ı𝑛ı 𝑠ı𝑥𝑎𝑛", 
"𝐻ə𝑦𝑎𝑡 𝑖rəl𝑖𝑦ə 𝑏𝑎𝑥ı𝑙𝑎𝑟𝑎𝑞 𝑦𝑎ş𝑎𝑛ı𝑟 𝑔𝑒𝑟𝑖𝑦ə 𝑏𝑎𝑥𝑎𝑟𝑎𝑞 𝑎𝑛𝑙𝑎şı𝑙ı𝑟",
"𝑆ə𝑛 ç𝑜𝑥 𝑠𝑒𝑣 , 𝑔𝑒𝑑ə𝑛 𝑦𝑎𝑟 𝑢𝑡𝑎𝑛𝑠ı𝑛",
"𝐵𝑖𝑟 𝑀𝑜‌𝑐𝑢‌𝑧ə𝑦ə 𝐸ℎ𝑡𝑖𝑦𝑎𝑐ı𝑚 𝑉𝑎𝑟 𝑖𝑑𝑖 𝐻ə𝑦𝑎𝑡 𝑆ə𝑛𝑖 𝑄𝑎𝑟şı𝑚𝑎 Çı𝑥𝑎𝑟𝑑ı",
"İ𝑛𝑠𝑎𝑛 𝑎𝑛𝑙𝑎𝑑ığı 𝑣ə 𝑎𝑛𝑙𝑎şı𝑙𝑑ığı 𝑖𝑛𝑠𝑎𝑛𝑑𝑎 ç𝑖çə𝑘 𝑎ç𝑎𝑟",
"𝑢‌𝑟ə𝑦𝑖𝑚𝑖𝑛 𝑡𝑎𝑚 𝑜𝑟𝑡𝑎𝑠ı𝑛𝑑𝑎 𝑏𝑜‌𝑦ü𝑘 𝑏𝑖𝑟 𝑦𝑜𝑟𝑔‌𝑢𝑛𝑙𝑢𝑞 𝑣𝑎𝑟",
"𝑄ə𝑙𝑏𝑖 𝑔𝑜‌𝑧ə𝑙 𝑜𝑙𝑎𝑛ı𝑛 𝑔ö𝑧ü𝑛𝑑ə𝑛 𝑦𝑎ş ə𝑘𝑠𝑖𝑘 𝑜𝑙𝑚𝑎𝑧𝑚ış",
"𝐻ə𝑟 ş𝑒𝑦𝑖𝑛 𝑏𝑖𝑡𝑑𝑖𝑦𝑖 𝑦𝑒𝑟𝑑ə 𝑚ə𝑛𝑑ə 𝑏𝑖𝑡𝑑𝑖𝑚 𝑑ə𝑦𝑖ş𝑑𝑖𝑛 𝑑𝑒𝑦ə𝑛𝑙ə𝑟𝑖𝑛 ə𝑠ə𝑟𝑖𝑦ə𝑚",
"𝐺ü𝑣ə𝑛𝑚ə𝑘 𝑠𝑒𝑣𝑚ə𝑘𝑑ə𝑛 𝑑𝑎ℎ𝑎 𝑑ə𝑦ə𝑟𝑙𝑖, 𝑍𝑎𝑚𝑎𝑛𝑙𝑎 𝑎𝑛𝑙𝑎𝑟𝑠ı𝑛",
"İ𝑛ş𝑎𝑙𝑙𝑎ℎ 𝑠ə𝑏𝑟𝑙ə 𝑔𝑜‌𝑧𝑙ə𝑑𝑖𝑦𝑖𝑛 ℎ𝑒𝑟 ş𝑒𝑦 𝑢‌𝑐‌𝑢‌𝑛 𝑥𝑒𝑦𝑖𝑟𝑙𝑖 𝑏𝑖𝑟 𝑥ə𝑏ə𝑟 𝑎𝑙ı𝑟𝑠ı𝑛",
"İ𝑛𝑠𝑎𝑛 𝑏ə𝑧ə𝑛 𝑏𝑜‌𝑦𝑢‌𝑘 𝑥ə𝑦𝑎𝑙𝑙𝑎𝑟𝚤𝑛𝚤 𝑘𝑖𝑐‌𝑖𝑘 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑙𝑎 𝑧𝑖𝑦𝑎𝑛 𝑒𝑑ə𝑟 ",
"Ö𝑙𝑚ə𝑘 𝐵𝑖𝑟 ş𝑒𝑦 𝑑𝑒y𝑖𝑙 𝑦𝑎ş𝑎𝑚𝑎𝑚𝑎𝑞 𝑞𝑜𝑟𝑥𝑢𝑛𝑐",
"𝐻ə𝑟𝑘ə𝑠𝑖𝑛 𝑏𝑖𝑟 𝑘𝑒ç𝑚𝑖ş𝑖 𝑣𝑎𝑟, 𝐵𝑖𝑟𝑑ə 𝑣𝑎𝑧𝑔𝑒ç𝑚𝑖ş𝑖",
"𝐺ü𝑐𝑙ü 𝑔ö𝑟ü𝑛ə 𝑏𝑖𝑙ə𝑟ə𝑚 𝑎𝑚𝑎 𝑖𝑛𝑎𝑛 𝑦𝑜𝑟𝑔‌𝑢𝑛𝑎𝑚",
"𝐻ə𝑦𝑎𝑡 𝑛ə 𝑔𝑒𝑑ə𝑛𝑖 𝑔𝑒𝑟𝑖 𝑔ə𝑡𝑖𝑟𝑖𝑟 𝑛ə𝑑ə 𝑖𝑡𝑖𝑟𝑑𝑖𝑦𝑖𝑛𝑖𝑧 𝑧𝑎𝑚𝑎𝑛ı 𝑔𝑒𝑟𝑖 𝑔ə𝑡𝑖𝑟𝑖𝑟", 
"𝐸𝑘𝑚𝑒𝑘 𝑝𝑎ℎ𝑎𝑙ı 𝑒𝑚𝑒𝑘 𝑢𝑐𝑢𝑧𝑑𝑢."
)
	
@client.on(events.NewMessage(pattern="^.sotag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qurup və kanallar üçün keçərlidi. ❗**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmr sadəcə adminlər istifadə edə bilər 〽️**")
  if event.pattern_match.group(0):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(0)
  elif event.reply_to_msg_id:
    mode = ""
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
      usrtxt += f"• [{random.choice(asoz)}](tg://user?id={usr.id})"
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Tag Prosesi Uğurla dayandırıldı")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"• [{random.choice(asoz)}](tg://user?id={usr.id})"
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Tag Prosesi Uğurla Dayandırıldı")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	








	
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
  if event.pattern_match.group(0):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(0)
  elif event.reply_to_msg_id:
    mode = ""
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
        await client.send_message(event.chat_id, f"{usrtxt}")
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
