import subprocess
import shutil
import os
import mmap
import os
import sys
import urllib.request
import requests
import threading
import time
import hashlib
import shutil
import struct

CDN = "ph.prd.cdnfiles"

import json

json_data = '''
[
	"Bulbasaur",
	"Ivysaur",
	"Venusaur",
	"Charmander",
	"Charmeleon",
	"Charizard",
	"Squirtle",
	"Wartortle",
	"Blastoise",
	"Caterpie",
	"Metapod",
	"Butterfree",
	"Weedle",
	"Kakuna",
	"Beedrill",
	"Pidgey",
	"Pidgeotto",
	"Pidgeot",
	"Rattata",
	"Raticate",
	"Spearow",
	"Fearow",
	"Ekans",
	"Arbok",
	"Pikachu",
	"Raichu",
	"Sandshrew",
	"Sandslash",
	"Nidoran♀",
	"Nidorina",
	"Nidoqueen",
	"Nidoran♂",
	"Nidorino",
	"Nidoking",
	"Clefairy",
	"Clefable",
	"Vulpix",
	"Ninetales",
	"Jigglypuff",
	"Wigglytuff",
	"Zubat",
	"Golbat",
	"Oddish",
	"Gloom",
	"Vileplume",
	"Paras",
	"Parasect",
	"Venonat",
	"Venomoth",
	"Diglett",
	"Dugtrio",
	"Meowth",
	"Persian",
	"Psyduck",
	"Golduck",
	"Mankey",
	"Primeape",
	"Growlithe",
	"Arcanine",
	"Poliwag",
	"Poliwhirl",
	"Poliwrath",
	"Abra",
	"Kadabra",
	"Alakazam",
	"Machop",
	"Machoke",
	"Machamp",
	"Bellsprout",
	"Weepinbell",
	"Victreebel",
	"Tentacool",
	"Tentacruel",
	"Geodude",
	"Graveler",
	"Golem",
	"Ponyta",
	"Rapidash",
	"Slowpoke",
	"Slowbro",
	"Magnemite",
	"Magneton",
	"Farfetch’d",
	"Doduo",
	"Dodrio",
	"Seel",
	"Dewgong",
	"Grimer",
	"Muk",
	"Shellder",
	"Cloyster",
	"Gastly",
	"Haunter",
	"Gengar",
	"Onix",
	"Drowzee",
	"Hypno",
	"Krabby",
	"Kingler",
	"Voltorb",
	"Electrode",
	"Exeggcute",
	"Exeggutor",
	"Cubone",
	"Marowak",
	"Hitmonlee",
	"Hitmonchan",
	"Lickitung",
	"Koffing",
	"Weezing",
	"Rhyhorn",
	"Rhydon",
	"Chansey",
	"Tangela",
	"Kangaskhan",
	"Horsea",
	"Seadra",
	"Goldeen",
	"Seaking",
	"Staryu",
	"Starmie",
	"Mr. Mime",
	"Scyther",
	"Jynx",
	"Electabuzz",
	"Magmar",
	"Pinsir",
	"Tauros",
	"Magikarp",
	"Gyarados",
	"Lapras",
	"Ditto",
	"Eevee",
	"Vaporeon",
	"Jolteon",
	"Flareon",
	"Porygon",
	"Omanyte",
	"Omastar",
	"Kabuto",
	"Kabutops",
	"Aerodactyl",
	"Snorlax",
	"Articuno",
	"Zapdos",
	"Moltres",
	"Dratini",
	"Dragonair",
	"Dragonite",
	"Mewtwo",
	"Mew",
	"Chikorita",
	"Bayleef",
	"Meganium",
	"Cyndaquil",
	"Quilava",
	"Typhlosion",
	"Totodile",
	"Croconaw",
	"Feraligatr",
	"Sentret",
	"Furret",
	"Hoothoot",
	"Noctowl",
	"Ledyba",
	"Ledian",
	"Spinarak",
	"Ariados",
	"Crobat",
	"Chinchou",
	"Lanturn",
	"Pichu",
	"Cleffa",
	"Igglybuff",
	"Togepi",
	"Togetic",
	"Natu",
	"Xatu",
	"Mareep",
	"Flaaffy",
	"Ampharos",
	"Bellossom",
	"Marill",
	"Azumarill",
	"Sudowoodo",
	"Politoed",
	"Hoppip",
	"Skiploom",
	"Jumpluff",
	"Aipom",
	"Sunkern",
	"Sunflora",
	"Yanma",
	"Wooper",
	"Quagsire",
	"Espeon",
	"Umbreon",
	"Murkrow",
	"Slowking",
	"Misdreavus",
	"Unown",
	"Wobbuffet",
	"Girafarig",
	"Pineco",
	"Forretress",
	"Dunsparce",
	"Gligar",
	"Steelix",
	"Snubbull",
	"Granbull",
	"Qwilfish",
	"Scizor",
	"Shuckle",
	"Heracross",
	"Sneasel",
	"Teddiursa",
	"Ursaring",
	"Slugma",
	"Magcargo",
	"Swinub",
	"Piloswine",
	"Corsola",
	"Remoraid",
	"Octillery",
	"Delibird",
	"Mantine",
	"Skarmory",
	"Houndour",
	"Houndoom",
	"Kingdra",
	"Phanpy",
	"Donphan",
	"Porygon2",
	"Stantler",
	"Smeargle",
	"Tyrogue",
	"Hitmontop",
	"Smoochum",
	"Elekid",
	"Magby",
	"Miltank",
	"Blissey",
	"Raikou",
	"Entei",
	"Suicune",
	"Larvitar",
	"Pupitar",
	"Tyranitar",
	"Lugia",
	"Ho-Oh",
	"Celebi",
	"Treecko",
	"Grovyle",
	"Sceptile",
	"Torchic",
	"Combusken",
	"Blaziken",
	"Mudkip",
	"Marshtomp",
	"Swampert",
	"Poochyena",
	"Mightyena",
	"Zigzagoon",
	"Linoone",
	"Wurmple",
	"Silcoon",
	"Beautifly",
	"Cascoon",
	"Dustox",
	"Lotad",
	"Lombre",
	"Ludicolo",
	"Seedot",
	"Nuzleaf",
	"Shiftry",
	"Taillow",
	"Swellow",
	"Wingull",
	"Pelipper",
	"Ralts",
	"Kirlia",
	"Gardevoir",
	"Surskit",
	"Masquerain",
	"Shroomish",
	"Breloom",
	"Slakoth",
	"Vigoroth",
	"Slaking",
	"Nincada",
	"Ninjask",
	"Shedinja",
	"Whismur",
	"Loudred",
	"Exploud",
	"Makuhita",
	"Hariyama",
	"Azurill",
	"Nosepass",
	"Skitty",
	"Delcatty",
	"Sableye",
	"Mawile",
	"Aron",
	"Lairon",
	"Aggron",
	"Meditite",
	"Medicham",
	"Electrike",
	"Manectric",
	"Plusle",
	"Minun",
	"Volbeat",
	"Illumise",
	"Roselia",
	"Gulpin",
	"Swalot",
	"Carvanha",
	"Sharpedo",
	"Wailmer",
	"Wailord",
	"Numel",
	"Camerupt",
	"Torkoal",
	"Spoink",
	"Grumpig",
	"Spinda",
	"Trapinch",
	"Vibrava",
	"Flygon",
	"Cacnea",
	"Cacturne",
	"Swablu",
	"Altaria",
	"Zangoose",
	"Seviper",
	"Lunatone",
	"Solrock",
	"Barboach",
	"Whiscash",
	"Corphish",
	"Crawdaunt",
	"Baltoy",
	"Claydol",
	"Lileep",
	"Cradily",
	"Anorith",
	"Armaldo",
	"Feebas",
	"Milotic",
	"Castform",
	"Kecleon",
	"Shuppet",
	"Banette",
	"Duskull",
	"Dusclops",
	"Tropius",
	"Chimecho",
	"Absol",
	"Wynaut",
	"Snorunt",
	"Glalie",
	"Spheal",
	"Sealeo",
	"Walrein",
	"Clamperl",
	"Huntail",
	"Gorebyss",
	"Relicanth",
	"Luvdisc",
	"Bagon",
	"Shelgon",
	"Salamence",
	"Beldum",
	"Metang",
	"Metagross",
	"Regirock",
	"Regice",
	"Registeel",
	"Latias",
	"Latios",
	"Kyogre",
	"Groudon",
	"Rayquaza",
	"Jirachi",
	"Deoxys",
	"Turtwig",
	"Grotle",
	"Torterra",
	"Chimchar",
	"Monferno",
	"Infernape",
	"Piplup",
	"Prinplup",
	"Empoleon",
	"Starly",
	"Staravia",
	"Staraptor",
	"Bidoof",
	"Bibarel",
	"Kricketot",
	"Kricketune",
	"Shinx",
	"Luxio",
	"Luxray",
	"Budew",
	"Roserade",
	"Cranidos",
	"Rampardos",
	"Shieldon",
	"Bastiodon",
	"Burmy",
	"Wormadam",
	"Mothim",
	"Combee",
	"Vespiquen",
	"Pachirisu",
	"Buizel",
	"Floatzel",
	"Cherubi",
	"Cherrim",
	"Shellos",
	"Gastrodon",
	"Ambipom",
	"Drifloon",
	"Drifblim",
	"Buneary",
	"Lopunny",
	"Mismagius",
	"Honchkrow",
	"Glameow",
	"Purugly",
	"Chingling",
	"Stunky",
	"Skuntank",
	"Bronzor",
	"Bronzong",
	"Bonsly",
	"Mime Jr.",
	"Happiny",
	"Chatot",
	"Spiritomb",
	"Gible",
	"Gabite",
	"Garchomp",
	"Munchlax",
	"Riolu",
	"Lucario",
	"Hippopotas",
	"Hippowdon",
	"Skorupi",
	"Drapion",
	"Croagunk",
	"Toxicroak",
	"Carnivine",
	"Finneon",
	"Lumineon",
	"Mantyke",
	"Snover",
	"Abomasnow",
	"Weavile",
	"Magnezone",
	"Lickilicky",
	"Rhyperior",
	"Tangrowth",
	"Electivire",
	"Magmortar",
	"Togekiss",
	"Yanmega",
	"Leafeon",
	"Glaceon",
	"Gliscor",
	"Mamoswine",
	"Porygon-Z",
	"Gallade",
	"Probopass",
	"Dusknoir",
	"Froslass",
	"Rotom",
	"Uxie",
	"Mesprit",
	"Azelf",
	"Dialga",
	"Palkia",
	"Heatran",
	"Regigigas",
	"Giratina",
	"Cresselia",
	"Phione",
	"Manaphy",
	"Darkrai",
	"Shaymin",
	"Arceus",
	"Victini",
	"Snivy",
	"Servine",
	"Serperior",
	"Tepig",
	"Pignite",
	"Emboar",
	"Oshawott",
	"Dewott",
	"Samurott",
	"Patrat",
	"Watchog",
	"Lillipup",
	"Herdier",
	"Stoutland",
	"Purrloin",
	"Liepard",
	"Pansage",
	"Simisage",
	"Pansear",
	"Simisear",
	"Panpour",
	"Simipour",
	"Munna",
	"Musharna",
	"Pidove",
	"Tranquill",
	"Unfezant",
	"Blitzle",
	"Zebstrika",
	"Roggenrola",
	"Boldore",
	"Gigalith",
	"Woobat",
	"Swoobat",
	"Drilbur",
	"Excadrill",
	"Audino",
	"Timburr",
	"Gurdurr",
	"Conkeldurr",
	"Tympole",
	"Palpitoad",
	"Seismitoad",
	"Throh",
	"Sawk",
	"Sewaddle",
	"Swadloon",
	"Leavanny",
	"Venipede",
	"Whirlipede",
	"Scolipede",
	"Cottonee",
	"Whimsicott",
	"Petilil",
	"Lilligant",
	"Basculin",
	"Sandile",
	"Krokorok",
	"Krookodile",
	"Darumaka",
	"Darmanitan",
	"Maractus",
	"Dwebble",
	"Crustle",
	"Scraggy",
	"Scrafty",
	"Sigilyph",
	"Yamask",
	"Cofagrigus",
	"Tirtouga",
	"Carracosta",
	"Archen",
	"Archeops",
	"Trubbish",
	"Garbodor",
	"Zorua",
	"Zoroark",
	"Minccino",
	"Cinccino",
	"Gothita",
	"Gothorita",
	"Gothitelle",
	"Solosis",
	"Duosion",
	"Reuniclus",
	"Ducklett",
	"Swanna",
	"Vanillite",
	"Vanillish",
	"Vanilluxe",
	"Deerling",
	"Sawsbuck",
	"Emolga",
	"Karrablast",
	"Escavalier",
	"Foongus",
	"Amoonguss",
	"Frillish",
	"Jellicent",
	"Alomomola",
	"Joltik",
	"Galvantula",
	"Ferroseed",
	"Ferrothorn",
	"Klink",
	"Klang",
	"Klinklang",
	"Tynamo",
	"Eelektrik",
	"Eelektross",
	"Elgyem",
	"Beheeyem",
	"Litwick",
	"Lampent",
	"Chandelure",
	"Axew",
	"Fraxure",
	"Haxorus",
	"Cubchoo",
	"Beartic",
	"Cryogonal",
	"Shelmet",
	"Accelgor",
	"Stunfisk",
	"Mienfoo",
	"Mienshao",
	"Druddigon",
	"Golett",
	"Golurk",
	"Pawniard",
	"Bisharp",
	"Bouffalant",
	"Rufflet",
	"Braviary",
	"Vullaby",
	"Mandibuzz",
	"Heatmor",
	"Durant",
	"Deino",
	"Zweilous",
	"Hydreigon",
	"Larvesta",
	"Volcarona",
	"Cobalion",
	"Terrakion",
	"Virizion",
	"Tornadus",
	"Thundurus",
	"Reshiram",
	"Zekrom",
	"Landorus",
	"Kyurem",
	"Keldeo",
	"Meloetta",
	"Genesect",
	"Chespin",
	"Quilladin",
	"Chesnaught",
	"Fennekin",
	"Braixen",
	"Delphox",
	"Froakie",
	"Frogadier",
	"Greninja",
	"Bunnelby",
	"Diggersby",
	"Fletchling",
	"Fletchinder",
	"Talonflame",
	"Scatterbug",
	"Spewpa",
	"Vivillon",
	"Litleo",
	"Pyroar",
	"Flabebe",
	"Floette",
	"Florges",
	"Skiddo",
	"Gogoat",
	"Pancham",
	"Pangoro",
	"Furfrou",
	"Espurr",
	"Meowstic",
	"Honedge",
	"Doublade",
	"Aegislash",
	"Spritzee",
	"Aromatisse",
	"Swirlix",
	"Slurpuff",
	"Inkay",
	"Malamar",
	"Binacle",
	"Barbaracle",
	"Skrelp",
	"Dragalge",
	"Clauncher",
	"Clawitzer",
	"Helioptile",
	"Heliolisk",
	"Tyrunt",
	"Tyrantrum",
	"Amaura",
	"Aurorus",
	"Sylveon",
	"Hawlucha",
	"Dedenne",
	"Carbink",
	"Goomy",
	"Sliggoo",
	"Goodra",
	"Klefki",
	"Phantump",
	"Trevenant",
	"Pumpkaboo",
	"Gourgeist",
	"Bergmite",
	"Avalugg",
	"Noibat",
	"Noivern",
	"Xerneas",
	"Yveltal",
	"Zygarde",
	"Diancie",
	"Hoopa",
	"Volcanion",
	"Rowlet",
	"Dartrix",
	"Decidueye",
	"Litten",
	"Torracat",
	"Incineroar",
	"Popplio",
	"Brionne",
	"Primarina",
	"Pikipek",
	"Trumbeak",
	"Toucannon",
	"Yungoos",
	"Gumshoos",
	"Grubbin",
	"Charjabug",
	"Vikavolt",
	"Crabrawler",
	"Crabominable",
	"Oricorio",
	"Cutiefly",
	"Ribombee",
	"Rockruff",
	"Lycanroc",
	"Wishiwashi",
	"Mareanie",
	"Toxapex",
	"Mudbray",
	"Mudsdale",
	"Dewpider",
	"Araquanid",
	"Fomantis",
	"Lurantis",
	"Morelull",
	"Shiinotic",
	"Salandit",
	"Salazzle",
	"Stufful",
	"Bewear",
	"Bounsweet",
	"Steenee",
	"Tsareena",
	"Comfey",
	"Oranguru",
	"Passimian",
	"Wimpod",
	"Golisopod",
	"Sandygast",
	"Palossand",
	"Pyukumuku",
	"Type: Null",
	"Silvally",
	"Minior",
	"Komala",
	"Turtonator",
	"Togedemaru",
	"Mimikyu",
	"Bruxish",
	"Drampa",
	"Dhelmise",
	"Jangmo-o",
	"Hakamo-o",
	"Kommo-o",
	"Tapu Koko",
	"Tapu Lele",
	"Tapu Bulu",
	"Tapu Fini",
	"Cosmog",
	"Cosmoem",
	"Solgaleo",
	"Lunala",
	"Nihilego",
	"Buzzwole",
	"Pheromosa",
	"Xurkitree",
	"Celesteela",
	"Kartana",
	"Guzzlord",
	"Necrozma",
	"Magearna",
	"Marshadow",
	"Poipole",
	"Naganadel",
	"Stakataka",
	"Blacephalon",
	"Zeraora",
	"Meltan",
	"Melmetal",
	"Grookey",
	"Thwackey",
	"Rillaboom",
	"Scorbunny",
	"Raboot",
	"Cinderace",
	"Sobble",
	"Drizzile",
	"Inteleon",
	"Skwovet",
	"Greedent",
	"Rookidee",
	"Corvisquire",
	"Corviknight",
	"Blipbug",
	"Dottler",
	"Orbeetle",
	"Nickit",
	"Thievul",
	"Gossifleur",
	"Eldegoss",
	"Wooloo",
	"Dubwool",
	"Chewtle",
	"Drednaw",
	"Yamper",
	"Boltund",
	"Rolycoly",
	"Carkol",
	"Coalossal",
	"Applin",
	"Flapple",
	"Appletun",
	"Silicobra",
	"Sandaconda",
	"Cramorant",
	"Arrokuda",
	"Barraskewda",
	"Toxel",
	"Toxtricity",
	"Sizzlipede",
	"Centiskorch",
	"Clobbopus",
	"Grapploct",
	"Sinistea",
	"Polteageist",
	"Hatenna",
	"Hattrem",
	"Hatterene",
	"Impidimp",
	"Morgrem",
	"Grimmsnarl",
	"Obstagoon",
	"Perrserker",
	"Cursola",
	"Sirfetch'd",
	"Mr. Rime",
	"Runerigus",
	"Milcery",
	"Alcremie",
	"Falinks",
	"Pincurchin",
	"Snom",
	"Frosmoth",
	"Stonjourner",
	"Eiscue",
	"Indeedee",
	"Morpeko",
	"Cufant",
	"Copperajah",
	"Dracozolt",
	"Arctozolt",
	"Dracovish",
	"Arctovish",
	"Duraludon",
	"Dreepy",
	"Drakloak",
	"Dragapult",
	"Zacian",
	"Zamazenta",
	"Eternatus",
	"Kubfu",
	"Urshifu",
	"Zarude",
	"Regieleki",
	"Regidrago",
	"Glastrier",
	"Spectrier",
	"Calyrex",
	"Wyrdeer",
	"Kleavor",
	"Ursaluna",
	"Basculegion",
	"Sneasler",
	"Overqwil",
	"Enamorus",
	"Sprigatito",
	"Floragato",
	"Meowscarada",
	"Fuecoco",
	"Crocalor",
	"Skeledirge",
	"Quaxly",
	"Quaxwell",
	"Quaquaval",
	"Lechonk",
	"Oinkologne",
	"Tarountula",
	"Spidops",
	"Nymble",
	"Lokix",
	"Pawmi",
	"Pawmo",
	"Pawmot",
	"Tandemaus",
	"Maushold",
	"Fidough",
	"Dachsbun",
	"Smoliv",
	"Dolliv",
	"Arboliva",
	"Squawkabilly",
	"Nacli",
	"Naclstack",
	"Garganacl",
	"Charcadet",
	"Armarouge",
	"Ceruledge",
	"Tadbulb",
	"Bellibolt",
	"Wattrel",
	"Kilowattrel",
	"Maschiff",
	"Mabostiff",
	"Shroodle",
	"Grafaiai",
	"Bramblin",
	"Brambleghast",
	"Toedscool",
	"Toedscruel",
	"Klawf",
	"Capsakid",
	"Scovillain",
	"Rellor",
	"Rabsca",
	"Flittle",
	"Espathra",
	"Tinkatink",
	"Tinkatuff",
	"Tinkaton",
	"Wiglett",
	"Wugtrio",
	"Bombirdier",
	"Finizen",
	"Palafin",
	"Varoom",
	"Revavroom",
	"Cyclizar",
	"Orthworm",
	"Glimmet",
	"Glimmora",
	"Greavard",
	"Houndstone",
	"Flamigo",
	"Cetoddle",
	"Cetitan",
	"Veluza",
	"Dondozo",
	"Tatsugiri",
	"Annihilape",
	"Clodsire",
	"Farigiraf",
	"Dudunsparce",
	"Kingambit",
	"Great Tusk",
	"Scream Tail",
	"Brute Bonnet",
	"Flutter Mane",
	"Slither Wing",
	"Sandy Shocks",
	"Iron Treads",
	"Iron Bundle",
	"Iron Hands",
	"Iron Jugulis",
	"Iron Moth",
	"Iron Thorns",
	"Frigibax",
	"Arctibax",
	"Baxcalibur",
	"Gimmighoul",
	"Gholdengo",
	"Wo-Chien",
	"Chien-Pao",
	"Ting-Lu",
	"Chi-Yu",
	"Roaring Moon",
	"Iron Valiant",
	"Koraidon",
	"Miraidon"
]

'''
pokemon_array = json.loads(json_data)
def calculate_file_hash(id):
    hash2 = md5_hash(f"{CDN}/{id}")
    idx = int(hash2[:1], 16)
    hash2 = hash2[idx:] + hash2[:idx]
    return md5_hash(hash2)


def md5_hash(value):
    md5 = hashlib.md5()
    md5.update(value.encode('utf-8'))
    return md5.hexdigest()


def get_file_size(url):
    # Open the URL
    with urllib.request.urlopen(url) as response:
        # Get the size of the file
        file_size = int(response.headers["Content-Length"])
        return file_size


def print_cube(num):
    version = 58800
    print(f"Latest version = {version}")
    download_url = f'https://resource.pokemon-home.com/{str(calculate_file_hash(version))}/md/dro/diff/MD_AssetbundleDLPackVer.snd'
    download_folder = "downloaded_files"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    download_path = os.path.join(download_folder, "MD_AssetbundleDLPackVer.snd")
    urllib.request.urlretrieve(download_url, download_path)

def Hash(id):
    hash = hashlib.md5(f"{CDN}/{id}".encode('utf-8')).hexdigest()
    idx = int(hash[:1], 16)
    d = hash[idx:] + hash[:idx]
    return hashlib.md5(d.encode('utf-8')).hexdigest()

def pad_number_with_zeros(number):
    if number < 10:
        return f"000{number}"
    elif number < 100:
        return f"00{number}"
    elif number < 1000:
        return f"0{number}"
    else:
        return str(number)


class BinaryReader:
    def __init__(self, file):
        self.file = file

    def read_string(self, length = None):
        length = self.read_char() if not length else length
        return self.file.read(length).decode("utf-8")

    def read_bytes(self, length):
        return self.file.read(length)

    def read_char(self):
        return struct.unpack(">b", self.file.read(1))[0]

    def read_int(self):
        return struct.unpack("<i", self.file.read(4))[0]



if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_cube, args=(31,))

    # starting thread 1
    t1.start()

    # wait until thread 1 is completely executed
    t1.join()

    # both threads completely executed
file_path = "downloaded_files/MD_AssetbundleDLPackVer.snd"
deleteAll = False
with open(file_path, "rb") as f:
    reader = BinaryReader(f)
    reader.read_bytes(4)
    assets_len = reader.read_int()
    reader.read_bytes(8)
    assets = []
    for i in range(assets_len):
        nm = reader.read_string()
        sa = reader.read_int()
        si = reader.read_int()
        vr_ios = reader.read_int()
        vr_dro = reader.read_int()
        a = reader.read_char()
        file_len = int(reader.read_string(a).replace("@", ""))
        filenames = [reader.read_string() for _ in range(file_len)]
        assets.append({"nm": nm, "sa": sa, "si": si, "vr_ios": vr_ios, "vr_dro": vr_dro, "files": filenames})

    url_list = [f"https://resource.pokemon-home.com/{Hash(e['vr_dro'])}/dro/{e['nm']}.abap" for e in assets]

    if not os.path.exists("downloaded_files"):
        os.makedirs("downloaded_files")

    # download ABA_Decryptor.exe
    decryptor_url = "https://github.com/FlicksDaModdle/important-files/raw/main/ABA_Decryptor.exe"
    decryptor_file_path = os.path.join("downloaded_files", "ABA_Decryptor.exe")
    response = requests.get(decryptor_url)
    open(decryptor_file_path, "wb").write(response.content)

    while True:
        user_input = input(
            "Enter the Pokemon name that you want to download. If you want to clear all files, type 'clear', or type 'all' to download all files. Option: ")

        if user_input.lower() == "clear":
            deleteAll = True
            break

        if user_input.lower() == "all":
            files_to_download = assets
            break

        try:
            input_ID = pokemon_array.index(user_input)
            real_ID = int(input_ID) + 1


            real_ID = pad_number_with_zeros(real_ID)
            files_to_download = [e for e in assets if real_ID in e['nm']]
            break

        except ValueError:
            print("Invalid Pokemon name. Please try again.")
    if deleteAll == False:
        # download and decrypt each .abap file for the selected number
        for file_to_download in files_to_download:
            url = f"https://resource.pokemon-home.com/{Hash(file_to_download['vr_dro'])}/dro/{file_to_download['nm']}.abap"
            response = requests.get(url)
            abap_file_name = url.split('/')[-1]
            temp_file_path = os.path.join("downloaded_files", abap_file_name)
            open(temp_file_path, "wb").write(response.content)
            subprocess.call([decryptor_file_path, temp_file_path, os.path.join("downloaded_files", abap_file_name)])
            os.remove(temp_file_path)
        # delete ABA_Decryptor.exe file
        decryptor_file_path = os.path.join("downloaded_files", "ABA_Decryptor.exe")
        os.remove(decryptor_file_path)
os.remove(file_path)
if deleteAll == True:
    # Delete all files in "downloaded_files"
    shutil.rmtree("downloaded_files", ignore_errors=True)
    print("All files in 'downloaded_files' have been deleted.")
