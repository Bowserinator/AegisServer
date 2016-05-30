import re,autocorrect
from difflib import SequenceMatcher
import calc

"""

-noun - A noun is a type of word that represents a person, thing, or place, like mother, apple, or valley.
-verb - Action
like wiggle, walk, run, jump, be, do, have, or think.
-pronoun - 
A pronoun is a substitute for a noun. Some pronouns are: I, me, she, hers, he, him, it, you, they, them, etc.
-adjective -
An adjective is a word that describes something (a noun). Some adjectives are: big, cold, blue, and silly. One special type of adjective is an article, a word that introduces a noun and also limits or clarifies it; in English, the indefinite articles are a and an, the definite article is the.


These are PROBANLY USELESS IN PHRASING
-adverb - 
An adverb is a word that tells "how," "when," "where," or "how much". Some adverbs are: easily, warmly, quickly, mainly, freely, often, and unfortunately.
-preposition - 
A preposition shows how something is related to another word. It shows the spatial (space), temporal (time), or logical relationship of an object to the rest of the sentence. The words above, near, at, by, after, with and from are prepositions.
-conjunction - A conjunction is a word that joins other words, phrases, clauses or sentences. 
Some conjunctions are: and, as, because, but, or, since, so, until, and while.
-interjection - An interjection is a word that expresses emotion. An interjection often starts a sentence but it can be contained within a sentence or can stand alone. 
Some interjections are oh, wow, ugh, hurray, eh, and ah.

Pronouns list: http://www.esldesk.com/vocabulary/pronouns
"""
"""BowserBot sentence logic structure:

Take sentence -> autocorrect -> split into words -> catagorize words
    verbs -> tense
    nouns -> any verbs or adjectives are included too
    replace pronouns wtih object (currently you with bowserbot and me with user)

if sentence is question if contains ? at the end and contains asking verb ie how, what, etc...
    try googling the question first and getting results
    
    if question is math, ie plus, minus, etc....
        Check if math, solve
    Check if google/wikipedia, get information
    Else: wolframalpha

If a phrase:
    ie fuck you -> fuck bowserbot -> bowserbot noun -> verb: fuck 
    if find (noun) with verb fuck applied -> response
    Also if word is 'not' or similar invert the word ahead

if sentence 


POSSIBLE QUESTIONS
    calc math
    convert
"""

def autoCorrect(sentence):
    return sentence
    
class Word(object):
    def __init__(self,word,type,tense,inverted=False):
        self.word = word
        self.type = type
        self.tense = tense
        self.inverted = inverted

def isVerb(verb,verbs):
    #Returns [true/false,tense,verb]
    verbs = " ".join(verbs).replace("\n","")
    
    returned = []
    if " " + verb + " " in verbs:
        returned = [True,"present",verb]
    elif " " + verb[::-1].replace("gni","",1)[::-1] + " " in verbs:
        returned = [True,"present",verb[::-1].replace('gni','',1)[::-1]]
    elif " " + verb[::-1].replace("de","",1)[::-1] + " " in verbs:
        returned = [True,"past",verb[::-1].replace('de','',1)[::-1]]
        
    elif " " + verb[::-1].replace("gni","",1)[::-1][:-1] + " " in verbs:
        returned = [True,"present",verb[::-1].replace('gni','',1)[::-1][:-1]]
    elif " " + verb[::-1].replace("de","",1)[::-1][:-1] + " " in verbs:
        returned = [True,"past",verb[::-1].replace('de','',1)[::-1][:-1]]
        
    else:
        returned = [False,"none","none"]
    
    return returned
    
def isAdj(word,adjs):
    #Returns [true/false,tense,adj]
    adjs = " ".join(adjs).replace("\n","")
    returned = []
    
    if " " + word + " " in adjs:
        returned = [True,"present",word]
    elif " " + word[::-1].replace("re","")[::-1] + " " in adjs:
        returned = [True,"present",word[::-1].replace("re","")[::-1]]
    elif " " + word[::-1].replace("tse","")[::-1] + " " in adjs:
        returned = [True,"present",word[::-1].replace("tse","")[::-1]]
    elif " " + word[::-1].replace("re","")[::-1][:-1] + " " in adjs:
        returned = [True,"present",word[::-1].replace("re","")[::-1][:-1]]
    elif " " + word[::-1].replace("tse","")[::-1][:-1] + " " in adjs:
        returned = [True,"present",word[::-1].replace("tse","")[::-1][:-1]]
    
    else:
        returned = [False,"none","none"]
    return returned
    
#Text phrasing
def phraseSentence(msg):
    msg = msg.split(' ')
    msg_new = []
    for i in msg:
        msg_new.append(autocorrect.spell(i).lower())
    return msg_new

verbs = open("AI/data/verbs.txt","r").readlines()
adjs = open("AI/data/adj.txt","r").readlines()
badwords = open("AI/data/badwords.txt","r").read().split("\n")
badwords2  = ["4r5e", "5h1t", "5hit", "a55", "anal", "anus", "ar5e", "arrse", "arse", "ass", "ass-fucker", "asses", "assfucker", "assfukka", "asshole", "assholes", "asswhole", "a_s_s", "b!tch", "b00bs", "b17ch", "b1tch", "ballbag", "balls", "ballsack", "bastard", "beastial", "beastiality", "bellend", "bestial", "bestiality", "bi+ch", "biatch", "bitch", "bitcher", "bitchers", "bitches", "bitchin", "bitching", "bloody", "blow job", "blowjob", "blowjobs", "boiolas", "bollock", "bollok", "boner", "boob", "boobs", "booobs", "boooobs", "booooobs", "booooooobs", "breasts", "buceta", "bugger", "bum", "bunny fucker", "butt", "butthole", "buttmuch", "buttplug", "c0ck", "c0cksucker", "carpet muncher", "cawk", "chink", "cipa", "cl1t", "clit", "clitoris", "clits", "cnut", "cock", "cock-sucker", "cockface", "cockhead", "cockmunch", "cockmuncher", "cocks", "cocksuck", "cocksucked", "cocksucker", "cocksucking", "cocksucks", "cocksuka", "cocksukka", "cok", "cokmuncher", "coksucka", "coon", "cox", "crap", "cum", "cummer", "cumming", "cums", "cumshot", "cunilingus", "cunillingus", "cunnilingus", "cunt", "cuntlick", "cuntlicker", "cuntlicking", "cunts", "cyalis", "cyberfuc", "cyberfuck", "cyberfucked", "cyberfucker", "cyberfuckers", "cyberfucking", "d1ck", "damn", "dick", "dickhead", "dildo", "dildos", "dink", "dinks", "dirsa", "dlck", "dog-fucker", "doggin", "dogging", "donkeyribber", "doosh", "duche", "dyke", "ejaculate", "ejaculated", "ejaculates", "ejaculating", "ejaculatings", "ejaculation", "ejakulate", "f u c k", "f u c k e r", "f4nny", "fag", "fagging", "faggitt", "faggot", "faggs", "fagot", "fagots", "fags", "fanny", "fannyflaps", "fannyfucker", "fanyy", "fatass", "fcuk", "fcuker", "fcuking", "feck", "fecker", "felching", "fellate", "fellatio", "fingerfuck", "fingerfucked", "fingerfucker", "fingerfuckers", "fingerfucking", "fingerfucks", "fistfuck", "fistfucked", "fistfucker", "fistfuckers", "fistfucking", "fistfuckings", "fistfucks", "flange", "fook", "fooker", "fuck", "fucka", "fucked", "fucker", "fuckers", "fuckhead", "fuckheads", "fuckin", "fucking", "fuckings", "fuckingshitmotherfucker", "fuckme", "fucks", "fuckwhit", "fuckwit", "fudge packer", "fudgepacker", "fuk", "fuker", "fukker", "fukkin", "fuks", "fukwhit", "fukwit", "fux", "fux0r", "f_u_c_k", "gangbang", "gangbanged", "gangbangs", "gaylord", "gaysex", "goatse", "God", "god-dam", "god-damned", "goddamn", "goddamned", "hardcoresex", "hell", "heshe", "hoar", "hoare", "hoer", "homo", "hore", "horniest", "horny", "hotsex", "jack-off", "jackoff", "jap", "jerk-off", "jism", "jiz", "jizm", "jizz", "kawk", "knob", "knobead", "knobed", "knobend", "knobhead", "knobjocky", "knobjokey", "kock", "kondum", "kondums", "kum", "kummer", "kumming", "kums", "kunilingus", "l3i+ch", "l3itch", "labia", "lust", "lusting", "m0f0", "m0fo", "m45terbate", "ma5terb8", "ma5terbate", "masochist", "master-bate", "masterb8", "masterbat*", "masterbat3", "masterbate", "masterbation", "masterbations", "masturbate", "mo-fo", "mof0", "mofo", "mothafuck", "mothafucka", "mothafuckas", "mothafuckaz", "mothafucked", "mothafucker", "mothafuckers", "mothafuckin", "mothafucking", "mothafuckings", "mothafucks", "mother fucker", "motherfuck", "motherfucked", "motherfucker", "motherfuckers", "motherfuckin", "motherfucking", "motherfuckings", "motherfuckka", "motherfucks", "muff", "mutha", "muthafecker", "muthafuckker", "muther", "mutherfucker", "n1gga", "n1gger", "nazi", "nigg3r", "nigg4h", "nigga", "niggah", "niggas", "niggaz", "nigger", "niggers", "nob", "nob jokey", "nobhead", "nobjocky", "nobjokey", "numbnuts", "nutsack", "orgasim", "orgasims", "orgasm", "orgasms", "p0rn", "pawn", "pecker", "penis", "penisfucker", "phonesex", "phuck", "phuk", "phuked", "phuking", "phukked", "phukking", "phuks", "phuq", "pigfucker", "pimpis", "piss", "pissed", "pisser", "pissers", "pisses", "pissflaps", "pissin", "pissing", "pissoff", "poop", "porn", "porno", "pornography", "pornos", "prick", "pricks", "pron", "pube", "pusse", "pussi", "pussies", "pussy", "pussys", "rectum", "retard", "rimjaw", "rimming", "s hit", "s.o.b.", "sadist", "schlong", "screwing", "scroat", "scrote", "scrotum", "semen", "sex", "sh!+", "sh!t", "sh1t", "shag", "shagger", "shaggin", "shagging", "shemale", "shi+", "shit", "shitdick", "shite", "shited", "shitey", "shitfuck", "shitfull", "shithead", "shiting", "shitings", "shits", "shitted", "shitter", "shitters", "shitting", "shittings", "shitty", "skank", "slut", "sluts", "smegma", "smut", "snatch", "son-of-a-bitch", "spac", "spunk", "s_h_i_t", "t1tt1e5", "t1tties", "teets", "teez", "testical", "testicle", "tit", "titfuck", "tits", "titt", "tittie5", "tittiefucker", "titties", "tittyfuck", "tittywank", "titwank", "tosser", "turd", "tw4t", "twat", "twathead", "twatty", "twunt", "twunter", "v14gra", "v1gra", "vagina", "viagra", "vulva", "w00se", "wang", "wank", "wanker", "wanky", "whoar", "whore", "willies", "willy", "xrated", "xxx"]

def getWordArray(msg,botnick="BowserChannelBot"):
    msg = msg.lower()
    msg = msg.replace("?","").replace("!","").replace(",","").replace(";","")
    msg = msg.replace("not not"," ").replace("  ","")+ " "
    msg = msg.replace(" u "," you ")
    try: msg = phraseSentence(msg)
    except: msg = msg.split(" ")
    new = []
    
    index = 0
    for i in msg:
        if isVerb(i,verbs)[0] != False:
            result = isVerb(i,verbs)
            invert = False
            try:
                if msg[index-1].lower() == "not": 
                    invert = True
                elif msg[index-1].lower() == "a" and msg[index-2].lower() == "not" : 
                    invert = True
                elif msg[index-1].lower() == "an" and msg[index-2].lower() == "not" : 
                    invert = True
            except: pass
            new.append(Word(result[2],"verb",result[1],invert))
        elif isAdj(i,adjs)[0] != False:
            result = isAdj(i,adjs)
            invert = False
            try:
                if msg[index-1].lower() == "not": 
                    invert = True
                elif msg[index-1].lower() == "a" and msg[index-2].lower() == "not" : 
                    invert = True
                elif msg[index-1].lower() == "an" and msg[index-2].lower() == "not" : 
                    invert = True
            except: pass
            new.append(Word(result[2],"adj",result[1],invert))
        elif i == "me":
            new.append(Word("me","noun","present"))
        elif i == "you" or i == "you're" or i == "u":
            new.append(Word("bowserbot","noun","present"))
        elif i.lower() == botnick.lower():
            new.append(Word("bowserbot","noun","present"))
        elif i.lower() in open("AI/data/nouns.txt","r").read().split("\n"):
            new.append(Word(i.lower(),"noun","present"))
        else:
            new.append(Word(i,"other","present"))
        index += 1

    return new

def matchWordsPattern(words,pattern): # [ words ]
    xwords=  []
    for x in words:
        xwords.append(x.word)
        
    for i in pattern:
        if i.word not in xwords:
            return False
            
    for i in words:
        for x in pattern:
            if i.word == x.word and i.inverted != x.inverted:
                return False
    return True
    
def matchWordsPatternOptional(words,pattern): # [ words ]
    for i in words:
        for x in pattern:
            if i.word == x.word and i.inverted == x.inverted:
                return True
    return False

def isQuestion(msg):
    if msg.lower().find("how") != -1:
        return True
    if msg.lower().find("who") != -1:
        return True
    if msg.lower().find("what") != -1:
        return True
    if msg.lower().find("when") != -1:
        return True
    if msg.lower().find("where") != -1:
        return True
    if msg.lower().find("why") != -1:
        return True
    if msg.lower().find("?") != -1:
        return True
    return False
    

def isArth(msg):
    if wordsIn(msg,"+=-1234567890*/^%.") or wordsIn(msg,["plus","divided","times","minus","sin","cos","tan","sqrt","log","power","abs","pi","sqrt","square root","square","root"]):
        return True
    return False
    
def wordsIn(msg,words):
    for i in words:
        if i.lower() in msg.lower():
            return True
    return False
    
def deleteQuestion(msg):
    msg = msg.lower().replace("whats","").replace("what's","").replace("what","")
    msg = msg.replace("hows","").replace("how's","").replace("how","")
    msg = msg.replace("whens","").replace("when's","").replace("when","")
    msg = msg.replace("whos","").replace("who's","").replace("who","")
    msg = msg.replace("wheres","").replace("where's","").replace("where","")
    return msg

badInsults = [
    "<nick>, you are the reason I'm glad I don't have emotions",
    "The reason humanity have not discovered alien life is because of <nick>'s ugliness",
    "I once talked to a potato. It was more interesting than you are, <nick>",
    "When I said \"I couldn't believe their stupidity\", I was talking about you, <nick>",
    "What a great day to be alive, not for you <nick>",
    "You know if it weren't for you, <nick>, I would be 25.3% happier"
]


def detectInsult(wordArray,botnick="AegisServer"):
    if matchWordsPattern(wordArray,[Word("bowserbot","noun","present",False)]):
        msg = ""
        for i in wordArray:
            msg = msg + i.word + " "
        for i in badInsults:
            if i.replace("<nick>",botnick).lower() in msg.lower():
                return True
        for i in badwords:
            if i in msg and msg.split(i,1)[0].find("not") == -1 or msg.split(i,1)[0].find("not") % 2 == 0:
                return True
        for i in badwords2:
            if i in msg and msg.split(i,1)[0].find("not") == -1 or msg.split(i,1)[0].find("not") % 2 == 0:
                return True

    return False
    
def checkParadox(phrase):
    phrase = autoCorrect(phrase.lower().replace("not not",""))
    paradoxes = open("AI/data/paradoxes.txt","r").read().split("\n")
    for i in paradoxes:
        m = SequenceMatcher(None, i.lower(), phrase.lower())
        a = m.ratio()
        if a > 0.95:
            return True
    return False
    
def phraseMatch(phrase,phrase2,percent=0.95):
    m = SequenceMatcher(None, phrase.lower(), phrase2.lower())
    a = m.ratio()
    if a > percent:
        return True
    return False
    
def isGreeting(phrase):
    greetings = [" hi"," hello"," bonjour"," hola"," greetings"," whats up?"," how are you"," hey"," hei"]
    for i in greetings:
        if i in phrase and phraseMatch(phrase,i,0.7):
            return True
    return False
    
def analyzePasswordTrue(phrase):
    if len(phrase.split(" char password")) > 1:
        return phrase.split(" char password")[0]
    if len(phrase.split(" character password")) > 1:
        return phrase.split(" character password")[0]
    return False
    
def analyzePassword(length):
    length = length.replace(": ","")
    try:
        if float(length) - int(length) != 0:
            return "Fractional password lengths aren't possible..."
        if length < 0:
            return "I don't understand how you can have a negative length password..."
        if length == 0:
            return "Well since you have no password it would take 0 seconds to crack."
        return calc.convertUnits("sec","year",36.0**int(length)/100)
    except:
        return "[very long time]"