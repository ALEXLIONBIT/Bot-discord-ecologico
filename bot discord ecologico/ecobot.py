import discord
from discord.ext import commands
import random
import aiohttp
import os
import asyncio
from diffusers import StableDiffusionPipeline
from PIL import Image
import torch

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="eco.", intents=intents)

try:
    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",  
        torch_dtype=torch.float32 if not torch.cuda.is_available() else torch.float16,
        safety_checker=None  
    )
    pipe = pipe.to("cpu" if not torch.cuda.is_available() else "cuda")  
    print("Stable Diffusion pipeline caricata con successo!")
except Exception as e:
    print(f"Errore caricamento Stable Diffusion: {e}")



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


carta_list = [
    "📄 Riduci l’uso della carta",
    "📝 Scrivi solo quando necessario",
    "📖 Usa entrambi i lati della carta",
    "🖨️ Stampa solo se serve",
    "♻️ Ricicla tutta la carta usata",
    "📚 Compra quaderni riciclati",
    "✂️ Riusa carta per appunti veloci",
    "📦 Evita imballaggi di carta inutili",
    "📬 Preferisci bollette digitali",
    "📰 Riutilizza vecchi giornali",
    "🧾 Riduci scontrini cartacei",
    "🖋️ Preferisci note digitali",
    "🗂️ Organizza documenti senza stampare",
    "📃 Ricicla vecchi appunti",
    "📦 Usa scatole di cartone riciclato",
    "📦 Riusa pacchi e scatole",
    "🖨️ Imposta stampa fronte/retro",
    "📄 Non sprecare fogli bianchi",
    "🗑️ Evita buttare carta buona",
    "🖨️ Ottimizza layout di stampa",
    "📄 Fai bozze su carta usata",
    "📖 Dona libri usati",
    "📚 Scambia libri con amici",
    "✂️ Riusa carta per disegni",
    "📝 Preferisci quaderni a riempimento completo",
    "📦 Usa carta da pacco riciclata",
    "♻️ Separare carta e cartone dai rifiuti",
    "📄 Evita volantini pubblicitari",
    "📄 Chiedi digitale invece di stampato",
    "📰 Usa giornali per pulizie domestiche",
    "📚 Compra carta certificata FSC",
    "📖 Leggi e presta libri invece di comprare nuovi",
    "📦 Imballaggi: preferisci cartone riciclabile",
    "🖨️ Stampa PDF solo se indispensabile",
    "📝 Appunti: scrivi a mano solo se utile",
    "♻️ Carta da ufficio: riciclata è meglio",
    "📄 Usa quaderni multipagina",
    "🖋️ Penne ricaricabili invece di monouso",
    "📖 Non buttare libri danneggiati, riparali",
    "📦 Riutilizza scatole per conservare",
    "📰 Carta straccia: riciclala",
    "📄 Riduci note adesive inutili",
    "📝 Digitalizza documenti vecchi",
    "📚 Biblioteche e scambi di libri",
    "✂️ Fai collage con carta usata",
    "🖨️ Usa font piccoli per risparmiare carta",
    "📄 Stampa solo pagine necessarie",
    "📦 Carta per imballaggi: riusa più volte",
    "📖 Evita libri con copertina inutile",
    "📝 Appunti online quando possibile",
    "📄 Fai liste digitali",
    "♻️ Carta colorata: ricicla separatamente",
    "📚 Non buttare quaderni quasi vuoti",
    "📦 Scatole di cartone: piega e ricicla",
    "📖 Leggi libri digitali",
    "🖋️ Preferisci matite a penne usa e getta",
    "📝 Riusa fogli per schizzi",
    "📄 Evita stampare email inutili",
    "📚 Dai libri usati a scuole o associazioni",
    "📦 Imballaggi regalo: usa carta riciclata",
    "📰 Giornali: usali per rivestire superfici",
    "🖨️ Usa modalità bozza in stampa",
    "📄 Evita carta plastificata",
    "📚 Prenditi cura dei libri per farli durare",
    "📝 Scrivi appunti digitali",
    "♻️ Fai compost con carta non lucida",
    "📦 Riusa carta e cartone in bricolage",
    "📄 Riduci flyer pubblicitari",
    "📚 Dona libri alle biblioteche",
    "📖 Scambia libri con amici",
    "📦 Usa scatole di cartone multiple volte",
    "📝 Appunti e schizzi su carta riciclata",
    "📄 Non buttare fogli solo per piccole correzioni",
    "📚 Fai scaffali per libri usati",
    "🖨️ Stampa fronte/retro sempre",
    "📦 Imballaggi regalo: riusa carta già utilizzata",
    "📖 Leggi ebook invece di libri nuovi",
    "📝 Appunti digitali salvati nel cloud",
    "♻️ Carta da ufficio: riciclata o riutilizzata",
    "📄 Usa fogli spaiati per bozze",
    "📚 Scambia libri usati online",
    "📰 Carta straccia per pulizie domestiche",
    "📦 Cartone: riutilizza pacchi",
    "📝 Fai note brevi su Post-it digitali",
    "📄 Riduci volantini pubblicitari",
    "📚 Compra libri usati",
    "📖 Riusa pagine dei libri vecchi per arte",
    "📦 Cartone: usa come base per pittura",
    "📄 Fai bozze su fogli già stampati",
    "📝 Digitalizza vecchi appunti",
    "♻️ Carta di giornale: ricicla o compost",
    "📚 Prestito libri invece di acquistare",
    "📖 Leggi online quando possibile",
    "📦 Riutilizza scatole per spedizioni",
    "🖨️ Ottimizza stampa riducendo margini",
    "📄 Usa carta monouso solo se necessario",
    "📝 Note adesive: preferisci app digitali",
    "📚 Scambia libri a scuola o in biblioteca",
    "📦 Cartone: piega e ricicla correttamente",
    "📖 Ebook e PDF: alternativa ecologica",
    "📝 Appunti condivisi online",
    "♻️ Carta lucida o patinata: smaltisci correttamente",
    "📄 Fai liste digitali per ridurre fogli",
    "📚 Dona libri in buono stato",
    "📦 Carta da pacco: riutilizza più volte",
    "📄 Non sprecare fogli bianchi",
    "📝 Preferisci documenti digitali",
    "📖 Biblioteca digitale: leggi ebook",
    "📚 Scambi di libri fra amici",
    "📦 Imballaggi: riusa carta di giornale",
    "🖨️ Stampa solo pagine essenziali",
    "📄 Usa quaderni fino all’ultima pagina",
    "📝 Appunti a mano solo se necessario",
    "♻️ Carta da ufficio: riciclata e riutilizzata",
    "📚 Fai circolare libri usati",
    "📖 Ebook: riduci spreco di carta",
    "📦 Carta: riusa e ricicla sempre",
    "📝 Fai bozze su fogli già utilizzati",
    "📄 Riduci pubblicità cartacea"
]


cartone_list = [
    "📦 Riutilizza scatole di cartone per spedizioni",
    "📦 Piega le scatole prima di riciclarle",
    "♻️ Separare cartone da altri rifiuti",
    "📦 Usa cartone per organizzare oggetti in casa",
    "🖼️ Trasforma scatole in contenitori creativi",
    "📦 Imballaggi: preferisci cartone riciclato",
    "🖌️ Usa cartone per lavoretti creativi",
    "📦 Riusa scatole per archiviazione documenti",
    "♻️ Ricicla correttamente il cartone ondulato",
    "📦 Riusa cartoni per traslochi",
    "📝 Usa cartone come base per appunti o schizzi",
    "📦 Cartone come protezione per mobili",
    "♻️ Cartoni da imballaggio: taglia e ricicla",
    "📦 Riutilizza scatole per conservare vestiti",
    "🖌️ Fai arte con cartone riciclato",
    "📦 Riutilizza scatole per regali",
    "♻️ Cartone dei pacchi: separa nastro adesivo",
    "📦 Cartoni come supporto per piante",
    "🖼️ Crea scaffali o contenitori con cartone",
    "📦 Riusa cartone per spedizioni personali",
    "♻️ Cartoni di pizza: compostabili se non unti",
    "📦 Conserva scatole per giochi dei bambini",
    "🖌️ Crea decorazioni con cartone usato",
    "📦 Riusa cartone per organizzare cassetti",
    "♻️ Cartone: taglia e piega prima del riciclo",
    "📦 Riutilizza scatole per hobby e bricolage",
    "🖌️ Cartone per collage o disegni",
    "📦 Riutilizza cartone come divisori",
    "♻️ Cartone pulito: riciclabile al 100%",
    "📦 Cartoni: conservare libri o oggetti fragili",
    "🖌️ Cartone per lavoretti scolastici",
    "📦 Riusa scatole per spedire pacchi",
    "♻️ Separare cartone dai rifiuti misti",
    "📦 Cartone: riutilizza per archiviazione",
    "🖼️ Trasforma scatole in supporti per disegni",
    "📦 Cartone per organizzare armadi",
    "♻️ Ricicla scatole di cartone ondulato",
    "📦 Riutilizza scatole come contenitori gioco",
    "🖌️ Crea oggetti decorativi con cartone",
    "📦 Scatole come protezione in traslochi",
    "♻️ Cartone pulito e asciutto: riciclabile",
    "📦 Riusa cartone per spedizioni sicure",
    "🖌️ Cartone come base per pittura",
    "📦 Conserva cartoni per archiviazione",
    "♻️ Ricicla il cartone ondulato separatamente",
    "📦 Cartone come divisorio per scaffali",
    "🖌️ Crea oggetti artigianali con cartone",
    "📦 Riutilizza scatole per regali",
    "♻️ Separare nastro adesivo prima del riciclo",
    "📦 Riusa scatole come contenitori per attrezzi",
    "🖌️ Cartone per lavoretti creativi dei bambini",
    "📦 Cartoni: organizzare materiali da ufficio",
    "♻️ Cartone dei pacchi: riciclabile solo pulito",
    "📦 Riutilizza cartoni per spedizioni",
    "🖌️ Crea supporti e stand con cartone riciclato",
    "📦 Cartone per protezione pavimenti",
    "♻️ Taglia cartoni grandi prima del riciclo",
    "📦 Riusa cartoni come contenitori per vestiti",
    "🖌️ Cartone per progetti scolastici",
    "📦 Scatole come divisori per armadi",
    "♻️ Ricicla cartoni ondulati separatamente",
    "📦 Riutilizza cartone per hobby e bricolage",
    "🖌️ Lavoretti artistici con cartone riciclato",
    "📦 Cartoni come protezione fragile",
    "♻️ Mantieni cartone pulito e asciutto",
    "📦 Riusa scatole per spedizioni sicure",
    "🖌️ Cartone per collage e pittura",
    "📦 Conserva cartoni per organizzare casa",
    "♻️ Ricicla scatole solo pulite",
    "📦 Cartone come divisorio scaffali",
    "🖌️ Crea oggetti decorativi con cartone",
    "📦 Riutilizza cartoni per regali",
    "♻️ Taglia cartone e separa adesivi prima del riciclo",
    "📦 Riusa scatole per attrezzi o materiali",
    "🖌️ Lavoretti creativi con cartone dei bambini",
    "📦 Cartoni come organizzatori da ufficio",
    "♻️ Cartone da pacchi: riciclare pulito",
    "📦 Riusa cartoni per spedizioni",
    "🖌️ Supporti e stand con cartone riciclato",
    "📦 Cartone per protezione pavimenti",
    "♻️ Taglia cartone prima del riciclo",
    "📦 Riusa cartoni per vestiti",
    "🖌️ Progetti scolastici con cartone",
    "📦 Scatole come divisori",
    "♻️ Ricicla cartoni ondulati separatamente",
    "📦 Riutilizza per bricolage",
    "🖌️ Lavoretti artistici",
    "📦 Protezione oggetti fragili",
    "♻️ Mantieni cartone asciutto",
    "📦 Riusa per spedizioni sicure",
    "🖌️ Collage e pittura",
    "📦 Organizza casa con cartoni",
    "♻️ Ricicla solo cartone pulito",
    "📦 Divisori scaffali con cartone",
    "🖌️ Crea decorazioni con cartone",
    "📦 Riutilizza per regali",
    "♻️ Separare adesivi e plastica prima del riciclo",
    "📦 Contenitori per attrezzi",
    "🖌️ Lavoretti creativi",
    "📦 Organizzatori da ufficio",
    "♻️ Cartoni da pacchi puliti sono riciclabili",
    "📦 Riusa cartoni per spedizioni",
    "🖌️ Supporti e stand fai-da-te",
    "📦 Proteggi pavimenti e oggetti",
    "♻️ Taglia cartone prima del riciclo",
    "📦 Contenitori per vestiti o giocattoli",
    "🖌️ Progetti scolastici con cartone",
    "📦 Scatole come divisori",
    "♻️ Ricicla correttamente i cartoni",
    "📦 Riutilizzo creativo per casa",
    "🖌️ Lavoretti artistici con cartone"
]

umido_list = [
    "🍌 Le bucce di banana sono perfette per il compost! Si decompongono velocemente 🌱",
    "🍎 I torsoli di mela vanno nell'umido, mai nella plastica! ♻️",
    "☕️ I fondi di caffè sono un ottimo concime naturale per le piante 🪴",
    "🥚 I gusci d'uovo tritati arricchiscono il compost di calcio 🥚",
    "🍊 Le bucce di agrumi ci vanno, ma con moderazione (acidificano il compost) 🍋",
    "🥕 I resti di carote, zucchine e verdure crude sono benvenuti nell'umido 🥦",
    "🍞 Il pane raffermo si può compostare, ma meglio spezzettarlo prima 🍞",
    "🥬 Le foglie di insalata appassite sono ottime per il compost 🥗",
    "🍅 I pomodori schiacciati o andati a male vanno nell'umido 🍅",
    "🧅 Le bucce di cipolla sono compostabili, ma in piccole quantità 🧅",
    "🥔 Le bucce di patata sono perfette per l'umido, lavale prima! 🥔",
    "🍇 I raspi dell'uva e gli acini schiacciati finiscono nell'organico 🍇",
    "🌿 Le erbe aromatiche appassite vanno nel compost, profumano pure! 🌱",
    "🍓 I fragole ammuffite? Umido senza esitare! 🍓",
    "🧄 L'aglio e le sue bucce sono compostabili al 100% 🧄",
    "🥜 I gusci di noci e nocciole tritati vanno nell'umido (ma lentamente si decompongono) 🥜",
    "🍯 Il miele cristallizzato si può buttare nell'umido in piccole quantità 🍯",
    "🧀 Piccoli resti di formaggio fresco (non stagionato) possono andare nell'umido 🧀",
    "🥛 Il latte scaduto va nell'umido, ma meglio diluirlo prima 🥛",
    "🍳 I resti di uova strapazzate o omelette sono organici! 🍳",
    "🍚 Il riso cotto avanzato è perfetto per il compost 🍚",
    "🍝 La pasta cotta senza sugo va nell'umido ♻️",
    "🥗 Gli avanzi di insalata condita (senza troppi oli) sono compostabili 🥗",
    "🍲 I fondi di zuppa vegetale vanno nell'organico 🍲",
    "🌽 Le pannocchie di mais sgranocchiate finiscono nell'umido 🌽",
    "🍯 Le bucce di melone e anguria sono ottime per il compost 🍉",
    "🥦 I gambi di broccoli e cavolfiori sono super compostabili 🥦",
    "🍆 Le melanzane avanzate o bruciate? Umido! 🍆",
    "🥒 I cetrioli ammuffiti vanno nell'organico 🥒",
    "🌶️ I peperoni e i loro semi sono perfetti per il compost 🌶️",
    "🍄 I funghi appassiti o avanzati sono compostabili 🍄",
    "🥜 I gusci di arachidi sono ottimi per il compost 🥜",
    "🍍 L'ananas e la sua corona fogliosa vanno nell'umido (tritati meglio) 🍍",
    "🥑 Il nocciolo di avocado si può compostare, ma ci vuole tempo 🥑",
    "🌰 Le castagne bollite avanzate sono organiche 🌰",
    "🍐 Le pere troppo mature vanno nell'umido 🍐",
    "🍑 Le pesche e le loro noccioli (schiacciati) sono compostabili 🍑",
    "🥝 I kiwi e le loro bucce pelose finiscono nell'organico 🥝",
    "🍋 I limoni spremuti e le bucce sono perfetti 🍋",
    "🫐 I mirtilli ammuffiti? Umido subito 🫐",
    "🍒 Le ciliegie e i loro noccioli (meglio tritati) vanno nell'umido 🍒",
    "🧈 Piccoli resti di burro o margarina vegetale sono compostabili 🧈",
    "🥖 I crostini di pane avanzati si decompongono facilmente 🥖",
    "🧄 Le bucce di scalogno sono come quelle di cipolla 🧅",
    "🥬 Le coste di bietola o spinaci appassiti sono ottime 🥬",
    "🌱 I germogli troppo cresciuti vanno nel compost 🌱",
    "🍌 Le banane troppo mature (anche nere) sono oro per il compost 🍌",
    "🥕 Le foglie delle carote sono compostabili al 100% 🥕",
    "🧹 I tovaglioli di carta usati (non sporchi di detersivi) vanno nell'umido 🧻",
    "🌹 I fiori appassiti del vaso sono perfetti per il compost 🌸",
    "☘️ Le foglie secche delle piante d'appartamento sono organiche ☘️",
    "🍂 I piccoli rametti tritati possono andare nell'umido 🍂",
    "🪴 La terra vecchia delle piante in vaso è compostabile 🪴",
    "🧹 La segatura di legno non trattato è ottima per bilanciare l'umido 🪵",
    "📄 La carta da cucina usata per asciugare frutta/verdura va nell'umido 📄",
    "🍃 Le bustine di tè (senza graffette) sono compostabili 🍵",
    "☕️ I filtri di carta del caffè vanno nell'umido ☕️",
    "🥜 I gusci di pistacchi sono organici 🥜",
    "🌰 Le bucce di mandorle e noci sono perfette 🌰",
    "🍯 La cera d'api naturale (piccole quantità) è compostabile 🐝",
    "🧀 I croste di parmigiano? No, quelle sono indifferenziata! ❌",
    "🍖 La carne e il pesce NON vanno nell'umido in molti comuni! Controlla le regole locali 🚫",
    "🦴 Le ossa non sono compostabili in casa 🦴",
    "🥑 Le bucce di avocado sono sì, ma il nocciolo meglio tritato 🥑",
    "🍌 Non buttare le banane intere: spezzettale! Aiuta la decomposizione ✊",
    "🌧️ Mescola spesso il compost per farlo respirare meglio 🔄",
    "☀️ Tieni il compost al riparo dalla pioggia forte ☔",
    "🪱 I lombrichi adorano i resti di frutta e verdura 🪱",
    "🌡️ Il compost caldo è segno che sta lavorando bene 🔥",
    "🪴 Usa il compost maturo per concimare le tue piante 🪴",
    "♻️ Riciclare l'umido riduce le emissioni di metano in discarica 🌍",
    "💚 Ogni kg di umido compostato salva il pianeta un po' 💚",
    "🌱 Il compost fatto in casa è il miglior fertilizzante naturale 🌱",
    "🗑️ Controlla sempre le regole del tuo comune per l'umido 📜",
    "🍂 Bilancia l'umido con materiale secco (carta, foglie) ⚖️",
    "🚰 Evita troppi liquidi nel bidone dell'umido 🚰",
    "🪰 Per evitare odori, copri i rifiuti umidi con carta o foglie 🪰",
    "🧴 Non mettere plastica biodegradabile se non certificata OK Compost 🧴",
    "🛍️ Usa sacchetti certificati compostabili per l'umido 🛍️",
    "🌸 I petali di fiori recisi sono bellissimi nel compost 🌸",
    "🍁 Le foglie autunnali sono ottime per coprire l'umido 🍁",
    "🪴 Il compost aiuta a trattenere l'acqua nel terreno 💧",
    "🌍 Compostare è un piccolo gesto per un grande impatto 🌍",
    "🪴 Regala il tuo compost agli amici con l'orto 🎁",
    "🍌 Le bucce di banana attirano farfalle nel compost 🦋",
    "🥚 I gusci d'uovo tritati tengono lontane le lumache 🐌",
    "☕️ I fondi di caffè acidificano il terreno (perfetti per ortensie!) 💙",
    "🍞 Il pane vecchio attira microrganismi utili 🦠",
    "🥬 Le verdure crucifere (cavoli) rilasciano azoto prezioso 🥬",
    "🍊 Le bucce di agrumi tengono lontani gli insetti molesti 🦟",
    "🌿 Le erbe aromatiche nel compost profumano tutto 🌿",
    "🪱 Più umido vario metti, più il compost è ricco 🪱",
    "♻️ L'umido riciclato diventa energia e concime ♻️",
    "💪 Compostare è facile e fa bene all'ambiente 💪",
    "🌱 Inizia oggi a separare meglio l'umido! 🌱",
    "🎄 Anche gli aghi di pino (in piccole quantità) sono compostabili 🎄",
    "🥀 I fiori secchi del bouquet vanno nell'umido 🥀",
    "🧻 La carta assorbente usata per alimenti puliti è ok 🧻",
    "🍂 L'equilibrio tra verde (umido) e marrone (secco) è la chiave ⚖️",
    "🌍 Grazie per riciclare l'umido: stai salvando il pianeta! 🌍❤️"
]

@bot.command()
async def plastica(ctx):
    await ctx.send("consiglio per diminuire la plastica:" + random.choice(plastica_list))

@bot.command()
async def carta(ctx):
    await ctx.send("consiglio per diminuire la carta:" + random.choice(carta_list))

@bot.command()
async def vetro(ctx):
    await ctx.send("consiglio per diminuire il vetro:" + random.choice(vetro_list))

@bot.command()
async def cartone(ctx):
    await ctx.send("consiglio per diminuire il cartone:" + random.choice(cartone_list))

@bot.command()
async def consiglio(ctx):
    await ctx.send("consiglio per sostenere l'ambiente:" + random.choice(ambiente_list))

bot.command()
async def umido(ctx):
    await ctx.send("consigli per l'umido:" + random.choice(umido_list))

bot.command()
async def lista(ctx):
    await ctx.send("lista dei comandi disponibili sono: eco.plastica, eco.carta, eco.vetro, eco.cartone, eco.consiglio, eco.umido, eco.ai")

async def chiedi_a_ollama(prompt):
    url = "http://127.0.0.1:11434/api/generate"

    payload = {"model": "gemma3:12b", "prompt": prompt, "stream": False}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data.get("response", "Errore: Ollama ha restituito un formato vuoto.")
                return f"Ollama ha risposto con errore: {resp.status}"
    except Exception as e:
        return f"Errore di connessione a Ollama: {e}"

async def genera_immagine(prompt: str) -> str | None:
    try:
        loop = asyncio.get_event_loop()

        image = await loop.run_in_executor(
            None,
            lambda: pipe(
                prompt,
                num_inference_steps=10,
                guidance_scale=7.5
            ).images[0]
        )

        os.makedirs("output", exist_ok=True)
        path = "output/immagine_sd.png"
        image.save(path)

        return path

    except Exception as e:
        print("❌ Errore Stable Diffusion:", e)
        return None



@bot.command(name="ai")
async def ai(ctx, *, contenuto: str):
    msg = await ctx.send("🤖 **L'AI ECO** sta elaborando la tua richiesta...")


    risposta_testo = await chiedi_a_ollama(
        f"Rispondi brevemente e in modo ecologico a: {contenuto}"
    )

    prompt_visivo = await chiedi_a_ollama(
        f"Crea un prompt breve in inglese per un'immagine realistica ed ecologica basata su: {contenuto}. Scrivi solo il prompt, niente altro."
    )

    await msg.edit(content=f"**ECO ai dice:** {risposta_testo}")

    img_path = await genera_immagine(prompt_visivo)

    if img_path:
        await ctx.send(
            content="🖼️ Ecco l'immagine generata:",
            file=discord.File(img_path)
        )
    else:
        await ctx.send("⚠️ Non è stato possibile generare l'immagine.")
        
bot.run("")




