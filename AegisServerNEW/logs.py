import datetime

logChan = "##bowserinator,##bwbellairs-bots,##powder-bots,##powder-mc,#bmn,#ezzybot,#botters-t".split(",")

def phraseText(ircmsg):
    #Kick, bans, modes, invites, messages, joins, parts, quits
    #Format: <Time> <Nick>: Message

    addTo = ""
    
    if " JOIN " in ircmsg.split(" :")[0]:
        nick = ircmsg.split("!")[0].replace(":","",1)
        channel = ircmsg.split("JOIN ")[1]
        hostmask = ircmsg.split("@")[1].split(" ")[0]
        addTo = addTo + " has joined " + channel
    
    elif " KICK " in ircmsg.split(" :")[0]:
        nick = ircmsg.split("!")[0].replace(":","",1)
        channel = ircmsg.split("KICK ")[1].split(" ")[0]
        hostmask = ircmsg.split("@")[1].split(" ")[0]
        addTo = addTo + " has kicked" + ircmsg.split(" :")[0].lower().split(channel.lower())[1]
    
    elif " MODE " in ircmsg.split(" :")[0]:
        nick = ircmsg.split(" ")[-1]
        channel = ircmsg.split(' MODE ')[1].split(' ')[0]
        hostmask = ircmsg.split(nick)[-1].split(" MODE ")[0].replace(" ","")
        addTo = addTo + " has set MODE" + ircmsg.lower().split(channel.lower())[1]

        
    elif " PART " in ircmsg.split(" :")[0]:
        channel = ircmsg.split("PART ")[1].split(" :")[0]
        hostmask = ircmsg.split("@")[1].split(" ")[0]
        nick = ircmsg.split("!")[0].replace(":","",1)
        addTo = addTo + " has quit the channel. (" + hostmask + ")"
    
    elif " QUIT " in ircmsg.split(" :")[0]:
        channel = ircmsg.split("QUIT ")[1].split(" :")[0]
        hostmask = ircmsg.split("@")[1].split(" ")[0]
        nick = ircmsg.split("!")[0].replace(":","",1)
        addTo = addTo + " has quit the channel. (" + hostmask + ")"
        
    elif " PRIVMSG " in ircmsg.split(" :")[0]:
        nick = ircmsg.split("!")[0][1:]
        channel = ircmsg.split(' PRIVMSG ')[-1].split(' :')[0]
        hostmask = ircmsg.split(" PRIVMSG ")[0].split("@")[1].replace(" ","")
        addTo = addTo + ircmsg.split(" :")[1]
    
    try:
        addTo = "["+datetime.datetime.now().strftime("%I:%M%p-%B %d, %Y")+"] ["  + nick + "][" + hostmask + "]: " + addTo
        if channel.lower() in logChan:
            with open("Logs/"+channel.lower()+".txt", "a") as myfile:
                myfile.write(addTo+'\n')
    except: pass
        
    