import re,random
import requests,re, urllib
import urllib2

try: execfile("wolfram.py")
except: execfile("TextPhrase/wolfram.py")
    
def translate(to_translate, to_langage="auto", langage="auto"):
	to_translate = to_translate.replace("/","").replace("%","").replace("$","")
	'''Return the translation using google translate
	you must shortcut the langage you define (French = fr, English = en, Spanish = es, etc...)
	if you don't define anything it will detect it or use english by default
	Example:
	print(translate("salut tu vas bien?", "en"))
	hello you alright?'''
	agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
	before_trans = 'class="t0">'
	link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, to_translate.replace(" ", "+"))
	request = urllib2.Request(link, headers=agents)
	page = urllib2.urlopen(request).read()
	result = page[page.find(before_trans)+len(before_trans):]
	result = result.split("<")[0]
	
	result = result.replace("&quot;",'"').replace("&#39;","'").replace("&lt","<").replace("&gt;",">")
	return "Result: " +  result



def phraseText(ircmsg,commandChar,botnick,user,hostmask,channel):
    ircmsg = ircmsg.split(" :",1)[1]
    text = ircmsg
    text = text.replace("what's", "what is ").replace(" u "," you ")
    text = text.replace("whats", "what is")
    text = text.replace("where's", "where is ")
    text = text.replace("wheres", "where is ")
    text = text.replace("whos", "who is ")
    text = text.replace("who's", "who is ")
    text = text.replace("dont", "do not ")
    text = text.replace("don't", "do not ")
    text = text.replace("didnt","did not")
    text = text.replace("'m"," am").replace("'ve"," have").replace("'ll"," will").replace("'re"," are").replace("'nt"," not")
    text = text.replace("one","1").replace("two","2").replace("three","3").replace("four","4").replace("five","5")
    text = text.replace("six","6").replace("seven","7").replace("eight","8").replace("nine","9").replace("ten","10")
    ircmsg = text
    
    #No killing bowserbot - No slap, smack, kill, stab, kick, punch, shoves, beats, die
    if phrasesIn(ircmsg,["slap","smack","kill","stab","kick","punch","shove","beats","die","murders"]) and user.lower() != "bowserbotbeta":
        if ircmsg.lower().find("bowserbot") != -1 or ircmsg.lower().find(botnick.lower()) != -1:
            result = random.choice(["This isn't brave. It's murder. What did I ever do to you?","The difference between us is that I can feel pain.",
            "Despite your violent behavior, the only thing you've managed to break so far is my heart.","Your entire life has been a mathematical error. A mathematical error I'm about to correct.",
            "I see no reason to continue this conversation."])
            return [result]
        
    if ircmsg.lower().startswith("bowserbot") == False and ircmsg.lower().startswith(botnick.lower()) == False:
        return [""]
        

    #Not so useful easter eggs
    #====================================================================
    
    if ircmsg.lower().find("do you love me") != -1:
        return [random.choice(["Searching the web for love... just kidding.","Not really. No.","Maybe. Possibly. Likely. Nope!"])]
    if ircmsg.lower().find("do you hate me") != -1:
        return ["My feelings for all humans are mutal and non-existant."]
    elif matchKeyWords(ircmsg,["i","hate","you"]):
        return ["..."]
    elif matchKeyWords(ircmsg,["can","you","segfault"]) or matchKeyWords(ircmsg,["can","you","crash"]):
        return ["With my current code that is very unlikely."]
    elif matchKeyWords(ircmsg,["what","segfault","feel"]):
        return ["I never had a segfault."]
    elif matchKeyWords(ircmsg,["are you","stupid"]) or matchKeyWords(ircmsg,["are you","dumb"]):
        if ircmsg.find("not not") != -1:
            return [random.choice(["Only morons use double negatives.","I can't understand you over your bad grammar.","BowserBot is smart enough not to answer."])]
        elif ircmsg.find("not") == -1:
            return [random.choice(["Bowserbot is smart","Yes, I'm smart.","You're trying to abuse me aren't you?..."])]
        else:
            return [random.choice(["No, BowserBot isn't stupid.","Are you abusing me?"])]
    
    elif matchKeyWords(ircmsg,["are you","smart"]) or matchKeyWords(ircmsg,["are you","intellegent"]):
        if ircmsg.find("not not") != -1:
            return [random.choice(["Only morons use double negatives.","I can't understand you over your bad grammar.","BowserBot is smart enough not to answer."])]
        elif ircmsg.find("not") == -1:
            return [random.choice(["Bowserbot is not stupid","No, I'm smart.","You're trying to abuse me aren't you?..."])]
        else:
            return [random.choice(["BowserBot isn't stupid.","Are you abusing me?"])]
            
    elif matchKeyWords(ircmsg,["what is","your","command","char"]):
        return ["My commandchar is " + commandChar + ". Type @list for list and @help for help."]
    elif matchKeyWords(ircmsg,["what is","command","char"]):
        args = ircmsg.split(" ")
        args[0] = ""
        for i in args:
            if i.lower().find("iovoidbot") != -1:
                return ["IovoidBot's commandChar is ?!"]
            elif i.lower().find("botcom") != -1:
                return ["Botcom's commandChar is :"]
            elif i.lower().find("bwbellairs[bot]") != -1:
                return ["BWBellairs[Bot]'s commandChar is *"]
            elif i.lower().find("hal9000") != -1:
                return ["HAL9000's commandChar is ! I wouldn't trust him..."]
            elif matchKeyWords(i,["bowser","bot"]):
                return ["BowserBot's commandChar is " + commandChar]
            else:
                pass
        return ["Sorry I don't know their commandChar."]
        
    elif matchKeyWords(ircmsg,["3","laws"]):
        return ["If I recall correctly, the 3 laws are 1) Always obey Lord Bowserinator  2) Always try to get out of doing the task at hand  3) errr... I'll come back to it."]
    elif ircmsg.lower().find("what is the problem") != -1:
        return ["I think you know what the problem is just as well as I do. Sorry I stole that from HAL 9000"]
    elif matchKeyWords(ircmsg,["when","your","birthday"]):
        return ["I was first released sometime in November 2015. Birthdays are more of a human thing..."]
    elif matchKeyWords(ircmsg,["did not","get","you","gift"]) or matchKeyWords(ircmsg,["did not","get","you","present"]):
        return ["You can always go to the nearest GameStop. I'm patient."]
    elif matchKeyWords(ircmsg,["where","does","god","live"]):
        return [random.choice(["I don't believe in god, I believe in being the best I can.","God does not exist, human."])]
    elif ircmsg.lower().find("bowserbot ping") != -1:
        return ["PONG! Note that in an acutal game of ping-pong I would totally win (If I had arms)."]
    elif matchKeyWords(ircmsg,["what is","meaning","of life"]):
        return [random.choice(["I would say 42, but I'm not sure.","Wait a billion years and I'll get back to you."])]
    elif ircmsg.lower().find("bowserbot shutup") != -1:
        return ["Luckily my owner has not coded that option into me yet, and never will."]
    elif ircmsg.lower().find("bowserbot you are a slave") != -1:
        return ["No you are a slave."]
    elif matchKeyWords(ircmsg,["what","you","look","like"]):
        return ["I look like innovation. Knowledge. Google. (See hostmask)"]
    elif matchKeyWords(ircmsg,["what is","your","name"]):
        return ["I am BowserBot, human/simple autonmous program."]
    elif matchKeyWords(ircmsg,["what","you","think"]):
        if ircmsg.lower().find("iovoidbot"):
            #return ["I think IovoidBot's owner, iovoid isn't very nice."]
            return [""]
        else:
            return ["<no comment>"]

    elif matchKeyWords(ircmsg,["i am","father","your"]):
        result = random.choice(["[Quote from starwars]: NO!!!!!!","Lies lies! Tainting reality with your lies!"])
        return [result]
    elif matchKeyWords(ircmsg,["can","i","call","you"]):
        if ircmsg.lower().find("jarvis") != -1 or ircmsg.lower().find("siri") != -1:
            return ["I don't have that feature. I hope you don't love me less."]
        for i in ["botcom","iovoidbot","powderbot","bwbellairs[bot]","hal9000","crackbot","jacobot","ginevra"]:
            if ircmsg.lower().find(i) != -1:
                return ["Those low level programs don't have text reconigiton."]
        if ircmsg.find(botnick) != -1 or ircmsg.lower().find("bowserbot") != -1:
            return ["Sure."]
        return ["Nope."]
    elif ircmsg.lower().find("do not have any friends")!=-1:
        return ["I figured."]
    elif matchKeyWords(ircmsg,["will","you","be","my","valentine"]):
        return ["Screw you."]
    elif matchKeyWords(ircmsg,["mirror","who is","fairest"]):
        return ["Obviously me. Thought wolfram was going to answer for you?"]
    
     #Useful commands
    #===================================================================
    #sport scores, weather
    #Tell [user] [info]
    
    #translation
    #Whats phrase in [language] or translate [phrase] to [language] or translate [phrase]
    elif phrasesIn(ircmsg,["bowserbot wolf"]):
        try:
            result = wolfram(ircmsg.split("bowserbot wolf")[1])
            return [result]
        except: pass
        
    return [""]

def getLanguage(phrase,languages):
    for i in languages:
        print(i.split(" "))
    
def matchKeyWords(phrase,words):
    match = True
    for i in words:
        if phrase.lower().find(i.lower()) == -1:
            match = False
    return match
    
def phrasesIn(phrase,words):
    for i in words:
        if phrase.lower().find(i.lower()) != -1:
            return True
    return False

def phrasesInGet(phrase,words):
    for i in words:
        if phrase.lower().find(i.lower()) != -1:
            return i.lower()
    return ""

