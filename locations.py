import random

def getberryset(location):
    common = ['cheri', 'chesto', 'pecha', 'rawst', 'aspear', 'leppa', 'oran', 'persim']

    uncommon = ['occa', 'passho', 'wacan', 'rindo', 'yache', 'chople', 'kebia', 'shuca', 'coba', 'payapa', 'tanga',
                'charti', 'kasib', 'haban', 'colbur', 'babiri', 'chilan', 'razz', 'nanab', 'pinap', 'bluk',
                'wepear', 'roseli', 'sitrus']

    rare = ['lum', 'figy', 'wiki', 'mago', 'aguav', 'iapapa', 'pomeg', 'kelpsy', 'qualot',
            'hondew', 'grepa', 'tamato', 'liechi', 'ganlon', 'salac', 'petaya', 'apicot', 'kee', 'maranga']

    super_rare = ['cornn', 'magost', 'rabuta', 'nomel', 'spelon', 'pamtre', 'watmel', 'durin', 'belue',
                  'lansat', 'micle', 'custap', 'jaboca', 'rowap', 'enigma']

    legendary = ['starf']

    egg = ['egg']

    if location == 'flowerfields':
        common = ['cheri', 'rawst', 'rawst', 'leppa', 'leppa', 'leppa', 'oran', 'oran']

        uncommon = ["rindo", "rindo", 'roseli', 'roseli', 'roseli', 'roseli', 'coba', 'coba', 'sitrus', 'sitrus', 'razz', 'nanab', 'nanab', 'chilan']

        rare = ['hondew', 'hondew', 'mago', 'mago', 'mago', 'pomeg', 'iapapa', 'qualot', 'grepa', 'grepa', 'lum']

        super_rare = ['magost', 'magost', 'magost', 'magost', 'lansat', 'nomel', 'custap', 'custap']

        egg = ['flowerfieldsegg']

    if location == 'city':

        common = ['oran', 'oran', 'oran', 'cheri', 'cheri', 'cheri', 'rawst', 'rawst', 'persim', 'chesto']

        uncommon = ['colbur', 'colbur', 'colbur', 'colbur', 'wacan', 'wacan', 'babiri', 'chilan', 'chilan', 'sitrus', 'sitrus', 'bluk', 'bluk', 'kebia', 'nanab', 'pinap', 'pinap']

        rare = ['pomeg', 'pomeg', 'pomeg', 'grepa', 'tamato', 'tamato', 'ganlon', 'ganlon', 'kee', 'hondew', 'iapapa', 'liechi']

        super_rare = ['nomel', 'nomel', 'belue', 'belue', 'belue', 'custap', 'jaboca', 'jaboca', 'enigma', 'lansat']

        egg = ['cityegg']

    if location == 'beach':

        common = ['aspear', 'aspear', 'aspear', 'chesto', 'chesto', 'leppa', 'persim']

        uncommon = ['passho', 'passho', 'passho', 'passho', 'roseli', 'yache', 'shuca', 'nanab', 'nanab', 'wepear', 'wepear', 'wepear', 'sitrus', 'sitrus', 'charti', 'charti']

        rare = ['aguav', 'aguav', 'aguav', 'kelpsy', 'kelpsy', 'kelpsy', 'liechi', 'apicot', 'apicot', 'kee', 'maranga', 'mago', 'mago']

        super_rare = ['custap', 'custap', 'custap', 'custap', 'watmel', 'watmel', 'watmel', 'pamtre', 'pamtre', 'pamtre', 'rowap', 'magost', 'jaboca', 'durin']

        legendary = ['cosnut']

        egg = ['beachegg']

    if location == 'desert':
        rare = ['salac']

    if location == 'jungle':
        super_rare = ['magost', 'magost', 'magost', 'durin', 'durin']

    if location == 'snowy':
        common = ['aspear', 'aspear', 'aspear', 'leppa', 'oran', 'oran', 'chesto', 'rawst']

        uncommon = ['yache', 'yache', 'yache', 'yache', 'kasib', 'kasib', 'bluk', 'bluk', 'wepear', 'coba', 'coba', 'razz', 'wiki', 'colbur', 'colbur']

        rare = ['iapapa', 'iapapa', 'pomeg', 'pomeg', 'grepa', 'grepa', 'grepa', 'ganlon', 'ganlon', 'apicot', 'kee', 'qualot', 'qualot']

        super_rare = ['cornn', 'cornn', 'cornn', 'cornn', 'nomel', 'nomel', 'belue', 'belue', 'micle', 'rabuta', 'enigma']

        egg = ['snowyegg']

    if location == 'mountain':
        common = ['rawst', 'rawst', 'rawst', 'cheri', 'cheri', 'oran']

        uncommon = ['chople', 'chople', 'chople', 'chople', 'charti', 'bluk', 'bluk', 'bluk', 'razz', 'razz', 'wepear', 'wepear']

        rare = ['figy', 'figy', 'figy']

    if location == 'swamp':
        common = ['pecha', 'pecha', 'pecha', 'pecha', 'leppa', 'leppa', 'leppa', 'oran', 'persim', 'persim']

        uncommon = ['kebia', 'kebia', 'kebia', 'kebia', 'kasib', 'kasib', 'passho', 'passho', 'bluk', 'sitrus', 'sitrus', 'tanga', 'nanab', 'nanab']

        rare = ['figy', 'figy', 'mago', 'lum', 'iapapa', 'pomeg', 'pomeg', 'kelpsy', 'grepa', 'grepa', 'apicot', 'apicot', 'maranga']

        super_rare = ['magost', 'magost', 'belue', 'durin', 'durin', 'jaboca', 'jaboca', 'jaboca', 'rowap', 'enigma']

        egg = ['swampegg']

        legendary = ['acai']
    return common, uncommon, rare, super_rare, legendary, egg



def getpokemon(eggtype):
    mons = ['Eevee', 'Eevee', 'Eevee', 'Oshawott', 'Nickit', 'Snivy', 'Tepig',
            'Vulpix', 'Minccino', 'Spheal', 'Phanpy', 'Cleffa', 'Pichu',
            'Hoppip', 'Azurill', 'Togepi', 'Mareep', 'Skitty']

    if eggtype == 'flowerfieldsegg':
        mons1 = ['Gossifleur', 'Budew', 'Petilil', 'Cherubi', 'Fomantis', 'Bounsweet', 'Cottonee', 'Cutiefly', 'Eevee']
        flabebes = ['Flabébé_red','Flabébé_orange', 'Flabébé_yellow', 'Flabébé_blue', 'Flabébé_white', 'Eternal_Floette']
        mons1.append(random.choice(flabebes))
        mons1.append(random.choice(flabebes))

        mons = []
        for each in mons1:
            mons.append(each)
            mons.append(each)

        mons.append("Sprigatito")
        mons.append("Comfey")
        mons.append("Ralts")

    if eggtype == 'cityegg':

        mons1 = ['Purrloin', 'Skitty', 'Eevee', 'Lillipup', 'Nickit', 'Glameow']

        mons = []
        for each in mons1:
            mons.append(each)
            mons.append(each)

        mons.append("Rattata")
        mons.append("Alolan_Rattata")
        mons.append("Zigzagoon")
        mons.append("Galarian_Zigzagoon")
        mons.append("Meowth")
        mons.append("Alolan_Meowth")

        mons.append("Zorua")
        mons.append("Litten")
        mons.append("Trubbish")
        mons.append("Minccino")

    if eggtype == 'beachegg':

        mons1 = ['Spheal', 'Oshawott', 'Dwebble', 'Azurill', 'Eevee', 'Buizel', 'Staryu']

        mons = []
        for each in mons1:
            mons.append(each)
            mons.append(each)

        mons.append("Frillish_Male")
        mons.append("Frillish_Female")
        mons.append("Slowpoke")
        mons.append("Galarian_Slowpoke")

        mons.append("Lapras")
        mons.append("Corsola")
        mons.append("Popplio")

        legendaries = ['Phione', 'Manaphy']
        if random.randint(1,2) == 2:
            mons.append(random.choice(legendaries))

    if eggtype == 'snowyegg':
        mons1 = ['Eevee', 'Spheal', 'Sneasel', 'Swinub', 'Amaura', 'Chingling', 'Sentret']

        mons = []
        for each in mons1:
            mons.append(each)
            mons.append(each)

        mons.append('Chatot')
        mons.append('Alolan_Vulpix')
        mons.append('Alolan_Sandshrew')

        legendaries = ['Meloetta', 'Meloetta_Pirouette']
        if random.randint(1,2) == 2:
            mons.append(random.choice(legendaries))

    return mons