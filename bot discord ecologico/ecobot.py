import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="eco.", intents=intents)

#questo è un bot ecologico con comandi per la differienziata no sus no meme , nella lista ci devono essere i comandi del bot
@bot.command()
async def lista(ctx):
    await ctx.send("ecco la lista dei comandi ")

ambiente_list = [
    "💡 Spegni le luci quando non servono",
    "💡 Usa lampadine a LED",
    "🚰 Chiudi l’acqua mentre ti lavi i denti",
    "🚿 Fai docce più brevi",
    "🧴 Usa meno plastica monouso",
    "🥤 Porta una borraccia riutilizzabile",
    "🛍️ Usa borse di stoffa",
    "♻️ Ricicla correttamente",
    "🍽️ Riduci gli sprechi alimentari",
    "🛒 Compra solo ciò che serve",

    "🌍 Scegli prodotti locali",
    "🍎 Mangia frutta di stagione",
    "🥦 Riduci il consumo di carne",
    "🚌 Usa i mezzi pubblici",
    "🚶 Vai a piedi quando puoi",
    "🚲 Usa la bicicletta",
    "🚗 Condividi l’auto",
    "⛽ Spegni il motore da fermo",
    "🛞 Controlla la pressione delle gomme",
    "❄️ Usa meno aria condizionata",

    "🏠 Isola bene la casa",
    "🌡️ Abbassa il riscaldamento",
    "🔌 Usa elettrodomestici efficienti",
    "🧺 Lava a basse temperature",
    "🌬️ Evita l’asciugatrice",
    "☀️ Stendi i panni all’aria",
    "🔧 Ripara invece di buttare",
    "🔁 Riutilizza gli oggetti",
    "🎁 Dona ciò che non usi",
    "🪑 Compra prodotti durevoli",

    "🚫🥤 Evita usa e getta",
    "🍽️ Usa stoviglie riutilizzabili",
    "📄 Riduci l’uso della carta",
    "🖨️ Stampa solo se necessario",
    "📘 Usa carta riciclata",
    "🌳 Pianta alberi",
    "🌿 Cura il verde",
    "🚯 Non buttare rifiuti in natura",
    "🐾 Rispetta gli animali",
    "🐝 Proteggi le api",

    "🧼 Usa detersivi ecologici",
    "🛢️ Non versare olio nello scarico",
    "🚜 Riduci pesticidi",
    "🌱 Fai compost",
    "🥕 Separa l’organico",
    "🛒 Compra sfuso",
    "📦 Riduci imballaggi",
    "🧽 Evita microplastiche",
    "💄 Usa cosmetici ecologici",
    "🔥 Riduci acqua calda",

    "🔌 Scollega caricabatterie",
    "🔘 Usa multiprese con interruttore",
    "☀️ Scegli energie rinnovabili",
    "🔋 Installa pannelli solari",
    "🏢 Sostieni aziende green",
    "📚 Informati sull’ambiente",
    "🗣️ Sensibilizza gli altri",
    "🧹 Partecipa a pulizie ambientali",
    "🏞️ Proteggi i parchi naturali",
    "📜 Rispetta le regole ambientali",

    "💻 Riduci consumo digitale",
    "📧 Cancella email inutili",
    "📺 Riduci streaming in HD",
    "⏻ Spegni dispositivi inutili",
    "📱 Allunga la vita dei dispositivi",
    "🖥️ Ricicla elettronica",
    "👕 Evita fast fashion",
    "🧥 Compra vestiti di qualità",
    "🪡 Ripara i vestiti",
    "🔄 Scambia abiti",

    "✈️ Viaggia in modo sostenibile",
    "🗺️ Rispetta i luoghi visitati",
    "🦌 Non disturbare la fauna",
    "🧴 Usa creme solari ecologiche",
    "🌼 Non raccogliere piante protette",
    "🔇 Riduci rumore",
    "🚰 Chiudi bene i rubinetti",
    "🚿 Usa riduttori di flusso",
    "🚱 Bevi acqua del rubinetto",
    "🌍 Ricorda che ogni gesto conta 💚"
]
@bot.command()
async def consigli(ctx):
    await ctx.send("facendo questo aiuti l'ambiente: " + random.choice(ambiente_list))

plastica_list = [
    "🚫🥤 Evita bottiglie di plastica monouso",
    "🥤 Usa una borraccia riutilizzabile",
    "🛍️ Porta borse di stoffa per la spesa",
    "🍽️ Evita piatti e posate di plastica",
    "🥡 Riduci l’uso di contenitori usa e getta",
    "♻️ Ricicla correttamente la plastica",
    "🧃 Preferisci confezioni in vetro",
    "📦 Riduci gli imballaggi inutili",
    "🛒 Compra prodotti sfusi",
    "🧴 Riutilizza i flaconi",

    "🪥 Usa spazzolini biodegradabili",
    "🧼 Evita microplastiche nei cosmetici",
    "🧽 Scegli spugne naturali",
    "🧃 Evita cannucce di plastica",
    "🥄 Usa cannucce riutilizzabili",
    "🍱 Porta il pranzo da casa",
    "🥪 Avvolgi il cibo con stoffa cerata",
    "🧊 Evita sacchetti di plastica per il ghiaccio",
    "🍎 Compra frutta senza imballaggi",
    "🧺 Usa sacchetti riutilizzabili",

    "🧴 Compra detersivi alla spina",
    "🧼 Usa saponi solidi",
    "🚿 Evita flaconi usa e getta",
    "🪒 Usa rasoi riutilizzabili",
    "🧴 Scegli shampoo solidi",
    "👶 Evita prodotti plastici inutili",
    "🧸 Preferisci giochi senza plastica",
    "🪑 Compra oggetti durevoli",
    "🔁 Riutilizza prima di buttare",
    "🛠️ Ripara gli oggetti rotti",

    "🏖️ Non lasciare plastica in spiaggia",
    "🌊 Proteggi mari e oceani",
    "🐢 Evita plastica che danneggia gli animali",
    "🚯 Non buttare plastica a terra",
    "🧹 Partecipa a pulizie ambientali",
    "📚 Informati sull’inquinamento da plastica",
    "🗣️ Sensibilizza chi ti circonda",
    "🏫 Riduci plastica a scuola",
    "🏠 Riduci plastica in casa",
    "🏢 Riduci plastica al lavoro",

    "🍴 Usa stoviglie riutilizzabili",
    "☕ Usa tazze riutilizzabili",
    "🥤 Evita bicchieri di plastica",
    "🧃 Scegli confezioni riciclabili",
    "📦 Riusa scatole e contenitori",
    "📬 Evita imballaggi eccessivi",
    "🧴 Compra ricariche",
    "🧼 Diluisci detergenti concentrati",
    "🪣 Usa secchi riutilizzabili",
    "🚿 Riduci consumo di prodotti plastici",

    "🧵 Evita tessuti sintetici",
    "👕 Lava meno i capi sintetici",
    "🧺 Usa filtri anti-microplastiche",
    "👟 Compra scarpe durevoli",
    "🧳 Viaggia con meno plastica",
    "🍽️ Porta posate riutilizzabili",
    "🥡 Rifiuta imballaggi inutili",
    "🧾 Scegli alternative eco",
    "🌍 Riduci la tua impronta di plastica",
    "💚 Ogni scelta senza plastica conta"
]

@bot.command()
async def platica(ctx):
    await ctx.send("Ecco un consiglio per ridurre la plastica: " + random.choice(plastica_list))

vetro_list = [
    "🚫🥤 Evita bottiglie di plastica monouso",
    "🥤 Usa una borraccia riutilizzabile",
    "🛍️ Porta borse di stoffa per la spesa",
    "🍽️ Evita piatti e posate di plastica",
    "🥡 Riduci l’uso di contenitori usa e getta",
    "♻️ Ricicla correttamente la plastica",
    "🧃 Preferisci confezioni in vetro",
    "📦 Riduci gli imballaggi inutili",
    "🛒 Compra prodotti sfusi",
    "🧴 Riutilizza i flaconi",

    "🪥 Usa spazzolini biodegradabili",
    "🧼 Evita microplastiche nei cosmetici",
    "🧽 Scegli spugne naturali",
    "🧃 Evita cannucce di plastica",
    "🥄 Usa cannucce riutilizzabili",
    "🍱 Porta il pranzo da casa",
    "🥪 Avvolgi il cibo con stoffa cerata",
    "🧊 Evita sacchetti di plastica per il ghiaccio",
    "🍎 Compra frutta senza imballaggi",
    "🧺 Usa sacchetti riutilizzabili",

    "🧴 Compra detersivi alla spina",
    "🧼 Usa saponi solidi",
    "🚿 Evita flaconi usa e getta",
    "🪒 Usa rasoi riutilizzabili",
    "🧴 Scegli shampoo solidi",
    "👶 Evita prodotti plastici inutili",
    "🧸 Preferisci giochi senza plastica",
    "🪑 Compra oggetti durevoli",
    "🔁 Riutilizza prima di buttare",
    "🛠️ Ripara gli oggetti rotti",

    "🏖️ Non lasciare plastica in spiaggia",
    "🌊 Proteggi mari e oceani",
    "🐢 Evita plastica che danneggia gli animali",
    "🚯 Non buttare plastica a terra",
    "🧹 Partecipa a pulizie ambientali",
    "📚 Informati sull’inquinamento da plastica",
    "🗣️ Sensibilizza chi ti circonda",
    "🏫 Riduci plastica a scuola",
    "🏠 Riduci plastica in casa",
    "🏢 Riduci plastica al lavoro",

    "🍴 Usa stoviglie riutilizzabili",
    "☕ Usa tazze riutilizzabili",
    "🥤 Evita bicchieri di plastica",
    "🧃 Scegli confezioni riciclabili",
    "📦 Riusa scatole e contenitori",
    "📬 Evita imballaggi eccessivi",
    "🧴 Compra ricariche",
    "🧼 Diluisci detergenti concentrati",
    "🪣 Usa secchi riutilizzabili",
    "🚿 Riduci consumo di prodotti plastici",

    "🧵 Evita tessuti sintetici",
    "👕 Lava meno i capi sintetici",
    "🧺 Usa filtri anti-microplastiche",
    "👟 Compra scarpe durevoli",
    "🧳 Viaggia con meno plastica",
    "🍽️ Porta posate riutilizzabili",
    "🥡 Rifiuta imballaggi inutili",
    "🧾 Scegli alternative eco",
    "🌍 Riduci la tua impronta di plastica",
    "💚 Ogni scelta senza plastica conta"
]

@bot.command()
async def vetro(ctx):
    await ctx.send("Ecco un consiglio per ridurre il vetro: " + random.choice(vetro_list))




