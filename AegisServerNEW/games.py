#bomb
import random, time, datetime
#import ephem  

#o=ephem.Observer()  
#o.lat='49'  
#o.long='3'  
#sun=ephem.Sun()  
#sun.compute()  

def coin():
    return "Result: " +  random.choice(["Heads","Tails"])
    
def dice():
    return "Result: " + str(random.randint(1,6))
    
chambers = 6

def roulette(chambers):
    if random.random() < 1.0/chambers:
        return True
    return False
    
def eightball():
    choices=  [
        "It is certain",
"It is decidedly so",
"Without a doubt",
"Yes, definitely",
"You may rely on it",
"As I see it, yes",
"Most likely",
"Outlook good",
"Yes",
"Signs point to yes",
"Reply hazy try again",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Concentrate and ask again",
"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good",
"Very doubtful"
        ]
    return random.choice(choices)

def sendmsg(chan,msg,ircsock):
    ircsock.send("PRIVMSG {0} :{1}\n".format(chan, msg))
def kickuser(channel,user,message,ircsock):
    user = user.replace(" ","").replace(":","")
    ircsock.send("KICK " + channel + " " + user+ " :" + message +"\r\n")
    
def runCommands(channel,nick,commandChar,ircmsg,ircsock,hostmask):
    chambers = 6
    
    #Dice and coin
    if ircmsg.find(commandChar+"coin") != -1:
        sendmsg(channel,coin(),ircsock)
    elif ircmsg.find(commandChar+"dice") != -1:
        sendmsg(channel,dice(),ircsock)
    elif ircmsg.find(commandChar+"8ball") != -1:
        sendmsg(channel,eightball(),ircsock)
        
    elif ircmsg.find(commandChar+"rand ") != -1:
        choice = ircmsg.split(commandChar+"rand ",1)[1].split(',')
        try:
            sendmsg(channel,"Result: " + str(random.randint(int(choice[0]),int(choice[1]))),ircsock)
        except:
            sendmsg(channel,"Invalid input was found.",ircsock)
        
    elif ircmsg.find(commandChar+"roulette") != -1:
        if roulette(chambers) == True:
            #Bamn, kick the user, reload the chambers
            chambers = 6
            sendmsg(channel,"You shot yourself in the head :P Reloading...",ircsock)
            kickuser(channel,nick,"Shot yourself.",ircsock)
        else:
            sendmsg(channel,"*click* Nothing happens",ircsock)
    
    elif ircmsg.find(commandChar+"time") != -1:
        result = "\x02Current Time: \x0f" + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        result = result + " \x02CTime: \x0f" + str(time.time())
        
        #sun.compute()  
        #result = result + "\x02 Next full moon: \x0f" + str(ephem.next_full_moon(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())))
        #result = result + "\x02 Next new moon: \x0f" + str(ephem.next_new_moon(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())))
        #result = result + "\x02 Sunrise: \x0f" + str(o.previous_rising(sun))
        #result = result + "\x02 Sunset: \x0f" + str(o.next_setting(sun))

        sendmsg(channel, result, ircsock)
        