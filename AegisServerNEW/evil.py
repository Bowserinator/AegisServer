execfile("config/hostmask.py")
import time

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

    
def runCommands(hostmask,user,channel,ops,commandChar,ircsock,ircmsg):
    for i in ops:
        if hostmask == i.split(",")[0] and int(i.split(",")[1]) >= 4: #Must have level 4 or higher to be evil >:D
            
            pass

            
            