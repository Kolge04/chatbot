



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
@Nermin.on(events.NewMessage(pattern='(?i)maal+'))
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
    
    

    
    








  

		



    
    
    
   
    

client_run = client_start.decode("utf8")
print(">> Chat bot işləyir ♿ <<")
print(f"{client_run}")
client.run_until_disconnected()
