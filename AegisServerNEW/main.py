from __future__ import division
import random
import sys, datetime
import math
from math import *
import re, socket
import time, pickle, imp
import traceback, ssl, socks

import pastebin
import calc
import proxies
import op
import Trivial
import BowserBucks
import General
import TextPhrase
import QuizSolver
import stats
import config
import autocorrect
import games
import word
import AI
import MC
import evil
import logs

server = "irc.freenode.net"   # Server irc.freenode.net
channels = ["#ezzybot-bots","#bmn","##bowserinator","##radioneat","##powder-mc","##powder-bots","#botters-test","#ezzybot"]   # Channels
botnick = config.config.botnick
commandChar = "@" 

blacklistchan = ["##socialanalysis"]

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock = ssl.wrap_socket(ircsock)
ircsock.connect((server, 6697)) #SSL for secure connection :D
ircsock.send("USER {0} {0} {0} :Bowserinator's Channel Helper.\n".format(botnick).encode('utf-8'))
ircsock.send("NICK {0}\n".format(botnick).encode('utf-8'))

auto_opsF = open('data/auto-op.txt', 'r')
auto_ops = []  #Save usernames in format user,channel (Or all),voice/op
for i in auto_opsF:
    auto_ops.append(i.replace("\n",""))
    
data_channelsF = open('data/urlDataChannels.txt', 'r')
data_channels = []  #Save usernames in format user,channel (Or all),voice/op
for i in data_channelsF.readlines():
    data_channels.append(i.replace("\n",""))

opsF = open('data/ops.txt', 'r')
ops = []  #Save usernames in format user,channel (Or all),perm levl
for i in opsF.readlines():
    ops.append(i.replace("\n",""))

# Stuff------------------------
def ping(): 
    ircsock.send("PONG :pingis\n".encode('utf-8'))

def partchan(chan):
    ircsock.send("PART {0}\n".format(chan).encode('utf-8'))
    
def changenick(nick):
    ircsock.send("NICK {0}\n".format(nick).encode('utf-8'))
    
def sendmsg(chan, msg):
    ircsock.send("PRIVMSG {0} :{1}\n".format(chan, msg))#.encode('utf-8'))


def joinchan(chan):  
    ircsock.send("JOIN {0}\n".format(chan).encode('utf-8'))
    

def action(channel,message):
    sendmsg(channel,"\x01ACTION " + message + "\x01")

def voice(channel,nick):
    ircsock.send("MODE {0} +v {1}\n".format(channel,nick).encode('utf-8'))
def opnick(channel,nick):
    ircsock.send("MODE {0} +o {1}\n".format(channel,nick).encode('utf-8'))
def deopnick(channel,nick):
    ircsock.send("MODE {0} -o {1}\n".format(channel,nick).encode('utf-8'))
def kickuser(channel,user,message="Default kick message"):
    user = user.replace(" ","").replace(":","")
    ircsock.send("KICK " + channel + " " + user+ " :" + message +"\r\n")
def ban(channel,nick):
    ircsock.send("MODE {0} +b {1}\n".format(channel,nick).encode('utf-8'))
def unban(channel,nick):
    ircsock.send("MODE {0} -b {1}\n".format(channel,nick).encode('utf-8'))
    
for i in channels:
    joinchan(i)
    if i != "#botters-test":
        sendmsg("ChanServ","op " + i)

BWBellairsTrue = True
loginServer = False

#THE ACTUAL LOOP
while 1:
    try:
        ircmsg = ircsock.recv(2048)#.decode('utf-8', 'ignore')  # receive data from the server
        ircmsg = ircmsg.strip('\n\r')  # removing any unnecessary linebreaks.
        print(ircmsg)   #USED TO PRINT IRCM
        
        nick = ircmsg.split("!")[0][1:]
        user = nick
        botnick = config.config.botnick
        commandChar = config.config.commandChar
        
        logs.phraseText(ircmsg)
        
        #Spam
        if config.config.spamCount > 0:
            sendmsg("##bwbellairs-bots","SPAM")
            config.config.spamCount -= 1
        
        #Auto-oping, these users will be auto-maticlly opped. Run when user is deopped or has joined
        #User,channel/all,(voice/op)
        
        #:Windows98!Windows98@gateway/shell/layerbnc/x-ddwovzqkwekqsahf INVITE AegisServer :##socialanalysis
        if "invite "  + botnick.lower() in ircmsg.lower() and "windows98se" not in ircmsg.lower():
            if ircmsg.split(" :")[1].lower() not in blacklistchan:
                joinchan(ircmsg.split(":")[-1])
            
        #if ircmsg.find(" KICK ") != -1:
            #if ircmsg.split(" KICK ")[1].find("Bowserinator") != -1 and ircmsg.split(" KICK ")[1].split(" ")[0].lower() != botnick.lower():
                #kickuser(ircmsg.split(" KICK ")[1].split(" ")[0],ircmsg.split("!",1)[0].replace(":","",1))
                #ban(ircmsg.split(" KICK ")[1].split(" ")[0],ircmsg.split("!",1)[0].replace(":","",1))
            
        if ircmsg.find(" MODE ") != -1:
            channel = ircmsg.split(' MODE ')[1].split(' ')[0]
            hostmask = ircmsg.split(nick)[-1].split(" MODE ")[0].replace(" ","")
            nick = ircmsg.split(" ")[-1]
            
            if ircmsg.find("+b *!*@222.213.197.104") != -1 or ircmsg.lower().find("+b " + botnick.lower()) != -1:
                unban(channel,ircmsg.split(" +b ")[1])
            #if ircmsg.find("+o ") != -1 and ircmsg.find('iovoid') != -1: 
               # deopnick(channel,"iovoid")
                
            #Deop
            if ircmsg.find("MODE {0} -o".format(channel)) != -1:
                if nick.lower() == botnick.lower():
                    sendmsg("ChanServ","op " + channel)
                    
                for i in auto_ops:
                    data = i.split(',')
                    if data[0].lower() == nick.lower()  or data[0].lower() in hostmask.lower():
                        if data[1] == channel or data[1] == "all":
                            if data[2] == "op":
                                opnick(channel,nick)
            if ircmsg.find("MODE {0} +o".format(channel)) != -1:
                for i in auto_ops:
                    data = i.split(',')
                    if data[0].lower() == nick.lower()  or data[0].lower() in hostmask.lower():
                        if data[1].lower() == channel.lower() or data[1] == "all":
                            if data[2] == "deop":
                                deopnick(channel,nick)
            if ircmsg.find("MODE {0} -v".format(channel)) != -1:
                for i in auto_ops:
                    data = i.split(',')
                    if data[0].lower() == nick.lower()  or data[0].lower() in hostmask.lower():
                        if data[1] == channel or data[1] == "all":
                            if data[2] == "voice":
                                voice(channel,nick)
            if ircmsg.find("MODE {0} +b".format(channel)) != -1: #ANTI BANS
                for i in auto_ops:
                    data = i.split(',')
                    if data[2] == "noban":
                        if data[0].lower() == nick.lower() or nick.lower().find(data[3].lower()) != -1:
                            if data[1] == channel or data[1] == "all":
                                    unban(channel,nick)
                            
        if ircmsg.find(" JOIN ") != -1:
            nick = ircmsg.split("!")[0].replace(":","",1)
            channel = ircmsg.split(' JOIN ')[-1].split(' :')[0]
            hostmask = ircmsg.split(nick)[-1].split(" JOIN ")[0].replace(" ","")
            
            for i in auto_ops:
                data = i.split(',')
                if data[0].lower() == nick.lower() or data[0].lower() in hostmask.lower():
                    if data[1].lower() == channel or data[1] == "all":
                        if data[2] == "voice":
                            voice(channel,nick)
                        if data[2] == "op":
                            opnick(channel,nick)
                        if data[2] == "deop":
                            deopnick(channel,nick)
                        if data[2] == "kick":
                            kickuser(channel,nick,"Sorry you are autokicked")
                                
        if ircmsg.find(' PRIVMSG ') != -1:
            nick = ircmsg.split("!")[0][1:]
            channel = ircmsg.split(' PRIVMSG ')[-1].split(' :')[0]
            user = nick
            hostmask = ircmsg.split(" PRIVMSG ")[0].split("@")[1].replace(" ","")
            
            if loginServer == False:
                sendmsg("DataX","LOGIN la78zg294dap7swpe6wx ")
                loginServer = True
                
            if nick.lower() == "datax":
                ircmsg = ircmsg.split(" :",1)[1]
                if "ECHO PENDING " in ircmsg:
                    sendmsg("datax","ECHO " + ircmsg.split("ECHO PENDING")[1])
                elif "JOIN " in ircmsg:
                    joinchan(ircmsg.split(" ")[-1])
                elif "SEND" in ircmsg and "PRIVMSG" in ircmsg:
                    sendmsg(ircmsg.split(" :")[0].split(" ")[-1]," " + ircmsg.split(":")[1])
            
            #Get titles of items if in special channels
            urlData = General.urlInfo(data_channels,channel,ircmsg)
            if urlData != None:
                sendmsg(channel,urlData)
                
            #Copy of auto op
            for i in auto_ops:
                data = i.split(',')
                if data[0].lower() == nick.lower()  or data[0].lower() == hostmask.lower():
                    if data[1].lower() == channel or data[1] == "all":
                        if data[2] == "kick":
                            kickuser(channel,nick,"Sorry you are autokicked")
            
            #Anti iovoidbot inforce :D
            if ircmsg.find("?!enforce +b") != -1 and ircmsg.find("unaffiliated/bowserinator") != -1:
                sendmsg(channel,"?!unenforce +b *!*@unaffiliated/bowserinator")
                kickuser(channel,"IovoidBot","Damn you iovoid")
            if ircmsg.find("?!enforce -o") != -1 and ircmsg.find("unaffiliated/bowserinator") != -1:
                sendmsg(channel,"?!unenforce -o *!*@unaffiliated/bowserinator")
                kickuser(channel,"IovoidBot","Damn you iovoid")
            if ircmsg.find("?!enforce +b") != -1 and ircmsg.lower().find("bowserinator") != -1:
                sendmsg(channel,"?!unenforce +b bowserinator@*")
                kickuser(channel,"IovoidBot","Damn you iovoid")
            if ircmsg.find("?!enforce -o") != -1 and ircmsg.lower().find("bowserinator") != -1:
                sendmsg(channel,"?!unenforce -o bowserinator@*")
                kickuser(channel,"IovoidBot","Damn you iovoid")
            
            #Commands
            if "bowserbot reset commandchar" in ircmsg:
                config.config.commandChar = "@"
                sendmsg(channel,"Commandchar reset to @")
            
            ircmsg = config.mcPhrase(ircmsg,nick)
                                
            try:
                if ircmsg.split(channel + " :")[1].startswith(commandChar) or config.config.unsafeCommandChar:
                    current_command = ircmsg.split(" :")[1].split(" ")[0]
                    
                    if ircmsg.find(commandChar+"reloadFiles") != -1:
                        auto_opsF = open('data/auto-op.txt', 'r')
                        auto_ops = []  #Save usernames in format user,channel (Or all),voice/op
                        for i in auto_opsF:
                            auto_ops.append(i.replace("\n",""))
                            
                        data_channelsF = open('data/urlDataChannels.txt', 'r')
                        data_channels = []  #Save usernames in format user,channel (Or all),voice/op
                        for i in data_channelsF.readlines():
                            data_channels.append(i.replace("\n",""))
                        
                        opsF = open('data/ops.txt', 'r')
                        ops = []  #Save usernames in format user,channel (Or all),perm levl
                        for i in opsF.readlines():
                            ops.append(i.replace("\n",""))
                        sendmsg(channel,"Files reloaded")
        
                    if ircmsg.find(commandChar+"reloadBot") != -1 and hostmask == "unaffiliated/bowserinator":
                        quote = random.choice(
                            ["Make it idiot proof and someone will make a better idiot.",
                            "He was too busy asking if he could, he didn't stop to ask if he should.",
                            "I pretend I can touch BWBellairs[Bot] and the BWBellairs[Bot] would say something to me..."]
                        )
                        ircsock.send("QUIT :{0}\n".format(quote).encode('utf-8'))
                        execfile("main.py")
                    
                    if current_command == commandChar+"randomProxy" and hostmask == "unaffiliated/bowserinator":
                        #ircsock.send("QUIT: Changing Proxy\n")
                        #ircsock.close()
                        
                        #ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        #ircsock = ssl.wrap_socket(ircsock)
                        
                        sock = socks.socksocket()
                        randomproxy = random.choice(proxies.sockslist.split("\n"))
                        ircsock.set_proxy(socks.SOCKS5, randomproxy.split(":")[0], int(randomproxy.split(":")[1]))
                        ircsock.connect((server, 6697)) #SSL for secure connection :D
                        #ircsock.send("USER {0} {0} {0} :Bowserinator's Channel Helper.\n".format(botnick).encode('utf-8'))
                        #ircsock.send("NICK {0}\n".format(botnick).encode('utf-8'))
                        
                        #for i in channels:
                            #joinchan(i)
                            #sendmsg("ChanServ","op " + i)

                        
                    if current_command == commandChar+"r":
                        sendmsg(channel,"Reloading modules...")
                        reload(op)
                        reload(proxies)
                        reload(calc)
                        reload(Trivial)
                        reload(General)
                        reload(pastebin)
                        reload(BowserBucks)
                        reload(TextPhrase)
                        reload(stats)
                        reload(config)
                        reload(QuizSolver)
                        reload(games)
                        reload(autocorrect)
                        reload(word)
                        reload(AI)
                        reload(MC)
                        reload(evil)
                        reload(logs)
                    
                    if config.config.enablePM == True:            
                        if channel == botnick:
                            channel = user
                    op.runOpCommands(ops,hostmask,channel,nick,commandChar,ircmsg,ircsock)
                    calc.runCommands(channel,nick,commandChar,ircmsg,ircsock)
                    BowserBucks.runCommands2(channel,nick,commandChar,ircmsg,ircsock,hostmask)
                    General.runCommands(channel,nick,commandChar,ircmsg,ircsock,ops,hostmask)
                    config.adminCommands(hostmask,user,channel,ops,commandChar,ircsock,ircmsg,config.config)
                    config.changeConfig(hostmask,user,channel,ops,commandChar,ircsock,ircmsg,config.config)
                    games.runCommands(channel,nick,commandChar,ircmsg,ircsock,hostmask)
                    word.runCommands(channel,nick,commandChar,ircmsg,hostmask,ircsock)
                    MC.runCommands(ircmsg,commandChar,ircsock,channel,hostmask,nick)
                    evil.runCommands(hostmask,user,channel,ops,commandChar,ircsock,ircmsg)
            except: pass
        
            if config.config.enableAutocorrect == True:
                sendmsg(channel, autocorrect.correctMsg(ircmsg.split(" :",1)[1]))
            
            if config.config.enablePM == True:
                if channel == botnick:
                    channel = user
                    
            stats.phraseText(ircmsg,commandChar,botnick,user,hostmask,channel)
            stats.botStats(ircmsg,commandChar,botnick,user,hostmask,channel)
            MC.phraseText(ircmsg,commandChar,botnick,user,hostmask,channel)
            
            if TextPhrase.phraseText(ircmsg,commandChar,botnick,user,hostmask,channel) != [""]:
                sendmsg(channel,TextPhrase.phraseText(ircmsg,commandChar,botnick,user,hostmask,channel)[0])
            
            if ircmsg.lower().find("bowserbot") != -1 or ircmsg.lower().find(botnick.lower()) != -1:
                if ircmsg.find(commandChar) == -1 and ircmsg.find("op") == -1 and "aegisserver2" not in ircmsg.lower():
                    result = TextPhrase.phraseText(ircmsg,commandChar,botnick,user,hostmask,channel)
                    sendmsg(channel,result[0])
            try:
                if stats.runCommands(channel,nick,commandChar,ircmsg,ircsock,hostmask) != None:
                    sendmsg(channel,stats.runCommands(channel,nick,commandChar,ircmsg,ircsock,hostmask))
            except: pass
            
            if Trivial.birthday(nick,BWBellairsTrue) != False:
                for i in Trivial.birthday(nick,BWBellairsTrue):
                    sendmsg(channel,i)
                BWBellairsTrue = False   
                    
            if config.config.enableQuizCheat:
                a = QuizSolver.phraseChat(ircmsg,nick)
                sendmsg(channel,a)
            
            #TEMP TEST!!
            if ircmsg.split(" :",1)[1].startswith("bowserbot") or ircmsg.lower().split(" :",1)[1].startswith(botnick.lower()):
                if "aegisserver2" not in ircmsg.lower():
                    AI.phraseText(ircmsg.lower().split(" :",1)[1].replace('bowserbot','').replace(botnick.lower(),""),channel,nick,hostmask,ircsock,botnick)
            
            
        
        #Auto rejoin
        for channel in channels:
            if ircmsg.lower().find("kick " + channel.lower() + " " + botnick.lower()) != -1:
                joinchan(channel)
                time.sleep(1)
                joinchan(channel)
            if ircmsg.lower().find("part " + channel.lower()) != -1:
                joinchan(channel)
                time.sleep(1)
                joinchan(channel)

        
        if ircmsg.find("PING :") != -1:
            ping()
    except:
        traceback.print_exc()
