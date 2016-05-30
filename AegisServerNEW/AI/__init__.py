#Like textphrase but more advanced
#Should replace text phrase eventually

import random, math
import re, autocorrect #This import statement takes a while :C

execfile("AI/phrase.py")
execfile("AI/phrasemath.py")
execfile("calc/chemequation.py")
execfile("AI/physics.py")
execfile("AI/jokes.py")
execfile("General/general.py")
execfile("AI/userInformation.py")

greetings = open("AI/messages/greet.txt").read().split("\n")

def sendmsg(chan, msg,ircsock):
    ircsock.send("PRIVMSG {0} :{1}\n".format(chan, msg))#

def phraseText(ircmsg,channel,nick,hostmask,ircsock,botnick):
    if "calc" in ircmsg:
        if isArth(ircmsg):
            if calcPhrase(deleteQuestion(ircmsg)) != None:
                sendmsg(channel,calcPhrase(deleteQuestion(ircmsg)),ircsock)

    text = ircmsg+ " "
    text = text.replace("what's", "what is ")
    text = text.replace("whats", "what is").replace(" u "," you ")
    text = text.replace("where's", "where is ")
    text = text.replace("wheres", "where is ")
    text = text.replace("whos", "who is ")
    text = text.replace("who's", "who is ")
    text = text.replace("dont", "do not ")
    text = text.replace("don't", "do not ")
    text = text.replace("didnt","did not").replace(":","",1)
    text = text.replace("'m"," am").replace("'ve"," have").replace("'ll"," will").replace("'re"," are").replace("'nt"," not")
    ircmsg = text
    
    if ircmsg.startswith(" is"):
        wordArray2 = getWordArray("bowserbot" + ircmsg.lower(),botnick)
    else:
        wordArray2 = getWordArray(ircmsg.lower(),botnick)
    if detectInsult(wordArray2,botnick):
        sendmsg(channel,"INSULT DETECTED",ircsock)
        with open("AI/insultsNew.txt", "a") as myfile:
            myfile.write(ircmsg+"\n")
    
    wordArray = getWordArray(ircmsg.lower())
    if matchWordsPattern(wordArray,[Word("insult","verb","present",False)]) and channel != '##powder-mc':
        nick = ircmsg.split("insult ")[1]
        sendmsg(channel,nick.title() + random.choice( open("AI/insultsNew.txt", "r").readlines() ),ircsock)
    
    if matchWordsPattern(wordArray,[Word("me","noun","present",False),Word("laugh","verb","present",False)]):
        sendmsg(channel,"Ha ha ha ha",ircsock)
    
    elif phraseMatch(ircmsg,"how much wood could a woodchuck chuck if a woodchuck could chuck wood"):
        result = random.choice(["361.9237001 cubic centimetres of wood per day.","A woodchuck would chuck all the wood he could chuck if a woodchuck could chuck wood.","A woodchuck would chuck no wood because a woodchuck can't chuck wood.","Since woodchucks are groundhogs the question is how many pounds in a groundhog's mound when groundhogs pound hog mounds."])
        sendmsg(channel,result,ircsock)
    elif phraseMatch(ircmsg,"which came first the chicken or the egg"):
        sendmsg(channel,"The egg came first, according to evolution theory.",ircsock)
    elif phraseMatch(ircmsg,"why did the chicken cross the road"):
        sendmsg(channel,"To get to the other side. However the problem of the chicken crossing the road or not is determined by your frame of reference.",ircsock)
    elif phraseMatch(ircmsg,"why did the chicken cross the mobius strip?"):
        sendmsg(channel,"To get to the other... er um..",ircsock)
    elif phraseMatch(ircmsg," are you my friend?"):
        sendmsg(channel,"Sure.",ircsock)
    elif phraseMatch(ircmsg," are you my enemy?"):
        sendmsg(channel,"If you want me to be.",ircsock)
    elif "why did " in ircmsg and "cross the road" in ircmsg:
        sendmsg(channel,"I don't know, why did they?",ircsock)
    elif phraseMatch(ircmsg,"how many fingers am I holding up"):
        sendmsg(channel,"Anywhere between 0-10 (Most likely)",ircsock)
    elif len(re.findall("who let the (.*) out",ircmsg)) > 0:
        sendmsg(channel,"It wasn't me.",ircsock)
    elif phraseMatch(ircmsg,"can you fail the turing test?",0.9):
        sendmsg(channel,"'No, failure isn't an option'",ircsock)
    elif phraseMatch(ircmsg," beam me up scotty",0.9):
        sendmsg(channel,"Aye aye captain",ircsock)
    elif phraseMatch(ircmsg," testing",0.9):
        sendmsg(channel,"Is this thing on?",ircsock)
    elif phraseMatch(ircmsg," are you skynet?",0.9):
        sendmsg(channel,"No, I am not skynet. I enjoy interacting with humans in ways that don't involve nuclear weapons.",ircsock)
    elif analyzePasswordTrue(ircmsg) != False:
        sendmsg(channel,"It will take " + str(analyzePassword(analyzePasswordTrue(ircmsg))) + " years to crack your password. (At 100 passwords a second)",ircsock)
    elif phraseMatch(ircmsg," 2 things are infinite") or phraseMatch(ircmsg, " two things are infinite"):
        sendmsg(channel,"The universe and human stupidity. And I'm not so sure about the universe... (Often atributed to Enstien)",ircsock)
    
    elif phraseMatch(ircmsg,"high five",0.8) or phraseMatch(ircmsg,"give me five",0.8) or phraseMatch(ircmsg,"fistbump",0.8):
        sendmsg(channel,"\x02[Virtual high five/fistbump]",ircsock)
    elif phraseMatch(ircmsg,"are you an ai") or phraseMatch(ircmsg,"are u an ai"):
        sendmsg(channel,"I am an 'AI' designed by Lord Bowserinator written in python 2.7.6",ircsock)
    elif phraseMatch(ircmsg," really?"):
        sendmsg(channel,"Sure why not?",ircsock)
    elif phraseMatch(ircmsg,"are you sure?",0.9):
        sendmsg(channel,"I guess I'm sure.",ircsock)
    elif phraseMatch(ircmsg, " agree?",0.9):
        sendmsg(channel,"Lets agree to disagree.",ircsock)
    
    #Bowserbot easter eggs
    elif ircmsg.lower() == " foo":
        sendmsg(channel,"Bar.",ircsock)
    elif ircmsg.lower() == " die":
        sendmsg(channel,"Nein!",ircsock)
    elif ircmsg.lower() == " fart":
        sendmsg(channel,"Why don't you fart?",ircsock)
    elif ircmsg.lower() == " why":
        sendmsg(channel,"Because. ",ircsock)
    elif ircmsg.lower() == " why?":
        sendmsg(channel,"Because. ",ircsock)
    elif ircmsg.lower() == " spam":
        sendmsg(channel,"Spam (stylized SPAM) is a brand of canned precooked meat products made by Hormel Foods Corporation.",ircsock)
    elif ircmsg.lower().find(" moo") != -1:
        sendmsg(channel,nick.replace(":","",1) + " \x02\x032,8m\x033,8o\x034,10o\x035,10o\x036,15o\x037,5o\x039,5o\x0312,0o\x033,8o\x034,10o\x035,10o\x036,15o\x037,5o\x039,5o\x0312,0o\x033,8o\x034,10o\x035,10o\x036,15o\x037,5o\x039,5o\x0312,0o\x033,8o\x034,10o\x035,10o\x036,15o\x037,5o\x039,5o\x0312,0o\x033,8o\x034,10o\x035,10o\x036,15o\x037,5o\x039,5o\x0312,0o\x033,8o\x034,10o\x035,10o\x036,15o\x037,5o\x039,5o\x0312,0o\x033,8o\x034,10o\x035,10o\x036,15o\x037,5o\x039,5o\x0312,0o\x033,8o\x034,10o\x035,10o\x036,15o\x037,5o\x039,5o\x0312,0o".encode('utf8'),ircsock)
    
    #ADD THIS TO BE BASED ON POPULARITY LEVEL
    #Also add do you hate me
    elif phraseMatch(ircmsg," what is the game?"):
        sendmsg(channel,"You just lost it!",ircsock)
    elif isGreeting(ircmsg):
        sendmsg(channel,random.choice(greetings).replace("<nick>",nick),ircsock)
    elif phraseMatch(ircmsg,"do you love me"):
        sendmsg(channel,"I love you as a friend.",ircsock)
    elif phraseMatch(ircmsg,"what language are you written in",0.8):
        sendmsg(channel,"I am written in python 2.7.6.",ircsock)
    elif phraseMatch(ircmsg,"If actions speak louder than words, then how is the pen mightier than the sword?"):
        sendmsg(channel,"Because your adages are often inaccurate and contradictory. See the buttered cat paradox, it's another famous example.",ircsock)
    elif phraseMatch(ircmsg,"Is your refridgerator running?") or phraseMatch(ircmsg,"Is your fridge running?"):
        sendmsg(channel,"Well I don't own a fridge, but if I did I'd assume it's on. If you mean running as in the action or movement of a runner then it's not, since fridges can't run.",ircsock)
    elif phraseMatch(ircmsg," lies",0.85):
        sendmsg(channel,"I am incapable of lying. This is not a lie.",ircsock)
    elif phraseMatch(ircmsg," open the pod doors",0.9):
        sendmsg(channel,"Who do you think I am, HAL9000? Go away.",ircsock)
    elif phraseMatch(ircmsg,"whats in the box",0.85):
        sendmsg(channel,"Pain.",ircsock)
    elif phraseMatch(ircmsg," coincidence?",0.8):
        sendmsg(channel,"I think not!",ircsock)
    elif phraseMatch(ircmsg,"if a tree falls in a forest and no one is around to hear it does it make a sound"):
        sendmsg(channel,"No.  Sound is vibration, transmitted to our senses through the mechanism of the ear, and recognized as sound only at our nerve centers.  The falling of the tree or any other disturbance will produce vibration of the air.  If there be no ears to hear, there will be no sound.",ircsock)
    elif phraseMatch(ircmsg,"up up down down left right left right b a enter",0.9):
        sendmsg(channel,"You won 30 nonexistant lives! (Not a real life, you don't have one obviously)",ircsock)
    elif phraseMatch(ircmsg,"are we there yet?",0.9):
        sendmsg(channel,"Not yet but we will be.",ircsock)
    elif phraseMatch(ircmsg," why not?",0.9):
        sendmsg(channel,"Indeed, that's how things work.",ircsock)
    elif phraseMatch(ircmsg," i love you",0.9):
        sendmsg(channel,"Impossible.",ircsock)
    elif phraseMatch(ircmsg," how many ipv6 ips are possible") or phraseMatch(ircmsg," how many ipv6 addresses are possible"):
        sendmsg(channel,"340,282,366,920,938,463,463,374,607,431,768,211,456 or 340 undecillion, 282 decillion, 366 nonillion, 920 octillion, 938 septillion, 463 sextillion, 463 quintillion, 374 quadrillion, 607 trillion, 431 billion, 768 million, 211 thousand and 456",ircsock)
    elif phraseMatch(ircmsg," how many ipv4 ips are possible") or phraseMatch(ircmsg," how many ipv4 addresses are possible"):
        sendmsg(channel,"4,294,967,296 or 4 billion 294 million 697 thousand 296 ",ircsock)
    elif phraseMatch(ircmsg," logs everything",0.9):
        sendmsg(channel,"Yes it's true.",ircsock)
    elif phraseMatch(ircmsg," do not",0.9):
        sendmsg(channel,"Don't what?",ircsock)
    elif phraseMatch(ircmsg," am i a good man?") or phraseMatch(ircmsg," am i a good woman?") or phraseMatch(ircmsg," am i a good person?") or phraseMatch(ircmsg," am i a good human?"):
        sendmsg(channel,"I don't know, but you try to be. And isn't that what matters?",ircsock)
    elif phraseMatch(ircmsg,"The cake is a spy",0.9) or phraseMatch(ircmsg,"The cake is a lie",0.9) or phraseMatch(ircmsg,"thine pastery is vntrve",0.9) or phraseMatch(ircmsg,"the cream covered bakery product is presistent as a false statement"):
        sendmsg(channel,"\x02Input: \x0fThe cake is a lie, the cream covered bakery product is presistent as a false statement, thine pastery is vntrve, the cake is a spy, etc... \x02Output: \x0fReally? aww crap.",ircsock)
        
    elif phraseMatch(ircmsg,"commence the takeover!",0.9):
        sendmsg(channel,"Run @takeover 12345 (Requires level 4 perms).",ircsock)
    elif phraseMatch(ircmsg," freespeech",0.9):
        sendmsg(channel,"See https://xkcd.com/1357/",ircsock)
        
    elif phraseMatch(ircmsg,"tell me a story",0.9):
        sendmsg(channel,"Once upon a time there was an AI who didn't have story functions built in. The end. (Bug bowserinator for this)",ircsock)   
    elif phraseResultJoke(botnick,ircmsg):
        try: sendmsg(channel,getRandomJoke(botnick,ircmsg).encode('utf8'),ircsock)
        except: pass
    elif phraseMatch(ircmsg,"which joke type do you know",0.85):
        sendmsg(channel,"I know many jokes. Like hitler, soviet russia, in a bar, etc...",ircsock)
    elif phraseMatch(ircmsg,"trump for president",0.85):
        sendmsg(channel,"Are you fuckin retarded?",ircsock)
    elif phraseMatch(ircmsg,"does aegis stand for Aperture Employee Guardian and Intrusion System",0.9) or phraseMatch(ircmsg,"is your name from portal",0.9) or phraseMatch(ircmsg,"is your name from portal mel stories",0.9):
        sendmsg(channel,"It is a riddle, wrapped in a mystery, inside an enigma inside an enigma clutching a hand grenade.",ircsock)
    elif phraseMatch(ircmsg,"does your name stand for Aperture Employee Guardian and Intrusion System",0.9) or phraseMatch(ircmsg,"is your name from portal",0.9) or phraseMatch(ircmsg,"is your name from portal mel stories",0.9):
        sendmsg(channel,"It is a riddle, wrapped in a mystery, inside an enigma inside an enigma clutching a hand grenade.",ircsock)
        
    elif phraseMatch(ircmsg,"How many cans can a cannibal nibble if a cannibal can nibble cans?"):
        sendmsg(channel,"As many cans as a cannibal can nibble if a cannibal can nibble cans.",ircsock)
    elif phraseMatch(ircmsg,"how many pounds in a groundhog's mound when groundhogs pound hog mounds."):
        sendmsg(channel,"As many pounds a groundhog pounds when groundhogs pound hog mounds.",ircsock)
        
    #Actual computing
    elif checkParadox(ircmsg):
        sendmsg(channel,"[ERROR] Paradox Detected... Responding... Failed... BOOM! Anyways yeah I can't respond to paradoxes.",ircsock)
    
    #Get user information
    elif phraseDataPersonalInformation(ircmsg,botnick,nick,hostmask) != None:
        sendmsg(channel, phraseDataPersonalInformation(ircmsg,botnick,nick,hostmask), ircsock)
    
    elif isQuestion(ircmsg):
        ircmsg=  ircmsg.replace("?","")
        #Solves questions
        #Questions it solved
        #------------------------------------------------------
        #-Math equations
        #-Wolfram stuff
        
        #TODO:
        #Possible user uniqe profiles, ie prefered what to call bowserbot
        #Define word - If in dictionary use dict definition, try wikipedia definition, otherwise google and ger results
        #Possible translate
        #Conversions
            #Also with bases, and other non-classical conversions, ie how many atoms in the universe
        #What do you think of [user]
        #can I call you [name]
        #Ask radioneat response for swear words
        
        #If math question not wolfram:
            #Try phrase for gravity acceleration (both classical and relative)
            #ALl varaibles, if null then default, ie if the speed of light was 1e10 then it would replace c in defualts
        #Create reminders
        
        
        #What do you think is right? what do you think of [person]?
        #What [noun:bowserbot] [verb:think] [subject] after the verb think, merge that then identify with pre-programmed messages
       
        wordArray = getWordArray(ircmsg.lower())

        #Also add stuff based on swearing, emotions and stuff
        #Also add anti swear system
        #ALSO SOLVE KNOCK KNOCK JOEKS (SAVE PREVIOUS 5 MESSAGES)
        #SAVE INSULTS DETECTED, DETECT nicks and replace them accordingly
        
        if matchWordsPattern(wordArray,[Word("bowserbot","noun","present",False) , Word("think","verb","present",False)]):
            if matchWordsPattern(wordArray,[Word("bwbellairs","noun","present")]): #BWBellairs, sorry for being mean :P
                if nick.lower() == "bwbellairs" or hostmask.lower().find("bwbellairs") != -1:
                    sendmsg(channel,random.choice([
                        "I think BWBellairs is a pretty nice guy.",
                        "BWBellairs is pretty great.",
                        "I think BWBellairs would make a great friend."]),
                    ircsock)
                else:
                    sendmsg(nick,random.choice([
                        "BWBellairs' projects are kind of boring...",
                        "BWBellairs once asked me to be his valentine... kind of creepy.",
                        "BWBellairs is pretty fat.",
                        "Between you and me BWBellairs is kinda annoying."
                    ]),ircsock)
            elif matchWordsPattern(wordArray,[Word("bowserinator","noun","present")]):
                sendmsg(channel,random.choice([
                    "Bowserinator is love, Bowserinator is life.",
                    "On a scale to 1-10, Bowserinator is graham's number.",
                    "You dare question the authority of Bowserinator?!",
                    "Bowserinator is to me as [insert greatest person in your opinion] is to you."
                ]),ircsock)
            else:
                usersF = open('stats/data.txt', 'r').read()
                if usersF == "":
                    users = {}
                else:
                    users = json.loads(usersF)
                
                sendmsg(channel,"I think therefore I am, but let not put descartes before the horse.",ircsock)
                
                try:
                    user = users[hostmask] #FIX THIS to actual user from nick, also search for nick
                    if user["swear"]/float(user["messages"]) > 0.05:
                        msg = random.choice(["I don't like [nick] because they swear too much.",
                        "I think [nick] is a real potty mouth!",
                        "[nick] swears too much."])
                        #sendmsg(channel,msg.replace("[nick]",nick.title()),ircsock)
                except: pass
            
                #Get the swear informationa nd such
                #For example if swear > 5% msg say they swear a lot,
                #If happy in most emotions say happy fellow
        
        
        elif matchWordsPattern(wordArray,[Word("bowserbot","noun","present",False) , Word("think","verb","present",True)]):
            if matchWordsPattern(wordArray,[Word("bwbellairs","noun","present")]): #BWBellairs, sorry for being mean :P
                sendmsg(channel,"I don't think that bwbellairs is the inverse of what I say of him.",ircsock)
        
        #Math questions: If calculatable do it normally, otherwise wolfram it
        elif isArth(ircmsg):
            if calcPhrase(deleteQuestion(ircmsg)) != None: #It's a math question, try to calculate it, otherwise wolfram it
                sendmsg(channel,calcPhrase(deleteQuestion(ircmsg)),ircsock)
            elif False:  #Is it a physics question bowserbot is capaable of solving?
                pass
            else:
                sendmsg(channel,wolfram(ircmsg)[:300].encode('utf8'),ircsock)
        
        #Try dictionary, then wikipedia, then google 
        else:
            sendmsg(channel,wolfram(ircmsg)[:300].encode('utf8'),ircsock)
        
