#Generate random news article
#Replace:
#[geometry dash youtuber] with geometry dash youtuber
#[largerand] random with random number (100000 - 600000
#[level name] With random level
import random

def genLevelName():
    space = random.choice([""," "])
    start = random.choice(["Death","Blood","Cata","After","End","Doom","Final"])
    end = random.choice(["Bath","Moon","Star","Game","Glow","Room","Valley","Mountain"])
    return start+space+end

youtubersgd = ["Bycraftxx","GuitarHeroStyles","AleXPain24","Creepy Dash","MiKhaXx","Zobros","Viprin","Riot"]
nicks = ["jacob1","iovoid","BWBellairs","IndigoTiger","JZTech1O1"]

def randomNews(news):
    returned = random.choice(news)
    returned = returned.replace("[geometry dash youtuber]",random.choice(youtubersgd))
    returned = returned.replace("[largerand]",str(random.randint(100000,600000)))
    returned = returned.replace("[level name]",genLevelName())
    returned = returned.replace("[nick]",random.choice(nicks))
    return returned
    
