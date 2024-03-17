## Sprites for gen 6+ pokemon from https://play.pokemonshowdown.com/sprites/gen5/
## All other sprites are from various pokemon games

from mathstuffdontask import simpleintegral

import asyncio

locationslist = ['flowerfields', 'city', 'beach', 'snowy']
specialmons = ['eternal_floette', 'phione', 'manaphy', 'meloetta', 'meloetta_pirouette']

lock = []
softlock = []

import locations

from typing import Final
import os

import discord
from dotenv import load_dotenv
from discord import Intents, Client, Message, File, Guild, utils, channel, voice_client
import random
from discord.ext import commands
import time
import math
import datetime
import aioconsole
import json
import ffmpeg

from berrydict import getberrydict

berrydict = getberrydict()

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

intents: Intents = Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.reactions = True

client: Client = Client(intents=intents)

bot = commands.Bot(command_prefix='espurr.', intents=intents)



common = ['cheri', 'chesto', 'pecha', 'rawst', 'aspear', 'leppa', 'oran', 'persim']

uncommon = ['occa', 'passho', 'wacan', 'rindo', 'yache', 'chople', 'kebia', 'shuca', 'coba', 'payapa', 'tanga',
            'charti', 'kasib', 'haban', 'colbur', 'babiri', 'chilan', 'razz', 'nanab', 'pinap', 'bluk',
            'wepear', 'roseli', 'sitrus']

rare = ['lum', 'figy', 'wiki', 'mago', 'aguav', 'iapapa', 'pomeg', 'kelpsy', 'qualot',
        'hondew', 'grepa', 'tamato', 'liechi', 'ganlon', 'salac', 'petaya', 'apicot', 'kee', 'maranga',
        'silver_razz', 'silver_nanab', 'silver_pinap']

super_rare = ['cornn', 'magost', 'rabuta', 'nomel', 'spelon', 'pamtre', 'watmel', 'durin', 'belue',
              'lansat', 'micle', 'custap', 'jaboca', 'rowap', 'enigma', 'golden_razz', 'golden_nanab', 'golden_pinap']

legendary = ['starf', 'cosnut']

eggs = ['egg']

allberries = [common, uncommon, rare, super_rare, legendary]

allberrystrings = common + uncommon + rare + super_rare + legendary

alledibles = allberrystrings.copy()

import levelups

juices = []

mail = ['<:BridgeMailD:1205739955499040808>',
        '<:BridgeMailM:1205739953410023424>',
        '<:BridgeMailS:1205739954622431242>',
        '<:BridgeMailT:1205739956522324050>',
        '<:BridgeMailV:1205739958225207326>',
        '<:BubbleMail:1205740003020247091>',
        '<:DreamMail:1205739959584292895>',
        '<:FavoredMail:1205740002114408458>',
        '<:Greetmail:1205738183741153281>',
        '<:InquiryMail:1205739999266607164>',
        '<:SnowMail:1205740000302342164>',
        '<:ThanksMail:1205739952147800144>',
        '<:TropicMail:1205739960737730622>',
        '<:FlameMail:1205740593272332319>',
        '<:BloomMail:1205741248514625548>',
        '<:WaveMail:1205741247118184468>',
        '<:AirMail:1205741248057704508>',
        '<:MosaicMail:1205741249617723478>',
        '<:GlitterMail:1205741251521945620>']

berrytypes = {'fire': "occa",
              'water': 'passho',
              'electric': 'wacan',
              'grass': 'rindo',
              'ice': 'yache',
              'fighting': 'chople',
              'poison': 'kebia',
              'ground': 'shuca',
              'flying': 'coba',
              'psychic': 'payapa',
              'bug': 'tanga',
              'rock': 'charti',
              'ghost': 'kasib',
              'haban': 'dragon',
              'dark': 'colbur',
              'steel': 'babiri',
              'fairy': 'roseli',
              'dragon': 'haban',
              'normal': 'chilan'}

typetogememote = {'fire': "<:FireGem:1205746134698426388>",
              'water': '<:WaterGem:1205746137764470875>',
              'electric': '<:ElectricGem:1205746136732667934>',
              'grass': '<:GrassGem:1205746132173721661>',
              'ice': '<:IceGem:1205746130558779402>',
              'fighting': '<:FightingGem:1205746010152767508>',
              'poison': '<:PoisonGem:1205746009284804658>',
              'ground': '<:GroundGem:1205746008173051934>',
              'flying': '<:FlyingGem:1205745797015019560>',
              'psychic': '<:PsychicGem:1205745962925039668>',
              'bug': '<:BugGem:1205745794213478450>',
              'rock': '<:RockGem:1205745793156386887>',
              'ghost': '<:GhostGem:1205745792065732638>',
              'dragon': '<:DragonGem:1205745791277469766>',
              'dark': '<:DarkGem:1205745790467973180>',
              'steel': '<:SteelGem:1205745788937048105>',
              'fairy': '<:FairyGem:1205746133054525500>',
              'normal': '<:NormalGem:1205745788349583362>'}

berriestoemoteid = {
    "aguav": '<:Aguav_Berry:1176959310836805713>',
    "apicot": "<a:Apicot_Berry:1176973588591542272>",
    "aspear": '<:Aspear_Berry:1176956991327965306>',
    "babiri": "<a:Babiri_Berry:1176972885475209226>",
    "belue": '<:Belue_Berry:1176964389744681050>',
    "bluk": '<:Bluk_Berry:1176959306436980848>',
    "charti": '<:Charti_Berry:1176972796962799639>',
    "cheri": '<:Cheri_Berry:1176961011312492544>',
    "chesto": "<:Chesto_Berry:1176955896551702548>",
    "chilan": "<a:Chilan_Berry:1176972882488852610>",
    "chople": "<:Chople_Berry:1176972806915887176>",
    "coba": "<:Coba_Berry:1176972801391997019>",
    "colbur": "<:Colbur_Berry:1176972787856965813>",
    "cornn": "<:Cornn_Berry:1176963633788497990>",
    "custap": "<a:Custap_Berry:1176973039859150879>",
    "durin": "<:Durin_Berry:1176964392470978631>",
    "enigma": "<a:Enigma_Berry:1176973043273318540>",
    "figy": "<:Figy_Berry:1176958151904481401>",
    "ganlon": "<a:Ganlon_Berry:1176972878999191702>",
    "grepa": "<:Grepa_Berry:1176962963383529614>",
    "haban": "<:Haban_Berry:1176972790658773092>",
    "hondew": "<:Hondew_Berry:1176962964805394462>",
    "iapapa": "<:Iapapa_Berry:1176959309578502246>",
    "jaboca": "<a:Jaboca_Berry:1176973037132849193>",
    "kasib": "<:Kasib_Berry:1176972795666776105>",
    "kebia": "<:Kebia_Berry:1176972805405954179>",
    "kee": "<a:Kee_Berry:1176973030682005514>",
    "kelpsy": "<:Kelpsy_Berry:1176962007426146464>",
    "lansat": "<a:Lansat_Berry:1176973046708445224>",
    "leppa": "<:Leppa_Berry:1176956989704785991>",
    "liechi": "<a:Liechi_Berry:1176972880991490078>",
    "lum": "<:Lum_berry:1176958155222159360>",
    "mago": "<:Mago_Berry:1176959312845865012>",
    "magost": "<:Magost_Berry:1176963632358236292>",
    "maranga": "<a:Maranga_Berry:1176973027183972443>",
    "micle": "<a:Micle_Berry:1176973041264238723>",
    "nanab": "<:Nanab_Berry:1176962012937470002>",
    "nomel": "<:Nomel_Berry:1176963629057319033>",
    "occa": "<:Occa_Berry:1176972676909252688>",
    "oran": "<:Oran_Berry:1177001065678372874>",
    "pamtre": "<:Pamtre_Berry:1176964396732383232>",
    "passho": "<:Passho_Berry:1176965277943087195>",
    "payapa": "<:Payapa_Berry:1176972800221790338>",
    "pecha": "<:Pecha_Berry:1176955792809799720>",
    "persim": "<:Persim_Berry:1176958156644024561>",
    "petaya": "<a:Petaya_Berry:1176973050495897691>",
    "pinap": "<:Pinap_Berry:1176962011616268339>",
    "pomeg": "<:Pomeg_Berry:1176962009049346058>",
    "qualot": "<:Qualot_Berry:1176962965950443520>",
    "rabuta": "<:Rabuta_Berry:1176963630420463757>",
    "rawst": "<:Rawst_Berry:1176956993362210876>",
    "razz": "<:Razz_Berry:1176959308014035115>",
    "rindo": "<:Rindo_Berry:1176965273782321314>",
    "roseli": "<a:Roseli_Berry:1176973032846274662>",
    "rowap": "<a:Rowap_Berry:1176973035748737095>",
    "salac": "<a:Salac_Berry:1176972877405372506>",
    "shuca": "<:Shuca_Berry:1176972803774357514>",
    "sitrus": "<:Sitrus_Berry:1176958154051948544>",
    "spelon": "<:Spelon_Berry:1176964398078771221>",
    "starf": "<a:Starf_Berry:1176973551136428073>",
    "tamato": "<:Tamato_Berry:1176962960934047815>",
    "tanga": "<:Tanga_Berry:1176972797852008550>",
    "wacan": "<:Wacan_Berry:1176965275900465212>",
    "watmel": "<:Watmel_Berry:1176964394228391997>",
    "wepear": "<:Wepear_Berry:1176962160916697119>",
    "wiki": "<:Wiki_Berry:1176959314578112542>",
    "yache": "<:Yache_Berry:1176965271056027688>",

    'silver_razz': '<a:Silver_Razz_Berry:1176973025720148028>',
    'silver_nanab': '<a:Silver_Nanab_Berry:1176973022482149387>',
    'silver_pinap': '<a:Silver_Pinap_Berry:1176973021416800276>',
    'golden_razz': '<a:Golden_Razz_Berry:1176973019277705296>',
    'golden_nanab': '<a:Golden_Nanab_Berry:1176973018006823034>',
    'golden_pinap': '<a:Golden_Pinap_Berry:1176972953955610684>',


    "egg": "<a:egg:1205735769377869844>",
    "flowerfieldsegg": "<a:flowerfieldsegg:1209618123146395678>",
    "cityegg": "<a:cityegg:1209991120671744110>",
    "beachegg": "<a:beachegg:1210322577021730887>",
    "cosnut": "<a:Cosnut_Berry_custom:1210399482462871553>",
    'snowyegg': '<a:snowyegg:1211085168417448058>'
}

juicestoemoteid = {
    "aguav": '<:aguavjuiceup:1204920953167945818>',
    "apicot": "<:apicotjuiceup:1204134173430915082>",
    "aspear": '<:aspearjuiceup:1204134070020341821>',
    "babiri": "<a:Babiri_Berry:1176972885475209226>",
    "belue": '<:beluejuiceup:1204133920111853638>',
    "bluk": '<:blukuiceup:1204920516520190042>',
    "charti": '<:Charti_Berry:1176972796962799639>',
    "cheri": '<:cherijuiceup:1204134206884806707>',
    "chesto": "<:chestojuiceup:1204133887639289946>",
    "chilan": "<a:Chilan_Berry:1176972882488852610>",
    "chople": "<:Chople_Berry:1176972806915887176>",
    "coba": "<:Coba_Berry:1176972801391997019>",
    "colbur": "<:Colbur_Berry:1176972787856965813>",
    "cornn": "<:Cornn_Berry:1176963633788497990>",
    "custap": "<a:Custap_Berry:1176973039859150879>",
    "durin": "<:Durin_Berry:1176964392470978631>",
    "enigma": "<a:Enigma_Berry:1176973043273318540>",
    "figy": "<:figyjuiceup:1204920956691283978>",
    "ganlon": "<:ganlonjuiceup:1204133866533814454>",
    "grepa": "<:grepajuiceup:1204920508345491497>",
    "haban": "<:Haban_Berry:1176972790658773092>",
    "hondew": "<:hondewjuiceup:1204920509729349714>",
    "iapapa": "<:iapapajuiceup:1204920765481230378>",
    "jaboca": "<a:Jaboca_Berry:1176973037132849193>",
    "kasib": "<:Kasib_Berry:1176972795666776105>",
    "kebia": "<:Kebia_Berry:1176972805405954179>",
    "kee": "<a:Kee_Berry:1176973030682005514>",
    "kelpsy": "<:kelpsyjuiceup:1204920511558320208>",
    "lansat": "<a:Lansat_Berry:1176973046708445224>",
    "leppa": "<:leppajuiceup:1204133843834241044>",
    "liechi": "<:liechijuiceup:1204133817128976385>",
    "lum": "<:lumjuiceup:1204133760103223307>",
    "mago": "<:magojuiceup:1204920954787209266>",
    "magost": "<:Magost_Berry:1176963632358236292>",
    "maranga": "<a:Maranga_Berry:1176973027183972443>",
    "micle": "<a:Micle_Berry:1176973041264238723>",
    "nanab": "<:nanabjuiceup:1204133729367490582>",
    "nomel": "<:Nomel_Berry:1176963629057319033>",
    "occa": "<:Occa_Berry:1176972676909252688>",
    "oran": "<:oranjuiceup:1204134245472411668>",
    "pamtre": "<:Pamtre_Berry:1176964396732383232>",
    "passho": "<:passhojuiceup:1204133706382704772>",
    "payapa": "<:payapajuiceup:1204133466271252550>",
    "pecha": "<:pechajuiceup:1204133443840245790>",
    "persim": "<:persimjuiceup:1204133420628709438>",
    "petaya": "<a:Petaya_Berry:1176973050495897691>",
    "pinap": "<:pinapjuiceup:1204920513625985154>",
    "pomeg": "<:pomegjuiceup:1204920512631803954>",
    "qualot": "<:qualotjuiceup:1204920510635319296>",
    "rabuta": "<:Rabuta_Berry:1176963630420463757>",
    "rawst": "<:rawstjuiceup:1204133383119306863>",
    "razz": "<:razzjuiceup:1204920519967907980>",
    "rindo": "<:Rindo_Berry:1176965273782321314>",
    "roseli": "<a:Roseli_Berry:1176973032846274662>",
    "rowap": "<a:Rowap_Berry:1176973035748737095>",
    "salac": "<:salacjuiceup:1204133338814746624>",
    "shuca": "<:Shuca_Berry:1176972803774357514>",
    "sitrus": "<:sitrusjuiceup:1204920958113288252>",
    "spelon": "<:Spelon_Berry:1176964398078771221>",
    "starf": "<a:Starf_Berry:1176973551136428073>",
    "tamato": "<:tamatojuiceup:1204920506663305306>",
    "tanga": "<:Tanga_Berry:1176972797852008550>",
    "wacan": "<:Wacan_Berry:1176965275900465212>",
    "watmel": "<:watmeljuiceup:1204920505111543889>",
    "wepear": "<:wepearjuiceup:1204920876873551873>",
    "wiki": "<:wikijuiceup:1204920804765343774>",
    "yache": "<:Yache_Berry:1176965271056027688>",
    "cosnut": "<a:Cosnut_Berry_custom:1210399482462871553>",

    'silver_razz': '<a:Silver_Razz_Berry:1176973025720148028>',
    'silver_nanab': '<a:Silver_Nanab_Berry:1176973022482149387>',
    'silver_pinap': '<a:Silver_Pinap_Berry:1176973021416800276>',
    'golden_razz': '<a:Golden_Razz_Berry:1176973019277705296>',
    'golden_nanab': '<a:Golden_Nanab_Berry:1176973018006823034>',
    'golden_pinap': '<a:Golden_Pinap_Berry:1176972953955610684>'

}

monstoemoteid = {
    'eevee': '<a:eevee:1205752611358384199>',
    'eevee_shiny': '<a:shinyeevee:1214069998990135336>',
    'espurr': '<a:espurr:1214054736983097344>',
    'espurr_shiny': '<a:shinyespurr:1214054735062245457>',
    'pichu': '<a:pichu:1205752553707544656>',
    'cleffa': '<a:cleffa:1205752496044380200>',
    'oshawott': '<a:oshawott:1209022518527266886>',
    'snivy': '<a:snivy:1205752605192749097>',
    'tepig': '<a:tepig:1205752602730561597>',
    'phanpy': '<a:phanpy:1205752550029139978>',
    'minccino': '<a:minccino:1205752601006833705>',
    'nickit': '<:nickitbw:1208836208000507936>',
    'vulpix': '<a:vulpix:1205752561068671016>',
    'spheal': '<a:spheal:1205752562540875887>',
    'egg': '<a:egg:1205735769377869844>',
    'flarespeon': '<a:flarespeon:1205981820785791017>',
    'vaporeon': '<a:vaporeon:1206000587884466256>',
    'jolteon': '<a:jolteon:1206000542141386883>',
    'flareon': '<a:flareon:1206000534176141392>',
    'espeon': '<a:espeon:1206000556238176306>',
    'umbreon': '<a:umbreon:1206001653468110929>',
    'leafeon': '<a:leafeon:1206000567705411614>',
    'glaceon': '<a:glaceon:1206000579659300934>',
    'sylveon': '<:sylveonbw:1208836206205468753>',
    'hoppip': '<a:hoppip:1206110790776651827>',
    'azurill': '<a:azurill:1205770985509232661>',
    'togepi': '<a:togepi:1205770652959903775>',
    'mareep': '<a:mareep:1206115650742001664>',
    'skitty': '<a:skitty:1208814564993663007>',

    'gossifleur': '<:gossifleur:1209613381955362886>',
    'budew': '<a:budew:1209613383440011386>',
    'petilil': '<a:petilil:1209613380290215946>',
    'cherubi': '<a:cherubi:1209613378310643772>',
    'fomantis': '<:fomantis:1209613376762683482>',
    'bounsweet': '<:bounsweet:1209613375739527168>',
    'cottenee': '<a:cottonee:1209613374800003082>',
    'cutiefly': '<:cutiefly:1209613328666861628>',
    'sprigatito': '<:sprigatitoexport:1209613504987009164>',
    'comfey': '<:comfey:1209613969367760906>',
    'ralts': '<a:ralts:1209613968038166548>',
    'flabebe_red': '<:flabebe:1209613511710351360>',
    'flabebe_orange': '<:flabebeorange:1209613509743349790>',
    'flabebe_yellow': '<:flabebeyellow:1209613507708985445>',
    'flabebe_blue': '<:flabebeblue:1209613510347067503>',
    'flabebe_white': '<:flabebewhite:1209613508489248809>',
    'eternal_floette': '<:floetteeternal:1209613506454749254>',
    "flowerfieldsegg": "<a:flowerfieldsegg:1209618123146395678>",

    'purrloin': '<a:purrloin:1209987215774720071>',
    'meowth': '<:meowthalola:1209987209479061585>',
    'alolan_Meowth': '<:meowthalola:1209987209479061585>',
    'zigzagoon': '<a:zigzagoon:1209992091258585129>',
    'galarian_Zigzagoon': '<:zigzagoongalar:1209987210456342628>',
    'lillipup': '<a:lillipup:1209987218488299520>',
    'glameow': '<a:glameow:1209987224964177980>',
    'rattata': '<a:rattata:1209987230387544125>',
    'alolan_Rattata': '<:rattataalola:1209987228558823505>',
    'zorua': '<a:zorua:1209987212796502047>',
    'litten': '<:litten:1209987226881097789>',
    'trubbish': '<a:trubbish:1209987221634023494>',
    'cityegg': '<a:cityegg:1209991120671744110>',

    'dwebble': '<a:dwebble:1210321941211385957>',
    'buizel': '<a:buizel:1210321939541794888>',
    'slowpoke': '<a:slowpoke:1210321937042116650>',
    'staryu': '<a:staryu:1210330670610522112>',
    'frillish_male': '<a:frillishmale:1210330669138313326>',
    'frillish_female': '<a:frillishfemale:1210330664818450442>',
    'frillish_Male': '<a:frillishmale:1210330669138313326>',
    'frillish_Female': '<a:frillishfemale:1210330664818450442>',
    'galarian_Slowpoke': '<:slowpokegalar:1210321934575996958>',
    'galarian_slowpoke': '<:slowpokegalar:1210321934575996958>',
    'lapras': '<a:laprase:1210321933497925752>',
    'corsola': '<a:corsola:1210321930851188827>',
    'popplio': '<:popplio:1210321923809083413>',
    'phione': '<a:phione:1210321927231504394>',
    'manaphy': '<a:manaphy:1210321943778041937>',
    'beachegg': '<a:beachegg:1210322577021730887>',

    'sneasel': '<a:sneasel:1211083971438452786>',
    'chatot': '<a:chatot:1211083963724992522>',
    'alolan_sandshrew': '<:sandshrewalola:1211083966141173770>',
    'alolan_Sandshrew': '<:sandshrewalola:1211083966141173770>',
    'alolan_vulpix': '<:vulpixalola:1211083965100855336>',
    'alolan_Vulpix': '<:vulpixalola:1211083965100855336>',
    'swinub': '<a:swinub:1211083945051951194>',
    'amaura': '<:amaura:1211083967344943164>',
    'chingling': '<a:chingling:1211083958746480750>',
    'sentret': '<a:sentret:1211083960742969344>',
    'meloetta': '<a:meloettaaria:1211084478370422897>',
    'meloetta_pirouette': '<a:meloettapirouette:1211083949573541939>',
    'meloetta_Pirouette': '<a:meloettapirouette:1211083949573541939>',
    'snowyegg': '<a:snowyegg:1211085168417448058>',

    'bulbasaur': '<a:bulbasaur:1212557282982891570>',
    'wooper': '<a:wooper:1212557279954739273>',
    'paldean_Wooper': '<:wooperpaldea:1212557305879465995>',
    'paldean_wooper': '<:wooperpaldea:1212557305879465995>',
    'nidoran_male': '<a:nidoranm:1212557314687770665>',
    'nidoran_female': '<a:nidoranf:1212557310782734358>',
    'morelull': '<:morelull:1212557309281046558>',
    'foongus': '<a:foongus:1212557285185036348>',
    'venipede': '<a:venipede:1212557603721318440>',
    'gulpin': '<a:gulpin:1212557290302079067>',
    'grafaiai': '<:grafaiai:1212557306928300092>',
    'mudkip': '<a:mudkip:1212557293640618005>',
    'pecharunt': '<:pecharunt:1212557308220018728>',
    'stunky': '<a:stunky:1212557297176543303>',
    'seviper': '<a:seviper:1212557301022462062>',
    'croagunk': '<a:croagunk:1212557304747130921>',
    'swampegg': ''
}

favoriteberries = {
    'eevee': 'oran|pinap|razz|nanab|grepa|enigma|Harvest Pie',
    'eevee_shiny': 'pinap|razz|nanab|silver_pinap|silver_razz|silver_nanab|golden_pinap|golden_razz|golden_nanab|Silver Platter|Golden Delicacy',
    'espurr': 'sitrus',
    'espurr_shiny': 'sitrus|Silver Platter|Golden Delicacy',
    'pichu': 'leppa|coba|aguav|belue',
    'cleffa': 'oran|sitrus|maranga|micle',
    'oshawott': 'chesto|charti|aguav|pamtre|Tropical Custard',
    'snivy': 'pecha|kebia|salac|lansat|Forest Berry Medley',
    'tepig': 'cheri|chople|liechi|spelon',
    'phanpy': 'persim|shuca|grepa|rabuta|Desert Delight Cocktail',
    'minccino': 'oran|chilan|mago|micle',
    'nickit': 'oran|bluk|pomeg|magost|Crimson Cocktail',
    'vulpix': 'cheri|razz|petaya|spelon',
    'spheal': 'aspear|yache|wiki|watmel',
    'flarespeon': 'aspear|nanab|liechi|custap',
    'vaporeon': 'chesto|passho|kelpsy|pamtre',
    'jolteon': 'rawst|wacan|salac|nomel',
    'flareon': 'cheri|occa|tamato|spelon',
    'espeon': 'chesto|payapa|lum|rabuta|Desert Delight Cocktail',
    'umbreon': 'persim|colbur|ganlon|jaboca',
    'leafeon': 'leppa|rindo|kee|lansat',
    'glaceon': 'rawst|yache|wiki|cornn',
    'sylveon': 'pecha|roseli|mago|custap|Kalosian Thunderstruck Macarons',
    'hoppip': 'leppa|coba|grepa|cornn|Cornn Berry Popcorn',
    'azurill': 'oran|sitrus|apicot|watmel|Tropical Custard',
    'togepi': 'aspear|wepear|lum|micle',
    'mareep': 'cheri|wacan|iapapa|rowap',
    'skitty': 'oran|bluk|qualot|magost',

    'gossifleur': 'cheri|coba|tamato|cornn',
    'budew': 'cheri|kebia|aguav|spelon',
    'petilil': 'pecha|sitrus|liechi|magost',
    'cherubi': 'cheri|roseli|mago|custap',
    'fomantis': 'oran|tanga|hondew|rabuta',
    'bounsweet': 'nanab|chople|apicot|durin',
    'cottenee': 'oran|rindo|wiki|cornn',
    'cutiefly': 'pecha|roseli|mago|cornn',
    'sprigatito': 'persim|razz|hondew|enigma',
    'comfey': 'leppa|haban|iapapa|rabuta',
    'ralts': 'leppa|payapa|wiki|rowap',
    'flabebe_red': 'pecha|roseli|qualot|magost',
    'flabebe_orange': 'pecha|roseli|qualot|magost',
    'flabebe_yellow': 'pecha|roseli|qualot|magost',
    'flabebe_blue': 'pecha|roseli|qualot|magost',
    'flabebe_white': 'pecha|roseli|qualot|magost',
    'eternal_floette': 'haban|petaya',

    'purrloin': 'rawst|chilan|apicot|nomel',
    'meowth': 'persim|wepear|hondew|lansat',
    'alolan_meowth': 'persim|pinap|pomeg|durin|Alolan Smoked Pinap',
    'zigzagoon': 'persim|shuca|liechi|custap',
    'galarian_Zigzagoon': 'cheri|colbur|ganlon|jaboca',
    'lillipup': 'oran|chilan|grepa|micle',
    'glameow': 'pecha|nanab|mago|watmel',
    'rattata': 'cheri|razz|figy|cornn',
    'alolan_Rattata': 'oran|pinap|iapapa|watmel|Alolan Smoked Pinap',
    'zorua': 'cheri|kasib|pomeg|enigma',
    'litten': 'cheri|occa|pomeg|spelon',
    'trubbish': 'oran|kebia|kelpsy|jaboca',

    'dwebble': 'oran|charti|liechi|custap|cosnut',
    'buizel': 'cheri|coba|wiki|pamtre|cosnut',
    'slowpoke': 'aspear|payapa|kelpsy|pamtre|cosnut',
    'staryu': 'chesto|payapa|kelpsy|enigma|cosnut',
    'frillish_male': 'oran|kasib|pomeg|belue|cosnut',
    'frillish_female': 'aspear|kasib|pomeg|rowap|cosnut',
    'galarian_Slowpoke': 'chesto|wepear|kelpsy|pamtre|cosnut',
    'galarian_slowpoke': 'chesto|wepear|kelpsy|pamtre|cosnut',
    'lapras': 'pecha|sitrus|salac|durin|cosnut',
    'corsola': 'aspear|charti|aguav|cornn|cosnut',
    'popplio': 'oran|roseli|kelpsy|magost|cosnut',
    'phione': 'payapa|cosnut',
    'manaphy': 'tanga|cosnut',

    'sneasel': 'oran|colbur|liechi|jaboca',
    'chatot': 'chesto|razz|grepa|cornn',
    'alolan_sandshrew': 'chesto|pinap|ganlon|durin|Alolan Smoked Pinap',
    'alolan_Sandshrew': 'chesto|pinap|ganlon|durin|Alolan Smoked Pinap',
    'alolan_vulpix': 'oran|pinap|petaya|magost|Alolan Smoked Pinap',
    'alolan_Vulpix': 'oran|pinap|petaya|magost|Alolan Smoked Pinap',
    'swinub': 'cheri|sitrus|liechi|lansat',
    'amaura': 'aspear|yache|mago|micle',
    'chingling': 'leppa|payapa|hondew|micle',
    'sentret': 'leppa|chilan|iapapa|nomel',
    'meloetta': 'chilan',
    'meloetta_pirouette': 'chople',
    'meloetta_Pirouette': 'chople',
}

import pandas

import foods

foodlist = foods.getfoodlist()

def playsound(message,sound):
    uservoicechannel = message.author.voice.channel
    if uservoicechannel != None:
        voice_client = discord.utils.get(client.voice_clients, guild=message.guild)
        botvoicechannel = voice_client.channel
        print(botvoicechannel)

        if uservoicechannel == botvoicechannel:
            print('meow')
            voice_client.play(discord.FFmpegPCMAudio(f'sounds/{sound}.mp3', executable='ffmpeg/bin/ffmpeg.exe'))

def playcry(message,cry):
    uservoicechannel = message.author.voice.channel
    if uservoicechannel != None:
        voice_client = discord.utils.get(client.voice_clients, guild=message.guild)
        botvoicechannel = voice_client.channel
        print(botvoicechannel)

        if uservoicechannel == botvoicechannel:
            print('meow')
            voice_client.play(discord.FFmpegPCMAudio(f'sounds/cries/{cry}.mp3', executable='ffmpeg/bin/ffmpeg.exe'))


def makepetlist(userid):
    if not os.path.exists(f'pets/{userid}.csv'):
        print('No file for user, creating one...')

        with open(f'pets/{userid}.csv', 'w') as petfile:
            petfile.write('id,species,name,level,energytimer,lastfed,onexpedition,since,expeditiontime,exp')
    with open(f'pets/{userid}.csv', 'r') as petfile:
        lines = len(petfile.readlines())
        pets = []

    if lines > 1:
        file = pandas.read_csv(f"pets/{userid}.csv")
        pets = file.to_dict('records')
    return pets

def makeboxlist(userid,box):
    if box != 'all':
        if not os.path.exists(f'pets/boxes/{userid}'):
            os.mkdir(f'pets/boxes/{userid}')
        if not os.path.exists(f'pets/boxes/{userid}/{str(box)}.csv'):
            print('No file for user, creating one...')

            with open(f'pets/boxes/{userid}/{str(box)}.csv', 'w') as petfile:
                petfile.write('id,species,name,level,energytimer,lastfed,onexpedition,since,expeditiontime,exp')
        with open(f'pets/boxes/{userid}/{str(box)}.csv', 'r') as petfile:
            lines = len(petfile.readlines())
            pets = []
            print("LINES")
            print(lines)
            if lines > 1:
                file = pandas.read_csv(f"pets/boxes/{userid}/{str(box)}.csv")
                pets = file.to_dict('records')
            return pets
    else:
        pets = []
        if not os.path.exists(f'pets/boxes/{userid}'):
            os.mkdir(f'pets/boxes/{userid}')
        if len(os.listdir(f'pets/boxes/{userid}')) == 0:
            return None
        for file in os.listdir(f'pets/boxes/{userid}'):
            print(file)
            with open (f'pets/boxes/{userid}/{file}', 'r') as petfile:
                lines = len(petfile.readlines())
                if lines > 1:
                    file2 = pandas.read_csv(f'pets/boxes/{userid}/{file}')
                    pets.append(file2.to_dict('records'))
                else:
                    pets.append([{
                        'id': '999999999999999'
                    }])
        print(pets)
        return pets



def writetopetlist(userid,pets):
    with open(f'pets/{userid}.csv', 'r') as petfile:
        line1 = petfile.readline()
        line1 = line1.split(',')
        lastitem = line1[-1]
        lastitem = lastitem.replace('\n', '')
    with open(f'pets/{userid}.csv', 'w') as petfile:
        petfile.write('id,species,name,level,energytimer,lastfed,onexpedition,till,exp\n')
        for petdict in pets:
            for each in petdict:
                petfile.write(f'{petdict.get(each)}')
                if each != lastitem:
                    petfile.write(',')
            petfile.write('\n')

def writetoboxlist(userid,pets,box):
    with open(f'pets/boxes/{userid}/{box}.csv', 'r') as petfile:
        line1 = petfile.readline()
        line1 = line1.split(',')
        lastitem = line1[-1]
        lastitem = lastitem.replace('\n', '')
    with open(f'pets/boxes/{userid}/{box}.csv', 'w') as petfile:
        petfile.write('id,species,name,level,energytimer,lastfed,onexpedition,till,exp\n')
        for petdict in pets:
            for each in petdict:
                petfile.write(f'{petdict.get(each)}')
                if each != lastitem:
                    petfile.write(',')
            petfile.write('\n')

def deposit(userid,petid,where):
    boxlist = makeboxlist(userid,str(where))
    userpets = makepetlist(userid)
    response = "Error"
    if len(boxlist) >= 16:
        response = "That box is full!"
    else:
        for each in userpets:
            print(each.get('id'))
            if str(each.get('id')) == str(petid):
                print('found pet')
                depositedpet = each
                boxlist.append(depositedpet)
                userpets.remove(each)
                response = f"{each.get('name')} was deposited to cardboard box {str(where)}"

        print("MEOW")
        writetoboxlist(userid,boxlist,str(where))
        writetopetlist(userid,userpets)
    return response

def findbyid(userid,petid):
    if not os.path.exists(f'pets/boxes/{userid}'):
        os.mkdir(f'pets/boxes/{userid}')

    allpets = makeboxlist(userid,'all')
    i=0
    try:
        if len(allpets) == 0:
            print('')
    except:
        with open (f"pets/boxes/{userid}/1.csv", 'w') as file:
            file.write('id,species,name,level,energytimer,lastfed,onexpedition,till,exp\n')
            return '1'
    for boxes in allpets:
        for pet in boxes:
            print(pet)
            if str(pet.get('id')) == str(petid):
                correctpet = pet
                correctboxindex = i



                filelist = os.listdir(f'pets/boxes/{userid}')
                print(filelist)

                location = filelist[correctboxindex]
                print(location)

                where = location.split('.')[0]
                print('')
                print('where?')
                print(where)
                return where

        i+=1
        print(i)
    return 'none'

def findemptybox(userid):
    if not os.path.exists(f'pets/boxes/{userid}'):
        os.mkdir(f'pets/boxes/{userid}')
    filelist = os.listdir(f'pets/boxes/{userid}')
    empty = False
    i=0
    print("CCCC")
    for file in filelist:
        file = file.split('.')[0]
        boxlist = makeboxlist(userid,file)
        if len(boxlist) < 16 and file != "none":
            empty = True
            return file
        i += 1

    if not empty:
        i=0
        while not empty:
            i+=1

            filename = str(i)

            if filename not in filelist:
                return filename


def findemptyid(userid,partyids):
    notfound = True
    id = 0
    print("BBBBB")
    while notfound:
        print("DDDD")
        id += 1
        mon = findbyid(userid,id)
        if mon == 'none':
            if id not in partyids:
                notfound = False

    print(f'Empty ID found: {id}')
    return id



def retrieve(userid,petid):
    where = findbyid(userid,petid)
    userpets = makepetlist(userid)
    boxpets = makeboxlist(userid,str(where))
    print(boxpets)
    items = makeitemdict(userid)
    if 'Normal Gem' not in items:
        maximum = 5
    else:
        maximum = int(items.get('Normal Gem')) + 5
    if len(userpets) < maximum:
        print('meow1')
        for each in boxpets:
            print('meow')
            print(each.get('id'))
            print(petid)
            print('')
            if str(each.get('id')) == str(petid):
                boxpets.remove(each)
                userpets.append(each)
                response = f"Succesfully retrieved {each.get('name')} from cardboard box {where}"
                writetopetlist(userid,userpets)
                writetoboxlist(userid,boxpets,where)
                return response
        response = "Couldn't find that id"
    else:
        response = f'You already have {len(userpets)}/{maximum} pets active!'
    return response

def notify(userid,message):
    if not os.path.exists(f'pets/notifications/{userid}.csv'):
        print('No file for user, creating one...')

        with open(f'pets/notifications/{userid}.csv', 'w') as notificationfile:
            notificationfile.write('')
    with open(f'pets/notifications/{userid}.csv', 'r') as notificationfile:
        content = notificationfile.read()
        content = content + (message+'\n')
    with open(f'pets/notifications/{userid}.csv', 'w') as notificationfile:
        notificationfile.write(content)











def makefreezelist(userid):
    if not os.path.exists(f'berryfiles/freeze/{userid}.txt'):
        print('No file for user, creating one...')

        with open(f'berryfiles/freeze/{userid}.txt', 'w') as berryfile:
            berryfile.write('')
    with open(f'berryfiles/freeze/{userid}.txt', 'r') as berryfile:
        items = berryfile.read()
        freezelist = items.split("|")
        return freezelist


def writetofreezefile(userid, freezelist):
    with open(f'berryfiles/freeze/{userid}.txt', 'w') as berryfile:
        for each in freezelist:
            berryfile.write(f"{each}|")


def getscore(userid, type):
    if not os.path.exists(f'scores/{type}/{userid}.csv'):
        print('No cooldown file for user, creating one...')

        with open(f'scores/{type}/{userid}.csv', 'w+') as berryfile:
            berryfile.write('0')
    with open(f'berryfiles/{type}/{userid}.csv', 'r') as berryfile:
        points = berryfile.read()
    return points


def makeitemdictjson(userid):
    if not os.path.exists(f'berryfiles/{userid}.csv'):
        print('No file for user, creating one...')

        with open(f'berryfiles/{userid}.csv', 'w') as berryfile:
            items = {}
            items['energy'] = 0
            json.dump(items, berryfile)
    with open(f'berryfiles/{userid}.csv', 'r') as berryfile:
        items = json.load(berryfile)
        print(items)
        return items

def makeequipmentdict(userid):
    if not os.path.exists(f'equipment/{userid}.csv'):
        print('No file for user, creating one...')

        with open(f'equipment/{userid}.csv', 'w+') as berryfile:
            berryfile.write('gem,none,')
    with open(f'equipment/{userid}.csv', 'r') as berryfile:
        items = {}
        for line in berryfile:
            line = line.split(',')
            items[line[0]] = line[1]
        return items
def makeitemdict(userid):
    if not os.path.exists(f'berryfiles/{userid}.csv'):
        print('No file for user, creating one...')

        with open(f'berryfiles/{userid}.csv', 'w+') as berryfile:
            berryfile.write('item,count,\n')
            berryfile.write('energy,0,')
    with open(f'berryfiles/{userid}.csv', 'r') as berryfile:
        items = {}
        for line in berryfile:
            line = line.split(',')
            items[line[0]] = line[1]
        return items


def makecooldowndict(userid):
    if not os.path.exists(f'berryfiles/cooldowns/{userid}.csv'):
        print('No cooldown file for user, creating one...')

        with open(f'berryfiles/cooldowns/{userid}.csv', 'w+') as berryfile:
            berryfile.write('energy,0,\n')
            berryfile.write('zap,0,')
    with open(f'berryfiles/cooldowns/{userid}.csv', 'r') as berryfile:
        items = {}
        for line in berryfile:
            line = line.split(',')
            items[line[0]] = line[1]
        return items


def capitalizefirstletter(item):
    itemend = item[1:]
    firstchar = item[0]
    firstchar = firstchar.upper()
    word = firstchar + itemend
    return word

def lowerfirstletter(item):
    itemend = item[1:]
    firstchar = item[0]
    firstchar = firstchar.lower()
    word = firstchar + itemend
    return word

dishes = ['Pie', 'Barbaque', 'Chicken', 'Cake', 'Steak', 'Pork', 'Cookies']

allberrydishes = []
for berry in allberrystrings:
    for dish in dishes:
        allberrydishes.append(f'{capitalizefirstletter(berry)+' Berry'} {dish}')
print(allberrydishes)

berrymodifiers = {
    'fire': 'Flaming',
    'water': 'Refreshing',
    'electric': 'Electrifying',
    'ice': 'Chillded',
    'grass': 'Herbaceous',
    'fighting': 'Robust',
    'poison': '',
    'ground': 'Earthy',
    'flying': 'Whimsical',
    'psychic': 'Mystic',
    'bug': '',
    'rock': 'Sturdy',
    'ghost': 'Spectral',
    'dragon': 'Draconic',
    'dark': 'Mysterious',
    'steel': 'Resilient',
    'fairy': 'Enchanted'

}

allberrydishesandmodifiers = []
for dish in allberrydishes:
    allberrydishesandmodifiers.append(dish)
    for each in berrymodifiers:
        modifier = berrymodifiers.get(each)
        allberrydishesandmodifiers.append(f'{modifier} {dish}')



def writetoitemfile(userid, items):
    with open(f'berryfiles/{userid}.csv', 'w') as berryfile:
        for key in items:
            berryfile.write(f"{key},{items.get(key)},\n")

def writetoequipmentfile(userid, items):
    with open(f'equipment/{userid}.csv', 'w') as berryfile:
        for key in items:
            berryfile.write(f"{key},{items.get(key)},\n")


def writetocooldownfile(userid, items):
    with open(f'berryfiles/cooldowns/{userid}.csv', 'w') as berryfile:
        for key in items:
            berryfile.write(f"{key},{items.get(key)},\n")


def writetopointfile(userid, num):
    with open(f'scores/points/{userid}.csv', 'w') as berryfile:
        berryfile.write(str(num))


def makescoredict(guildid, type):
    if not os.path.exists(f'scores/{type}/{guildid}.csv'):
        print('No score file for guild, creating one...')
        with open(f'scores/{type}/{guildid}.csv', 'w+') as berryfile:
            berryfile.write(f'user,{type},\n')
    with open(f'scores/{type}/{guildid}.csv', 'r') as berryfile:
        items = {}
        for line in berryfile:
            line = line.split(',')
            items[line[0]] = line[1]
        return items


def writetoscorefile(guildid, items, type):
    with open(f'scores/{type}/{guildid}.csv', 'w') as berryfile:
        for key in items:
            berryfile.write(f"{key},{items.get(key)},\n")


for each in allberrystrings:
    juicename = capitalizefirstletter(each) + ' Berry Juice'
    juices.append(juicename)
    alledibles.append(juicename)


gems = []
for each in berrytypes:
    gemname = capitalizefirstletter(each) + ' Gem'
    gems.append(gemname)



juicessorted = []
for rarity in allberries:
    juicessorted.append('|')
    for juice in juices:
        juicesplit = juice.split(' ')
        berry = juicesplit[0]
        berry = lowerfirstletter(berry)
        if berry in rarity:
            juicessorted.append(juice)
print(juicessorted)




def gettimeinminutes():
    now = datetime.datetime.now(datetime.timezone.utc)
    yearminutes = (now.year - 2024) * 525600
    monthminutes = (now.month - 1) * 43800
    dayminutes = (now.day - 1) * 1440
    hourminutes = (now.hour - 1) * 60
    minutes = (now.minute - 1)
    totalminutes = yearminutes + monthminutes + dayminutes + hourminutes + minutes
    return totalminutes


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty, intents were likely not enabled')
        return

    userid: str = str(message.author.id)
    lowered: str = user_message.lower()

    petlist = makepetlist(userid)


    if "espurr." not in lowered and "esp." not in lowered and "es." not in lowered and "e." not in lowered:

        if "im straight" in lowered or "i'm straight" in lowered or "i‘m straight" in lowered or "i am straight" in lowered:
            await message.add_reaction('<:false:1217205478862622730>')

        if "gay" in lowered:
            await message.add_reaction("<a:Gay_Espurr:1211869778940272722>")

        if "i like berries" in lowered:
            for count in range(20):
                await message.add_reaction(berriestoemoteid.get(random.choice(allberrystrings)))

        currenttime = gettimeinminutes()
        print(currenttime)

        cooldowns = makecooldowndict(userid)
        cooldowndifference = currenttime - int(cooldowns.get('energy'))

        if cooldowndifference >= 2:

            print(cooldowns)
            cooldowns['energy'] = str(currenttime)
            print(cooldowns)
            writetocooldownfile(userid, cooldowns)

            energymodifier = 1
            if "energyboost" in cooldowns:
                energyboostdifference = currenttime - int(cooldowns.get('energyboost'))
                if energyboostdifference < 0:
                    print('Player has energy boost')
                    energymodifier = 1.5

            items = makeitemdict(userid)
            pointadd = math.trunc(random.randint(15, 25) * energymodifier)

            energygain = pointadd

            if 'Electric Gem' in items:
                energygain = math.trunc(((int(items.get("Electric Gem")) * 0.1) + 1) * pointadd)

            items['energy'] = str(int(items.get('energy')) + int(energygain))
            writetoitemfile(userid, items)
            print("energy granted")
            print(pointadd)

            ##pets uwu
            for petdict in petlist:


                eggtypes = ['egg', 'flowerfieldsegg', 'cityegg', 'beachegg', 'snowyegg']

                if petdict.get('species') in eggtypes:
                    if 'Fire Gem' in items:
                        # eggtime = ((int(items.get("Fire Gem")) * 0.2) + 1) * pointadd
                        eggtime = (((math.sqrt(int(items.get("Fire Gem"))))*0.5) + 0.7) * pointadd
                        currentenergy = math.trunc(int(petdict.get('energytimer')) - eggtime)
                    else:
                        currentenergy = int(petdict.get('energytimer')) - pointadd

                else:
                    currentenergy = int(petdict.get('energytimer')) - pointadd



                petdict['energytimer'] = str(currentenergy)
                writetopetlist(userid, petlist)

                if int(petdict.get('energytimer')) <= 0:


                    if petdict.get("species") in eggtypes:
                        mons = locations.getpokemon(petdict.get("species"))

                        monchoice = random.choice(mons)
                        monemote = monstoemoteid.get(lowerfirstletter(monchoice))

                        monchoicename = monchoice
                        if monchoice == 'Flabebe_red' or monchoice == 'Flabebe_orange' or monchoice == 'Flabebe_yellow' or monchoice == 'Flabebe_blue' or monchoice == 'Flabebe_white':
                            monchoicename = 'Flabebe'

                        await message.channel.send("Oh? It looks like your egg is hatching?")
                        time.sleep(3)
                        await message.channel.send(f"A(n) {monchoicename} popped out of the egg! {monemote}")

                        petdict['energytimer'] = 150
                        petdict['species'] = lowerfirstletter(monchoice)
                        if petdict.get('name') == "Egg":
                            petdict['name'] = monchoicename
                        petdict['level'] = 1

                        writetopetlist(userid, petlist)
                        print("MEOWWWWW")




                    if petdict.get("species") != 'egg':


                        berryoptions = levelups.getberryoptions(petdict)

                        berrychoice = random.choice(berryoptions)
                        if berrychoice in items:
                            items[berrychoice] = str(int(items.get(berrychoice)) + 1)
                        else:
                            items[berrychoice] = '1'
                        print("MEOW")
                        berryemote = berriestoemoteid.get(berrychoice)
                        notify(userid,f"{petdict.get('name')} brought you a(n) {berrychoice} berry {berryemote}")
                        petdict['energytimer'] = 150 - int(petdict.get('level'))
                        writetoitemfile(userid,items)

                        writetopetlist(userid,petlist)

            scores = makescoredict(message.guild.id, 'energy')
            if str(message.author.id) not in scores:
                scores[str(message.author.id)] = '0'
            scores[str(message.author.id)] = str(int(scores.get(str(message.author.id))) + pointadd)
            writetoscorefile(message.guild.id, scores, 'energy')

    if prefix_used := user_message[:7] == "espurr.":
        user_message = user_message[7:]
        prefix_used = True

    elif prefix_used := user_message[:4] == "esp.":
        user_message = user_message[4:]
        prefix_used = True

    elif prefix_used := user_message[:3] == "es.":
        user_message = user_message[3:]
        prefix_used = True

    elif prefix_used := user_message[:2] == "e.":
        user_message = user_message[2:]
        prefix_used = True

    lowered: str = user_message.lower()

    try:
        if prefix_used == True:

            ##commands

            print(lowered)
            if lowered == 'meow':
                response = "Meow!"
                ping = client.latency * 1000
                await message.channel.send(f'Meow! ({round(ping, 2)}ms)')







            elif (lowered == 'teleportberry' or lowered == 'tpb'):

                if userid in lock:
                    await message.channel.send("Wait for your spin to finish")
                else:
                    lock.append(userid)


                    freezelist = makefreezelist(userid)

                    items = makeitemdict(userid)

                    canspin = False
                    defaultlocation = True
                    if 'currentlocation' not in items:
                        items['currentlocation'] = 'default'
                        writetoitemfile(userid,items)
                        common_options, uncommon_options, rare_options, super_rare_options, legendary_options, eggs_options = locations.getberryset('default')
                        canspin = True
                        await message.channel.send("Current location: default")

                    elif items.get('currentlocation') == 'default':
                        common_options, uncommon_options, rare_options, super_rare_options, legendary_options, eggs_options = locations.getberryset('default')
                        canspin = True
                        writetoitemfile(userid, items)
                        await message.channel.send("Current location: default")


                    elif items.get('currentlocation') == 'flowerfields':
                        common_options, uncommon_options, rare_options, super_rare_options, legendary_options, eggs_options = locations.getberryset('flowerfields')
                        if int(items.get('flowerfieldsspins')) < 1:
                            await message.channel.send("You don't have any spins left here, use **espurr.travel** to return back")
                        else:
                            canspin = True
                            defaultlocation = False
                            items['flowerfieldsspins'] = str(int(items.get('flowerfieldsspins'))-1)
                            writetoitemfile(userid, items)
                            spinsleft = items.get((items.get('currentlocation')) + 'spins')
                            await message.channel.send(
                                f"Current location: Flowers of Eternity (**{str(int(spinsleft)+1)}** spins left!)")

                    elif items.get('currentlocation') == 'city':
                        common_options, uncommon_options, rare_options, super_rare_options, legendary_options, eggs_options = locations.getberryset('city')
                        if int(items.get('cityspins')) < 1:
                            await message.channel.send("You don't have any spins left here, use **espurr.travel** to return back")
                        else:
                            canspin = True
                            defaultlocation = False
                            items['cityspins'] = str(int(items.get('cityspins'))-1)
                            writetoitemfile(userid, items)
                            spinsleft = items.get((items.get('currentlocation')) + 'spins')
                            await message.channel.send(
                                f"Current location: The City (**{str(int(spinsleft)+1)}** spins left!)")

                    elif items.get('currentlocation') == 'beach':
                        common_options, uncommon_options, rare_options, super_rare_options, legendary_options, eggs_options = locations.getberryset('beach')
                        if int(items.get('beachspins')) < 1:
                            await message.channel.send("You don't have any spins left here, use **espurr.travel** to return back")
                        else:
                            canspin = True
                            defaultlocation = False
                            items['beachspins'] = str(int(items.get('beachspins'))-1)
                            writetoitemfile(userid, items)
                            spinsleft = items.get((items.get('currentlocation')) + 'spins')
                            await message.channel.send(
                                f"Current location: Cosmic Coastline (**{str(int(spinsleft)+1)}** spins left!)")

                    elif items.get('currentlocation') == 'snowy':
                        common_options, uncommon_options, rare_options, super_rare_options, legendary_options, eggs_options = locations.getberryset('snowy')
                        if int(items.get('snowyspins')) < 1:
                            await message.channel.send("You don't have any spins left here, use **espurr.travel** to return back")
                        else:
                            canspin = True
                            defaultlocation = False
                            items['snowyspins'] = str(int(items.get('snowyspins'))-1)
                            writetoitemfile(userid, items)
                            spinsleft = items.get((items.get('currentlocation')) + 'spins')
                            await message.channel.send(
                                f"Current location: Aria Peaks (**{str(int(spinsleft)+1)}** spins left!)")

                    else:
                        common_options, uncommon_options, rare_options, super_rare_options, legendary_options, eggs_options = locations.getberryset(
                            'default')
                        canspin = True
                        items['currentlocation'] = 'default'
                        writetoitemfile(userid, items)
                        await message.channel.send("Current location: default")


                    if canspin:
                        btype = 'none'
                        berry_chance = random.randint(1, 1000)
                        if berry_chance < 700:
                            commonlist = common_options.copy()
                            if defaultlocation == True:
                                for each in freezelist:
                                    if each in commonlist:
                                        commonlist.remove(each)
                            berry_choice = random.choice(commonlist)
                            btype = 'common'
                        if berry_chance >= 700 and berry_chance < 900:
                            uncommonlist = uncommon_options.copy()
                            if defaultlocation == True:
                                for each in freezelist:
                                    if each in uncommonlist:
                                        uncommonlist.remove(each)
                            berry_choice = random.choice(uncommonlist)
                            btype = 'uncommon'
                        if berry_chance >= 900 and berry_chance < 975:
                            rarelist = rare_options.copy()
                            if defaultlocation == True:
                                for each in freezelist:
                                    if each in rarelist:
                                        rarelist.remove(each)
                            berry_choice = random.choice(rarelist)
                            btype = 'rare'
                        if berry_chance >= 975 and berry_chance < 1000:
                            exoticlist = super_rare_options.copy()
                            if defaultlocation == True:
                                for each in freezelist:
                                    if each in exoticlist:
                                        exoticlist.remove(each)
                            berry_choice = random.choice(exoticlist)
                            btype = 'super_rare'
                        if berry_chance == 1000:
                            berry_choice = random.choice(legendary_options)
                            btype = 'legendary'

                        egg_chance = random.randint(1,50)
                        if egg_chance == 25:
                            berry_choice = random.choice(eggs_options)
                            btype = 'egg'



                        userid: str = str(message.author.id)
                        items = makeitemdict(userid)






                        berryemote = berriestoemoteid.get(berry_choice)




                        chance = 0
                        count = 1

                        energycost = 50

                        if int(items["energy"]) < int(energycost):
                            response = f"Sorry, you need {energycost} psychic energy to do that"
                            if items.get('currentlocation')+'spins' not in items:
                                items[items.get('currentlocation') + 'spins'] = '1'
                            else:
                                items[items.get('currentlocation')+'spins'] = str(int(items.get(items.get('currentlocation')+'spins'))+1)
                            writetoitemfile(userid,items)
                            await message.channel.send(response)

                        else:
                            items["energy"] = str(int(items.get("energy")) - energycost)
                            writetoitemfile(userid, items)

                            if 'Psychic Gem' in items:
                                psychicgemlevel = (int(items.get('Psychic Gem')))

                            firstroll = True
                            donea = False
                            while donea == False:
                                btype = 'none'
                                berry_chance = random.randint(1, 1000)
                                if berry_chance < 700:
                                    commonlist = common_options.copy()
                                    if defaultlocation == True:
                                        for each in freezelist:
                                            if each in commonlist:
                                                commonlist.remove(each)
                                    print(commonlist)
                                    berry_choice = random.choice(commonlist)
                                    btype = 'common'
                                if 700 <= berry_chance < 900:
                                    uncommonlist = uncommon_options.copy()
                                    if defaultlocation == True:
                                        for each in freezelist:
                                            if each in uncommonlist:
                                                uncommonlist.remove(each)
                                    print(uncommonlist)
                                    berry_choice = random.choice(uncommonlist)
                                    btype = 'uncommon'
                                if 900 <= berry_chance < 975:
                                    rarelist = rare_options.copy()
                                    if defaultlocation == True:
                                        for each in freezelist:
                                            if each in rarelist:
                                                rarelist.remove(each)
                                    berry_choice = random.choice(rarelist)
                                    btype = 'rare'
                                if 975 <= berry_chance < 1000:
                                    exoticlist = super_rare_options.copy()
                                    if defaultlocation == True:
                                        for each in freezelist:
                                            if each in exoticlist:
                                                exoticlist.remove(each)
                                    berry_choice = random.choice(exoticlist)
                                    btype = 'super_rare'
                                if berry_chance == 1000:
                                    berry_choice = random.choice(legendary_options)
                                    btype = 'legendary'
                                egg_chance = random.randint(1, 50)
                                if egg_chance == 25:
                                    berry_choice = random.choice(eggs_options)
                                    btype = 'egg'







                                if 'Grass Gem' in items:
                                    print("User has grass gem")
                                    grassgemlevel = int(items.get('Grass Gem'))
                                    chance = 1.9 / (math.log(1 / ((1 / 200) * grassgemlevel + 1.04472022), 10)) + 100
                                    print(chance)

                                    count = 1
                                    done = False
                                    while done == False:
                                        n = random.random() * 100
                                        if n <= chance:
                                            count = count + 1
                                        else:
                                            done = True

                                if btype == "egg":
                                    count = 1

                                equipment = makeequipmentdict(userid)
                                type = equipment.get('gem')
                                if berry_choice in common or berry_choice in uncommon:
                                    if type != 'none':
                                        gemname = capitalizefirstletter(type) + ' Gem'
                                        gemlevel = items.get(gemname)
                                        berry = berrytypes.get(type)
                                        print(f'Wearing {gemname} Lvl.{gemlevel}')
                                        chance = random.randint(1, 100)
                                        if chance >= 85:
                                            berry_choice = berry
                                            btype = 'uncommon'

                                berryemote = berriestoemoteid.get(berry_choice)

                                if 'Psychic Gem' in items:
                                    if psychicgemlevel > 0:
                                        if count == 1:
                                            response = f"(You would get a {berry_choice} {berryemote}, is this what you want? Skips left: {psychicgemlevel})"
                                        else:
                                            response = f"(You would get {count} {berry_choice} berries {berryemote}, is this what you want? Skips left: {psychicgemlevel})"
                                        if firstroll:
                                            msg = await message.channel.send(response)
                                            await msg.add_reaction('✅')
                                            await msg.add_reaction('❌')
                                            firstroll = False
                                        else:
                                            await msg.clear_reactions()
                                            await msg.edit(content=response)
                                            await msg.add_reaction('✅')
                                            await msg.add_reaction('❌')
                                        username: str = str(message.author)

                                        def check(reaction, user):
                                            return user == message.author and str(reaction.emoji) in ['✅', '❌']
                                        try:
                                            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
                                            print(reaction)
                                            if str(reaction) == '✅':
                                                donea = True
                                                items = makeitemdict(userid)
                                                print("user accepted")
                                            elif str(reaction) == '❌':
                                                psychicgemlevel = psychicgemlevel - 1
                                        except asyncio.TimeoutError:
                                            donea = True
                                            items = makeitemdict(userid)
                                            print("user timed out -> accepted")
                                    else:
                                        donea = True
                                else:
                                    donea = True

                            if btype != 'egg':
                                if count == 1:
                                    response = f"*Espurr teleports {berry_choice} berry to you* {berryemote * count}"
                                else:
                                    response = f"*Espurr teleports {count} {berry_choice} berries to you* {berryemote * count}"
                                await message.channel.send(response)

                            if btype == 'uncommon':
                                response = "(This berry seems to be uncommon)"
                                await message.channel.send(response)
                                try:
                                    playsound(message, 'uncommonget')
                                except:
                                    print('')
                            if btype == 'rare':
                                response = "(This berry seems to be quite rare)"
                                await message.channel.send(response)
                                try:
                                    playsound(message, 'rareget')
                                except:
                                    print('')
                            if btype == 'super_rare':
                                response = "(This berry seems to be exotic)"
                                await message.channel.send(response)
                                try:
                                    playsound(message, 'superrareget')
                                except:
                                    print('')
                            if btype == 'legendary':
                                response = "(Oh? This berry seems to be exceedingly rare)"
                                await message.channel.send(response)
                                try:
                                    playsound(message, 'legendaryget')
                                except:
                                    print('')
                            if btype == 'egg':
                                await message.channel.send("Huh? It seems espurr brought you an egg by mistake\nMaybe it will hatch into something eventually...")
                                try:
                                    playsound(message, 'eggget')
                                except:
                                    print('')
                            else:
                                try:
                                    playsound(message, 'commonget')
                                except:
                                    print('')
                            print('test')



                            if btype != 'egg':
                                print('not an egg')
                                if berry_choice in items:
                                    items[berry_choice] = str(int(items.get(berry_choice)) + count)
                                else:
                                    items[berry_choice] = count
                                writetoitemfile(userid, items)
                                writetopetlist(userid, petlist)

                            else:
                                meow = False
                                petlist = makepetlist(userid)
                                usedids = []
                                notfull = True
                                for each in petlist:
                                    usedids.append(int(each.get('id')))
                                petid = findemptyid(userid,usedids)
                                items = makeitemdict(userid)
                                if 'Normal Gem' not in items:
                                    maximum = 5
                                else:
                                    maximum = int(items.get('Normal Gem')) + 5
                                if len(usedids) >= maximum:
                                    notfull = False

                                    petlist = makepetlist(userid)
                                    boxlist = makeboxlist(userid,'all')
                                    where = findemptybox(userid)


                                    await message.channel.send(f'You have too many pets, egg was deposited to box "{where}"')
                                    notfull = True
                                    meow = True





                                if notfull:
                                    newegg = {
                                            'id': petid,
                                            'species': f'{berry_choice}',
                                            'name': 'Egg',
                                            'level': 0,
                                            'energytimer': 500,
                                            'lastfed': 0,
                                            'onexpedition': False,
                                            'till': 0,
                                            'exp': 0
                                    }
                                    petlist.append(newegg)
                                    writetopetlist(userid, petlist)
                                    if meow:
                                        deposit(userid, petid, where)

                                else:
                                    await message.channel.send("(You discarded the egg)")

                                writetoitemfile(userid, items)
                    else:
                        await message.channel.send("You do not have enough energy")

                del lock[lock.index(userid)]



            elif lowered[:9] == "inventory" or lowered[:3] == 'inv':
                userid: str = str(message.author.id)
                guildid: str = str(message.guild.id)
                args = lowered.split(' ')
                if len(args) == 2:
                    targetname = args[1]

                    if "@" not in targetname:
                        guildid = str(message.guild.id)
                        print(guildid)
                        guild = client.get_guild(int(guildid))
                        print(guild)
                        target = guild.get_member_named(targetname)
                        print(target)

                    if "@" in targetname:
                        targetid = args[1]
                        targetid = targetid.replace('<', '')
                        targetid = targetid.replace('>', '')
                        targetid = targetid.replace('@', '')
                        target = await client.fetch_user(int(targetid))

                    userid = target.id

                if not os.path.exists(f'berryfiles/{userid}.csv'):
                    print('No file for user, creating one...')

                    with open(f'berryfiles/{userid}.csv', 'w+') as berryfile:
                        berryfile.write('item,count,')

                items = makeitemdict(userid)

                freezelist = makefreezelist(userid)

                # Write to temporary file
                line = 0

                with open(f'temp.txt', 'w') as tempfile:
                    listnames = ['Common', 'Uncommon', 'Rare', 'Exotic', 'Legendary']
                    i = 0
                    tempfile.write(f"# Berries\n")
                    for list in allberries:
                        tempfile.write(f"**{listnames[i]}**\n")
                        for item in list:
                            if item in items:
                                if item in freezelist:
                                    tempfile.write(':ice_cube: ')
                                itemname = capitalizefirstletter(item)
                                berryemote = berriestoemoteid.get(item)
                                tempfile.write(f"{itemname} Berries: {items.get(item)} {berryemote}")
                                if item in freezelist:
                                    tempfile.write(' (frozen) :ice_cube:')
                                tempfile.write('\n')
                                line = line + 1
                                if line % 20 == 0:
                                    tempfile.write(f"|")
                        tempfile.write(f"\n")
                        line = line + 1
                        if line % 20 == 0:
                            tempfile.write(f"|")
                        i += 1

                    tempfile.write(f"# Juices\n")

                    i = 0

                    listnames = ['Common', 'Uncommon', 'Rare', 'Exotic', 'Legendary']
                    i = 0
                    for juice in juicessorted:
                        if juice == '|':
                            tempfile.write(f"\n**{listnames[i]}**\n")
                            i += 1

                            line = line + 1
                            if line % 20 == 0:
                                tempfile.write(f"|")

                        berry = juice.split(' ')
                        berry = berry[0]
                        berry = lowerfirstletter(berry)
                        juiceemote = berriestoemoteid.get(berry)
                        if berry in juicestoemoteid:
                            juiceemote = juicestoemoteid.get(berry)

                        if juice in items:
                            tempfile.write(f"{juice}: {items.get(juice)} {juiceemote}\n")

                            line = line + 1
                            if line % 20 == 0:
                                tempfile.write(f"|")

                    tempfile.write(f"# Gems\n")
                    for each in gems:
                        if each in items:
                            itemname = capitalizefirstletter(each)
                            gemtype = lowerfirstletter(itemname.split(' ')[0])
                            gememote = typetogememote.get(gemtype)
                            tempfile.write(f"{itemname} Lvl.{items.get(each)} {gememote}\n")

                            line = line + 1
                            if line % 20 == 0:
                                tempfile.write(f"|")

                    tempfile.write(f"# Foods\n")
                    for each in foodlist:
                        if each in items:
                            foodemote = (foods.getfood(each)).get('Emoteid')
                            tempfile.write(f"{each}: {items.get(each)} {foodemote}")

                with open(f'temp.txt', 'r') as tempfile:
                    content = tempfile.read()
                    content = content.split('|')
                    print(content)

                    if content[-1] == '':
                        del content[-1]

                    pagelimit = len(content)
                    currentpage = 0
                    print(len(content))

                    first = True
                    done = False

                    while not done:
                        if first:
                            msg = await message.channel.send(content[currentpage] + f"\n(Page {currentpage+1} of {pagelimit})")
                            await msg.add_reaction('⬅️')
                            await msg.add_reaction('➡️')
                            await msg.add_reaction('<:Oran_Berry:1177001065678372874>')
                            await msg.add_reaction('<:oranjuiceup:1204134245472411668>')
                            await msg.add_reaction('💎')
                            first = False
                        else:
                            response = content[currentpage] + f"\n(Page {currentpage+1} of {pagelimit})"

                            await msg.clear_reactions()
                            await msg.edit(content=response)
                            await msg.add_reaction('⬅️')
                            await msg.add_reaction('➡️')
                            await msg.add_reaction('<:Oran_Berry:1177001065678372874>')
                            await msg.add_reaction('<:oranjuiceup:1204134245472411668>')
                            await msg.add_reaction('💎')
                        username: str = str(message.author)

                        def check(reaction, user):
                            return user == message.author and str(reaction.emoji) in ['⬅️', '➡️', '<:Oran_Berry:1177001065678372874>', '<:oranjuiceup:1204134245472411668>', '💎']

                        reaction, user = await client.wait_for('reaction_add', timeout=300.0, check=check)
                        print(reaction)
                        if str(reaction) == '⬅️':
                            currentpage -= 1
                            if currentpage < 0:
                                currentpage = pagelimit-1
                        elif str(reaction) == '➡️':
                            currentpage += 1
                            if currentpage > (pagelimit-1):
                                currentpage = 0
                        elif str(reaction) == '<:Oran_Berry:1177001065678372874>':
                            page = 0
                            for each in content:
                                if '# Berries' in each:
                                    currentpage = page
                                else:
                                    page = page + 1

                        elif str(reaction) == '<:oranjuiceup:1204134245472411668>':
                            page = 0
                            for each in content:
                                if '# Juices' in each:
                                    currentpage = page
                                else:
                                    page = page + 1

                        elif str(reaction) == '💎':
                            page = 0
                            for each in content:
                                if '# Gems' in each:
                                    currentpage = page
                                else:
                                    page = page + 1




                    #for each in content:
                    #    await message.channel.send(each)



            elif lowered[:9] == "inventory" or lowered[:3] == 'inv':
                userid: str = str(message.author.id)
                guildid: str = str(message.guild.id)
                args = lowered.split(' ')
                if len(args) == 2:
                    targetname = args[1]

                    if "@" not in targetname:
                        guildid = str(message.guild.id)
                        print(guildid)
                        guild = client.get_guild(int(guildid))
                        print(guild)
                        target = guild.get_member_named(targetname)
                        print(target)

                    if "@" in targetname:
                        targetid = args[1]
                        targetid = targetid.replace('<', '')
                        targetid = targetid.replace('>', '')
                        targetid = targetid.replace('@', '')
                        target = await client.fetch_user(int(targetid))

                    userid = target.id
                if not os.path.exists(f'berryfiles/{userid}.csv'):
                    print('No file for user, creating one...')

                    with open(f'berryfiles/{userid}.csv', 'w+') as berryfile:
                        berryfile.write('item,count,')

                items = makeitemdict(userid)
                print(items)
                freezelist = makefreezelist(userid)

                # Write to temporary file
                line = 0

                with open(f'temp.txt', 'w') as tempfile:
                    listnames = ['Common', 'Uncommon', 'Rare', 'Exotic', 'Legendary']
                    i = 0
                    for list in allberries:
                        tempfile.write(f"**{listnames[i]}**\n")
                        for item in list:
                            if item in items:
                                if item in freezelist:
                                    tempfile.write(':ice_cube: ')
                                itemname = capitalizefirstletter(item)
                                berryemote = berriestoemoteid.get(item)
                                tempfile.write(f"{itemname} Berries: {items.get(item)} {berryemote}")
                                if item in freezelist:
                                    tempfile.write(' (frozen) :ice_cube:')
                                tempfile.write('\n')
                            line = line+1
                            if line%20 == 0:
                                tempfile.write(f"|")
                        tempfile.write(f"\n")
                        line = line + 1
                        if line % 20 == 0:
                            tempfile.write(f"|")
                        i += 1

                        tempfile.write(f"# Juices\n")

                        i = 0


                        listnames = ['Common', 'Uncommon', 'Rare', 'Exotic', 'Legendary']
                        i = 0
                        for juice in juicessorted:
                            if juice == '|':
                                tempfile.write(f"**{listnames[i]}**\n")
                                i += 1

                                line = line + 1
                                if line % 20 == 0:
                                    tempfile.write(f"|")

                            if juice in items:
                                itemname = capitalizefirstletter(juice)
                                tempfile.write(f"{itemname}: {items.get(juice)}\n")

                                line = line + 1
                                if line % 20 == 0:
                                    tempfile.write(f"|")

                        tempfile.write(f"# Gems\n")
                        for each in gems:
                            if each in items:
                                itemname = capitalizefirstletter(each)
                                tempfile.write(f"{itemname} Lvl.{items.get(each)}\n")

                    tempfile.write(f"**Juices**\n")
                    for each in juices:
                        if each in items:
                            itemname = capitalizefirstletter(each)
                            tempfile.write(f"{itemname}: {items.get(each)}\n")

                    tempfile.write(f"\n**Gems**\n")
                    for each in gems:
                        if each in items:
                            itemname = capitalizefirstletter(each)
                            tempfile.write(f"{itemname} Lvl.{items.get(each)}\n")

                with open(f'temp.txt', 'r') as tempfile:
                    chars = tempfile.read()

                i = 0
                for each in chars:
                    i = i + 1

                if i > 2000:
                    # try again with no emotes
                    with open(f'temp.txt', 'w') as tempfile:
                        listnames = ['Common', 'Uncommon', 'Rare', 'Exotic', 'Legendary']
                        i = 0
                        for list in allberries:
                            tempfile.write(f"**{listnames[i]}**\n")
                            for item in list:
                                if item in items:
                                    if item in freezelist:
                                        tempfile.write(':ice_cube: ')
                                    itemname = capitalizefirstletter(item)
                                    tempfile.write(f"{itemname} Berries: {items.get(item)}")
                                    if item in freezelist:
                                        tempfile.write(' (frozen) :ice_cube:')
                                    tempfile.write('\n')
                            tempfile.write(f"\n")
                            i += 1

                        tempfile.write(f"**Juices**\n")
                        for each in juices:
                            if each in items:
                                itemname = capitalizefirstletter(each)
                                tempfile.write(f"{itemname}: {items.get(each)}\n")

                        tempfile.write(f"\n**Gems**\n")
                        for each in gems:
                            if each in items:
                                itemname = capitalizefirstletter(each)
                                tempfile.write(f"{itemname} Lvl.{items.get(each)}\n")

                    with open(f'temp.txt', 'r') as tempfile:
                        chars = tempfile.read()

                    i = 0
                    for each in chars:
                        i = i + 1

                    if i > 2000:

                        username = await client.fetch_user(int(userid))
                        file = File(f'temp.txt', filename=f"{username}'s_inventory.txt")
                        await message.channel.send(file=file)

                    else:

                        with open(f'temp.txt', 'r') as tempfile:
                            response = tempfile.read()
                        await message.channel.send(response)
                else:
                    with open(f'temp.txt', 'r') as tempfile:
                        response = tempfile.read()
                    await message.channel.send(response)






            elif lowered[:9] == "makejuice":
                args = lowered[10:]
                args = args.split(' ')
                print(args)

                items = makeitemdict(userid)

                if len(args) == 2:
                    try:
                        count = int(args[1])
                    except:
                        if args[1] == 'max' or args[1] == 'all':
                            if args[0] in items:
                                count = int(items.get(args[0])) // 3
                else:
                    count = 1
                if count < 1:
                    count = 1

                userid: str = str(message.author.id)


                cost = count * 3


                if True:
                    if args[0] in allberrystrings:
                        juiceemote = juicestoemoteid.get(args[0])
                        if args[0] in items:
                            owned = items.get(args[0])
                            if int(owned) >= cost:
                                itemname = capitalizefirstletter(args[0])
                                juicename = itemname + " Berry Juice"
                                print("Made " + juicename)
                                if juicename in items:
                                    items[juicename] = str(int(items.get(juicename)) + count)
                                else:
                                    items[juicename] = str(count)
                                items[args[0]] = int(items.get(args[0])) - cost
                                if items[args[0]] == 0:
                                    del items[args[0]]
                                writetoitemfile(userid, items)
                                response = "*Espurr creates some " + juicename + " for you* " + juiceemote
                                if count > 1:
                                    response = f"*Espurr creates {count} {juicename}s for you* " + juiceemote
                            else:
                                response = "You need 3 of the same berries to make juice"
                        else:
                            response = "You don't have that berry"
                    else:
                        response = "That is not a berry"

                await message.channel.send(response)


            elif lowered == "pet":
                response = "(You pet espurr, espurr is happy)"
                await message.channel.send(response)

                file = File(f'gifs/happy.gif', filename="happy.gif")
                await message.channel.send(file=file)

                response = "*purr*"
                await message.channel.send(response)

                cooldowns = makecooldowndict(userid)
                print(cooldowns)
                if 'pet' not in cooldowns:
                    cooldowns['pet'] = '0'
                writetocooldownfile(userid, cooldowns)

                now = datetime.datetime.now(datetime.timezone.utc)
                lastused = cooldowns.get('pet')

                if int(lastused) != int(now.day):

                    print(cooldowns)
                    cooldowns['pet'] = str(now.day)
                    print(cooldowns)
                    writetocooldownfile(userid, cooldowns)
                    print(1)

                    items = makeitemdict(userid)
                    pointadd = 250
                    items['energy'] = str(int(items.get('energy')) + int(pointadd))
                    writetoitemfile(userid, items)
                    print("energy granted")

                    scores = makescoredict(message.guild.id, 'energy')
                    if str(message.author.id) not in scores:
                        scores[str(message.author.id)] = '0'
                    scores[str(message.author.id)] = str(int(scores.get(str(message.author.id))) + pointadd)
                    writetoscorefile(message.guild.id, scores, 'energy')
                    response = "*Obtained 250 energy for petting espurr today*"
                    await message.channel.send(response)
                else:
                    await message.channel.send("(Recieve energy for petting espurr again at 0:00UTC!)")








            elif lowered[:9] == "givejuice":
                args = lowered[10:]
                args = args.split(' ')
                print(args)

                if len(args) == 3:
                    count = int(args[2])
                else:
                    count = 1
                if count < 1:
                    count = 1

                targetname = args[1]
                print(targetname)
                if "@" not in targetname:
                    guildid = message.guild.id
                    print(guildid)
                    guild = client.get_guild(guildid)
                    print(guild)
                    target = guild.get_member_named(targetname)
                    print(target)

                if "@" in targetname:
                    targetid = args[1]
                    targetid = targetid.replace('<', '')
                    targetid = targetid.replace('>', '')
                    targetid = targetid.replace('@', '')
                    target = await client.fetch_user(int(targetid))

                berry = args[0]
                if berry in juicestoemoteid:
                    juiceemote = juicestoemoteid.get(berry)

                userid: str = str(message.author.id)
                items = makeitemdict(userid)

                juicetogive = capitalizefirstletter(berry)
                juicetogive = juicetogive + " Berry Juice"

                print(juicetogive)
                print(juices)
                print(items)

                if juicetogive in juices:
                    if juicetogive in items:
                        if int(items.get(juicetogive)) >= int(count):
                            a = int(items.get(juicetogive)) - count
                            print(a)
                            items[juicetogive] = str(a)
                            if items[juicetogive] == "0":
                                del items[juicetogive]
                            writetoitemfile(userid, items)

                            userid: str = str(message.author.id)
                            if not os.path.exists(f'pointcounts/{userid}.csv'):
                                print('No point file for user, creating one...')

                                with open(f'pointcounts/{userid}.csv', 'w+') as berryfile:
                                    berryfile.write('0')

                            if not os.path.exists(f'pointcounts/{target.id}.csv'):
                                print('No point file for user, creating one...')

                                with open(f'pointcounts/{target.id}.csv', 'w+') as berryfile:
                                    berryfile.write('0')

                            pointvalues = {"common": 100,
                                           "uncommon": 300,
                                           "rare": 1000,
                                           "super_rare": 2500,
                                           "legendary": 10000}

                            btype = "common"
                            if berry in uncommon:
                                btype = "uncommon"
                            if berry in rare:
                                btype = "rare"
                            if berry in super_rare:
                                btype = "super_rare"
                            if berry in legendary:
                                btype = "legendary"

                            pointvalue = pointvalues.get(btype)

                            with open(f'pointcounts/{userid}.csv', 'r') as file:
                                pointcount = int(file.read())
                            with open(f'pointcounts/{target.id}.csv', 'r') as file:
                                targetpointcount = int(file.read())
                            print(target.id)
                            target = await client.fetch_user(int(target.id))
                            print(target)

                            if target.bot:
                                pointvalue = math.trunc(pointvalue / 2)
                                print('bot')

                            if 'Fairy Gem' in items:
                                print("User has fairy gem")
                                fairygemlevel = int(items.get('Fairy Gem'))
                                boost = 1 + (fairygemlevel * 0.05)
                                pointvalue = math.trunc(pointvalue * boost)

                            pointvalue = pointvalue * count
                            pointcount = pointcount + pointvalue

                            targetpointvalue = math.trunc(pointvalue / 5)
                            targetpointcount = targetpointcount + targetpointvalue

                            print(userid)
                            print(target.id)
                            if int(userid) != int(target.id):
                                with open(f'pointcounts/{userid}.csv', 'w+') as file:
                                    file.write(str(pointcount))
                                with open(f'pointcounts/{target.id}.csv', 'w+') as file:
                                    file.write(str(targetpointcount))
                                response = "*You gave <@" + str(
                                    target.id) + "> some " + juicetogive + " to drink.* " + juiceemote + "\n*Recieved " + str(
                                    pointvalue) + " points*\n*" + target.name + " received " + str(
                                    targetpointvalue) + " points*"

                            try:
                                targetitems = makeitemdict(target.id)
                                if "noping" in targetitems:
                                    if targetitems.get("noping") == '1':
                                        response = "*You gave " + target.name + " some " + juicetogive + " to drink.* " + juiceemote + "\n*Recieved " + str(
                                            pointvalue) + " points*\n*" + target.name + " received " + str(
                                            targetpointvalue) + " points*"
                            except:
                                print("user does not have items")

                            if target.id == 1199118078907269271:
                                response = "Eh? You're giving it to me? I suppose I'll drink it" + juiceemote + "\n*Received " + str(
                                    pointvalue) + " points*"
                            if int(target.id) == int(userid):
                                response = "*You drank the " + juicetogive + "* " + juiceemote
                        else:
                            response = "You don't have enough of that berry"
                    else:
                        response = "You don't have that juice"
                else:
                    response = "That is not a juice"

                with open(f'pointcounts/{message.author.id}.csv', 'r') as file:
                    pointcount = file.read()
                with open(f'pointcounts/{target.id}.csv', 'r') as file:
                    targetpointcount = file.read()
                scores = makescoredict(message.guild.id, 'points')
                scores[str(message.author.id)] = pointcount
                scores[str(target.id)] = targetpointcount
                writetoscorefile(message.guild.id, scores, 'points')

                await message.channel.send(response)









            elif lowered == "points":
                userid: str = str(message.author.id)
                guildid: str = str(message.guild.id)
                scoredict = makescoredict(guildid, 'points')
                pointcount = str(scoredict.get(userid))
                response = "You have " + pointcount + " points"
                await message.channel.send(response)

            elif lowered == "energy":
                userid: str = str(message.author.id)
                items = makeitemdict(userid)
                response = "You have " + items['energy'] + " psychic energy"
                await message.channel.send(response)




            elif lowered[:8] == "craftgem" or lowered[:9] == "creategem":
                userid: str = str(message.author.id)
                items = makeitemdict(userid)

                args = lowered.split(" ")[1:]
                print(args)

                gemtype = args[0]

                ingredient = berrytypes.get(gemtype)

                gemname = capitalizefirstletter(gemtype)
                gemname = gemname + ' Gem'

                if gemtype in berrytypes:
                    if ingredient in items:
                        if gemname not in items:
                            if int(items.get(ingredient)) >= 1:

                                items[ingredient] = str(int(items.get(ingredient)) - 1)
                                if items.get(ingredient) == 0:
                                    del items[ingredient]
                                items[gemname] = '1'
                                gememote = typetogememote.get(gemtype)
                                response = '*Espurr creates a gem out of ' + gemtype + ' energy from a ' + ingredient + ' berry* ' + gememote
                                await message.channel.send(response)
                                if gemname == "Fairy Gem":
                                    response = '(You feel like you might be able to gain more points from giving to others)'
                                    await message.channel.send(response)
                                writetoitemfile(userid, items)



                            else:
                                response = 'You need a ' + ingredient + ' berry to do that'
                                await message.channel.send(response)
                        else:
                            response = 'You already have that gem, use espurr.upgrade gem if you want to upgrade it'
                            await message.channel.send(response)
                    else:
                        response = 'You need a ' + ingredient + ' berry to do that'
                        await message.channel.send(response)
                else:
                    response = 'That is not a valid type'
                    await message.channel.send(response)



            elif lowered[:10] == "upgradegem":

                userid: str = str(message.author.id)
                items = makeitemdict(userid)
                args = lowered[11:]
                args = args.split(' ')
                print(args)
                gemtype = args[0]
                ingredient = berrytypes.get(gemtype)
                gememote = typetogememote.get(gemtype)
                gemname = capitalizefirstletter(gemtype)
                gemname = gemname + ' Gem'

                if gemname in items:
                    if gemtype == 'grass':
                        cost = math.trunc(int(items.get(gemname)) * 1.5 * 1) + 1
                    elif gemtype == 'psychic':
                        multiplier = 1 + (0.5) * (int(items.get(gemname)))
                        cost = math.trunc(int(items.get(gemname)) * 2 * multiplier) + 1
                    elif gemtype == 'normal':
                        multiplier = 1 + (0.5) * (int(items.get(gemname)))
                        cost = math.trunc((int(items.get(gemname))+1) ** 1.5) + 1
                    elif gemtype == 'ice':

                        multiplier = 1 + (0.5) * (int(items.get(gemname)))
                        cost = math.trunc(int(items.get(gemname)) * 2 * multiplier) + 1
                    else:
                        multiplier = 1 + (0.3) * (int(items.get(gemname)))
                        cost = math.trunc(int(items.get(gemname)) * 2 * multiplier) + 1
                    if ingredient in items:
                        if cost <= int(items.get(ingredient)):
                            items[ingredient] = str(int(items.get(ingredient)) - cost)
                            items[gemname] = str(int(items.get(gemname)) + 1)
                            if items.get(ingredient) == 0:
                                del items[ingredient]
                            response = '*Espurr upgrades your ' + gemtype + ' gem out of ' + gemtype + ' energy from ' + str(
                                cost) + ' ' + ingredient + ' berries* ' + gememote
                            await message.channel.send(response)
                            if gemtype == 'fairy':
                                response = '(You feel like you might be able to gain even more points from giving to others)'
                                await message.channel.send(response)
                            if gemtype == 'psychic':
                                response = '(You feel like you might be able to better predict what espurr will bring you)'
                                await message.channel.send(response)
                            if gemtype == 'grass':
                                response = '(You feel like you might be able to gain more berries from espurr)'
                                await message.channel.send(response)
                            if gemtype == 'normal':
                                response = '(You feel like you might be able to hold more pets)'
                                await message.channel.send(response)
                            if gemtype == 'fire':
                                response = '(You feel like you might be able to hatch eggs faster)'
                                await message.channel.send(response)
                            if gemtype == 'electric':
                                response = '(You feel like you might be able to gain more energy from activity)'
                                await message.channel.send(response)
                            writetoitemfile(userid, items)
                        else:
                            response = f'You need {cost} {ingredient} berries to do that'
                            await message.channel.send(response)
                    else:
                        response = "You dont have that berry"
                        await message.channel.send(response)
                else:
                    response = "That is not a valid gem type"
                    await message.channel.send(response)




            elif lowered == "help":
                response = """
**espurr.meow**: espurr meows and also provides the bot latency
**espurr.pet**: pets espurr
\n---\n                
**espurr.teleportberry**: espurr teleports a random berry to you. This costs psychic energy (obtained from activity)
**espurr.makejuice <berry> [count]**: espurr creates a juice out of the chosen berry if you own it
**espurr.inventory**: displays the items you have
**espurr.givejuice <berry> <target> [count]**: gives a user juice to drink, this gives you points based on the rarity of the berry used to make it, a 50% penalty is applied if juice is given to bots, the target will also recieve points, but only 20% of what the user obtains
**espurr.points**: displays how many points you have
**espurr.energy**: displays how much energy you have
**espurr.berrypings**: disables pings for berry related commands
**espurr.top <'points'/'energy'>**: displays the guild leaderboard for either current *points* or *total* energy collected
**espurr.eat <berry>**: eat a berry to boost energy gain for a certain amount of time (based on the berries rarity)
\n---\n
**espurr.craftgem <type>**: espurr will attempt to create a gem out of a supereffective berries that match with the type, please use **espurr.gemhelp** to get more information on this
**espurr.upgradegem <type>**: espurr will attempt to upgrade the gem using the respective berries
**espurr.equipgem <type/none>**: equip a gem to get more of the berry used to upgrade it from teleporting berries
\n
**More Help**
**espurr.gemhelp**: provides more information on how the gems work
**espurr.buddieshelp/petshelp**: provides help on how buddies/pets work
**espurr.boxhelp**: see how boxes work to store pets
"""

                await message.channel.send(response)

                response = """**espurr.slots <berry> <amount>**: Gamble (run the command without any arguments for more info on how it works)

**espurr.make <food> [count]**: Make food, which provides a greater amount of experience than the berries used to craft it!
**espurr.recipes**: See what foods espurr can make 

**espurr.shinyhunt <espurr/eevee>**: Go shiny hunting! Feed wild pokemon to keep a streak going and increase your chances of a shiny!
"""
                await message.channel.send(response)

            elif lowered == "gemhelp":
                response = """
Gems can be created with the super effective berries and will help you in a variety of ways
Below is a list of the gems in the bot currently and what they do, as well as what berries are required to make and upgrade them
\n
**Grass gem (rindo)**: Allows you to have a chance of getting extra berries when teleporting, higher levels = higher chance 
**Fairy gem (roseli)**: Increases the amount of points you and your target gets when giving juice, higher levels increase this further
**Psychic gem (payapa)**: Allows you to predict and skip rolls from teleport berry as many times as you have gem level
**Electric gem (wacan)**: Allows you to use **espurr.zap** to zap points from another user on a two hour cooldown, higher levels = more points zapped
**Ice gem (yache)**: Allows you to use **espurr.freeze** to freeze as many berries as you have gem level. If you receive a frozen berry from teleport berry it will automatically be rerolled to a new berry of the same rarity. You can also use **espurr.unfreeze** to unfreeze a berry
**Dragon gem (haban)**: Gives a small chance (depending on the gem level) for attacks like zap to crit, doing double damage
**Normal gem (chilan)**: Increases your max buddies by 1 per gem level
**Fire gem (occa)**: Decreases the time it takes eggs to hatch
**Electric gem (wacan)**: Increases the useable energy gained from activity"""

                await message.channel.send(response)

            elif lowered == "buddieshelp" or lowered == 'petshelp':
                response = """
Buddies will gather berries automatically as you gain energy (energy from petting espurr does not count)
Each species has a predetermined list of berries it can bring, a random berry will be chosen out of that list 
Leveling up your buddy can add new rarer berries to this list, and remove common ones
Increasing the level of your buddies also decreases the energy gain needed for them to bring a berry

**Obtaining**
Espurr will sometimes teleport an egg instead of a berry
You can only have 10 buddies at a time, so if you already have 10 buddies you will be prompted to dismiss one or the egg
The egg will hatch after enough energy is gained (energy from petting espurr does not count)


**espurr.buddies/pets**: See a list of the buddies you currently have including eggs
**espurr.feed <ID> <berry> [count]**: Feed a buddy to level it up, exp gain depends on berry rarity
**espurr.rename <ID> <newname>**: Rename a buddy to whatever you would like!
**espurr.dismiss <ID>**: Say goodbye to a buddy
**espurr.notifications**: Shows any new notifications related to buddies, such as items they have brought, if there are more than 20 new notifications it will only shows the last 20
"""
                await message.channel.send(response)

            elif lowered == "boxhelp" or lowered == "boxeshelp":
                response = """
Cardboard boxes can be used to store pets not currently in your party
You can store 16 pets in one box but you can have as many boxes as you want

**espurr.box**: Lists the boxes you have
**espurr.box <boxname>**: Lists the buddies in the desired box
**espurr.box deposit <petID> [boxname]**: deposits a buddy into the desired box (a new box will be created if you don't have the box you specified), If boxname is blank it will be stored to the next empty box, with a new box being created if all are full
**espurr.box retrieve <petID>**: retrieves desired buddy from the box system
**espurr.box remove <boxname>**: remove an box (be careful, this will delete any buddies that were stored inside, so make sure it is empty)

**espurr.box find <arguments>**: search for something within boxes, eligible matches will be displayed, along with which box they were found in
You can use one or more of the following as arguments:
- species:<species>
- name:<name>
- level:[>/</>=/<=/!=]<level>

For instance, if I wanted to find Eevees I had that are level 50 or greater, I could use **espurr.box find species:eevee level:>=50**
"""
                await message.channel.send(response)

            elif lowered == 'berrypings':
                userid: str = str(message.author.id)
                items = makeitemdict(userid)
                if "noping" in items:
                    if items.get("noping") == '0':
                        response = "You will no longer be pinged for berry related commands"
                        items['noping'] = '1'
                    elif items.get("noping") == '1':
                        response = "You will pinged for berry related commands"
                        items['noping'] = '0'
                else:
                    response = "You will no longer be pinged for berry related commands"
                    items['noping'] = '1'
                writetoitemfile(userid, items)
                await message.channel.send(response)


            elif lowered == "energy":
                userid: str = str(message.author.id)
                items = makeitemdict(userid)
                response = "You have " + items.get('energy') + " psychic energy"
                await message.channel.send(response)

            elif lowered[:3] == "top":

                args = lowered[4:]
                args = args.split(' ')

                if args[0] == 'points' or args[0] == 'energy':
                    scores = makescoredict(message.guild.id, args[0])
                    print(scores)
                    scoresusername = {}
                    for each in scores:
                        if each != 'user':
                            try:
                                user = await client.fetch_user(int(each))
                                if not user.bot:
                                    username = user.name
                                    nickname = 'krfjjsklfj'
                                    if username != nickname:
                                        username = f'{username}'
                                    scoresusername[username] = int(scores.get(each))
                            except:
                                print('Error with' + each)
                    sorteddict = sorted(scoresusername.items(), key=lambda x: x[1], reverse=True)
                    print(sorteddict)

                    with open(f'temp.txt', 'w') as tempfile:
                        if args[0] == 'energy':
                            tempfile.write('**Total energy collected**\n\n')
                        if args[0] == 'points':
                            tempfile.write('**Current points**\n\n')
                        for each in sorteddict:
                            tempfile.write(f'{each[0]}: {each[1]} {args[0]}\n')

                    with open(f'temp.txt', 'r') as tempfile:
                        response = tempfile.read()
                    await message.channel.send(response)


            elif lowered[:4] == 'info':

                args = lowered[5:]
                args = args.split(' ')
                item = args[0]
                item = item.lower()
                print(item)



                response = "Im sorry, I don't have information on that"

                if item in allberrystrings:
                    for each in berrydict:
                        if each['berry'] == item:
                            infos = ['info1', 'info2', 'info3']
                            info = random.choice(infos)
                            response = each[info]
                            response = response + " " + berriestoemoteid[item]

                if item in monstoemoteid:
                    levelup = levelups.getlevelups(item)
                    response = levelup

                    with (open ('temp.txt', 'w') as t):
                        t.write(f"# {capitalizefirstletter(item)}'s berry learnset {monstoemoteid.get(item)}\n")

                        t.write("**Starting Berries**\n")

                        for level in levelup:
                            if level == 1:
                                startingberries = levelup.get(level)
                                startingberries = startingberries[1:]
                                print(1)
                                startingberries = startingberries.split(' +')
                                print(startingberries)
                                startinglist = []
                                for each in startingberries:
                                    each = each + ' ' + berriestoemoteid.get(each)
                                    startinglist.append(each)
                                print(3)

                                t.write(f"{', '.join(startinglist)}\n")
                                t.write("\n**Levelup Berries**\n")
                            else:
                                levelupberries = levelup.get(level)
                                levelupberrieslist = levelupberries.split(' ')
                                finaltext = ''
                                for each in levelupberrieslist:
                                    text = each[1:]
                                    if each[0] == '+':
                                        text = 'adds ' + text + ' **+**' + berriestoemoteid.get(text)
                                    if each[0] == '-':
                                        text = 'removes ' + text + ' **-**' + berriestoemoteid.get(text)
                                    finaltext = finaltext + ', '+ text

                                t.write(f"Level {str(level)}: {text}\n")


                        favorites = favoriteberries.get(item)
                        favorites = favorites.split("|")
                        favoritelist = []
                        for each in favorites:
                            if each not in foodlist:
                                each = each + ' ' + berriestoemoteid.get(each)
                                favoritelist.append(each)
                            else:
                                each = each + ' ' + foods.getfood(each).get('Emoteid')
                                favoritelist.append(each)
                        favoritelist = ', '.join(favoritelist)

                        t.write(f"\n**Favorite Berries:** {favoritelist}")


                    with open ('temp.txt', 'r') as t:
                        response = t.read()


                if item == "cosmic" or item == 'beach':
                    response = """**Cosmic Coastline**
A mysterious beach where many water type Pokémon live
At night you could swear you see the stars of the galaxy in the water"""

                if item == "flowers" or item == 'flowerfields':
                    response = """**Flowers of Eternity**
A field of many colorful flowers
It is said that the flowers here can give or take away life in a second"""

                if item == "aria" or item == 'snowy':
                    response = """**Aria Peaks**
Mountain peaks covered in fluffy snow
If the wind blows just right, many swear you can hear music play, that has never been played before
Many pokemon come here to get inspiration for new pieces of music"""

                await message.channel.send(response)

            elif lowered[:12] == 'detailedinfo':

                args = lowered[13:]
                args = args.split(' ')
                item = args[0]
                item = item.lower()
                print(item)

                response = "Im sorry, I don't have information on that item"
                for each in berrydict:
                    if each['berry'] == item:
                        response = f'''
**Berry**: {each['berry']} {berriestoemoteid[item]}
**Flavor**
Spicy: {each['spicy']}
Dry: {each['dry']}
Sweet: {each['sweet']}
Bitter: {each['bitter']}
Sour: {each['sour']}

Smooth: {each['smooth']}
Color: {each['color']}
Type: {each['type']}
Effect: {each['effect']}
Number: {each['number']}
Size: {each['size']}cm
Firmness: {each['firmness']}
Inspiration: {each['inspiration']}

**Information**
{each['info1']}
{each['info2']}
{each['info3']}
'''
                await message.channel.send(response)

            elif lowered[:3] == 'zap':
                items = makeitemdict(userid)
                args = lowered[4:]
                args = args.split(' ')
                targetname = args[0]
                print(targetname)
                if "@" not in targetname:
                    guildid = message.guild.id
                    print(guildid)
                    guild = client.get_guild(guildid)
                    print(guild)
                    target = guild.get_member_named(targetname)
                    print(target)
                    targetid = target.id

                if "@" in targetname:
                    targetid = args[1]
                    targetid = targetid.replace('<', '')
                    targetid = targetid.replace('>', '')
                    targetid = targetid.replace('@', '')
                    target = await client.fetch_user(int(targetid))
                print(1)
                targetitems = makeitemdict(targetid)
                pointfile = makescoredict(guildid, 'points')
                print(pointfile)
                points = pointfile.get(str(userid))
                targetpoints = pointfile.get(str(targetid))
                print(targetpoints)
                cooldowns = makecooldowndict(userid)
                if 'zap' not in cooldowns:
                    cooldowns['zap'] = 0
                currenttime = gettimeinminutes()
                cooldowndifference = currenttime - int(cooldowns.get('zap'))
                cooldowntime = 120 - cooldowndifference
                print(2)
                if "Electric Gem" not in items:
                    await message.channel.send('You need an electric gem to do that')
                else:
                    if cooldowndifference > 120:

                        currenttargetpoints = int(pointfile.get(str(targetid)))
                        electricgemlevel = int(items.get("Electric Gem"))

                        cooldowns['zap'] = str(currenttime)
                        writetocooldownfile(userid, cooldowns)
                        print(1)

                        targetpoints = 190 + math.trunc(10*(electricgemlevel**1.5))

                        crit = False
                        if "Dragon Gem" in items:
                            dragongemlevel = int(items.get("Dragon Gem"))
                            chance = 1 / (math.log(1 / ((1 / 200) * dragongemlevel + 1.047), 10)) + 50
                            roll = random.randint(1,100)
                            if roll <= chance:
                                crit = True
                                targetpoints = targetpoints * 2
                        print(targetpoints)
                        pointfile[targetid] = str(int(pointfile.get(str(targetid))) - int(targetpoints))
                        writetoscorefile(guildid, pointfile, 'points')
                        if crit == True:
                            await message.channel.send('# Critical hit!')
                        await message.channel.send(f'*You zapped {targetpoints} points away from <@{targetid}>*')
                    else:
                        await message.channel.send(f'You can not use that again for {cooldowntime} minutes')


            elif lowered == 'cooktest':

                berries = []
                for each in berrydict:
                    berries.append(each.get('berry'))

                berrychoice = random.choice(allberrystrings)
                print(berrychoice)
                berrychoicename = capitalizefirstletter(berrychoice)
                dishchoice = random.choice(dishes)

                foodname = f'{berrychoicename} Berry {dishchoice}'

                response = f"*Espurr cooks some {foodname} for you*"
                await message.channel.send(response)

            elif lowered[:4] == 'cook':

                args = lowered.split(" ")
                berry = args[1]

                berries = []
                for each in berrydict:
                    berries.append(each.get('berry'))

                items = makeitemdict(userid)

                if 'Fire Gem' in items:
                    if berry in items:
                        if int(items.get(berry)) >= 3:

                            items[berry] = str(int(items.get(berry))-3)

                            berrychoicename = capitalizefirstletter(berry)

                            dishchoice = random.choice(dishes)


                            foodname = f'{berrychoicename} Berry {dishchoice}'

                            modifierchance = random.randint(1,100)
                            if modifierchance >= 90:
                                modifier = True
                                modifiername = 'Magic'
                                berrytype = None
                                for each in berrydict:
                                    if each.get('berry') == berry:
                                        berrytype = each.get('type')
                                        if berrytype in berrymodifiers:
                                            modifiername = berrymodifiers.get(berrytype)
                                foodname = f'{modifiername} {berrychoicename} Berry {dishchoice}'
                            else:
                                modifier = False


                            response = f"*Espurr cooks some {foodname} for you*"
                            await message.channel.send(response)

                            if foodname in items:
                                items[foodname] = str(int(items.get(foodname)) + 1)
                            else:
                                items[foodname] = '1'

                            writetoitemfile(userid,items)
                        else:
                            await message.channel.send("You need 3 berries to do that")
                    else:
                        await message.channel.send("You don't have that berry or it is not a valid berry type")
                else:
                    await message.channel.send("You need a fire gem to do that")

            elif lowered[:4] == "food":
                userid: str = str(message.author.id)
                guildid: str = str(message.guild.id)
                args = lowered.split(' ')
                if len(args) == 2:
                    targetname = args[1]

                    if "@" not in targetname:
                        guildid = str(message.guild.id)
                        print(guildid)
                        guild = client.get_guild(int(guildid))
                        print(guild)
                        target = guild.get_member_named(targetname)
                        print(target)

                    if "@" in targetname:
                        targetid = args[1]
                        targetid = targetid.replace('<', '')
                        targetid = targetid.replace('>', '')
                        targetid = targetid.replace('@', '')
                        target = await client.fetch_user(int(targetid))

                    userid = target.id

                if not os.path.exists(f'berryfiles/{userid}.csv'):
                    print('No file for user, creating one...')

                    with open(f'berryfiles/{userid}.csv', 'w+') as berryfile:
                        berryfile.write('item,count,')

                items = makeitemdict(userid)
                print(items)
                freezelist = makefreezelist(userid)

                # Write to temporary file
                with open(f'temp.txt', 'w') as tempfile:
                    for dish in allberrydishesandmodifiers:
                        if dish in items:
                            dishname = dish
                            if dish not in allberrydishes:
                                dishname = '*' + dish + '*'
                            tempfile.write(f"{dishname}: {items.get(dishname)}\n")

                with open(f'temp.txt', 'r') as tempfile:
                    content = tempfile.read()
                    await message.channel.send(content)



            elif lowered[:3] == "eat":
                    args = lowered[4:]
                    args = args.split(' ')
                    berry = args[0]

                    energymodifier = 1.5

                    if berry in allberrystrings:
                        items = makeitemdict(userid)
                        cooldowns = makecooldowndict(userid)
                        currenttime = gettimeinminutes()
                        if berry in items and int(items.get(berry)) > 0:
                            items[berry] = str(int(items.get(berry)) - 1)
                            energyboosttime = 5
                            boosttimename = '5 minutes'
                            if berry in uncommon:
                                energyboosttime = 20
                                boosttimename = '20 minutes'
                            if berry in rare:
                                energyboosttime = 60
                                boosttimename = 'an hour'
                            if berry in super_rare:
                                energyboosttime = 300
                                boosttimename = 'five hours'
                            if berry in legendary:
                                energyboosttime = 1440
                                boosttimename = 'a day'
                            if 'energyboost' not in cooldowns:
                                cooldowns['energyboost'] = '0'
                            if (int(cooldowns.get('energyboost')) - currenttime) > 0:
                                cooldowns['energyboost'] = str(currenttime + energyboosttime + (int(cooldowns.get('energyboost'))-currenttime))
                            else:
                                cooldowns['energyboost'] = str(currenttime + energyboosttime)
                            response = (f'*You ate the {berry} berry*')
                            await message.channel.send(response)
                            response = (f'(energy increased by {energymodifier}x times for {boosttimename})')
                            await message.channel.send(response)
                            writetoitemfile(userid, items)
                            writetocooldownfile(userid, cooldowns)

            elif lowered == 'multipliertime' or lowered == 'multtime' or lowered == 'boosttime':
                cooldowns = makecooldowndict(userid)
                energyboosttime = cooldowns.get('energyboost')
                currenttime = gettimeinminutes()
                remainingtime = int(energyboosttime) - currenttime
                response = f"You have {remainingtime} minutes of your 1.5x energy boost left"
                if remainingtime < 0:
                    response = "You do not currently have an energy boost"
                await message.channel.send(response)

            elif lowered[:6] == 'freeze':
                args = lowered.split(" ")
                berry = args[1]
                print(berry)
                items = makeitemdict(userid)
                if "Ice Gem" in items:
                    limit = items.get("Ice Gem")
                    freezelist = makefreezelist(userid)
                    while ('' in freezelist):
                        freezelist.remove('')
                    print(freezelist)

                    if berry in allberrystrings:
                        if len(freezelist) < int(limit):
                            allfrozen = False
                            if berry in common:
                                rarity = common
                            if berry in uncommon:
                                rarity = uncommon
                            if berry in rare:
                                rarity = rare
                            if berry in super_rare:
                                rarity = super_rare
                            if berry in legendary:
                                rarity = legendary

                            berrycount = 0
                            for each in freezelist:
                                if each in rarity:
                                    berrycount = berrycount + 1

                            print(berrycount)

                            freezelimit = (len(rarity) - 3)

                            if berrycount >= freezelimit:
                                allfrozen = True
                                print("All frozen")
                            if allfrozen:
                                await message.channel.send("You have already frozen too many berries of that rarity!")
                            else:
                                freezelist.append(berry)
                                await message.channel.send(
                                    f"*Espurr freezes your {berry} berry count*\n(You will not receive {berry} berries anymore)")
                                writetofreezefile(userid, freezelist)
                        else:
                            await message.channel.send("You have frozen the max amount of berries for your gem level")
                else:
                    await message.channel.send("You need an ice gem to do that")


            elif lowered[:8] == 'unfreeze':
                args = lowered.split(" ")
                berry = args[1]
                freezelist = makefreezelist(userid)
                if berry in freezelist:
                    freezelist.remove(berry)
                    await message.channel.send(f'*Espurr unfreezes your {berry} berry count*')
                    writetofreezefile(userid, freezelist)
                if berry == 'all':
                    freezelist = []
                    await message.channel.send(f'*Espurr unfreezes all of your berry counts*')
                    writetofreezefile(userid, freezelist)

            elif lowered == 'explode':
                if int(userid) == 380421338927726602:
                    await message.channel.send("*explodes*")
                    exit()
                else:
                    await message.channel.send("You are not allowed to do that")

            elif lowered[:8] == "equipgem":
                args = lowered.split(' ')
                type = args[1]

                items = makeitemdict(userid)
                equipment = makeequipmentdict(userid)

                gemname = f'{capitalizefirstletter(type)} Gem'

                oldgemtype = equipment.get('gem')
                oldgemname = f'{capitalizefirstletter(oldgemtype)} Gem'

                gemtype = lowerfirstletter((gemname.split(' '))[0])
                gememote = typetogememote.get(gemtype)
                oldgememote = typetogememote.get(oldgemtype)

                if gemname in items:
                    equipment['gem'] = type
                    if oldgemtype == 'none':
                        await message.channel.send(f"*You put the {gemname} on your forehead* {gememote}")
                    else:
                        await message.channel.send(f"*You took off the {oldgemname} and put the {gemname} on your forehead instead* {gememote}")

                elif type == 'none' or type == 'remove':
                    if oldgemname != 'none':
                        equipment['gem'] = 'none'
                        await message.channel.send(f"You took off the {oldgemname} {oldgememote}")
                    else:
                        await message.channel.send(f"You don't have a gem equipped!")

                writetoequipmentfile(userid,equipment)








            elif lowered == 'notifications' or lowered == 'mail':
                if not os.path.exists(f'pets/notifications/{userid}.csv'):
                    print('No file for user, creating one...')

                    with open(f'pets/notifications/{userid}.csv', 'w') as notificationfile:
                        notificationfile.write('')
                with open(f'pets/notifications/{userid}.csv', 'r') as notifications:
                    content = notifications.read()
                    split = content.split('\n')
                    if len(split) > 20:
                        content = '...\n' + '\n'.join(split[-20:])
                    if content == '':
                        await message.channel.send('You have no notifications!')
                    else:
                        await message.channel.send(content)
                with open(f'pets/notifications/{userid}.csv', 'w') as notifications:
                    notifications.write('')





            elif lowered[:8] == "psyshock":
                args = lowered.split(" ")
                count = 1
                if len(args) > 1:
                    count = int(args[1])
                count = count + 1
                if message.author.guild_permissions.administrator:
                    await message.channel.purge(limit=count)
                    if count == 2:
                        meow = await message.channel.send(f"*Psyshocked 1 message*")
                    else:
                        meow = await message.channel.send(f"*Psyshocked {str(count-1)} messages*")
                    time.sleep(3)
                    await meow.delete()
                else:
                    await message.channel.send("Sorry, you need administrator to do that")



            elif lowered == 'pets' or lowered == 'buddies' or lowered == 'children':
                petlist = makepetlist(userid)
                with open('temp.txt', 'w') as t:
                    for each in petlist:
                        petemote = monstoemoteid.get(each.get('species'))
                        t.write(f'''
ID {each.get('id')}: {each.get('name')} lvl.{each.get('level')} {petemote}''')
                with open('temp.txt', 'r') as t:
                    content = t.read()
                    await message.channel.send(content)

                if not os.path.exists(f'pets/notifications/{userid}.csv'):
                    print('No file for user, creating one...')

                    with open(f'pets/notifications/{userid}', 'w') as notificationfile:
                        notificationfile.write('')
                with open(f'pets/notifications/{userid}.csv', 'r') as notifications:
                    content = notifications.read()
                    split = content.split('\n')
                    number = str(len(split))
                    number = str(int(number)-1)
                    if int(number) >= 1:
                        if int(number) > 20:
                            number = "20+"
                        await message.channel.send(f'You have {number} new notifications {random.choice(mail)}\n(Use espurr.notifications to see them)')


            elif lowered[:6] == 'rename':
                petlist = makepetlist(userid)
                print(petlist)
                args = lowered.split(' ')
                petid = args[1]
                newname = capitalizefirstletter(args[2])
                canrename = True

                allowedchars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', '-', '1', '2', '3', '4', '5', '6',
                                '7', '8', '9', '0', '<', '>', '@']
                for each in str(args[2]):
                    print(each)
                    if each not in allowedchars:
                        print(1)
                        canrename = False

                if len(newname) > 21:
                    canrename = False

                if canrename:
                    for each in petlist:
                        if str(each.get('id')) == petid:
                            oldname = 'test'
                            oldname = each.get('name')
                            petemote = monstoemoteid.get(each.get('species'))
                            each['name'] = newname

                    writetopetlist(userid,petlist)

                    await message.channel.send(f'{oldname} was renamed to {newname} {petemote}')
                else:
                    await message.channel.send(f'Invalid name, please make sure it is 20 or less characters and uses only letters, numbers, -, _, @, <, or >')

            elif lowered[:7] == 'dismiss':
                i = 0
                args = lowered.split(' ')
                petid = args[1]
                for each in petlist:
                    petemote = monstoemoteid.get(each.get('species'))
                    if each.get('id') == int(petid):
                        del petlist[i]
                        await message.channel.send(f"Bye {each.get('name')}! {petemote}")
                    i += 1
                writetopetlist(userid, petlist)

            elif lowered[:4] == 'feed':
                petlist = makepetlist(userid)
                args = lowered.split(' ')
                petid = int(args[1])
                berrya = args[2:]
                berry = []
                numbers = ['1','2','3','4','5','6','7','8','9','0','max','all']

                for each in berrya:
                    isaword = True
                    if each in numbers:
                        isaword = False
                    for chars in each:
                        if chars in numbers:
                            isaword = False
                    if isaword:
                        berry.append((each))
                berrycapitalized = []

                print(berry)
                print('mmmeow')

                for each in berry:
                    berrycapitalized.append(capitalizefirstletter(each))

                berry = ' '.join(berry)
                print(berry)


                if 'juice' in berry.split(' '):
                        berry = ' '.join(berrycapitalized)
                        if 'Berry' not in berry:
                            berry = berry.split(' ')
                            berry = berry[0] + ' Berry ' + berry[1]

                isfood = False
                berry2 = berry.split(' ')
                berry3 = []
                for each in berry2:
                    berry3.append(capitalizefirstletter(each))
                berry4 = ' '.join(berry3)

                if berry in foodlist:
                    isfood = True
                    berry = berry4


                try:
                    if args[-1] == 'max' or args[-1] == 'all':
                        items = makeitemdict(userid)
                        count = int(items.get(berry))
                    else:
                        count = int(args[-1])
                except:
                    count = 1


                if count < 0:
                    count = 0

                atefavorite = False

                items = makeitemdict(userid)

                print(berry)
                for each in petlist:
                    if int(each.get('id')) == petid:
                        if berry in items:
                            if berry in items:
                                if int(items.get(berry)) >= count:
                                    items[berry] = str(int(items.get(berry))-count)
                                    if int(items.get(berry)) == 0:
                                        del items[berry]

                                    berryingredient = lowerfirstletter(berry)

                                    if berry in juices:
                                        berryingredient = lowerfirstletter(berrya[0])
                                        print(berryingredient)

                                    expgain = 0



                                    if isfood:
                                        fooddict = foods.getfood(berry)
                                        print(fooddict)
                                        for each2 in fooddict.get('Ingredients'):
                                            if each2 in common:
                                                expgain += 25
                                            if each2 in uncommon:
                                                expgain += 75
                                            if each2 in rare:
                                                expgain += 250
                                            if each2 in super_rare:
                                                expgain += 750
                                            if each2 in legendary:
                                                expgain += 10000
                                        print(expgain)
                                        expgain = math.trunc(float(fooddict.get('Multiplier'))*expgain)
                                        print(expgain)
                                        berryingredient = berry

                                    else:
                                        expgain = 0
                                        if berryingredient in common:
                                            expgain = 25
                                        if berryingredient in uncommon:
                                            expgain = 75
                                        if berryingredient in rare:
                                            expgain = 250
                                        if berryingredient in super_rare:
                                            expgain = 750
                                        if berryingredient in legendary:
                                            expgain = 10000


                                    favorites = favoriteberries.get(each.get('species'))
                                    favorites = favorites.split('|')

                                    if berryingredient in favorites:
                                        expgain = int(expgain * 1.5)
                                        atefavorite = True

                                    if berry in juices:
                                        expgain = int(expgain * 3 * 1.2)


                                    if each.get('species') in specialmons and atefavorite == False:
                                        expgain = int(expgain*0.5)


                                    each['exp'] = int(each.get('exp')) + expgain*count

                                    currentexp = int(each.get('exp'))
                                    print(currentexp)

                                    tonextlevel = 0
                                    currentlevel = each.get('level')
                                    oldlevel = currentlevel

                                    while currentexp > tonextlevel:
                                        nextlevel = currentlevel + 1
                                        tonextlevel = math.trunc(10 * ((nextlevel) ** 2))
                                        if nextlevel >= 101:
                                            tonextlevel = float('inf')
                                            print(tonextlevel)
                                        if currentexp >= tonextlevel:
                                            currentlevel = currentlevel + 1

                                    each['level'] = currentlevel

                                    petemote = monstoemoteid.get(each.get('species'))
                                    if berry in juices:
                                        await message.channel.send(
                                            f"{each.get('name')} ate the {berry} and gained {expgain * count} exp! {petemote}")
                                    elif berry in foodlist:
                                        await message.channel.send(f"{each.get('name')} ate the {berry} and gained {expgain * count} exp! {petemote}")
                                    else:
                                        await message.channel.send(
                                            f"{each.get('name')} ate the {berry} berry(s) and gained {expgain * count} exp! {petemote}")

                                    if currentlevel < oldlevel:
                                        try:
                                            print(each.get('species'))
                                            playcry(message,f'{each.get('species')}')
                                        except:
                                            print("Pokemon doesn't have sound")
                                    if atefavorite:
                                        if berry in juices:
                                            await message.channel.send(f"{each.get('name')} really liked that juice!")
                                        elif berry in foodlist:
                                            await message.channel.send(f"{each.get('name')} really liked that food!")
                                        else:
                                            await message.channel.send(f"{each.get('name')} really liked that berry!")
                                    if currentlevel > oldlevel:
                                        await message.channel.send(f"{each.get('name')} grew to level {each.get('level')}! {petemote}")
                                        try:
                                            playsound(message, 'levelup')
                                        except:
                                            print('')

                                    levelup = levelups.getlevelups(each.get('species'))

                                    for level in levelup:
                                        print('meow')
                                        if currentlevel >= level:
                                            if oldlevel < level:
                                                action = levelup.get(level)
                                                action = action.split(' ')[0]
                                                if '+' in action:
                                                    action = action.replace('+','')
                                                    berryemote = berriestoemoteid.get(action)
                                                    await message.channel.send(f'{each.get('name')} will now bring {action} berries! {berryemote}')
                                                elif '-' in action:
                                                    action = action.replace('-','')
                                                    berryemote = berriestoemoteid.get(action)
                                                    if each.get('species') == 'cleffa' or each.get('species') == 'mareep':
                                                        await message.channel.send(f'{each.get('name')} will bring less {action} berries! {berryemote}')
                                                    else:
                                                        await message.channel.send(f'{each.get('name')} will no longer bring {action} berries! {berryemote}')

                                else:
                                    await message.channel.send("You don't have enough!")
                            else:
                                await message.channel.send("You can't feed that item")
                        else:
                            await message.channel.send("You don't have that")
                writetopetlist(userid, petlist)
                writetoitemfile(userid, items)

            elif lowered[:8] == "gemtouch":
                items = makeitemdict(userid)

                args = lowered[9:]
                args = args.split(' ')
                targetname = args[0]
                pointstogive = args[1]
                if int(pointstogive) < 1:
                    pointstogive = 1
                print(targetname)
                if "@" not in targetname:
                    guildid = message.guild.id
                    print(guildid)
                    guild = client.get_guild(guildid)
                    print(guild)
                    target = guild.get_member_named(targetname)
                    print(target)
                    targetid = target.id

                if "@" in targetname:
                    targetid = args[0]
                    targetid = targetid.replace('<', '')
                    targetid = targetid.replace('>', '')
                    targetid = targetid.replace('@', '')
                    isbot = False
                    targetid = int(targetid)
                    print("Targetid")
                    print(targetid)
                    try:
                        await client.fetch_user((targetid))
                    except:
                        isbot = True
                print(1)
                targetitems = makeitemdict(targetid)
                equip = makeequipmentdict(userid)
                targetequip = makeequipmentdict(targetid)
                cooldowns = makecooldowndict(userid)
                date = datetime.datetime.now(datetime.timezone.utc)
                day = date.day


                if int(items.get('energy')) >= int(pointstogive):
                    if str(userid) != str(targetid):
                        if equip.get('gem') != 'none' and targetequip.get('gem') != 'none':
                            targetitems['energy'] = str(int(targetitems.get('energy'))+int(pointstogive))
                            items['energy'] = str(int(items.get('energy'))-int(pointstogive))
                            gem = typetogememote.get(equip.get('gem'))
                            targetgem = typetogememote.get(targetequip.get('gem'))
                            await message.channel.send(f"*You touched the gems on your forehead with <@{targetid}> and transfered {str(pointstogive)} energy to them* {gem}{targetgem}")
                            if 'gemtouch' not in cooldowns:
                                cooldowns['gemtouch'] = '0'
                            if str(cooldowns.get('gemtouch')) != str(day):
                                type = equip.get('gem')
                                targettype = targetequip.get('gem')
                                berry = berrytypes.get(type)
                                targetberry = berrytypes.get(targettype)

                                if berry not in items:
                                    items[berry] = '0'
                                if berry not in targetitems:
                                    targetitems[berry] = '0'
                                if targetberry not in items:
                                    items[targetberry] = '0'
                                if targetberry not in targetitems:
                                    targetitems[targetberry] = '0'

                                items[berry] = str(int(items.get(berry))+1)
                                targetitems[berry] = str(int(targetitems.get(berry)) + 1)
                                items[targetberry] = str(int(items.get(targetberry)) + 1)
                                targetitems[targetberry] = str(int(targetitems.get(targetberry)) + 1)

                                berryemote = berriestoemoteid.get(berry)
                                targetberryemote = berriestoemoteid.get(targetberry)

                                try:
                                    if berry != targetberry:
                                        await message.channel.send(f'You and {target.name} both recieved a(n) {berry} {berryemote} and {targetberry} {targetberryemote} berry for touching gems today')
                                    else:
                                        await message.channel.send(f'You and {target.name} both recieved two {berry} {berryemote}{berryemote} berries for touching gems today')
                                except:
                                    if berry != targetberry:
                                        await message.channel.send(f'You and {targetid} both recieved a(n) {berry} {berryemote} and {targetberry} {targetberryemote} berry for touching gems today')
                                    else:
                                        await message.channel.send(f'You and {targetid} both recieved two {berry} {berryemote}{berryemote} berries for touching gems today')



                                cooldowns['gemtouch'] = str(day)
                        else:
                            await message.channel.send("Either you or your target is not wearing a gem, use espurr.equipgem <type>!")
                    else:
                        await message.channel.send("You can't touch gems with yourself!")
                else:
                    await message.channel.send(f"You don't have that much energy")

                writetoitemfile(userid,items)
                writetoitemfile(targetid,targetitems)
                writetocooldownfile(userid,cooldowns)

            elif lowered[:6] == 'joinvc':
                voicechannel = message.author.voice.channel
                voice_client = discord.utils.get(client.voice_clients, guild=message.guild)
                if voice_client == None:
                    voice_client = await voicechannel.connect()
                else:
                    voice_client = await voice_client.move_to(voicechannel)


            elif lowered[:9] == 'soundtest':
                uservoicechannel = message.author.voice.channel
                if uservoicechannel != None:
                    voice_client = discord.utils.get(client.voice_clients, guild=message.guild)
                    botvoicechannel = voice_client.channel
                    print(botvoicechannel)

                    if uservoicechannel == botvoicechannel:
                        print('meow')
                        voice_client.play(discord.FFmpegPCMAudio('sounds/levelup.mp3', executable='ffmpeg/bin/ffmpeg.exe'))

            elif lowered == 'soundtest2':
                try:
                    playsound(message,'levelup')
                except:
                    return



            elif lowered[:6] == 'evolve':
                args = lowered.split(' ')
                items = makeitemdict(userid)
                petid = args[1]

                petlist = makepetlist(userid)




                eeveelutionscost = {
                    'flareon': 'occa',
                    'vaporeon': 'passho',
                    'jolteon': 'wacan',
                    'espeon': 'payapa',
                    'umbreon': 'colbur',
                    'leafeon': 'rindo',
                    'glaceon': 'yache',
                    'sylveon': 'roseli',
                    'flarespeon': 'occa and payapa'
                }

                cost = 10

                for each in petlist:
                    if each.get('id') == int(petid):

                        if each.get('species') == 'eevee':
                            if args[2] in eeveelutionscost:
                                berriesneeded = eeveelutionscost.get(args[2])
                                berriesneeded = berriesneeded.split(' and ')
                                canEvolve = True

                                for berry in berriesneeded:
                                    if berry in items:
                                        if int(items.get(berry)) < cost:
                                            canEvolve = False

                                if canEvolve:
                                    for berry in berriesneeded:
                                        items[berry] = str(int(items.get(berry))-cost)

                                    each['species'] = args[2]

                                    if each.get('name') == 'Eevee':
                                        each['name'] = capitalizefirstletter(args[2])

                                    writetopetlist(userid,petlist)
                                    writetoitemfile(userid,items)

                                    petemote = monstoemoteid.get(each.get('species'))
                                    await message.channel.send(f"{each.get("name")} evolved into {args[2]} {petemote} using {cost} {eeveelutionscost.get(args[2])} berries")

                                else:
                                    await message.channel.send(f"You need {cost} {eeveelutionscost.get(args[2])} berries to do that")



                            else:
                                await message.channel.send(
                                    f"That pokemon can currently not evolve into that")

                        else:
                            await message.channel.send(
                                f"That pokemon can currently not evolve")










            elif lowered[:3] == "box" or lowered[:5] == "boxes" or lowered[:9] == "cardboard" or lowered[:12] == "cardboardbox":
                isint = True
                args = lowered.split(' ')
                if len(args) != 1:
                    args = args[1:]
                    try:
                        val = int(args[0])
                    except:
                        isint = False
                else:
                    args = None

                if args == None:
                    with open('temp.txt', 'w') as t:
                        t.write("<a:box:1208509880902623292> Boxes:\n")
                        for file in os.listdir(f'pets/boxes/{userid}'):
                            file = file.split('.')[0]
                            t.write(f'''
{file}''')
                    with open('temp.txt', 'r') as t:
                        content = t.readlines()
                        content = ''.join(content)
                        await message.channel.send(content)


                elif len(args) == 1:
                    try:

                        notallowed = False
                        allowedchars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_','-','1','2','3','4','5','6','7','8','9','0']
                        for each in str(args[0]):
                            print(each)
                            if each not in allowedchars:
                                print(1)
                                notallowed = True

                        if len(args[0]) > 20:
                            notallowed = True
                            print(2)

                        if args[0] == 'none':
                            notallowed = True

                        if args[0] == 'None':
                            notallowed = True


                        if not notallowed:

                            pets = makeboxlist(userid,str(args[0]))
                            print(pets)
                            with open('temp.txt', 'w') as t:
                                if isint:
                                    t.write(f'''
        Cardboard box {args[0]} <a:box:1208509880902623292>''')
                                else:
                                    t.write(f'''
        Cardboard box "{args[0]} <a:box:1208509880902623292>"''')
                                print('meow')
                                for each in pets:
                                    print('meow2')
                                    petemote = monstoemoteid.get(each.get('species'))
                                    print('meow3')

                                    t.write(f'''
    ID {str(each.get('id'))}: {each.get('name')} lvl.{str(each.get('level'))} {petemote}''')

                            with open('temp.txt', 'r') as t:
                                content = t.readlines()
                                content = ''.join(content)
                                await message.channel.send(content)
                        else:
                            await message.channel.send("A box can be no more than 20 characters and can only use letters, numbers, -, or _")
                    except:
                        await message.channel.send("That is not a box you have")

                elif args[0] == "deposit":
                    petid = args[1]

                    notallowed = False
                    allowedchars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', '-', '1', '2', '3', '4', '5', '6',
                                    '7', '8', '9', '0']


                    try:
                        where = args[2]

                        notallowed = False
                        allowedchars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                                        'q',
                                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', '-', '1', '2', '3', '4', '5',
                                        '6',
                                        '7', '8', '9', '0']
                        print("Yes meow")


                        for each in str(where):
                            print(each)
                            if each not in allowedchars:
                                print(1)
                                notallowed = True

                        if len(where) > 20:
                            notallowed = True
                            print(2)

                        if not notallowed:
                            response = deposit(userid, petid, where)
                            await message.channel.send(response)
                    except:
                        where = findemptybox(userid)
                        response = deposit(userid, petid, where)
                        await message.channel.send(response)

                elif args[0] == "retrieve":
                    petid = args[1]
                    response = retrieve(userid,petid)
                    await message.channel.send(response)

                elif args[0] == "find":
                    args = args[1:]
                    allpets = makeboxlist(userid,'all')
                    eligiblepets = []
                    for boxes in allpets:
                        for pet in boxes:
                            eligiblepets.append(pet)

                    for each in args:
                        each = each.split(':')

                        if each[0] == 'species':
                            for boxes in allpets:
                                for pet in boxes:
                                    if pet.get('species') != each[1]:
                                        if pet in eligiblepets:
                                            eligiblepets.remove(pet)

                        elif each[0] == 'name':
                            for boxes in allpets:
                                for pet in boxes:
                                    if pet.get('name') != capitalizefirstletter(each[1]):
                                        if pet in eligiblepets:
                                            eligiblepets.remove(pet)

                        elif each[0] == 'level':
                            level = each[1]
                            action = level[0]
                            actions1 = ['>','<']
                            actions2 = ['>=','<=','!=', '=<', '=>']
                            if action in actions1:
                                level = level[1:]
                            if action in actions2:
                                level = level[2:]
                            print(level)
                            level = int(level)
                            print("AA")
                            for boxes in allpets:
                                for pet in boxes:
                                    if action == '>':
                                        if int(pet.get('level')) <= level:
                                            if pet in eligiblepets:
                                                eligiblepets.remove(pet)
                                    elif action == '<':
                                        if int(pet.get('level')) >= level:
                                            if pet in eligiblepets:
                                                eligiblepets.remove(pet)
                                    elif action == '>=' or action == '=>':
                                        if int(pet.get('level')) < level:
                                            if pet in eligiblepets:
                                                eligiblepets.remove(pet)
                                    elif action == '<=' or action == '=<':
                                        if int(pet.get('level')) > level:
                                            if pet in eligiblepets:
                                                eligiblepets.remove(pet)
                                    elif action == '!=':
                                        if int(pet.get('level')) == level:
                                            if pet in eligiblepets:
                                                eligiblepets.remove(pet)
                                    else:
                                        if int(pet.get('level')) != int(each[1]):
                                            if pet in eligiblepets:
                                                eligiblepets.remove(pet)

                        elif each[0] == 'brings':
                            for boxes in allpets:
                                for pet in boxes:
                                    berryoptions = levelups.getberryoptions(pet)
                                    if each[1] not in berryoptions:
                                        if pet in eligiblepets:
                                            eligiblepets.remove(pet)

                        elif each[0] == 'inlearnset':
                            for boxes in allpets:
                                for pet in boxes:
                                    maxlevelpet = pet.copy()
                                    maxlevelpet['level'] = '100'
                                    berryoptions = levelups.getberryoptions(maxlevelpet)
                                    if each[1] not in berryoptions:
                                        if pet in eligiblepets:
                                            eligiblepets.remove(pet)



                    if len(eligiblepets) != 0:
                        try:
                            with open('temp.txt', 'w') as t:
                                t.write("Matches:\n")
                                for each in eligiblepets:
                                    petemote = monstoemoteid.get(each.get('species'))
                                    t.write(f'''
    ID {each.get('id')}: {each.get('name')} lvl.{each.get('level')} {petemote} in box "{findbyid(userid,each.get('id'))}"''')

                            with open('temp.txt', 'r') as t:
                                content = t.readlines()
                                content = ''.join(content)
                                await message.channel.send(content)

                        except:
                            await message.channel.send("Too many to list! Try narrowing your search!")
                    else:
                        await message.channel.send("Couldn't find anything")

                elif args[0] == "remove":
                    os.remove(f'pets/boxes/{userid}/{args[1]}.csv')
                    await message.channel.send(f"Removed box {args[1]}")


            elif lowered[:7] == "deposit":
                args = lowered.split(' ')
                petid = args[1]
                try:
                    where = args[2]

                    notallowed = False
                    allowedchars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                                    'q',
                                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', '-', '1', '2', '3', '4', '5',
                                    '6',
                                    '7', '8', '9', '0']

                    for each in str(where):
                        print(each)
                        if each not in allowedchars:
                            print(1)
                            notallowed = True

                    if len(where) > 20:
                        notallowed = True
                        print(2)

                    if where == 'none':
                        notallowed = True

                    if where == 'None':
                        notallowed = True

                    if not notallowed:
                        response = deposit(userid, petid, where)
                        await message.channel.send(response)
                    else:
                        await message.channel.send(
                            "A box can be no more than 20 characters and can only use letters, numbers, -, or _")

                except:
                    where = findemptybox(userid)
                    response = deposit(userid, petid, where)
                    await message.channel.send(response)


            elif lowered[:8] == "retrieve":
                args = lowered.split(' ')
                petid = args[1]
                response = retrieve(userid, petid)
                await message.channel.send(response)



            elif lowered == "justatest":

                await message.channel.send(findbyid(userid,6))


            elif lowered[:4] == "play":
                song = lowered[5:]
                song = 'music/'+song
                playsound(message,song)

            elif lowered == "leavevc" or lowered == "stop" or lowered == "disconnect":
                uservoicechannel = message.author.voice.channel
                if uservoicechannel != None:
                    voice_client = discord.utils.get(client.voice_clients, guild=message.guild)
                    botvoicechannel = voice_client.channel
                    print(botvoicechannel)

                    if uservoicechannel == botvoicechannel:
                        print('meow')
                        await voice_client.disconnect()


            elif lowered == "locations" or lowered == "locationshelp" or lowered == "locationhelp" or lowered == "travelhelp":
                await message.channel.send("""**You can get rolls at these locations at a cost of 250 energy, how much you get will be based on your gem level, be warned it will still cost 50 energy to roll as normal though**:
Flowers of Eternity (flowerfields) (Requires level 7 fairy gem)
City (Requires level 7 dark gem)
Cosmic Coastline (beach) (Requires level 7 water gem)
Aria Peaks (snowy) (Requires level 5 ice gem)

use **espurr.buyteleports <location>** 
use **espurr.travel <location>** to move to that location, use espurr.travel default to get back""")

            elif lowered[:6] == "travel":
                args = lowered.split(" ")
                try:
                    where = args[1]
                except:
                    where = 'default'

                items = makeitemdict(userid)

                if where == 'flowerfields' or where == 'foe' or where == 'flowers_of_eternity' or where == 'flowersofeternity' or where == 'flowers':
                    where = 'flowerfields'
                    name = 'Flowers of Eternity'

                elif where == 'beach' or where == 'cosmiccoastline' or where == 'cosmic' or where == 'cosmic_coastline' or where == 'cc':
                    where = 'beach'
                    name = 'Cosmic Coastline'

                elif where == 'snowy' or where == 'ariapeaks' or where == 'aria' or where == 'aria_peaks' or where == 'ap' or where == 'peaks':
                    where = 'snowy'
                    name = 'Aria Peaks'

                elif where == 'city':
                    where = 'city'
                    name = 'The City'

                if where in locationslist:

                    items["currentlocation"] = where
                    await message.channel.send(f"*Espurr will now look for berries in {name}*")

                else:
                    items["currentlocation"] = 'default'
                    await message.channel.send(f"*Espurr will now look for berries everywhere*")
                writetoitemfile(userid,items)



            elif lowered[:12] == 'buyteleports':
                args = lowered.split(" ")
                where = args[1]

                items = makeitemdict(userid)

                print("meowmeow")





                if where == 'flowerfields' or where == 'foe' or where == 'flowers_of_eternity' or where == 'flowersofeternity' or where == 'flowers':

                    if int(items.get("Fairy Gem")) >= 7:
                        if int(items.get("energy")) >= 250:
                            items['energy'] = str(int(items.get('energy'))-250)

                            if where+'spins' not in items:
                                items[where+'spins'] = 10 + (((int(items.get('Fairy Gem')))-7)*5)
                            else:
                                items[where+'spins'] = str(int(items.get(where+'spins')) + 10 + (((int(items.get('Fairy Gem')))-7)*5))
                            writetoitemfile(userid,items)

                            await message.channel.send("Success!")


                        else:
                            await message.channel.send("You do not have enough energy")
                    else:
                        await message.channel.send("You need a higher gem level!")



                elif where == 'city':

                    if int(items.get("Dark Gem")) >= 7:
                        if int(items.get("energy")) >= 250:
                            items['energy'] = str(int(items.get('energy'))-250)

                            if where+'spins' not in items:
                                items[where+'spins'] = str(10 + (((int(items.get('Dark Gem')))-7)*5))
                            else:
                                items[where+'spins'] = str(int(items.get(where+'spins')) + 10 + (((int(items.get('Dark Gem')))-7)*5))
                            writetoitemfile(userid,items)

                            await message.channel.send("Success!")


                        else:
                            await message.channel.send("You do not have enough energy")
                    else:
                        await message.channel.send("You need a higher gem level!")

                elif where == 'beach' or where == 'cosmiccoastline' or where == 'cosmic' or where == 'cosmic_coastline' or where == 'cc':

                    if int(items.get("Water Gem")) >= 7:
                        if int(items.get("energy")) >= 250:
                            items['energy'] = str(int(items.get('energy'))-250)

                            if where+'spins' not in items:
                                items[where+'spins'] = str(10 + (((int(items.get('Water Gem')))-7)*5))
                            else:
                                items[where+'spins'] = str(int(items.get(where+'spins')) + 10 + (((int(items.get('Water Gem')))-7)*5))
                            writetoitemfile(userid,items)

                            await message.channel.send("Success!")


                        else:
                            await message.channel.send("You do not have enough energy")
                    else:
                        await message.channel.send("You need a higher gem level!")

                elif where == 'snowy' or where == 'ariapeaks' or where == 'aria' or where == 'aria_peaks' or where == 'ap' or where == 'peaks':

                    if int(items.get("Ice Gem")) >= 5:
                        if int(items.get("energy")) >= 250:
                            items['energy'] = str(int(items.get('energy'))-250)

                            if where+'spins' not in items:
                                items[where+'spins'] = str(10 + (((int(items.get('Ice Gem')))-5)*5))
                            else:
                                items[where+'spins'] = str(int(items.get(where+'spins')) + 10 + (((int(items.get('Ice Gem')))-5)*5))
                            writetoitemfile(userid,items)

                            await message.channel.send("Success!")


                        else:
                            await message.channel.send("You do not have enough energy")
                    else:
                        await message.channel.send("You need a higher gem level!")



                else:
                    await message.channel.send("Not a valid location")


            elif lowered[:4] == 'make':
                numbers = ['1','2','3','4','5','6','7','8','9']
                args = lowered.split(' ')

                hasnum = False
                for each in numbers:
                    if each in lowered:
                        hasnum = True

                if hasnum:
                    count = int(args[-1])
                    if count < 0:
                        count = 1
                    food = args[1:-1]
                else:
                    count = 1
                    food = args[1:]

                foodname = ' '.join(food)

                food2 = []
                for each in food:
                    food2.append(capitalizefirstletter(each))

                foodname2 = ' '.join(food2)

                print(food)
                print(count)
                print(foodname)
                print(foodname2)

                items = makeitemdict(userid)
                fooddict = foods.getfood(foodname)

                canmake = True
                if foodname in foodlist:

                    for ingredient in fooddict.get('Ingredients'):
                        if ingredient in items:
                            if int(items.get(ingredient)) >= count:
                                items[ingredient] = str(int(items.get(ingredient))-count)
                            else:
                                canmake = False
                                await message.channel.send("You do not have the ingredients required for that")
                        else:
                            canmake = False
                            await message.channel.send("You do not have the ingredients required for that")

                    if canmake:
                        if foodname2 in items:
                            items[foodname2] = str(int(items.get(foodname2))+count)
                        else:
                            items[foodname2] = str(count)
                        writetoitemfile(userid,items)
                        if count == 1:
                            await message.channel.send(f'*Espurr creates some {foodname2} for you* {fooddict.get("Emoteid")}')
                        else:
                            await message.channel.send(f'*Espurr creates {count} {foodname2}s for you* {fooddict.get("Emoteid")}')

                else:
                    await message.channel.send("That is not a food")


            elif lowered[:8] == 'recipies' or lowered[:7] == 'recipes':
                with open ("temp.txt", 'w') as t:
                    i = 0
                    for each in foodlist.values():
                        i = i+1
                        if i % 2 == 0:
                            ingredrients = each.get('Ingredients')
                            ingredientswithemotes = []
                            print('meowmeow')
                            for each2 in ingredrients:
                                ingredientswithemotes.append(f'{each2} {berriestoemoteid.get(each2)}')
                            ingredientswithemotes = ', '.join(ingredientswithemotes)
                            t.write(f'{each.get('Name')}: {ingredientswithemotes}\n')
                            if i % 20 == 0:
                                t.write(f"|")

                with open ('temp.txt', 'r') as t:
                    content = t.read()
                    content = content.split("|")
                    for each in content:
                        await message.channel.send(each)




            elif lowered[:5] == 'slots':
                berrieslol = allberrystrings.copy()

                print(lock)
                canspin = True

                if userid in lock:
                    await message.channel.send("Wait for your spin to finish")
                else:

                    args = lowered.split(' ')


                    try:
                        berryselect = args[1]
                        count = int(args[2])
                        if count <= 0:
                            meow

                    except:
                        await message.channel.send("""Please specify which berry you will sacrifice for the spin
                        
**espurr.slots <berry> <count>**

The potential return is based on how much and what berry you sacrifice

Three commons = 1
Uncommon = 1
Rare = 3
Exotic = 7
Legendary = 25

If you win you will get that many berries of whatever the spin matches 3 of

For example, if you do **espurr.slots sitrus 5** it will cost 5 sitrus berries, and if you win, you will recieve 5 of whatever you won
If you do **espurr.slots mago 3** it will cost 3 mago berries, and if you win, you will recieve 9 of whatever you won""")
                        canspin = False
                        berryselect = None
                        count = None


                    items = makeitemdict(userid)

                    if berryselect in common:
                        if count > 3:
                            returnvalue = math.trunc(count * 0.34)
                        else:
                            await message.channel.send("You need to use at least 5 commons")
                            canspin = False
                    elif berryselect in uncommon:
                        returnvalue = math.trunc(count)
                    elif berryselect in rare:
                        returnvalue = math.trunc(count*3)
                    elif berryselect in super_rare:
                        returnvalue = math.trunc(count*7)
                    elif berryselect in legendary:
                        returnvalue = math.trunc(count*25)
                    else:
                        returnvalue = None
                        canspin = False

                    if canspin:
                        if berryselect in items:
                            if int(items[berryselect]) >= count:
                                items[berryselect] = str(int(items.get(berryselect)) - count)
                                if int(items.get(berryselect)) == 0:
                                    del items[berryselect]
                            else:
                                await message.channel.send(f"You need {count} {berryselect} berries for that")
                                canspin = False
                        else:
                            await message.channel.send("You do not have that berry or it is not a valid berry")
                            canspin = False

                    if canspin:


                        lock.append(userid)

                        writetoitemfile(userid, items)

                        chance = random.randint(1,1000)

                        if chance < 550:
                            prize = False
                            berryset = False
                            rarity = False
                        elif chance >= 550 and chance < 750:
                            prize = common.copy()
                            berryset = common
                            rarity = 'common'
                        elif chance >= 750 and chance < 875:
                            prize = uncommon.copy()
                            berryset = uncommon
                            rarity = 'uncommon'
                        elif chance >= 875 and chance < 950:
                            prize = rare.copy()
                            berryset = rare
                            rarity = 'rare'
                        elif chance >= 950 and chance < 999:
                            prize = super_rare.copy()
                            berryset = super_rare
                            rarity = 'exotic'
                        else:
                            prize = legendary.copy()
                            berryset = legendary
                            rarity = 'legendary'

                        if prize == False:
                            slotberries = ['a','a','a']
                            while slotberries[0] == slotberries[1] and slotberries[1] == slotberries[2] and slotberries[0] == slotberries[2]:
                                i = 0
                                while i < 3:
                                    berry_chance = random.randint(1, 1000)
                                    if berry_chance < 600:
                                        berry_choice = random.choice(common)
                                    elif berry_chance >= 600 and berry_chance < 850:
                                        berry_choice = random.choice(uncommon)
                                    elif berry_chance >= 850 and berry_chance < 950:
                                        berry_choice = random.choice(rare)
                                    elif berry_chance >= 950 and berry_chance < 999:
                                        berry_choice = random.choice(super_rare)
                                    else:
                                        berry_choice = random.choice(legendary)
                                    slotberries[i] = berry_choice
                                    i+=1
                            print(slotberries)

                            randomnum = random.randint(1,100)
                            if randomnum >= 85:
                                if slotberries[0] != slotberries[1] and slotberries[1] != slotberries[2] and slotberries[0] != slotberries[2]:
                                    slotberries[1] = slotberries[0]

                        else:
                            slotberries = []
                            berry = random.choice(berryset)
                            for meow in range(3):
                                slotberries.append(berry)

                        await message.channel.send(f"""Cost: {count} {berryselect} berries
Potential return: {returnvalue}""")

                        response = f""

                        response += f"{berriestoemoteid.get(slotberries[0])}"
                        msg = await message.channel.send(response)
                        await asyncio.sleep(1)
                        response += f"{berriestoemoteid.get(slotberries[1])}"
                        await msg.edit(content=response)
                        await asyncio.sleep(1)
                        response += f"{berriestoemoteid.get(slotberries[2])}"
                        await msg.edit(content=response)
                        await asyncio.sleep(1)

                        if rarity:
                            response = f"You won {returnvalue} {slotberries[0]} berries! ({rarity})"
                            if slotberries[0] not in items:
                                items[slotberries[0]] = '0'
                            items[slotberries[0]] = str(int(items.get(slotberries[0]))+int(returnvalue))
                            writetoitemfile(userid,items)
                            await message.channel.send(response)

                        else:
                            await message.channel.send("No Prize")

                        del lock[lock.index(userid)]

            elif lowered[:9] == 'shinyhunt' or lowered[:2] == 'sh':
                args = lowered.split(' ')
                mon = args[1]
                shinyhuntable = {
                    'espurr': 'sitrus',
                    'eevee': 'razz pinap nanab'
                }

                berriesneeded = []

                berries = shinyhuntable.get(mon).split(" ")
                for each in berries:
                    berriesneeded.append(each)

                items = makeitemdict(userid)
                if userid in lock:
                    await message.channel.send("Finish your previous action first")
                else:
                    lock.append(userid)
                    if f"{mon}shinystreak" not in items:
                        items[f"{mon}shinystreak"] = '0'
                        shinystreak = 0
                    else:
                        shinystreak = int(items.get(f'{mon}shinystreak'))

                    shinychance = 4096 - (math.trunc((-0.001*shinystreak)+(47.5*shinystreak)))

                    if shinystreak > 86:
                        shinychance = 100

                    if shinychance < 100:
                        shinychance = 100

                    shiny = random.randint(1,shinychance)

                    if shiny == 1:
                        shiny = True
                    else:
                        shiny = False

                    if not shiny:

                        needed = random.choice(berriesneeded)

                        username: str = str(message.author)

                        response = f"""*An {capitalizefirstletter(mon)} appears* {monstoemoteid.get(mon)}
Would you like to feed the {capitalizefirstletter(mon)} a {needed} {berriestoemoteid.get(needed)} berry?
Current Streak: {shinystreak}
Current Odds: 1/{shinychance}"""
                        msg = await message.channel.send(response)
                        await msg.add_reaction('✅')
                        await msg.add_reaction('❌')



                        def check(reaction, user):
                            return user == message.author and str(reaction.emoji) in ['✅', '❌']

                        try:
                            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
                            print(reaction)
                            if str(reaction) == '✅':
                                if needed in items:
                                    if int(items.get(needed)) > 0:
                                        items[needed] = str(int(items.get(needed))-1)
                                        items[f'{mon}shinystreak'] = shinystreak+1
                                        await message.channel.send(f"*{capitalizefirstletter(mon)} is happy! Streak increased*")
                                    else:
                                        if shinystreak != 0:
                                            items[f'{mon}shinystreak'] = '0'
                                            await message.channel.send("You don't have one! Streak Ended")
                                else:
                                    if shinystreak != 0:
                                        items[f'{mon}shinystreak'] = '0'
                                        await message.channel.send("You don't have one! Streak Ended")
                            elif str(reaction) == '❌':
                                if shinystreak != 0:
                                    items[f'{mon}shinystreak'] = '0'
                                    await message.channel.send("Streak Ended")
                                else:
                                    await message.channel.send("No Streak")
                        except asyncio.TimeoutError:
                            if shinystreak != 0:
                                items[f'{mon}shinystreak'] = '0'
                                await message.channel.send("Streak Ended")

                        writetoitemfile(userid,items)
                        del lock[lock.index(userid)]


                    else:
                        shinymon = mon+"_shiny"
                        await message.channel.send(f"""*Oh wow! A shiny {capitalizefirstletter(mon)} appears* {monstoemoteid.get(shinymon)}
It seems to want to join you!""")

                        meow = False
                        petlist = makepetlist(userid)
                        usedids = []
                        notfull = True
                        for each in petlist:
                            usedids.append(int(each.get('id')))
                        petid = findemptyid(userid, usedids)
                        items = makeitemdict(userid)
                        if 'Normal Gem' not in items:
                            maximum = 5
                        else:
                            maximum = int(items.get('Normal Gem')) + 5
                        if len(usedids) >= maximum:
                            notfull = False

                            petlist = makepetlist(userid)
                            boxlist = makeboxlist(userid, 'all')
                            where = findemptybox(userid)

                            await message.channel.send(f'You have too many pets, so Shiny {capitalizefirstletter(mon)} went to box "{where}"')
                            notfull = True
                            meow = True
                        else:
                            await message.channel.send(
                                f'Shiny {capitalizefirstletter(mon)} jumped into your party!')

                        if notfull:
                            newmon = {
                                'id': petid,
                                'species': f'{shinymon}',
                                'name': f'Shiny {capitalizefirstletter(mon)}',
                                'level': 5,
                                'energytimer': 500,
                                'lastfed': 0,
                                'onexpedition': False,
                                'till': 0,
                                'exp': 0
                            }
                            petlist.append(newmon)
                            writetopetlist(userid, petlist)
                            if meow:
                                deposit(userid, petid, where)

                        writetoitemfile(userid, items)
                        del lock[lock.index(userid)]

            elif lowered[:4] == "sort":
                args = lowered.split(" ")

                what = args[1]

                by = args[2]

                newpetlist = []

                if what == 'party':
                    petlist = makepetlist(userid)

                ##else:
                ##    petlist = makeboxlist(userid,what)

                unsorted = []
                if by == 'id':
                    for each in petlist:
                        unsorted.append(int(each.get('id')))
                    sorteda = unsorted.copy()

                if by == 'name':
                    i = 0
                    for each in petlist:
                        i += 1
                        unsorted.append((each.get('name'))+str(i))

                if by == 'species':
                    i = 0
                    for each in petlist:
                        i += 1
                        unsorted.append((each.get('species'))+str(i))

                if by == 'level':
                    i = 1000
                    for each in petlist:
                        i += 1
                        unsorted.append(int((str(each.get('level'))+str(i))))


                sorteda = unsorted.copy()

                sorteda.sort()


                for each in sorteda:
                    index = unsorted.index(each)
                    newpetlist.append(petlist[index])


                print(newpetlist)



                if what == "party":
                    if by == "level" or by == "name" or by == "species" or by =="id":
                        writetopetlist(userid,newpetlist)
                        await message.channel.send("Sorted!")
                ##elif by == "level" or by == "name" or by == "species" or by =="id":
                ##    if newpetlist != []:
                ##        writetoboxlist(userid, newpetlist, what)
                ##        await message.channel.send("Sorted!")


















                        # math stuff dont worry about it

            elif lowered[:9] == 'integrate' or lowered[:3] == 'int':
                args = lowered.split(" ")

                problem = args[1:]
                problem = ' '.join(problem)

                response = simpleintegral(problem)


                await message.channel.send(response)


            elif lowered[:9] == 'berrycode':
                args = lowered.split(" ")
                if "key" in args[-1]:
                    key = args[-1].replace("key:", "")
                    del args[-1]
                else:
                    key = "none"

                berriesforcode = ['cheri', 'chesto', 'pecha', 'rawst', 'aspear', 'leppa', 'oran', 'persim',
'occa', 'passho', 'wacan', 'rindo', 'yache', 'chople', 'kebia', 'shuca', 'coba', 'payapa', 'tanga',
'charti', 'kasib', 'haban', 'colbur', 'babiri', 'chilan', 'razz', 'nanab', 'pinap', 'bluk',
'wepear', 'roseli', 'sitrus', 'lum', 'figy', 'wiki', 'mago', 'aguav', 'iapapa', 'pomeg', 'kelpsy', 'qualot',
'hondew', 'grepa', 'tamato', 'liechi', 'ganlon', 'salac', 'petaya', 'apicot', 'kee', 'maranga',
'cornn', 'magost', 'rabuta', 'nomel', 'spelon', 'pamtre', 'watmel', 'durin', 'belue',
'lansat', 'micle', 'custap', 'jaboca', 'rowap', 'enigma', 'starf']

                num = 0
                i = 0
                for each in key:
                    i = i + 1
                    num = num + int(ord(each)) * i

                print(num)

                letters = {
                    "a": '',
                    "b": '',
                    "c": '',
                    "d": '',
                    "e": '',
                    "f": '',
                    "g": '',
                    "h": '',
                    "i": '',
                    "j": '',
                    "k": '',
                    "l": '',
                    "m": '',
                    "n": '',
                    "o": '',
                    "p": '',
                    "q": '',
                    "r": '',
                    "s": '',
                    "t": '',
                    "u": '',
                    "v": '',
                    "w": '',
                    "x": '',
                    "y": '',
                    "z": ''
                }

                num = num + 1000000
                for each in letters:

                    index = (num % (len(berriesforcode)+1))-1
                    letters[each] = berriesforcode[index]
                    del berriesforcode[index]

                print(letters)

                msg = " ".join(args[1:])
                messagelist = []

                for each in msg:
                    messagelist.append(each)

                newmessagelist = []
                for each in messagelist:
                    if each in letters:
                        each = berriestoemoteid.get(letters.get(each))
                    newmessagelist.append(each)

                finalmessage = "".join(newmessagelist)

                await message.channel.send(finalmessage)

            elif lowered[:6] == "decode":
                args = lowered.split(" ")
                if "key" in args[-1]:
                    key = args[-1].replace("key:", "")
                    del args[-1]
                else:
                    key = "none"

                berriesforcode = ['cheri', 'chesto', 'pecha', 'rawst', 'aspear', 'leppa', 'oran', 'persim',
                                  'occa', 'passho', 'wacan', 'rindo', 'yache', 'chople', 'kebia', 'shuca', 'coba',
                                  'payapa', 'tanga',
                                  'charti', 'kasib', 'haban', 'colbur', 'babiri', 'chilan', 'razz', 'nanab', 'pinap',
                                  'bluk',
                                  'wepear', 'roseli', 'sitrus', 'lum', 'figy', 'wiki', 'mago', 'aguav', 'iapapa',
                                  'pomeg', 'kelpsy', 'qualot',
                                  'hondew', 'grepa', 'tamato', 'liechi', 'ganlon', 'salac', 'petaya', 'apicot', 'kee',
                                  'maranga',
                                  'cornn', 'magost', 'rabuta', 'nomel', 'spelon', 'pamtre', 'watmel', 'durin', 'belue',
                                  'lansat', 'micle', 'custap', 'jaboca', 'rowap', 'enigma', 'starf']

                num = 0
                i = 0
                for each in key:
                    i = i + 1
                    num = num + int(ord(each)) * i

                print(num)

                letters = {
                    "a": '',
                    "b": '',
                    "c": '',
                    "d": '',
                    "e": '',
                    "f": '',
                    "g": '',
                    "h": '',
                    "i": '',
                    "j": '',
                    "k": '',
                    "l": '',
                    "m": '',
                    "n": '',
                    "o": '',
                    "p": '',
                    "q": '',
                    "r": '',
                    "s": '',
                    "t": '',
                    "u": '',
                    "v": '',
                    "w": '',
                    "x": '',
                    "y": '',
                    "z": ''
                }

                num = num + 1000000
                for each in letters:
                    index = (num % (len(berriesforcode) + 1)) - 1
                    letters[each] = berriesforcode[index]
                    del berriesforcode[index]

                print(letters)



                msg = (args[1:])
                msg = " ".join(msg)
                print(msg)
                for each in berriestoemoteid:
                    if berriestoemoteid.get(each).lower() in msg:
                        replacement = None
                        berryname = None
                        for meow in letters:
                            if letters.get(meow) == each:
                                replacement = meow
                                print(replacement)
                        if replacement != None:
                            print(msg)
                            toreplace = str(berriestoemoteid.get(each).lower())
                            print(toreplace)
                            print(replacement)
                            msg = msg.replace(str(berriestoemoteid.get(each).lower()), replacement)


                for each in allberrystrings:
                    if each in msg:
                        replacement = None
                        for meow in letters:
                            if letters.get(meow) == each:
                                replacement = meow
                                print(replacement)
                        if replacement != None:
                            print(msg)
                            print(replacement)
                            msg = msg.replace(each, replacement)

                decodedmessage = "".join(msg)
                await message.channel.send(decodedmessage)

            elif lowered[:11] == 'v2berrycode':
                args = lowered.split(" ")
                if "key" in args[-1]:
                    key = args[-1].replace("key:", "")
                    del args[-1]
                else:
                    key = "none"

                berriesforcode = ['cheri', 'chesto', 'pecha', 'rawst', 'aspear', 'leppa', 'oran', 'persim',
                                  'occa', 'passho', 'wacan', 'rindo', 'yache', 'chople', 'kebia', 'shuca', 'coba',
                                  'payapa', 'tanga',
                                  'charti', 'kasib', 'haban', 'colbur', 'babiri', 'chilan', 'razz', 'nanab', 'pinap',
                                  'bluk',
                                  'wepear', 'roseli', 'sitrus', 'lum', 'figy', 'wiki', 'mago', 'aguav', 'iapapa',
                                  'pomeg', 'kelpsy', 'qualot',
                                  'hondew', 'grepa', 'tamato', 'liechi', 'ganlon', 'salac', 'petaya', 'apicot', 'kee',
                                  'maranga',
                                  'cornn', 'magost', 'rabuta', 'nomel', 'spelon', 'pamtre', 'watmel', 'durin', 'belue',
                                  'lansat', 'micle', 'custap', 'jaboca', 'rowap', 'enigma', 'starf']

                num = 0
                i = 0
                for each in key:
                    i = i + 1
                    num = num + int(ord(each)) * i

                print(num)





                msg2 = " ".join(args[1:])
                msg2decode = []



                for each in msg2:
                    msg2decode.append(each)

                print(msg2decode)

                num = num + len(msg2decode) + len(key)
                print("A")
                print(num)

                finalmessage = []

                max = len(key)
                keyindex = len(key)-1

                keylist = []
                for each in key:
                    keylist.append(each)

                i = -1
                j = len(msg2decode)+1
                print('j')
                print(j)

                for count in range(len(msg2decode)):
                    i = i + 1
                    j = j-1


                    if msg2decode[i] == " " or msg2decode[i] == "":
                        finalmessage.append(" ")

                    else:

                        num = num + 100 + ord(keylist[keyindex]) + keyindex + j
                        print(num)

                        num = num + ord(msg2decode[i])
                        print(ord(msg2decode[i]))

                        keyindex = keyindex - 1
                        if keyindex < 0:
                            keyindex = len(key)-1

                        index = (num % (len(berriesforcode)))

                        #index = -1
                        #for count in range(num):
                        #    index = index + 1
                        #    if index > (len(berriesforcode) - 1):
                        #        index = -1

                        finalmessage.append(berriestoemoteid.get(berriesforcode[index]))

                finalmessage = "".join(finalmessage)

                await message.channel.send("Encoded message: " + finalmessage)



            elif lowered[:8] == 'v2decode':

                args = lowered.split(" ")

                if "key" in args[-1]:

                    key = args[-1].replace("key:", "")

                    del args[-1]

                else:

                    key = "none"

                berriesforcode = ['cheri', 'chesto', 'pecha', 'rawst', 'aspear', 'leppa', 'oran', 'persim',

                                  'occa', 'passho', 'wacan', 'rindo', 'yache', 'chople', 'kebia', 'shuca', 'coba',

                                  'payapa', 'tanga',

                                  'charti', 'kasib', 'haban', 'colbur', 'babiri', 'chilan', 'razz', 'nanab', 'pinap',

                                  'bluk',

                                  'wepear', 'roseli', 'sitrus', 'lum', 'figy', 'wiki', 'mago', 'aguav', 'iapapa',

                                  'pomeg', 'kelpsy', 'qualot',

                                  'hondew', 'grepa', 'tamato', 'liechi', 'ganlon', 'salac', 'petaya', 'apicot', 'kee',

                                  'maranga',

                                  'cornn', 'magost', 'rabuta', 'nomel', 'spelon', 'pamtre', 'watmel', 'durin', 'belue',

                                  'lansat', 'micle', 'custap', 'jaboca', 'rowap', 'enigma', 'starf']

                num = 0

                i = 0

                for each in key:
                    i = i + 1

                    num = num + int(ord(each)) * i

                print(num)
                msg2 = " ".join(args[1:])

                if ">" not in msg2:
                    for each in berriesforcode:
                        msg2 = msg2.replace(each, berriestoemoteid.get(each))
                    print(msg2)



                msg2 = msg2.lower()
                msg2 = msg2.replace(">", "> ")
                msg2 = msg2.split(" ")






                msg2decode = msg2

                num = num + len(msg2) + len(key) - 1
                print("A")
                print(num)


                finalmessage = []

                max = len(key)

                keyindex = len(key) - 1

                keylist = []

                for each in key:
                    keylist.append(each)

                i = -1

                j = len(msg2decode)
                print('j')





                print(j)

                print(msg2)

                for each in msg2:

                    i = i + 1

                    j = j - 1

                    if each == '':

                        finalmessage.append(" ")


                    else:

                        num = num + 100 + ord(keylist[keyindex]) + keyindex + j
                        print(num)

                        testnum = 96
                        index2 = 0
                        first = True



                        for berry in berriestoemoteid:
                            if berriestoemoteid.get(berry).lower() == str(each):
                                each = berry
                                print("meow")

                        print(each)
                        a = 0


                        while berriesforcode[index2] != each and a <= 30 or first == True:

                            first = False
                            testnum = testnum + 1

                            if testnum > 122:
                                testnum = 97

                            num2 = num + testnum



                            keyindex2 = keyindex - 1

                            if keyindex2 < 0:
                                keyindex2 = len(key) - 1

                            index2 = (num2 % (len(berriesforcode)))

                            #index2 = -1
                            #for count in range(num2):
                            #    index2 = index2+1
                            #    if index2 > (len(berriesforcode)-1):
                            #        index2 = -1






                            a = a+1
                            print(a)
                            if a >= 30:
                                testnum = 42






                        num = num2
                        keyindex = keyindex2
                        char = chr(testnum)

                        if char == "U":
                            char = "m"

                        print(str(testnum) + ":" + str(char))



                        finalmessage.append(char)

                finalmessage = "".join(finalmessage)

                await message.channel.send("Decoded message: " + finalmessage)




















            else:
                response = random.choice(['Hmm? Im not sure if I understand'])
                await message.channel.send(response)













    except Exception as e:
        print(e)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

    channel = client.get_channel(1198075771223289926)
    guild = client.get_guild(1198065368636334080)

    while True:
        message = await aioconsole.ainput(f'{channel}: What would you like to do? ')
        command = message.split(' ')
        if command[0] == 'changeguild' or command[0] == 'cg':
            guild = client.get_guild(int(command[1]))
        elif command[0] == 'movechannel' or command[0] == 'move' or command[0] == 'mv':
            channel = client.get_channel(int(command[1]))
        elif command[0] == 'say':
            await channel.send(message[4:])
        elif command[0] == 'ls' or command[0] == 'channels' or command[0] == 'ch':
            channellist = str(guild.channels)
            channellist = channellist.split(',')
            finalchannellist = []
            for each in channellist:
                if 'CategoryChannel' not in each and 'VoiceChannel' not in each:
                    finalchannellist.append(each)
            channellist = '\n'.join(finalchannellist)
            print(channellist)
        elif command[0] == 'users' or command[0] == 'us':
            userlist = str(guild.members)
            userlist = userlist.split(',')
            userlist = '\n'.join(userlist)
            print(userlist)

        elif command[0] == 'give' or command[0] == 'gv':
            target = command[1]
            itemchoice = command[3:]
            itemchoice = " ".join(itemchoice)
            count = 1
            count = int(command[2])
            targetitems = makeitemdict(target)
            if itemchoice in targetitems:
                targetitems[itemchoice] = str(int(targetitems.get(itemchoice)) + count)
            else:
                targetitems[itemchoice] = count
            writetoitemfile(target, targetitems)
            if itemchoice in allberrystrings:
                itemchoice = itemchoice + " berry"
            if count == 1:
                await channel.send(f'*Gave <@{target}> a {itemchoice}*')
            else:
                await channel.send(f'*Gave <@{target}> {count} {itemchoice}(s)*')

        elif command[0] == 'take' or command[0] == 'tk':
            target = command[1]
            itemchoice = command[3:]
            itemchoice = " ".join(itemchoice)
            count = 1
            count = int(command[2])
            targetitems = makeitemdict(target)
            if itemchoice in targetitems:
                targetitems[itemchoice] = str(int(targetitems.get(itemchoice)) - count)
                if int(targetitems.get(itemchoice)) < 1:
                    del targetitems[itemchoice]

                writetoitemfile(target, targetitems)
                if itemchoice in allberrystrings:
                    itemchoice = itemchoice + " berry"
                if count == 1:
                    await channel.send(f'*Took a {itemchoice} from <@{target}>*')
                else:
                    await channel.send(f'*Took {count} {itemchoice}(s) from <@{target}>*')

        elif command[0] == 'items' or command[0] == 'it':
            target = command[1]
            targetitems = makeitemdict(target)
            print(targetitems)






@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        print('')

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    userid: str = str(message.author.id)
    guildid: str = str(message.guild.id)

    await send_message(message, user_message)


def gay() -> None:
    return


def main() -> None:
    client.run(token=TOKEN)


if __name__ == "__main__":
    main()
