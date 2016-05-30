import json, re, datetime

    
def phraseText(ircmsg,commandChar,botnick,user,hostmask,channel):
    usersF = open('stats/data.txt', 'r').read()
    if usersF == "":
        users = {}
    else:
        users = json.loads(usersF)
    
    #Stats is dictionary
    
    now = datetime.datetime.now()
            
    #Check if user is in users
    if userExist(users,hostmask) == False:
        users[hostmask] = {"user":user,"chars":0,"avg_word_line":0,"messages":0,"word_total":0,"avg_char_line":0,"questions":0,"screams":0,
        "attacks":0,"smiles":0,"sad":0,"swear":0,"angry":0,"url":0,"commands":0,"actions":0,"todo":0,"seen":str(now.month)+":"+str(now.day)+":"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)}
    
    ircmsg = ircmsg.split(" :",1)[1]
    #Add to total message word acount
    users[hostmask]["messages"] += 1
    users[hostmask]["word_total"] += len(ircmsg.replace("ACTION ","").split(" "))
    users[hostmask]["seen"] = str(now.month)+":"+str(now.day)+":"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)
    users[hostmask]["chars"] += len(ircmsg)
    
    if ircmsg.find("?") != -1:
        users[hostmask]["questions"] += 1
    if sum(1 for c in ircmsg if c.isupper())/float(len(ircmsg)) >= 0.8:
        users[hostmask]["screams"] += 1
    if ircmsg.find("ACTION ") != -1:
        users[hostmask]["actions"] += 1
        
    #TODO: avg_word_line, avg_char_line
    if isCommand(ircmsg):
        users[hostmask]["commands"] += 1
    if ircmsg.lower().find("http") != -1:
        users[hostmask]["url"] += 1
    if ircmsg.find(">:C") != -1 or ircmsg.find(">:(") != -1 or ircmsg.find("):<") != -1:
        users[hostmask]["angry"] += 1
    elif ircmsg.find(":C") != -1 or ircmsg.find(":(") != -1 or ircmsg.find(":<") != -1:
        users[hostmask]["sad"] += 1
    if ircmsg.find(":)") != -1 or ircmsg.find(":D") != -1 or ircmsg.find("(:") != -1 or ircmsg.find("C:") != -1:
        users[hostmask]["smiles"] += 1
    if phrasesIn(ircmsg,["slap","smack","kill","stab","kick","punch","shove","beats","die","murders"]):
        users[hostmask]["attacks"] += 1
    if phrasesIn(ircmsg,["fuck","bitch","fag","nigga","asshole","dick","shit","crap"]):
        users[hostmask]["swear"] += 1
    if ircmsg.lower().find("todo") != -1:
        try: users[hostmask]["todo"] += 1
        except: users[hostmask]["todo"] = 1
    users[hostmask]["avg_word_line"] = float(users[hostmask]["word_total"]) / users[hostmask]["messages"]
    users[hostmask]["avg_char_line"] = float(users[hostmask]["chars"]) / users[hostmask]["messages"]
        
    file = open("stats/data.txt", "w")
    file.write(json.dumps(users, sort_keys=True, indent=4, separators=(',', ': ')))
    file.close()
    
def runCommands(channel,nick,commandChar,ircmsg,ircsock,hostmask):
    usersF = open('stats/data.txt', 'r').read()
    if usersF == "":
        users = {}
    else:
        users = json.loads(usersF)
        
    botF = open('stats/botStats.txt', 'r').read()
    if botF == "":
        bot = {}
    else:
        bot = json.loads(botF)
    
    if ircmsg.split(channel + " :")[1][0] == commandChar:
        if ircmsg.find(commandChar+"userstats ") != -1:
            try:
                userTosearch = ircmsg.split(commandChar+"userstats ")[1]
                return getUserData(getHostmask(userTosearch.lower(),users),users)
            except: return "User not found or has not registered to bowserbot stats."
        elif ircmsg.find(commandChar+"userstats") != -1:
            return getUserData(hostmask,users)
        elif ircmsg.find(commandChar+"status") != -1:
             return "I have been awake {0} days {1} hours {2} minutes and {3} seconds and have seen {4} messages".format(
                0,0,0,0,bot["messages_seen"] )
        """elif ircmsg.find(commandChar+"seen ") != -1:
            userTosearch = ircmsg.split(commandChar+"seen ")[1]
            try: 
                now = datetime.datetime.now()
                seenD = users[getHostmask(userTosearch.lower(),users)]["seen"]
                return "\x02User was last seen: \x0f" + str(seenD)
            except: return "User not found or has not registered to bowserbot stats."
            """


def getUserData(hostmask,users):
    returned = ""
    returned += "\x02Smiles: \x0f" + str(users[hostmask]["smiles"])
    returned += " | \x02Angry: \x0f" + str(users[hostmask]["angry"])
    returned += " | \x02Sad: \x0f" + str(users[hostmask]["sad"])
    returned += " | \x02Commands: \x0f" + str(users[hostmask]["commands"])
    returned += " | \x02Screams: \x0f" + str(users[hostmask]["screams"])
    returned += " | \x02Questions: \x0f" + str(users[hostmask]["questions"])
    returned += " | \x02Urls: \x0f" + str(users[hostmask]["url"])
    returned += " | \x02Attacks: \x0f" + str(users[hostmask]["attacks"])
    returned += " | \x02Curses: \x0f" + str(users[hostmask]["swear"])
    
    returned += " | \x02Total Chars: \x0f" + str(users[hostmask]["chars"])
    returned += " | \x02Total words: \x0f" + str(users[hostmask]["word_total"])
    returned += " | \x02Lines said: \x0f" + str(users[hostmask]["messages"])
    returned += " | \x02Avg char/line: \x0f" + str(users[hostmask]["avg_char_line"])
    returned += " | \x02Avg word/line: \x0f" + str(users[hostmask]["avg_word_line"])
    try: returned += " | \x02Todos: \x0f" + str(users[hostmask]["todo"])
    except: returned += " | \x02Todos: \x0f"+"0"
    return returned
    
def userExist(users,username):
    for key in users:
        if key.lower() == username.lower():
            return True
    return False
    
def getHostmask(user,users):
    for key in users:
        if users[key]["user"].lower() == user.lower():
            return key
    return None

def isCommand(ircmsg):
    commandChars = ["@","!","$","%","^","&","*","\\","?!",";","`",":","./","+","!!","~"]
    for i in commandChars:
        if ircmsg.startswith(i):
            return True
    return False
    
    
def phrasesIn(phrase,words):
    for i in words:
        if phrase.lower().find(i.lower()) != -1:
            return True
    return False
    

def botStats(ircmsg,commandChar,botnick,user,hostmask,channel):
    usersF = open('stats/botStats.txt', 'r').read()
    if usersF == "":
        users = {}
        users["messages_seen"] = 0
    else:
        users = json.loads(usersF)

    
    #Stats is dictionary
    now = datetime.datetime.now()

    #Messages seen
    users["messages_seen"] += 1
    

    
        
    file = open("stats/botStats.txt", "w")
    file.write(json.dumps(users))
    file.close()