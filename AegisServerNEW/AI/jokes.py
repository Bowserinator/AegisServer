import requests,re , random
from difflib import SequenceMatcher

def getJokeTypes(): #Gets urls
    a = requests.get("http://jokes.cc.com/joke-categories").text
    b = re.findall('<a href="(.*)" title="',a)
    return b
    
def getJokeTypeNames():
    a = requests.get("http://jokes.cc.com/joke-categories").text
    b = re.findall('title="(.*)">',a)
    return b


def getJokeUrls(cat):
    a = requests.get(cat).text
    b = re.findall('<a href="(.*)">',a)
    returned = []
    for i in b:
        if i.startswith("http://jokes.cc.com/") and "title" not in i:
            returned.append(i)
    return returned

def getJoke(url):
    a = requests.get(url).text
    b = re.findall("<p>(.*)</p>",a)
    del b[-1]
    b = " ".join(b)
    b = b.replace("</p>","").replace("<p>","").replace("<BR>"," ").replace("</br>"," ").replace("</br"," ").replace("<br>"," ")
    b = b.replace("&copy; Copyright 2014 Comedy Partners. All Rights Reserved. Comedy Central and all related titles, logos and characters are trademarks of comedy partners.","")
    return b

#TODO: GET RANDOM JOKE
#TODO: REPICK JOKE IF URL RETURNS ""


#Joke ask format, delete me and bowserbot and stuff first
#Tell me a [catagory] joke
#tell me a joke about [catagory]
def phraseMatch(phrase,phrase2,percent=0.95):
    m = SequenceMatcher(None, phrase.lower(), phrase2.lower())
    a = m.ratio()
    if a > percent:
        return True
    return False
    
    
def phraseResultJoke(botnick,ircmsg):
    ircmsg = ircmsg.lower().replace(botnick.lower(),"").replace("bowserbot","").replace("an ","a ")
    if len(re.findall("a joke about (.*)",ircmsg.lower())) != 0:
        return ircmsg.split("a joke about ")[1]
    if len(re.findall("an joke about (.*)",ircmsg.lower())) != 0:
        return ircmsg.split("an joke about ")[1]
    if len(re.findall("me a (.*) joke",ircmsg.lower())) != 0:
        return re.findall("tell me a (.*) joke",ircmsg.lower())[0]
    if len(re.findall("me (.*) joke",ircmsg.lower())) != 0:
        return re.findall("tell me (.*) joke",ircmsg.lower())[0]
    if len(re.findall("make a (.*) joke",ircmsg.lower())) != 0:
        return re.findall("make a (.*) joke",ircmsg.lower())[0]
    if len(re.findall("me an (.*) joke",ircmsg.lower())) != 0:
        return re.findall("tell me an (.*) joke",ircmsg.lower())[0]
    if len(re.findall("me (.*) joke",ircmsg.lower())) != 0:
        return re.findall("tell me (.*) joke",ircmsg.lower())[0]
    return False

urls = getJokeTypes()

def getJokeCatagory(botnick,ircmsg): #GET THE JOKE cataogry url BASED ON NAME
    ircmsg = phraseResultJoke(botnick,ircmsg)
    if ircmsg != False:
        ircmsg = ircmsg.replace("computer","technology").replace(" ","")

        if phraseMatch("hitler",ircmsg,0.9) or phraseMatch("holocaust",ircmsg,0.9):
            return "hitler"
        if phraseMatch("irc",ircmsg,0.9):
            return "irc"
        if phraseMatch("soviet russia",ircmsg,0.9) or phraseMatch("in soviet russia",ircmsg,0.9):
            return "soviet"
        if phraseMatch("bwbellairs",ircmsg,0.9):
            return "bwbellairs"
            
        for i in urls:
            x = i.replace("http://jokes.cc.com/funny-","").replace("-","")
            if phraseMatch(x,ircmsg,0.9):
                return i
    return random.choice(urls)

def getRandomJoke(botnick,ircmsg):
    cat = getJokeCatagory(botnick,ircmsg)
    if cat != False:
        if cat == "hitler":
            return random.choice(open("AI/jokes/hitler.txt","r").read().split("\n"))
        if cat == "irc":
            return random.choice(open("AI/jokes/irc.txt","r").read().split("\n"))
        if cat == "soviet":
            return random.choice(open("AI/jokes/soviet_russia.txt","r").read().split("\n"))
        if cat == "bwbellairs":
            return random.choice(open("AI/jokes/bwbellairs.txt","r").read().split("\n"))
            
        jokes = getJokeUrls(cat)
        joke = ""
        while joke == "":
            joke = getJoke(random.choice(jokes))
        return joke
    return False
    


"""
for i in range(0,10):
    a = getJoke(getJokeUrls(getJokeTypes()[i])[0])
    print(a)
    print(i)"""
