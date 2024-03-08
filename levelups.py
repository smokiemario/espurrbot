import random

def getlevelups(species):
    if species == 'eevee':
        levelup = {
            1: '+oran +leppa +sitrus +pecha +chilan',
            10: '+roseli',
            20: '-pecha',
            30: '+razz',
            33: '+pinap',
            36: '+nanab',
            50: '+enigma',
            63: '-leppa'
        }
    elif species == 'eevee_shiny':
        levelup = {
            1: '+leppa +sitrus +sitrus +pecha +chilan',
            10: '+roseli',
            20: '-pecha',
            30: '+razz',
            33: '+pinap',
            36: '+nanab',
            50: '+micle',
            52: '+silver_razz +silver_razz',
            55: '+silver_pinap +silver_pinap',
            58: '+silver_nanab +silver_nanab',
            63: '-leppa',
            68: '+golden_razz',
            71: '+golden_pinap',
            74: '+golden_nanab',
            89: '-razz',
            92: '-pinap',
            95: '-nanab'
        }
    elif species == 'oshawott':
        levelup = {
            1: '+aspear +sitrus +passho +chesto +persim',
            10: '+charti',  
            20: '-persim',
            35: '+aguav',
            42: '-aspear',
            50: '+pamtre',
            65: '+watmel'
        }
    elif species == 'nickit':
        levelup = {
            1: '+cheri +rawst +persim +oran +colbur',
            10: '+kebia',
            20: '-cheri',
            30: '+pomeg',
            35: '-persim',
            42: '+bluk',
            50: '+magost'
        }
    elif species == 'vulpix':
        levelup = {
            1: '+cheri +leppa +sitrus +oran +occa',
            10: '+kasib',
            20: '-leppa',
            30: '+figy',
            35: '-oran',
            42: '+razz',
            50: '+petaya',
            56: '+spelon'
        }
    elif species == 'snivy':
        levelup = {
            1: '+pecha +rindo +persim +oran +wepear',
            10: '+lum',
            20: '-persim',
            30: '+salac',
            35: '-pecha',
            42: '+kebia',
            50: '+lansat'
        }
    elif species == 'tepig':
        levelup = {
            1: '+cheri +leppa +occa +oran +sitrus',
            10: '+chople',
            20: '-leppa',
            30: '+liechi',
            35: '-oran',
            42: '+tamato',
            50: '+spelon'
        }
    elif species == 'minccino':
        levelup = {
            1: '+oran +pecha +cheri +aspear +sitrus +chilan +persim +leppa +rawst +chesto',
            10: '+roseli',
            20: '+mago',
            30: '+yache',
            35: '+bluk',
            42: '+qualot',
            57: '-cheri',
            82: '+starf'
        }
    elif species == 'cleffa':
        levelup = {
            1: '+oran +oran +oran +oran +oran +oran +oran +oran +oran +oran +micle',
            10: '-oran',
            20: '-oran',
            30: '-oran',
            40: '-oran',
            50: '-oran',
            60: '-oran',
            70: '-oran',
            80: '-oran',
            90: '-oran'
        }
    elif species == 'pichu':
        levelup = {
            1: '+cheri +leppa +oran +wacan +sitrus',
            10: '+grepa',
            20: '-leppa',
            30: '+coba',
            35: '-oran',
            42: '+belue',
            50: '+rowap'
        }
    elif species == 'phanpy':
        levelup = {
            1: '+persim +leppa +oran +shuca +sitrus',
            10: '+chople',
            20: '-leppa',
            30: '-persim',
            35: '+kee',
            42: '+babiri',
            50: '+grepa',
            63: '-sitrus'
        }
    elif species == 'spheal':
        levelup = {
            1: '+aspear +aspear +aspear +aspear +oran +yache',
            10: '+passho',
            20: '+qualot',
            30: '+watmel',
            35: '-oran',
            42: '+wiki',
            50: '+custap'
        }
    elif species == 'flarespeon':
        levelup = {
            1: '+aspear +cheri +oran +occa +payapa +rawst',
            10: '+lansat',
            16: '+nanab',
            22: '+roseli',
            32: '-rawst',
            44: '-cheri',
            52: '+liechi',
            63: '+custap'
        }
    elif species == 'umbreon':
        levelup = {
            1: '+oran +colbur +colbur +colbur +leppa +persim',
            15: '+kebia',
            23: '-leppa',
            34: '+bluk',
            43: '-oran',
            54: '+ganlon',
            63: '+jaboca',
            83: '-persim'
        }
    elif species == 'leafeon':
        levelup = {
            1: '+oran +rindo +rindo +rindo +leppa +pecha',
            12: '+lum',
            23: '-oran',
            34: '+kee',
            43: '+lansat',
            54: '+babiri',
            63: '+salac',
            74: '-pecha',
            83: '-leppa',
            91: '+durin'
        }
    elif species == 'vaporeon':
        levelup = {
            1: '+aspear +passho +passho +passho +chesto +pecha',
            12: '+haban',
            23: '-aspear',
            34: '+apicot',
            43: '+watmel',
            54: '+kelpsy',
            63: '+maranga',
            74: '-pecha',
            83: '-chesto'
        }

    elif species == 'jolteon':
        levelup = {
            1: '+rawst +wacan +wacan +oran +wacan +pecha',
            12: '+chople',
            23: '-oran',
            38: '+salac',
            54: '+hondew',
            63: '+belue',
            74: '+nomel',
            83: '-rawst'
        }
    elif species == 'glaceon':
        levelup = {
            1: '+rawst +yache +yache +yache +oran +aspear',
            12: '+kasib',
            17: '+bluk',
            23: '-oran',
            38: '+durin',
            46: '-aspear',
            54: '+hondew',
            63: '+wiki',
            74: '+cornn',
            83: '-rawst'
        }
    elif species == 'sylveon':
        levelup = {
            1: '+pecha +roseli +roseli +roseli +pecha +sitrus',
            15: '+tanga +tanga',
            23: '+nanab +nanab',
            34: '+mago +mago',
            43: '+qualot',
            54: '+magost',
            63: '+custap',
            83: '+watmel',
            95: '+micle'
        }
    elif species == 'flareon':
            levelup = {
            1: '+cheri +occa +occa +occa +oran +leppa',
            12: '+shuca',
            17: '+razz',
            23: '-leppa',
            38: '+pomeg',
            46: '-cheri',
            54: '+liechi',
            63: '+tamato',
            74: '+lansat',
            83: '-oran'
        }
    elif species == 'espeon':
            levelup = {
            1: '+cheri +payapa +payapa +payapa +pecha +chesto',
            12: '+mago',
            17: '+lum',
            23: '-cheri',
            38: '+rabuta',
            46: '-chesto',
            54: '+apicot',
            63: '+petaya',
            74: '+maranga',
            83: '-pecha'
        }
    elif species == 'azurill':
        levelup = {
            1: '+sitrus +sitrus +sitrus +oran +leppa +roseli +oran +oran',
            10: '+passho',
            17: '+lum',
            24: '-leppa',
            35: '+watmel',
            47: '+watmel',
            53: '-oran',
            79: '+watmel',
            85: '-oran'
        }
    elif species == 'togepi':
        levelup = {
            1: '+aspear +aspear +aspear +aspear +wepear +wepear',
            5: '+chilan',
            10: '+roseli',
            15: '+occa',
            20: '+passho',
            25: '+wacan',
            30: '+rindo',
            35: '+yache',
            40: '+chople',
            50: '+kebia',
            55: '+shuca',
            60: '+coba',
            65: '+payapa',
            70: '+tanga',
            75: '+charti',
            80: '+kasib',
            85: '+haban',
            90: '+colbur',
            95: '+babiri',
        }
    elif species == 'hoppip':
        levelup = {
            1: '+coba +coba +coba +coba +coba +rindo +rindo +rindo +rindo +rindo +leppa +leppa +leppa +leppa +leppa +sitrus +sitrus',
            10: '+cornn',
            20: '+magost',
            30: '+rabuta',
            40: '+nomel',
            50: '+spelon',
            60: '+pamtre',
            70: '+durin',
            80: '+belue',
            90: '+micle'
        }
    elif species == 'mareep':
        levelup = {
            1: '+cheri +cheri +cheri +cheri +cheri +cheri +cheri +cheri +cheri +cheri +wacan +wacan +wacan +wacan +wacan +wacan +wacan +wacan +wacan +wacan +belue',
            10: '-cheri',
            20: '-cheri',
            30: '-cheri',
            40: '-cheri',
            50: '-cheri',
            60: '-cheri',
            70: '-cheri',
            80: '-cheri',
            90: '+rowap'
        }
    elif species == 'skitty':
        levelup = {
            1: '+pecha +nanab +nanab +chilan +chilan',
            12: '+bluk',
            21: '+chilan',
            25: '+bluk',
            32: '+apicot',
            38: '+liechi',
            43: '+qualot',
            53: '+magost',
            64: '-pecha'
        }

    # Flower Fields

    elif species == 'gossifleur':
        levelup = {
            1: '+roseli +coba +nanab +cheri +oran +leppa',
            12: '+coba',
            21: '+tamato',
            25: '+wepear',
            32: '-cheri',
            38: '+coba',
            43: '+hondew',
            53: '+cornn',
            64: '-oran'
        }

    elif species == 'budew':
        levelup = {
            1: '+roseli +rindo +rindo +cheri +pecha +oran',
            12: '+kebia',
            21: '+lum',
            25: '-oran',
            32: '-cheri',
            38: '+kebia',
            43: '+spelon',
            53: '+aguav',
            64: '-pecha'
        }

    elif species == 'petilil':
        levelup = {
            1: '+roseli +roseli +rindo +leppa +pecha +oran',
            12: '+sitrus',
            21: '+mago',
            27: '+chople',
            31: '-oran',
            34: '+chople',
            43: '+magost',
            53: '+liechi',
            64: '-leppa'
        }

    elif species == 'cottonee':
        levelup = {
            1: '+roseli +roseli +rindo +leppa +pecha +oran',
            12: '+sitrus',
            21: '+wiki',
            27: '+coba',
            31: '-oran',
            34: '+coba',
            43: '+iapapa',
            53: '+cornn',
            64: '-pecha'
        }

    elif species == 'cherubi':
        levelup = {
            1: '+pecha +pecha +pecha +leppa +leppa +leppa +leppa +cheri +cheri +cheri',
            12: '+mago',
            21: '-leppa',
            27: '+magost',
            31: '-leppa',
            34: '+tamato',
            43: '-leppa',
            53: '+custap',
            64: '-leppa'
        }

    elif species == 'fomantis':
        levelup = {
            1: '+rindo +tanga +sitrus +oran +oran +oran +pecha +leppa',
            12: '+nanab',
            21: '+mago',
            27: '-pecha',
            31: '+tanga',
            34: '+hondew',
            43: '+lansat',
            53: '+rabuta',
            64: '-leppa'
        }

    elif species == 'bounsweet':
        levelup = {
            1: '+rindo +nanab +nanab +oran +oran +leppa',
            12: '+roseli',
            21: '+mago',
            27: '-leppa',
            31: '+chople',
            34: '+apicot',
            43: '+hondew',
            53: '+magost',
            64: '-oran',
            74: '+magost',
            85: '+magost'
        }

    elif species == 'cutiefly':
        levelup = {
            1: '+roseli +roseli +roseli +roseli +roseli +pecha +pecha +pecha +pecha +pecha +mago +custap',
            12: '-pecha',
            21: '+mago',
            27: '-pecha',
            34: '-pecha',
            43: '-pecha',
            53: '+cornn',
            64: '-pecha'
        }

    elif species == 'sprigatito':
        levelup = {
            1: '+roseli +roseli +rindo +rindo +sitrus +oran +persim',
            12: '+colbur',
            21: '+mago',
            27: '+razz',
            29: '-persim',
            35: '+colbur',
            39: '+magost',
            45: '+hondew',
            58: '+enigma',
            67: '-oran',

        }

    elif species == 'comfey':
        levelup = {
            1: '+roseli +roseli +coba +coba +sitrus +leppa +persim',
            12: '+payapa',
            18: '+aguav',
            25: '+wiki',
            29: '+figy',
            33: '+mago',
            38: 'iapapa',
            42: '-persim',
            44: '+haban',
            48: '+rabuta',
            58: '+petaya',
            67: '+micle',

        }
    elif species == 'ralts':
        levelup = {
            1: '+payapa +payapa +payapa +roseli +sitrus +roseli +leppa',
            12: '+wiki',
            21: '+mago',
            27: '+rowap',
            29: '-persim',
            35: '+chople',
            39: '+magost',
            45: '+micle',
            67: '-leppa',

        }

    elif species == 'flabebe_red' or species == 'flabébe_orange' or species == 'flabebe_yellow' or species == 'flabebe_blue' or species == 'flabebe_white':
        levelup  = {
            1: '+roseli +rindo +oran +pecha +persim',
            12: '+payapa',
            21: '+aguav',
            27: '+mago',
            34: '-oran',
            43: '+qualot',
            53: '+magost',
            64: '-pecha'
        }

    elif species == 'eternal_floette' or species == 'eternal_Floette':
        levelup = {
            1: '+roseli +roseli +roseli +roseli +rindo +rindo +haban +haban +haban +haban +haban +haban',
            16: '+petaya',
            24: '+magost',
            32: '+petaya',
            43: '+magost',
            56: '+spelon',
            74: '+nomel',
            87: '+nomel',
            97: '+starf',
        }


    # City


    elif species == 'purrloin':
        levelup = {
            1: '+colbur +colbur +oran +cheri +rawst +aspear',
            12: '+chilan',
            21: '-aspear',
            27: '+bluk +bluk',
            31: '-cheri',
            34: '+pomeg',
            43: '+apicot',
            53: '+jaboca',
            64: '-oran',
            68: '+nomel',
            72: '-rawst'
        }

    elif species == 'meowth':
        levelup = {
            1: '+chilan +chilan +sitrus +rawst +cheri +persim',
            12: '+charti',
            21: '-rawst',
            27: '+wepear',
            31: '-cheri',
            34: '+hondew',
            43: '+qualot',
            53: '+lansat',
            64: '+lansat',
            78: '-oran'
        }

    elif species == 'alolan_meowth' or species == 'alolan_Meowth':
        levelup = {
            1: '+colbur +colbur +cheri +rawst +persim +pinap +pinap +oran',
            12: '+charti',
            21: '-persim',
            27: '+pomeg',
            31: '+nanab +nanab',
            34: '-cheri',
            43: '+durin',
            64: '+durin',
            78: '-rawst'
        }

    elif species == 'zigzagoon':
        levelup = {
            1: '+chilan +cheri +oran +persim +persim +persim',
            12: '+shuca',
            21: '+razz +razz',
            27: '+grepa',
            31: '+salac',
            34: '-cheri',
            43: '+custap',
            64: '+lansat',
        }

    elif species == 'galarian_Zigzagoon' or species == 'galarian_zigzagoon':
        levelup = {
            1: '+colbur +cheri +cheri +cheri +oran +persim',
            12: '+chople',
            21: '+bluk +bluk',
            27: '+tamato',
            31: '+ganlon',
            34: '-cheri',
            43: '+belue',
            64: '+jaboca',
        }

    elif species == 'lillipup':
        levelup = {
            1: '+chilan +chilan +chilan +chilan +chilan +oran +oran +oran +oran +oran +micle',
            20: '-oran',
            40: '-oran',
            60: '-oran',
            80: '-oran',
            99: '-oran',
        }

    elif species == 'glameow':
        levelup = {
            1: '+chilan +chilan +chilan +chilan +chilan +tanga +tanga +oran +chesto +pecha +cheri +persim +rawst +nanab +mago +custap',
            12: '-tanga',
            21: '-tanga',
            25: '+micle',
            29: '-chilan',
            36: '-chilan',
            45: '+watmel',
            56: '-chilan',
            63: '-chilan',
            67: '-chilan',
            74: '+magost',
        }

    elif species == 'zorua':
        levelup = {
            1: '+colbur +colbur +sitrus +cheri +cheri +oran +pecha',
            12: '+kasib',
            21: '+occa',
            27: '+pomeg',
            31: '-pecha',
            43: '+enigma',
            64: '+enigma',
            78: '-oran'
        }

    elif species == 'litten':
        levelup = {
            1: '+occa +occa +sitrus +oran +oran +cheri +leppa',
            12: '+colbur',
            15: '+colbur',
            21: '+chople',
            27: '+pomeg',
            31: '-leppa',
            43: '+spelon',
            64: '+spelon',
            78: '-oran'
        }

    elif species == 'rattata':
        levelup = {
            1: '+chilan +chilan +oran +razz +razz +razz +cheri',
            12: '+colbur',
            21: '-cheri',
            27: '+pomeg',
            31: '+figy',
            43: '-oran',
            64: '+aguav',
            78: '+cornn'
        }

    elif species == 'alolan_Rattata' or species == 'alolan_rattata':
        levelup = {
            1: '+colbur +colbur +oran +pinap +pinap +pinap +cheri',
            12: '+chilan',
            21: '-oran',
            27: '+pomeg',
            31: '+iapapa',
            43: '-cheri',
            64: '+aguav',
            78: '+watmel'
        }

    elif species == 'alolan_Rattata' or species == 'alolan_rattata':
        levelup = {
            1: '+colbur +colbur +oran +pinap +pinap +pinap +cheri',
            12: '+chilan',
            21: '-oran',
            27: '+pomeg',
            31: '+iapapa',
            43: '-cheri',
            64: '+aguav',
            78: '+watmel'
        }

    elif species == 'trubbish':
        levelup = {
            1: '+kebia +kebia +kebia +oran +persim +cheri +wiki',
            12: '+pinap',
            21: '-oran',
            27: '+kelpsy',
            31: '+liechi',
            43: '-persim',
            64: '+jaboca',
            78: '-cheri'
        }

    # Forest

    elif species == "emolga":
        levelup = {
            1: '+leppa +leppa +leppa +oran +sitrus +wacan +coba',
            14: '-oran',
            23: '+mago',
            34: '+apicot,',
            45: '+kee',
            54: '+belue',
            64: '+jaboca',
            71: '-sitrus',
            84: '+durin'

        }

    # Beach

    elif species == 'popplio':
        levelup = {
            1: '+passho +passho +oran +pecha +chesto +sitrus',
            10: '+roseli',
            20: '-pecha',
            30: '+kelpsy',
            35: '+watmel',
            42: '-oran',
            50: '+magost',
            63: '-chesto'
        }

    elif species == 'manaphy':
        levelup = {
            1: '+chesto +nanab +nanab +sitrus +passho +passho +tanga +durin',
            16: '+kelpsy',
            24: '+mago',
            32: '+watmel',
            43: '+rowap',
            56: '+watmel',
            74: '-chesto',
            87: '+pamtre',
            97: '+cosnut',
        }

    elif species == 'phione':
        levelup = {
            1: '+chesto +nanab +nanab +sitrus +passho +passho +payapa +durin',
            16: '+wiki',
            24: '+maranga',
            32: '+pamtre',
            43: '+magost',
            56: '+pamtre',
            74: '-chesto',
            87: '+watmel',
            97: '+cosnut',
        }

    elif species == 'slowpoke':
        levelup = {
            1: '+chesto +oran +cheri +persim +aspear +sitrus',
            16: '-cheri',
            24: '-persim',
            32: '-oran',
            43: '-chesto',
            56: '+payapa',
            74: '+watmel',
            87: '+pamtre'
        }

    elif species == 'galarian_Slowpoke' or species == 'galarian_slowpoke':
        levelup = {
            1: '+chesto +oran +cheri +persim +wepear +sitrus',
            16: '-cheri',
            24: '-persim',
            32: '-oran',
            43: '-chesto',
            56: '+kebia',
            74: '+watmel',
            87: '+jaboca'
        }

    elif species == 'buizel':
        levelup = {
            1: '+passho +passho +oran +chesto +cheri',
            10: '+coba',
            20: '-oran',
            30: '+pamtre',
            35: '+maranga',
            42: '+wiki',
            50: '+custap',
            64: '-chesto'
        }

    elif species == 'dwebble':
        levelup = {
            1: '+charti +tanga +oran +cheri +pecha',
            10: '+mago',
            20: '-oran',
            30: '+liechi',
            35: '+babiri',
            42: '-cheri',
            50: '+custap',
            64: '+spelon'
        }

    elif species == 'lapras':
        levelup = {
            1: '+passho +yache +sitrus +sitrus +sitrus',
            10: '+aguav',
            20: '+wiki',
            30: '+watmel',
            35: '+salac',
            42: '+durin',
            50: '+maranga',
            64: '+cornn'
        }

    elif species == 'frillish_male' or species == "frillish_Male":
        levelup = {
            1: '+passho +kasib +kasib +oran +aspear',
            10: '+coba',
            20: '-oran',
            30: '+kelpsy',
            35: '+aguav',
            42: '+pomeg',
            50: '+belue',
            64: '-aspear'
        }

    elif species == 'frillish_female' or species == "frillish_Female":
        levelup = {
            1: '+passho +kasib +kasib +oran +aspear',
            10: '+coba',
            20: '-oran',
            30: '+kelpsy',
            35: '+aguav',
            42: '+pomeg',
            50: '+rowap',
            64: '-aspear'
        }

    elif species == 'corsola':
        levelup = {
            1: '+roseli +roseli +passho +sitrus +aspear',
            10: '+charti',
            20: '+mago',
            30: '+aguav',
            35: '-aspear',
            42: '+pamtre',
            50: '+cornn',
            64: '+watmel',
            84: '-sitrus'
        }

    elif species == 'staryu':
        levelup = {
            1: '+passho +payapa +chesto +chesto +chesto',
            10: '+charti',
            20: '-chesto',
            30: '+kelpsy',
            35: '-chesto',
            42: '+enigma',
            50: '-chesto',
            64: '+pamtre'
        }

    # Snow

    elif species == 'sneasel':
        levelup = {
            1: '+colbur +colbur +yache +chesto +aspear +bluk',
            10: '+wepear',
            20: '+chople',
            30: '-chesto',
            35: '+wiki',
            42: '-bluk',
            50: '+cornn',
            64: '+custap'
        }

    elif species == 'chatot':
        levelup = {
            1: '+coba +coba +chesto +chesto +chilan +oran',
            10: '+razz',
            20: '+wepear',
            30: '-oran',
            35: '+wiki',
            42: '+grepa',
            56: '+cornn',
            67: '+jaboca'
        }

    elif species == 'alolan_Sandshrew' or species == 'alolan_sandshrew':
        levelup = {
            1: '+yache +babiri +leppa +aspear +oran',
            10: '+pinap',
            20: '-leppa',
            30: '+ganlon',
            35: '-oran',
            42: '-aspear',
            50: '+durin',
            64: '+rowap'
        }

    elif species == 'alolan_Vulpix' or species == 'alolan_vulpix':
        levelup = {
            1: '+yache +yache +oran +cheri +aspear +rawst',
            10: '+roseli',
            20: '+pinap',
            28: '+petaya',
            30: '-rawst',
            35: '+mago',
            42: '-cheri',
            50: '+magost',
            64: '+custap',
            71: '-aspear'
        }

    elif species == 'swinub':
        levelup = {
            1: '+shuca +shuca +yache +oran +aspear +wepear',
            10: '+sitrus',
            20: '+tamato',
            30: '-aspear',
            35: '+liechi',
            42: '-oran',
            50: '+lansat',
            64: '+jaboca',
            70: '-wepear'
        }

    elif species == 'amaura':
        levelup = {
            1: '+yache +charti +leppa +oran +aspear +wepear',
            10: '-oran',
            20: '+roseli',
            30: '+mago',
            35: '+apicot',
            42: '-wepear',
            50: '+petaya',
            64: '+micle',
            70: '+belue'
        }

    elif species == 'chingling':
        levelup = {
            1: '+payapa +roseli +oran +leppa +chesto +razz',
            10: '+chilan',
            20: '+grepa',
            30: '-oran',
            35: '+hondew',
            42: '-leppa',
            50: '+lansat',
            64: '+rowap',
            71: '+micle'
        }

    elif species == 'sentret':
        levelup = {
            1: '+chilan +chilan +leppa +oran +wepear',
            10: '+chople',
            20: '+tamato',
            30: '+kee',
            35: '+grepa',
            42: '-leppa',
            50: '+iapapa',
            64: '+cornn',
            70: '+nomel'
        }

    elif species == 'meloetta':
        levelup = {
            1: '+chilan +chilan +chilan +payapa +payapa +sitrus +cornn',
            16: '+petaya',
            24: '+qualot',
            32: '+cornn',
            43: '+magost',
            56: '+cornn',
            74: '-sitrus',
            87: '+lansat',
            97: '+starf',
        }

    elif species == 'meloetta_Pirouette' or species == 'meloetta_pirouette':
        levelup = {
            1: '+chople +chople +chople +chople +charti +sitrus +nomel',
            16: '+liechi',
            24: '+grepa',
            32: '+spelon',
            43: '+pamtre',
            56: '+spelon',
            74: '-sitrus',
            87: '+lansat',
            97: '+starf',
        }

    elif species == 'bulbasaur':
        levelup = {
            1: '+rindo +kebia +oran +leppa +pecha',
            10: '+wepear',
            20: '-leppa',
            30: '-pecha',
            35: '+salac',
            42: '+iapapa',
            50: '+nomel',
            64: '+rabuta'
        }

    elif species == 'wooper':
        levelup = {
            1: '+passho +shuca +persim +chesto +pecha',
            12: '-pecha',
            18: '+razz',
            24: '+kebia',
            35: '-chesto',
            42: '+ganlon',
            50: '+jaboca',
            64: '+durin'
        }

    elif species == 'paldean_wooper' or species == 'paldean_Wooper':
        levelup = {
            1: '+kebia +shuca +persim +chesto +pecha',
            12: '-chesto',
            18: '+bluk',
            24: '+passho',
            35: '-pecha',
            42: '+apicot',
            50: '+rowap',
            64: '+durin'
        }

    elif species == 'nidoran_male':
        levelup = {
            1: '+kebia +chilan +oran +leppa +chesto',
            14: '+pinap',
            21: '-leppa',
            30: '+shuca',
            35: '+hondew',
            42: '-oran',
            50: '+magost',
            64: '+durin'
        }

    elif species == 'nidoran_female':
        levelup = {
            1: '+kebia +chilan +oran +leppa +chesto',
            14: '+pinap',
            21: '-leppa',
            30: '+shuca',
            35: '+qualot',
            42: '-oran',
            50: '+magost',
            64: '+watmel'
        }

    elif species == 'morelull':
        levelup = {
            1: '+rindo +roseli +persim +leppa +bluk',
            14: '+kebia',
            21: '-leppa',
            30: '+razz',
            35: '+aguav',
            42: '+figy',
            50: '+nomel',
            64: '+jaboca'
        }

    elif species == 'foongus':
        levelup = {
            1: '+rindo +kebia +persim +leppa +oran',
            14: '+razz',
            21: '-leppa',
            30: '+tanga',
            35: '+figy',
            42: '+iapapa',
            50: '+rabuta',
            64: '+spelon'
        }

    elif species == 'venipede':
        levelup = {
            1: '+tanga +kebia +oran +oran +sitrus',
            14: '+charti',
            21: '-oran',
            30: '+lum',
            35: '+salac',
            42: '-oran',
            50: '+magost',
            64: '+spelon'
        }

    elif species == 'gulpin':
        levelup = {
            1: '+kebia +kebia +kebia +kebia +kebia +kebia +leppa +leppa +leppa +leppa +leppa +leppa +nanab +cornn',
            14: '-leppa',
            21: '-leppa',
            30: '-leppa',
            35: '-leppa',
            42: '-leppa',
            50: '-leppa',
            64: '+cornn'
        }

    elif species == 'grafaiai':
        levelup = {
            1: '+kebia +chilan +oran +sitrus +pecha',
            10: '+grepa',
            20: '+pomeg',
            30: '-oran',
            35: '+kelpsy',
            42: '+qualot',
            50: '+tamato',
            57: '+kee',
            64: '+rabuta',
            73: '+magost'
        }

    elif species == 'mudkip':
        levelup = {
            1: '+passho +shuca +oran +leppa +sitrus',
            10: '+wiki',
            20: '-oran',
            30: '+kelpsy',
            35: '+qualot',
            42: '-leppa',
            50: '+durin',
            64: '+belue'
        }

    elif species == 'stunky':
        levelup = {
            1: '+kebia +colbur +colbur +leppa +pecha',
            10: '+bluk',
            20: '-leppa',
            30: '+petaya',
            35: '-leppa',
            42: '+figy',
            50: '+durin',
            64: '+rabuta'
        }

    elif species == 'seviper':
        levelup = {
            1: '+kebia +kebia +colbur +razz +razz +oran +cheri',
            10: '+iapapa',
            20: '-cheri',
            30: '+hondew',
            35: '+salac',
            42: '-oran',
            50: '+rowap',
            64: '+jaboca',
            82: '+lansat'
        }

    elif species == 'croagunk':
        levelup = {
            1: '+kebia +chople +chesto +oran +persim',
            10: '+wepear',
            20: '-chesto',
            30: '+colbur',
            35: '-oran',
            42: '+liechi',
            50: '+spelon',
            64: '+pamtre'
        }

    elif species == 'espurr_shiny':
        levelup = {
            1: '+sitrus +sitrus +sitrus +oran +payapa +payapa',
            10: '+nanab',
            20: '+petaya',
            30: '+mago',
            35: '-oran',
            42: '+watmel',
            50: '+micle',
            97: '+starf'
        }

    # Desert



    # Desert

    else:
        levelup = {}
    return levelup


def getberryoptions(petdict):
    levelup = getlevelups(petdict.get('species'))
    berryoptions = []
    for each in levelup:
        if int(petdict.get('level')) >= each:
            actionlist = levelup.get(each)
            actions = actionlist.split(' ')
            for action in actions:
                if "+" in action:
                    action = action.replace('+','')
                    berryoptions.append(action)
                    done = True
                elif "-" in action:
                    action = action.replace('-','')
                    berryoptions.remove(action)
                    done = True
    return berryoptions

def test(species):
    levelup = getlevelups('cleffa')
    berryoptions = []
    for each in levelup:
        if 100 >= each:
            actionlist = levelup.get(each)
            actions = actionlist.split(' ')
            for action in actions:
                if "+" in action:
                    action = action.replace('+','')
                    berryoptions.append(action)
                    done = True
                elif "-" in action:
                    action = action.replace('-','')
                    berryoptions.remove(action)
                    done = True
    return berryoptions



