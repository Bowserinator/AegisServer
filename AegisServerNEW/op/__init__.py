
def kickuser(channel,user,message,ircsock):
    user = user.replace(" ","").replace(":","")
    print(user+"-")
    ircsock.send("KICK " + channel + " " + user+ " :" + message +"\r\n")

def opnick(channel,nick,ircsock):
    ircsock.send("MODE {0} +o {1}\n".format(channel,nick).encode('utf-8'))
    #/mode #bowserinator +o Bowserinator

def deopnick(channel,nick,ircsock):
    ircsock.send("MODE {0} -o {1}\n".format(channel,nick).encode('utf-8'))

def ban(channel,nick,ircsock):
    ircsock.send("MODE {0} +b {1}\n".format(channel,nick).encode('utf-8'))

def unban(channel,nick,ircsock):
    ircsock.send("MODE {0} -b {1}\n".format(channel,nick).encode('utf-8'))
    
def stab(channel,nick,ircsock):
    ircsock.send("MODE {0} -q {1}\n".format(channel,nick).encode('utf-8'))
    
def unstab(channel,nick,ircsock):
    ircsock.send("MODE {0} +q {1}\n".format(channel,nick).encode('utf-8'))
    
def unvoice(channel,nick,ircsock):
    ircsock.send("MODE {0} -v {1}\n".format(channel,nick).encode('utf-8'))
    
def voice(channel,nick,ircsock):
    ircsock.send("MODE {0} +v {1}\n".format(channel,nick).encode('utf-8'))

def setMode(channel,nick,mode,ircsock):
    ircsock.send("MODE {0} {1} {2}\n".format(channel,mode,nick).encode('utf-8'))
    
def setMode(channel,nick,mode,ircsock):
    ircsock.send("MODE {0} {1} {2}\n".format(channel,mode,nick).encode('utf-8'))

def whois(user,ircsock):  
    ircsock.send("WHOIS {0}\n".format(user).encode('utf-8'))


def runOpCommands(ops,hostmask,channel,nick,commandChar,ircmsg,ircsock):
    if ircmsg.lower().find(commandChar+"kickme") != -1:
        kickuser(channel,nick,"You asked for it!",ircsock)

    for i in ops:
        if hostmask == i.split(",")[0]: #Basic op commands, regardless of level
            if ircmsg.lower().find(commandChar+"kick ") != -1:  #KICK
                toKickOld = ircmsg.split(commandChar+"kick ")[1].split(" ",1)
                toKick = toKickOld[0].split(",")
                if len(toKickOld) == 1:
                    for i in toKick:
                        kickuser(channel,i,"[Insert default kick reason here]",ircsock)
                else:
                    reason = toKickOld[1]
                    for i in toKick:
                        kickuser(channel,i,reason,ircsock)
                
            #Bans: /MODE #demo +b *!*abcd@dialup*.provider.com
            elif ircmsg.lower().find(commandChar+"kban ") != -1:  #KBAN
                toKickOld = ircmsg.split(commandChar+"kban ")[1].split(" ",1)
                toKick = toKickOld[0].split(",")
                if len(toKickOld) == 1:
                    for i in toKick:
                        ban(channel,i,ircsock)
                        kickuser(channel,i,"[Insert default ban reason here]",ircsock)
                else:
                    reason = toKickOld[1]
                    for i in toKick:
                        ban(channel,i,ircsock)
                        kickuser(channel,i,reason,ircsock)
            
            elif ircmsg.lower().find(commandChar+"ban ") != -1:  #KBAN
                toKick = ircmsg.split(commandChar+"ban ")[1].split(",")
                for i in toKick:
                    ban(channel,i,ircsock)
                    
            elif ircmsg.lower().find(commandChar+"unban ") != -1:  #KBAN
                toKick = ircmsg.split(commandChar+"unban ")[1].split(",")
                for i in toKick:
                    unban(channel,i,ircsock)
                    
            elif ircmsg.lower().find(commandChar+"stab ") != -1:  #KBAN
                toKick = ircmsg.split(commandChar+"stab ")[1].split(",")
                for i in toKick:
                    stab(channel,i,ircsock)
                    
            elif ircmsg.lower().find(commandChar+"unstab ") != -1:  #KBAN
                toKick = ircmsg.split(commandChar+"unstab ")[1].split(",")
                for i in toKick:
                    unstab(channel,i,ircsock)
                    
            elif ircmsg.lower().find(commandChar+"op ") != -1:  #KBAN
                toKick = ircmsg.split(commandChar+"op ")[1].split(",")
                for i in toKick:
                    opnick(channel,i,ircsock)
            
            elif ircmsg.lower().find(commandChar+"deop ") != -1:  #KBAN
                toKick = ircmsg.split(commandChar+"deop ")[1].split(",")
                for i in toKick:
                    deopnick(channel,i,ircsock)
                    
                    
            #REMOTE CONTROL
            elif ircmsg.lower().find(commandChar+"remotekick ") != -1:  #KICK
                toKickOld = ircmsg.split(commandChar+"remotekick ")[1].split(" ",2)
                toKick = toKickOld[1].split(",")
                if len(toKickOld) == 2:
                    for i in toKick:
                        kickuser(toKickOld[0],i,"[Insert default kick reason here]",ircsock)
                else:
                    reason = toKickOld[2]
                    for i in toKick:
                        kickuser(toKick[0],i,reason,ircsock)
                
            #Bans: /MODE #demo +b *!*abcd@dialup*.provider.com
            elif ircmsg.lower().find(commandChar+"remotekban ") != -1:  #KBAN
                toKickOld = ircmsg.split(commandChar+"remotekban ")[1].split(" ",2)
                toKick = toKickOld[1].split(",")
                if len(toKickOld) == 2:
                    for i in toKick:
                        ban(toKick[0],i,ircsock)
                        kickuser(toKick[0],i,"[Insert default ban reason here]",ircsock)
                else:
                    reason = toKickOld[2]
                    for i in toKick:
                        ban(toKick[0],i,ircsock)
                        kickuser(toKick[0],i,reason,ircsock)
            
            elif ircmsg.lower().find(commandChar+"remoteban ") != -1:  #KBAN
                toKick2 = ircmsg.split(commandChar+"remoteban ")[1].split(" ",1)
                toKick = toKick2[1].split(",")
                for i in toKick:
                    ban(toKick2[0],i,ircsock)
                    
                    
            elif ircmsg.lower().find(commandChar+"remoteunban ") != -1:  #KBAN
                toKick2 = ircmsg.split(commandChar+"remoteunban ")[1].split(" ",1)
                toKick = toKick2[1].split(",")
                for i in toKick:
                    unban(toKick2[0],i,ircsock)
            
            #TODO
            elif ircmsg.lower().find(commandChar+"remotestab ") != -1:  #KBAN
                toKick2 = ircmsg.split(commandChar+"remotestab ")[1].split(" ",1)
                toKick = toKick2[1].split(",")
                for i in toKick:
                    stab(toKick2[0],i,ircsock)
                    
            elif ircmsg.lower().find(commandChar+"remoteunstab ") != -1:  #KBAN
                toKick2 = ircmsg.split(commandChar+"remoteunstab ")[1].split(" ",1)
                toKick = toKick2[1].split(",")
                for i in toKick:
                    unstab(toKick2[0],i,ircsock)
            
            
            elif ircmsg.lower().find(commandChar+"remoteop ") != -1:  #KBAN
                toKick2 = ircmsg.split(commandChar+"remoteop ")[1].split(" ",1)
                toKick = toKick2[1].split(",")
                for i in toKick:
                    opnick(toKick2[0],i,ircsock)
            
            elif ircmsg.lower().find(commandChar+"remotedeop ") != -1:  #KBAN
                toKick2 = ircmsg.split(commandChar+"remotedeop ")[1].split(" ",1)
                toKick = toKick2[1].split(",")
                for i in toKick:
                    deopnick(toKick2[0],i,ircsock)
                    
            elif ircmsg.lower().find(commandChar+"mode ") != -1:
                result = ircmsg.split(commandChar+"mode ")[1].split(" ")
                setMode(channel,result[0],result[1],ircsock)
            
            elif ircmsg.lower().find(commandChar+"remotemode ") != -1:
                result = ircmsg.split(commandChar+"remotemode ")[1].split(" ")
                if len(result) == 3:
                    setMode(result[0],result[1],result[2],ircsock)
                else:
                    setMode(result[0],result[1],"",ircsock)