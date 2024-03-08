

tropicalcustard = {
    'Name': 'Tropical Custard',
    'Ingredients': ['wiki', 'mago', 'custap'],
    'Multiplier': 1.4,
    'Emoteid': ''
}

harvestpie = {
    'Name': 'Harvest Pie',
    'Ingredients': ['wepear', 'aspear', 'leppa'],
    'Multiplier': 2.3,
    'Emoteid': ''
}

forestmedly = {
    'Name': 'Forest Berry Medley',
    'Ingredients': ['rindo', 'lum', 'rabuta', 'sitrus'],
    'Multiplier': 1.5,
    'Emoteid': ''
}

junglecookies = {
    'Name': 'Jungle Nanab Cookies',
    'Ingredients': ['nanab', 'nanab', 'occa', 'maranga'],
    'Multiplier': 1.5,
    'Emoteid': ''
}

cavernquiche = {
    'Name': 'Cavern Mushroom Quiche',
    'Ingredients': ['charti', 'persim', 'kee'],
    'Multiplier': 1.8,
    'Emoteid': ''
}

crimsoncocktail = {
    'Name': 'Crimson Cocktail',
    'Ingredients': ['pomeg', 'kasib', 'liechi'],
    'Multiplier': 2,
    'Emoteid': ''
}

wyverncrepe = {
    'Name': 'Mountain Wyvernn Crepe',
    'Ingredients': ['bluk', 'bluk', 'haban'],
    'Multiplier': 2.6,
    'Emoteid': ''
}

desertdelight = {
    'Name': 'Desert Delight Cocktail',
    'Ingredients': ['salac', 'payapa', 'watmel'],
    'Multiplier': 2.8,
    'Emoteid': ''
}

cornnpopcorn = {
    'Name': 'Cornn Berry Popcorn',
    'Ingredients': ['cornn', 'cornn', 'tamato'],
    'Multiplier': 1.3,
    'Emoteid': ''
}

smokedpinap = {
    'Name': 'Alolan Smoked Pinap',
    'Ingredients': ['pinap', 'pinap', 'figy', 'razz'],
    'Multiplier': 1.7,
    'Emoteid': ''
}

kalosmacarons = {
    'Name': 'Kalosian Thunderstruck Macarons',
    'Ingredients': ['roseli', 'wacan', 'ganlon'],
    'Multiplier': 1.9,
    'Emoteid': ''
}

silverdish = {
    'Name': 'Silver Platter',
    'Ingredients': ['silver_razz', 'silver_nanab', 'silver_pinap'],
    'Multiplier': 3,
    'Emoteid': ''
}

golddish = {
    'Name': 'Golden Delicacy',
    'Ingredients': ['golden_razz', 'golden_nanab', 'golden_pinap'],
    'Multiplier': 3,
    'Emoteid': ''
}


foods = {
    'Alolan Smoked Pinap': smokedpinap,
    'alolan smoked pinap': smokedpinap,

    'Cavern Mushroom Quiche': cavernquiche,
    'cavern mushroom quiche': cavernquiche,

    'Cornn Berry Popcorn': cornnpopcorn,
    'cornn cerry copcorn': cornnpopcorn,

    'Crimson Cocktail': crimsoncocktail,
    'crimson cocktail': crimsoncocktail,

    'Desert Delight Cocktail': desertdelight,
    'desert delight cocktail': desertdelight,

    'Forest Berry Medley': forestmedly,
    'forest berry medley': forestmedly,

    'Harvest Pie': harvestpie,
    'harvest pie': harvestpie,

    'Jungle Nanab Cookies': junglecookies,
    'jungle nanab cookies': junglecookies,

    'Kalosian Thunderstruck Macarons': kalosmacarons,
    'kalosian thunderstruck macarons': kalosmacarons,

    'Mountain Wyvern Crepe': wyverncrepe,
    'mountain wyvern crepe': wyverncrepe,

    'Tropical Custard': tropicalcustard,
    'tropical custard': tropicalcustard,

    'Silver Platter': silverdish,
    'silver platter': silverdish,

    'Golden Delicacy': golddish,
    'golden delicacy': golddish



}

def getfood(food):
    return foods.get(food)

def getfoodlist():
    return foods