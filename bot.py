import asyncio
from telethon import TelegramClient
import os

# Render ortam değişkenlerinden veya doğrudan buraya yazabilirsiniz
api_id = '38484685'
api_hash = '80294070fc9aec98068648ea313873b0'

grup_listesi = [
    'illegalforshell',
    'sohbetstrixz',
    'CHEIFTICARET',
    'gayrimesruturkye',
    'ticaretforumofficiall',
    'illegalsticaret',
    'jokerillegalticaret',
    'illegalsincahat',
    'AuraTicaret',
    'gustoillegalticaret'
]

mesaj = """TÜM PLATFORMLARDA SMS ONAY

WHATSAP SATIŞ YD TR

TELEGRAM SATIŞ TR YD

KİMLİK BİLGİLERİ

KİŞİ SORGULAMA VE PANELİ

İNSTAGRAM BEĞENİ VE TAKİPÇİ ATIŞ

TİKTOK BEĞENİ VE TAKİPÇİ ATIŞ

TELEGRAM KİŞİYE ÖZEL BOT KURMA"""

bekleme_suresi = 2462

client = TelegramClient('oturum_adi', api_id, api_hash)

async def toplu_mesaj_gonder():
    for grup in grup_listesi:
        try:
            hedef = f"@{grup}"
            await client.send_message(hedef, mesaj)
            print(f"Başarıyla gönderildi: {hedef}")
            await asyncio.sleep(bekleme_suresi)
        except Exception as e:
            print(f"Hata oluştu ({grup}): {e}")

with client:
    client.loop.run_until_complete(toplu_mesaj_gonder())
