import discord
from discord.ext import commands

# DİKKAT:
# Tokenini BURAYA yazacaksın; bu dosyayı asla kimseyle paylaşma,
# GitHub gibi yerlere yükleme. Sadece kendi bilgisayarında kalsın.
TOKEN = "MTQ0MjU3NDMwMDc3ODQ2MzI2Mg.GeQQ0f.zN-b7HuYF61BUuTJJx1O8AavsXx3BX5yRT-QIU"  # Örn: "MT....."

intents = discord.Intents.default()
# Komutları okuyabilmesi için message_content iznini açıyoruz
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

waste_data = {
    "plastik şişe": {
        "kategori": "geri dönüşüm (plastik kutusu)",
        "aciklama": "Mümkünse ezerek at, kapağını da ayrı topla.",
        "ayrisma": "yaklaşık 400–500 yıl",
    },
    "cam şişe": {
        "kategori": "geri dönüşüm (cam kutusu)",
        "aciklama": "Camlar sonsuza kadar geri dönüştürülebilir.",
        "ayrisma": "binlerce yıl (doğada neredeyse yok olmuyor)",
    },
    "kağıt": {
        "kategori": "geri dönüşüm (kâğıt kutusu)",
        "aciklama": "Temiz ve kuru kâğıtları geri dönüşüme at.",
        "ayrisma": "2–6 hafta",
    },
    "muz kabuğu": {
        "kategori": "organik atık / kompost",
        "aciklama": "Mümkünse kompost yapabilirsin.",
        "ayrisma": "yaklaşık 3–4 hafta",
    },
    "poşet": {
        "kategori": "geri dönüşüm (plastik) veya yakma tesisi",
        "aciklama": "Tekrar kullanmaya çalış, mümkünse bez çanta tercih et.",
        "ayrisma": "10–20 yıl (bazı türleri çok daha uzun)",
    },
    "alüminyum kutu": {
        "kategori": "geri dönüşüm (metal kutusu)",
        "aciklama": "İçecek kutularını mümkünse hafifçe çalkala ve ez.",
        "ayrisma": "yaklaşık 200–500 yıl",
    },
}


def normalize_item(text: str) -> str:
    return text.strip().lower()


@bot.event
async def on_ready():
    print(f"Bot giriş yaptı: {bot.user}")


@bot.command(name="çöp")
async def cop(ctx, *, esya: str):
    key = normalize_item(esya)
    data = waste_data.get(key)

    if not data:
        await ctx.send(
            f"{esya}** için veri bulamadım. Daha genel bir isimle tekrar dener misin?\n"
            f"Örn: plastik şişe, cam şişe, kağıt, muz kabuğu, poşet, alüminyum kutu"
        )
        return

    await ctx.send(
        f"{esya}** için öneri:\n"
        f"- *Kutusu*: {data['kategori']}\n"
        f"- *Not*: {data['aciklama']}"
    )


@bot.command(name="ayrışma")
async def ayrisma(ctx, *, esya: str):
    key = normalize_item(esya)
    data = waste_data.get(key)

    if not data or not data.get("ayrisma"):
        await ctx.send(
            f"{esya}** için ayrışma süresi verisi bulamadım. "
            f"Listeye eklememi istersen söyleyebilirsin."
        )
        return

    await ctx.send(
        f"{esya}** doğada *{data['ayrisma']}* sürede ayrışır (tahmini).\n"
        f"Çevreyi korumak için mümkün olduğunca *yeniden kullan* ve *geri dönüştür*."
    )


if __name__ == "__main__":
    # Buraya tokenini direkt yazdığın için bu dosyayı kimseye verme.
    bot.run(TOKEN)