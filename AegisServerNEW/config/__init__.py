import sys
execfile("config/hostmask.py")

def sendmsgraw(msg,ircsock):
    ircsock.send(msg)
    
def sendmsg(chan,msg,ircsock):
    ircsock.send("PRIVMSG {0} :{1}\n".format(chan, msg))
    
def partchan(chan,ircsock):
    ircsock.send("PART {0}\n".format(chan).encode('utf-8'))
    
def changenick(nick,ircsock):
    ircsock.send("NICK {0}\n".format(nick).encode('utf-8'))
    
def joinchan(chan,ircsock):  
    ircsock.send("JOIN {0}\n".format(chan).encode('utf-8'))

def action(channel,message,ircsock):
    sendmsg(channel,"\x01ACTION " + message + "\x01",ircsock)
    
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
    
def whois(user,ircsock):  
    ircsock.send("WHOIS {0}\n".format(user).encode('utf-8'))

    
class Config(object):
    def __init__(self):
        self.on = True #Accept commands?
        self.banBot = [] #Banned users from BOT
        self.bans = [] #Banned users, TODO
        self.permBans = [] #Perm bans on users, in format [hostmask],[username] TODO
        self.useOwnWolframKey = False #TODO
        self.enableQuizCheat = False #Done
        self.unsafeEchos = [] #Channels where unsafe echo is allowed TODO
        self.unsafeCommandChar = False #If command must start with @, so test @ is legal
        self.enablePM = True #Done
        self.enableAutocorrect = False
        
        self.spamCount = 0
        self.botnick = "AegisServer"
        self.commandChar = "@"
        
config = Config()
    
def changeConfig(hostmask,user,channel,ops,commandChar,ircsock,ircmsg,config):
    for i in ops:
        if hostmask == i.split(",")[0] and int(i.split(",")[1]) >= 2:
            if ircmsg.lower().find(commandChar + "config.enableQuizCheat".lower()) != -1:
                config.enableQuizCheat = True
                sendmsg(channel,"QuizCheat is now enabled.",ircsock)
            elif ircmsg.lower().find(commandChar + "config.disableQuizCheat".lower()) != -1:
                sendmsg(channel,"QuizCheat is now disabled.",ircsock)
                config.enableQuizCheat = False
                
            elif ircmsg.lower().find(commandChar + "config.enableUnsafeCommandchar".lower()) != -1:
                config.unsafeCommandChar = True
                sendmsg(channel,"UnsafeCommandchar is now enabled.",ircsock)
            elif ircmsg.lower().find(commandChar + "config.disableUnsafeCommandchar".lower()) != -1:
                sendmsg(channel,"UnsafeCommandchar is now disabled.",ircsock)
                config.unsafeCommandChar = False
                
            elif ircmsg.lower().find(commandChar + "config.pmenabled ".lower()) != -1:
                arg = ircmsg.lower().split(commandChar + "config.pmenabled ".lower())[1]
                if arg == "true":
                    config.enablePM = True; sendmsg(channel,"PMs are now enabled.",ircsock)
                else:
                    config.enablePM = False; sendmsg(channel,"PMs are now disabled.",ircsock)
                    
            elif ircmsg.lower().find(commandChar + "config.autocorrect ".lower()) != -1:
                arg = ircmsg.lower().split(commandChar + "config.autocorrect ".lower())[1]
                if arg == "true":
                    config.enableAutocorrect = True; sendmsg(channel,"Autocorrect is now enabled.",ircsock)
                else:
                    config.enableAutocorrect = False; sendmsg(channel,"Autocorrect is now disabled.",ircsock)
                    
            elif ircmsg.lower().find(commandChar + "config.spam ".lower()) != -1:
                arg = ircmsg.lower().split(commandChar + "config.spam ".lower())[1]
                try: config.spamCount = int(arg)
                except: pass
                sendmsg(channel,config.spamCount,ircsock)
                
def adminCommands(hostmask,user,channel,ops,commandChar,ircsock,ircmsg,config):
    for i in ops:
        if hostmask == i.split(",")[0] and int(i.split(",")[1]) >= 1: #Level 1 commands
            if ircmsg.find(commandChar + "adminecho ") != -1:
                query = ircmsg.split(commandChar + "adminecho ",1)[1]
                sendmsg(channel,query,ircsock)
            elif ircmsg.find(commandChar + "action ") != -1:
                query = ircmsg.split(commandChar + "action ",1)[1]
                action(channel,query,ircsock)
                
            elif ircmsg.find(commandChar + "hostmask ") != -1:
                query = ircmsg.split(commandChar + "hostmask ")[1]
                if query == False:
                    sendmsg(channel,"Not a valid user!",ircsock)
                else:
                    sendmsg(channel,"Hostmask: " + gethostmask(query,ircsock),ircsock)
            elif ircmsg.find(commandChar + "banmask ") != -1:
                query = ircmsg.split(commandChar + "banmask ")[1]
                if query == False:
                    sendmsg(channel,"Not a valid user!",ircsock)
                else:
                    sendmsg(channel,"Banmask: " + banmask(query,ircsock),ircsock)
                
        if hostmask == i.split(",")[0] and int(i.split(",")[1]) >= 2: #Level 2 commands
            if ircmsg.find(commandChar + "say ") != -1:
                query = ircmsg.split(commandChar + "say ")[1].split(" ",1)
                sendmsg(query[0],query[1],ircsock)
                
            if ircmsg.find(commandChar + "sayraw ") != -1:
                query = ircmsg.split(commandChar + "sayraw ")[1]
                sendmsgraw(query,ircsock)
                
            elif ircmsg.find(commandChar + "join ") != -1:
                query = ircmsg.split(commandChar + "join ")[1]
                joinchan(query,ircsock)
            elif ircmsg.find(commandChar + "part ") != -1:
                partchan( ircmsg.split(commandChar+"part ")[1] ,ircsock)
            elif ircmsg.find(commandChar + "part") != -1:
                partchan(channel,ircsock)
            elif ircmsg.find(commandChar + "cycle") != -1:
                partchan(channel,ircsock)
                joinchan(channel,ircsock)
            elif ircmsg.find(commandChar + "nick ") != -1:
                query = ircmsg.split(commandChar + "nick ")[1]
                changenick(query,ircsock)
                config.botnick = query
                 
            elif ircmsg.find(commandChar + "commandChar ") != -1:
                query = ircmsg.split(commandChar + "commandChar ")[1]
                config.commandChar = query
                sendmsg(channel,"The new command char is " + query,ircsock)

                
            elif ircmsg.find(commandChar + "eval ") != -1:
                import math,random,datetime,time,cmath,requests,wikipedia, config, re, sys, os, urllib, urllib2, cmath
                import calc,AI,op,BowserBucks,BowserCountry,General,MC,stats,Trivial
                from fractions import Fraction
                from decimal import Decimal

                
                bwbellairs_smells = True
                zz_smells = True
                bowserinator_smells = False
                
                try:
                    query = ircmsg.split(commandChar + "eval ")[1]
                    result = eval(query)
                    sendmsg(channel,"The result: " + str(result),ircsock)
                except Exception as e:sendmsg(channel,"There was an error: "+str(e),ircsock)
            elif ircmsg.find(commandChar + "exec ") != -1:
                try:
                    query = ircmsg.split(commandChar + "exec ")[1]
                    exec query
                    sendmsg(channel,"The result: " +str("It worked."),ircsock)
                except Exception as e:sendmsg(channel,"There was an error: "+str(e),ircsock)
                
                
def mcPhrase(ircmsg,nick):
    if (nick == "potatorelay" and "<" in ircmsg) or (nick == "creativerelay" and "<" in ircmsg):
        ircmsg = ircmsg.split(" :",1)[0] + " :" + ircmsg.split(" :",1)[1].split("> ",1)[1]
    return ircmsg