import random, json, datetime

execfile("BowserBucks/news.py")

def monify(string):
    return u"\u0243".encode("utf8") + "{:,}".format(string)
    
newsF = open('BowserBucks/news.txt', 'r')
news = []  #News!
for i in newsF:
    news.append(i.replace("\n",""))
    
factsF = open('BowserBucks/factcore.txt', 'r')
factCore = []  #News!
for i in factsF:
    factCore.append(i.replace("\n",""))

gladosF = open('BowserBucks/glados.txt', 'r')
gladosQuote = []  #News!
for i in gladosF:
    if i.replace("\n","") != "":
        gladosQuote.append(i.replace("\n",""))
    
def getItem(hostmask,money):
    #Json in format hostmask: [nick,amount,inv]
    try:
        return money[hostmask]
    except: return None
    
def nickExist(nick,money):
    for key in money:
        if money[key][0].lower() == nick.lower():
            return True
    return False
    
def giveMoneyToNick(nick,amount,money):
    for key in money:
        if money[key][0] == nick:
            money[key][1] += amount
    return money
    
def getHostMask(nick,money):
    for key in money:
        if money[key][0].lower() == nick.lower():
            return key
    return None
    
def gethostmask(nick,irc): #irc = ircsock
    irc.send("WHO {0}\r\n".format(nick).encode("UTF-8"))
    ircmsg = irc.recv(2048)
    ircmsg = ircmsg.decode("UTF-8")
    ircmsg = ircmsg.strip("\r\n")
    ircmsg = ircmsg.strip(":")
    ircmsg = ircmsg.split()

    if ircmsg[1] == "352":
        user = ircmsg[4]
        host = ircmsg[5]
        hm = "{0}!{1}@{2}".format(nick, user, host)
        return hm
    else:
        return False



#The run commands thing
def sendmsg(chan, msg,ircsock):
    ircsock.send("PRIVMSG {0} :".format(chan) + msg + "\n")
    
  
#In format name:{DispalyName,cost,information,instock(at the store)} 
#Names do not support more than 2 words and uppercase
#Also have can buy at the end
shopItems = {
    #Computer catagory
    "cheap computer":["Cheap Computer",100,"A cheap second hand computer you buy off the black market.",True,True],
    "gaming computer":["Gaming Computer",1500,"Expensive computer you can show off to your friends.",True,True],
    "server":["Server",2000,"Ultra powerful server you use to do your hacking.",True,True],
    "supercomputer":["Supercomputer",1000000,"Capable of 20 quadrillion calculations per second.",True,True],
    "quantum computer":["Quantum Computer",15000000,"It's 512 qBit power is capable of instantaneous calculation",True,True],
    "skynet":["SkyNet",45000000000,"Superintellegent computer with access to nuclear missiles.",False,False], #You get skynet through timetravel
    "glados":["GLaDOS",2000000000,"Genetic Lifeform and Disk Operating System. Comes with cores and neurotoxin.",True,True],
     
    #BUilding catagory 
    "company":["Company",25000000000,"A successful company that makes money.",True,True],
    "lab":["Lab",20000000000,"A high-tech labatory that does research.",True,True],
    "farm":["Farm",5000000,"A cheap farm with cows 'n crops.",True,True],
    "factory":["Factory",100000000,"Productive factory to make stuff.",True,True],
    "space station":["Space Station",10000000000,"A research lab in outer space.",True,True],
    "mine":["Mine",1000000,"A mine to mine precious minerals.",True,True],
    "estate":["Estate",300000,"A piece of land you can live in.",True,True],
    
    #Minerals, value can change
    "gold":["Gold",10000,"Shiny metal, highly conductive and acid resistant.",True,True],
    "diamond":["Diamond",1000000,"Compressed carbon arranged in a face-centered cubic crystal structure.",True,True],
    "kryptonite":["Kryptonite",1000000000,"Alien radioactive mineral, properties unknown.",True,True],
    "unobtanium":["Unobtanium",1000000000000000,"Room temperature superconductor with high melting point. Virtually indestructable.",False,False], #chance when using enterprise or tardis?
    "chronoton":["Chronoton",1000000000000000000,"An element capable of manipulating time itself.",False,False], #Chance when using tardis
    "ice nine":["Ice nine",1000000000,"A polymorph of water that seed crystalizes water into more ice nine. WARNING: You might lose all of your money when using.",False,False], #Chance through lab experiments
    "redstone":["Redstone",10000,"Common element. Conductive and ferromagnetic.",True,True],
    "neutronium":["Neutronium",1000000000000,"Hyper dense element composed entirely of neutrons.",False,False], #Chance through enterprise or tardis?
    "antimatter":["Antimatter",1000000000,"Matter composed of anti-protons and neutrons.",False,False],
    
    #Vechicles and stuff
    "enterprise":["Enterprise",50000000000,"Galaxy class starship.",True,True],
    "death star":["Death Star",8100000000000000,"A weapon that utterly and completely destroys everything.",True,True],
    "tardis":["TARDIS",100000000000000000,"Police Box: Deceptively spacious.",False,True], 
    "space laser":["Space Laser",10000000000,"A powerful city destroying laser in space.",True,True],
    "magic school bus":["Magic School Bus",1000000000000000,"A magical school bus that can transform into anything.",False,False],
     
     #items
    "cube":["Cube",10,"Cheap Rubik's cube you bought off of eBay.",True,True], 
    "alethiometer":["Alethiometer",100000000,"'It's an alethiometer. It tells the truth.'",True,False], #idk use tardis?
    "lightsaber":["Lightsaber",10000000,"Powerful laser sword that cuts through almost anything.",True,True],
    "smallpox":["Smallpox",1000000,"An offically eradicated virus that kills.",True,True],
    "ipad":["iPad",1099,"A brand new iPad. It's expensive because apple.",True,True],
    "voodoo doll":["Voodoo Doll",150000,"Spirtually linked with jacob1, do whatever you want.",True,True],
    
    "god":["God",999999999999999999999999999999999999999999999999,"Even god sold himself to obey your will.",False,True],
    "nuke":["Nuke",2000000,"Harness the power of atomic fission!",True,True],
    "paradox":["Paradox",-500000000000000000000000000000000,"Well you're screwed.",False,False],
    "blackhole":["Blackhole",-5000000000000000,"GET RID OF IT NOW!!",False,False],
    "io":["Io",1000000000000,"A small moon. Idk what you'd use it for.",True,True],
    
    "slave":["Slave",100,"Your personal slave. (There is the 13th admendment though)",True,True],
    "cat":["Cat",50,"A cat you bought at a pet store.",True,True],
    "stock":["Stock",1000,"A item with constantly changing value. Sell when it's worth more.",True,True],
}

def runCommands2(channel,nick,commandChar,ircmsg,ircsock,hostmask):
    #commandChar = commandChar + "b."
    if ircmsg.find(commandChar + "news") != -1:
        sendmsg(channel,"\x02[Breaking News]\x0f: " + randomNews(news),ircsock)
    
    #Actual money commands
    moneyF = open('BowserBucks/money.txt', 'r').read()
    if moneyF == "":
        money = {}
    else:
        money = json.loads(moneyF)

    if ircmsg.find(commandChar + "bal") != -1 or ircmsg.find(commandChar + "cash") != -1:
        if nickExist(nick,money) == False:
            money[hostmask] = [nick,10000,{}]
            sendmsg(channel,"An account has been created for your hostmask under the nick " + nick + "!",ircsock)
        else:
            value = int(money[hostmask][1])
            sendmsg(channel,"\x02Your balance:\x0f " + u"\u0243".encode('utf8') + "{:,}".format(value),ircsock)
    
    elif ircmsg.find(commandChar + "lottery") != -1: 
        if money == None or getItem(hostmask,money) == None:
            sendmsg(channel,"Type " + commandChar + "bal to register your hostmask!",ircsock)
        else:
            money[hostmask][1] -= 5
            sendmsg(channel,"You have bought a lottery ticket for " + u"\u0243".encode('utf8') + "5!",ircsock)
            if random.randint(0,6000000) == 1000:
                amount = random.randint(1e20,1.5e20)
                money[hostmask][1] += amount
                sendmsg(channel,"Congratulations! You have won " + u"\u0243".encode('utf8') + "{:,}".format(amount) + "!",ircsock)
            else:
                sendmsg(channel,"Sorry not a winner :C",ircsock)
                
    elif ircmsg.find(commandChar + "burnmoney ") != -1:
        burnmsg = ["BowserBucks aren't evil you know...","You must be very rich!","Burning cryptocurrency is bad for your health.","Save some money for insurance!",
        "Did you hear that computers emit toxic fumes when burned?","Donating to charity is better!","Why? Just why?"]
        if money == None or getItem(hostmask,money) == None:
            sendmsg(channel,"Type " + commandChar + "bal to register your hostmask!",ircsock)
        else:
            try:
                amount = int(ircmsg.split(commandChar+"burnmoney ")[1]) ;amount = -amount
                if amount >= 0:
                    sendmsg(channel,"\x035You can't burn that amount of money!!",ircsock) ;return ""
                if int(getItem(hostmask,money)[1]) < -amount:
                    sendmsg(channel,"\x035You can't burn that amount of money!!",ircsock) ;return ""
                money[hostmask][1] += amount
                sendmsg(channel,"You have burned " + u"\u0243".encode('utf8') + "{:,}".format(-amount) + ". " + random.choice(burnmsg),ircsock)
            except:
                sendmsg(channel,"\x035Not a valid amount of money to burn!!",ircsock)
    
    elif ircmsg.find(commandChar + "give ") != -1:
        nickToGive = ircmsg.split(commandChar+"give ")[1].split(" ")[0]
        if money == None or nickExist(nickToGive,money) == False:
            sendmsg(channel,"\x035That user is not online or does not exist.",ircsock)
        else:
            try:
                amount = int(ircmsg.split(commandChar+"give ")[1].split(" ")[1].replace(".0","")) 
                if amount <= 0:
                    sendmsg(channel,"\x035You can't give that amount of money!!",ircsock) ;return ""
                if int(getItem(hostmask,money)[1]) < amount:
                    sendmsg(channel,"\x035You can't give that amount of money!!",ircsock) ;return ""
                hostToGive = nickToGive
                if hostToGive.lower() == nick.lower():
                    sendmsg(channel,"\x035You can't give money to yourself!.",ircsock); return ""
                money = giveMoneyToNick(nickToGive,amount,money)
                money[hostmask][1] -= amount
                sendmsg(channel,"You have given " + u"\u0243".encode('utf8') + "{:,}".format(amount) + " to " + nickToGive,ircsock)
            except:
                sendmsg(channel,"\x035Not a valid amount of money to give!!",ircsock)
    
    elif ircmsg.find(commandChar + "flipall") != -1:
        bet = money[hostmask][1] 
        if random.random() > 0.5:
            money[hostmask][1] += bet
            sendmsg(channel,"Congratulations! You win! +"+"{:,}".format(bet),ircsock)
        else:
            money[hostmask][1] -= bet
            sendmsg(channel,"Sorry you did not win! -"+"{:,}".format(bet),ircsock)
            
    elif ircmsg.find(commandChar + "flip ") != -1:
        try:
            bet = int(ircmsg.split(commandChar + "flip ")[1])
            money[hostmask][1] -= bet
            if random.random() > 0.5:
                money[hostmask][1] += bet*2
                sendmsg(channel,"Congratulations! You win! +"+"{:,}".format(bet),ircsock)
            else:
                sendmsg(channel,"Sorry you did not win! -"+"{:,}".format(bet),ircsock)
        except:
            sendmsg(channel,"\x035Not a valid amount of money to bet!!",ircsock)
    
    #Inventory mangagment
    elif ircmsg.find(commandChar+"inv") != -1:
        inv = money[hostmask][2]
        returned = ["\x02"+money[hostmask][0]+": \x0f",""]; max_ir = 0
        for key in inv:
            if inv[key] != 0:
                max_ir += 1
                if max_ir <= 30:
                    returned[0] = returned[0] + "  " + shopItems[key][0] + ": " + str(inv[key])
                else:
                    returned[1] = returned[1] + "  " + shopItems[key][0] + ": " + str(inv[key])
        if max_ir == 0:
            sendmsg(channel,returned[0] + " You have nothing currently",ircsock)
        else:
            for i in returned:
                sendmsg(channel,i,ircsock)
    
    elif ircmsg.find(commandChar+"burnitem ") != -1:
        args = ircmsg.split(commandChar+"burnitem ")[1].split("21415") #TODO custom item burns
        if len(args) == 1:
            if money[hostmask][2][args[0].lower()] > 0:
                if args[0].lower() == "tardis":
                    sendmsg(channel,"You try to burn your TARDIS but it collapses into a temperal paradox. (-1 TARDIS) (+1 Paradox)",ircsock)
                    money[hostmask][2][args[0].lower()] -= 1
                    try: money[hostmask][2]["paradox"] += 1
                    except: money[hostmask][2]["paradox"] = 1
                elif args[0].lower() == "paradox":
                    sendmsg(channel,"You try to burn your paradox but nothing happens.",ircsock)
                elif args[0].lower() == "voodoo doll":
                    money[hostmask][2][args[0].lower()] -= 1
                    sendmsg(channel,"You burn your voodoo doll, as a result jac0b1 spontaneously combusts. (-1 voodoo doll)",ircsock)
                elif args[0].lower() == "nuke":
                    money[hostmask][2][args[0].lower()] -= 1
                    sendmsg(channel,"You burn your nuke, which blows up into a cloud of radioactive smoke. (-1 nuke)",ircsock)
                elif args[0].lower() == "god":
                    try: money[hostmask][2]["paradox"] += 10000
                    except: money[hostmask][2]["paradox"] = 10000
                    sendmsg(channel,"You try to burn god, but that creates paradoxes within paradoxes. (+10000 paradoxes)",ircsock)
                elif args[0].lower() == "blackhole":
                    money[hostmask][2][args[0].lower()] += 1
                    sendmsg(channel,"You try to burn your black hole, but it absorbs the fire and multiplies. (+1 black hole)",ircsock)
                elif args[0].lower() == "glados":
                    money[hostmask][2][args[0].lower()] -= 1
                    sendmsg(channel,"[GLaDOS]: As they burned it hurt because I felt so happy for you! [GLaDOS dies]",ircsock)
                elif args[0].lower() == "paradox":
                    sendmsg(channel,"You aren't getting rid of it that easily!",ircsock)
                elif args[0].lower() == "unobtanium":
                    sendmsg(channel,"Unobtanium doesn't burn apparently.",ircsock)
                else:
                    money[hostmask][2][args[0].lower()] -= 1
                    sendmsg(channel,"You have burned 1 " + args[0],ircsock)
            else:
                sendmsg(channel,"\x035You do not have enough of the item!",ircsock)

        
    #Shop commands
    elif ircmsg.find(commandChar+"info ") != -1:
        itemname = ircmsg.split(commandChar+"info ")[1]
        try:
            item = shopItems[itemname.lower()]
            sendmsg(channel,"\x02" + item[0] + ": \x0fCost: " + u"\u0243".encode('utf8') + "{:,}".format(item[1]) + " - " + item[2],ircsock)
        except:
            sendmsg(channel,"\x035Item not found, type " + commandChar +"shop.list for items",ircsock)
            
    elif ircmsg.find(commandChar+"shop.list") != -1:
        catagory = ircmsg.split(commandChar+"shop.list")[1]
        if catagory == "":
            sendmsg(channel,"\x02Catagories: \x0fcomputer, building, mineral, vehicle, item, other",ircsock); return ""
        elif catagory == " computer" or catagory == " computers":
            names = ["glados","server","skynet","quantum computer","cheap computer","supercomputer","gaming computer"]
        elif catagory == " building" or catagory == " buildings":
            names = ["lab","company","space station","mine","farm","factory","estate"]
        elif catagory == " mineral" or catagory == " minerals":
            names = ["diamond","gold","kryptonite","unobtanium","chronoton","ice nine","redstone","neutronium"]
        elif catagory == " vehicle" or catagory == " vehicles":
            names = ["tardis","death star","enterprise","space laser","magic school bus"]
        elif catagory == " item" or catagory == " items":
            names = ["cube","alethiometer","lightsaber","smallpox","ipad","voodoo doll"]
        else:
            names = []
            for key in shopItems:
                names.append(key)
        
        returned = ""
        for key in shopItems:
            #if shopItems[key][3] == True and key in names:
            if key in names:
                returned = returned + shopItems[key][0] +"(" + "{:,}".format(shopItems[key][1]) + "), "
        sendmsg(channel,returned,ircsock)

        
    elif ircmsg.find(commandChar+"buy ") != -1:
        args = ircmsg.split(commandChar+"buy ")[1]
        
        try:
            try:
                amount = int(float(args[args.rfind(' ')+1:]))
                itemname = args.split(" " +str(amount))[0]
            except:
                amount = 1
                itemname = args.lower()
        except:
            sendmsg(channel,"Use " + commandChar + "buy [item] [amount]",ircsock); return ""
        if amount <= 0:
            sendmsg(channel,"\x035Invalid amount of items to buy!",ircsock); return ""
        try:
            item = shopItems[itemname]
            if money[hostmask][1] - amount*item[1] < 0:
                sendmsg(channel,"\x035You do not have enough money!",ircsock); return ""
            elif item[4] == False:
                sendmsg(channel,"\x035You cannot buy this item!",ircsock); return ""
            money[hostmask][1] -= amount*item[1]
            try:
                money[hostmask][2][itemname] += amount
            except:
                money[hostmask][2][itemname] = amount
            sendmsg(channel,"You bought " + "{:,}".format(amount) + " " + shopItems[itemname.lower()][0] ,ircsock)
        except:
            sendmsg(channel,"\x035Type [command here] to get items",ircsock)
        
    elif ircmsg.find(commandChar+"sell ") != -1:
        args = ircmsg.split(commandChar+"sell ")[1] 
        try:
            try:
                amount = int(float(args[args.rfind(' ')+1:]))
                itemname = args.split(" " +str(amount))[0]
            except:
                amount = 1
                itemname = args
        except:
            sendmsg(channel,"Use " + commandChar + "buy [item] [amount]",ircsock); return ""
        if amount <= 0:
            sendmsg(channel,"\x035Invalid amount of items to sell!",ircsock); return ""
        try:
            item = shopItems[itemname]
            if money[hostmask][2][itemname.lower()] - amount < 0:
                sendmsg(channel,"\x03You do not have enough of the item!",ircsock); return ""
                
            if itemname == "nuke" and random.random() < 0.3:
                choices =  ["moon nazis","evil russians","jacob1","North Korea","your mom"]
                sendmsg(channel,"You have been caught illegally selling nukes to " + random.choice(choices) + ". You lose all your nukes and are fined 10,000,000",ircsock)
                money[hostmask][1] -= 10000000
                money[hostmask][2]["nuke"] = 0
            elif itemname == "paradox" or itemname == "blackhole":
                sendmsg(channel,"You aren't getting rid of it that easily!",ircsock); return ""
            else:
                money[hostmask][2][itemname.lower()] -= amount
                money[hostmask][1] += item[1]*amount
                sendmsg(channel,"You sold " + "{:,}".format(amount) + " " + itemname.lower().title() + " for " + "{:,}".format(item[1]*amount) ,ircsock)
        except:
            sendmsg(channel,"\x035Not enough item",ircsock)
    
    elif ircmsg.find(commandChar+"use ") != -1:
        item = ircmsg.split(commandChar+"use ")[1].lower()
        try: 
            #The actual items
            if item == "cheap computer" and money[hostmask][2]["cheap computer"] > 0:
                prob = random.random()
                if prob< 0.3:
                    sendmsg(channel,"Your computer gets so hot it catches on fire. (-1 cheap computer)",ircsock)
                    money[hostmask][2][item] -= 1
                elif prob < 0.6:
                    sendmsg(channel,"Your computer blows up for no reason. (-1 cheap computer)",ircsock)
                    money[hostmask][2][item] -= 1
                elif prob < 0.9:
                    sendmsg(channel,"Your computer is so laggy you throw it out of a window. (-1 cheap computer)",ircsock)
                    money[hostmask][2][item] -= 1
                elif prob < 0.95:
                    sendmsg(channel,"Your computer is taken by the police for containing US cold war secrets. (-1 cheap computer)",ircsock)
                    money[hostmask][2][item] -= 1
                else:
                    amount = random.randint(100000,500000)
                    sendmsg(channel,"Your computer was discovered to be worth " + "{:,}".format(amount) + " (-1 cheap computer) (+"+ "{:,}".format(amount)+")",ircsock)
                    money[hostmask][2][item] -= 1
                    money[hostmask][1] += amount
                    
            elif item == "gaming computer" and money[hostmask][2]["gaming computer"] > 0:
                prob = random.random()
                if prob < 0.8:
                    sendmsg(channel,"You play " + random.choice(["Minecraft","Fallout 4","Portal","Half Life","GTA V","Skyrim"]) + " all day.",ircsock)
                elif prob < 0.97:
                    sendmsg(channel,"You show off your amazing gaming computer to your friends.",ircsock)
                else:
                    amount = random.randint(1000,50000)
                    sendmsg(channel,"You win " + "{:,}".format(amount) + " in a video game tournament! (+"  + "{:,}".format(amount)+")",ircsock)
                    money[hostmask][1] += amount
            
            elif item.startswith("server") and len(item.split(" ")) == 2 and money[hostmask][2]["server"] > 0:
                #Hack user
                userToHack = item.split(" ")[1]
                if nickExist(userToHack.lower(),money) == False:
                    sendmsg(channel,"\x035That user does not have an account!",ircsock); return ""
                    
                prob = random.random()
                if prob < 0.25: #Sucessful hack
                    toSteal = random.randint(10000,100000)
                    sendmsg(channel,"You sucessfully hack into " + userToHack + "'s bank account and steal " + "{:,}".format(toSteal) + ".",ircsock)
                    money[getHostMask(userToHack,money)][1] -= toSteal
                    money[hostmask][1] += toSteal
                    if money[getHostMask(userToHack,money)][1] < 0:
                        money[getHostMask(userToHack,money)][1] = 0
                elif prob < 0.45:
                    fine = random.randint(200000,800000)
                    sendmsg(channel,"You turn evil and DDoS " + userToHack + " and all of their servers burn, but you get fined " + "{:,}".format(fine) + ".",ircsock)
                    money[getHostMask(userToHack,money)][2]["server"] = 0
                    if money[hostmask][1] < 0:
                        money[hostmask][1] = 0
                elif prob < 0.75:
                    deaths = [userToHack + " counterhacks your server and as a result it burns. (-1 server)",
                    userToHack + " makes your server calculate 5e10000 digits of pi, causing your server to blow up. (-1 server)",
                    userToHack + " gives your server a virus, as a result it gets sick and dies. (-1 server)"]
                    sendmsg(channel,random.choice(deaths),ircsock)
                    money[hostmask][2]["server"] -= 1
                else:
                    #Fined for hacking :C
                    fine = random.randint(100000,200000)
                    sendmsg(channel,"The NSA finds out about you hacking and you are fined " + "{:,}".format(fine) + ".",ircsock)
                    money[hostmask][1] -= fine
                    if money[hostmask][1] < 0:
                        money[hostmask][1] = 0
                
            elif item == "server" and money[hostmask][2]["server"] > 0:
                prob = random.random()
                if prob < 0.7:
                    sendmsg(channel,"You host a nice website. Great job.",ircsock)
                elif prob < 0.85:
                    deaths = ["Your server is taken away because you didn't pay your non-existant monthly fees. (-1 server)",
                    "You don't mantain your servers and their CPU melts. (-1 server)",
                    "Your server is taken away for hosting terrorist related websites. (-1 server)"]
                    sendmsg(channel,random.choice(deaths),ircsock)
                    money[hostmask][2]["server"] -= 1
                elif prob < 0.87:
                    sendmsg(channel,"Your website is so successful it turns into a company! (-1 server)(+1 company)",ircsock)
                    money[hostmask][2]["server"] -= 1
                    try:
                        money[hostmask][2]["company"] += 1
                    except:
                        money[hostmask][2]["company"] = 1
                else:
                    sendmsg(channel,"You stare at your servers, wishing they were faster.",ircsock)
                    
            elif item == "voodoo doll" and money[hostmask][2]["voodoo doll"] > 0:    
                #Possible: steal money from jacob1, jacob1 bans you, jacob1 dies, harms you instead
                prob = random.random()
                if prob < 0.2:
                    sendmsg(channel,"You found out the doll was gay and threw it away. (-1 voodoo doll)",ircsock)
                    money[hostmask][2]["voodoo doll"] -= 1
                elif prob < 0.5:
                    sendmsg(channel,"You make jac0b1 work for you, and you get access to the TPT servers! (+1 server)",ircsock)
                    try:money[hostmask][2]["server"] += 1
                    except:money[hostmask][2]["server"] = 1
                elif prob < 0.7:
                    sendmsg(channel,"You stab the doll and you bleed to death. (-1 voodoo doll)",ircsock)
                    money[hostmask][2]["voodoo doll"] -= 1
                else:
                    sendmsg(channel,"You throw your doll out the window and jac0b1 dies. (-1 voodoo doll)",ircsock)
                    money[hostmask][2]["voodoo doll"] -= 1
                    
            elif item == "skynet" and money[hostmask][2]["skynet"] > 0:
                prob = random.random()
                if prob < 0.4:
                    sendmsg(channel,"Skynet becomes self aware and beings firing all of your nuclear missiles! (-all nukes)",ircsock)
                    money[hostmask][2]["nuke"] = 0
                elif prob < 0.7:
                    sendmsg(channel,"Skynet decides to kill all humans, starting with " + nick + ". (-1 Skynet)",ircsock)
                    money[hostmask][2]["skynet"] -= 1
                elif prob < 0.9:
                    sendmsg(channel,"Skynet uses human slave labour to make nukes. (+10 nukes)",ircsock)
                    try:money[hostmask][2]["nuke"] += 10
                    except:money[hostmask][2]["nuke"] = 10
                else:
                    sendmsg(channel,"Skynet does some calculations. Nothing intresting happens.",ircsock)
                    
            elif item == "quantum computer" and money[hostmask][2]["quantum computer"] > 0:
                prob = random.random()
                if prob < 0.2:
                    randNick = random.choice(["jacob1","iovoid","BWBellairs","cracker64","MrProcom"])
                    sendmsg(channel,"You use the quantuam computer to steal " + randNick + "'s password.",ircsock)
                elif prob < 0.3:
                    sendmsg(channel,"You upload your conscience to a quantum computer.",ircsock)
                elif prob < 0.4:
                    sendmsg(channel,"You attach your brain to a quanum computer, however you lose all morality. (+1 GLaDOS)(-1 Quantum computer)",ircsock)
                    try:money[hostmask][2]["quantum computer"] -= 1
                    except:money[hostmask][2]["quantum computer"] = 0
                    try:money[hostmask][2]["glados"] += 1
                    except:money[hostmask][2]["glados"] = 1
                elif prob < 0.7:
                    sendmsg(channel,"The quantum computer looks cool. That's pretty much it.",ircsock)
                elif prob <= 1:
                    sendmsg(channel,"No one knows what to do with a quantum computer, so you defenestrate it. (-1 quantum computer)",ircsock)
                    try:money[hostmask][2]["quantum computer"] -= 1
                    except:money[hostmask][2]["quantum computer"] = 0
                
            elif item == "supercomputer" and money[hostmask][2]["supercomputer"] > 0:
                prob = random.random()
                if prob < 0.4:
                    reward = random.randint(1000000,10000000)
                    reason = ["the NP = P problem","the unique games conjecture","for US launch codes","how to break public-key encryption"]
                    sendmsg(channel,"You have solved " + random.choice(reason) + " and have won " + monify(reward)+"!",ircsock)
                    money[hostmask][1] += reward
                elif prob < 0.7:
                    reason = ["calculate pi","simulate earth's climate","calculate earth crust movement","simulate an atom","create a CGI movie"]
                    sendmsg(channel,"You " + random.choice(reason) +" on your supercomputer." ,ircsock)
                elif prob < 0.92:
                    fine = random.randint(100000,500000)
                    sendmsg(channel,"Your supercomputer needs maintenance and you pay " + monify(fine) + "!",ircsock)
                    money[hostmask][1] -= fine
                else:
                    sendmsg(channel,"Your supercomputer becomes self-aware and hacks into the military. (+1 skynet)(-1 supercomputer)",ircsock)
                    try:money[hostmask][2]["skynet"] += 1
                    except:money[hostmask][2]["skynet"] = 1
                
            elif item == "glados" and money[hostmask][2]["glados"] > 0:
                prob = random.random()
                if prob < 0.03:
                    money[hostmask][2]["cat"] = 0
                    sendmsg(channel,"All your cats die in a schrodinger's cat experiment. Apparently reality does not exist. (-all cats)",ircsock)
                elif prob < 0.06:
                    try: money[hostmask][2]["lab"] -= 1
                    except: money[hostmask][2]["lab"] = 0
                    sendmsg(channel,"GLaDOS floods your labatory with deadly neurotoxin, killing everybody. (-1 lab)",ircsock)
                elif prob < 0.4:
                    sendmsg(channel,random.choice(gladosQuote).replace("Chell",nick),ircsock)
                elif prob < 0.95:
                    sendmsg(channel,"[Fact Core]: " + random.choice(factCore),ircsock)
                else:
                    sendmsg(channel,"You are given a company to research ways to make GLaDOS less homicidal. (+1 company) ",ircsock)
                    try: money[hostmask][2]["company"] += 1
                    except: money[hostmask][2]["company"] = 1
            
            elif item.startswith("company") and len(item.split(" ")) == 2 and money[hostmask][2]["company"] > 0:
                userToHack = item.split(" ")[1]
                if nickExist(userToHack.lower(),money) == False:
                    sendmsg(channel,"\x035That user does not have an account!",ircsock); return ""
    
                prob = random.random()
                sueReasons=  ["hacking your servers","existing","for eating all the potatoes in the world","genocide","using slave labor","being stupid","random health issues", "coffee spills", "xkcd references"]
                if userToHack == "NotBowserChannel":
                    sendmsg(channel,"You try to sue the bot but nothing happens because it's a bot.",ircsock); return ""
                if prob < 0.2:
                    reasons = ["ice cream","virtual potatoes","apple products","donations to charity","hugs","nuking people","building weapons of mass destruction","helping the poor","death stars"]
                    sendmsg(channel,"Shareholders are angry at " + nick + "'s tendency to spend profits on " + random.choice(reasons) + " and select " + userToHack + " as the new CEO!",ircsock)
                    try: money[getHostMask(userToHack,money)][2]["company"] += 1
                    except: money[getHostMask(userToHack,money)][2]["company"] = 1
                    money[hostmask][2]["company"] -= 1
                elif prob < 0.7:
                    fine = random.randint(100000,1000000)
                    sendmsg(channel,"You sue " + userToHack + " for " + random.choice(sueReasons) + " and lose! You've lost " + monify(fine),ircsock)
                    money[hostmask][1] -= fine
                    money[getHostMask(userToHack,money)][1] += fine
                else:
                    fine = random.randint(100000,1000000)
                    sendmsg(channel,"You sue " + userToHack + " for " + random.choice(sueReasons) + " and win! You've gained " + monify(fine),ircsock)
                    money[hostmask][1] += fine
                    money[getHostMask(userToHack,money)][1] -= fine
                    
            
                    
            elif item == "company" and money[hostmask][2]["company"] > 0:
                pass
            
            elif item == "lab" and money[hostmask][2]["lab"] > 0:
                prob = random.random()
                print(prob)
                if prob < 0.08:
                    reason = random.choice(["A man rampages through the lab with a machine gun jetpack. (-1 lab)",
                    "The lab's centeral computer becomes sentient and floods the lab with neurotoxin. (-1 lab)",
                    "The lab blows up for no apparent reason. (-1 lab)",
                    "A potato cow genetic hybrid escapes, trashing the lab in the process. (-1 lab)"])
                    sendmsg(channel,reason,ircsock)
                    money[hostmask][2]["lab"] -= 1
                elif prob < 0.16:
                    reason =  random.choice(["illegal experiments","violating human rights","violating potato rights","unsafe procedures"])
                    fine = random.randint(100000,1000000)
                    sendmsg(channel,"Your lab was caught for " + reason + " and was fined " + monify(fine),ircsock)
                    money[hostmask][1] -= fine
                elif prob < 0.5:
                    prob = random.random()
                    if prob < 0.8:
                        itemGet = random.choice(["server","quantum computer","supercomputer"])
                        try: money[hostmask][2][itemGet] += 1
                        except: money[hostmask][2][itemGet] = 1
                        sendmsg(channel,"Someone generously donated a " + itemGet + " to your lab! (+1 " + itemGet + ")",ircsock)
                    elif prob < 0.84:
                        sendmsg(channel,"Your labatory has created GLaDOS, the world's first AI. (+1 GLaDOS)",ircsock)
                        try: money[hostmask][2]["glados"] += 1
                        except: money[hostmask][2]["glados"] = 1
                    elif prob < 0.95:
                        sendmsg(channel,"Your labatory has geneticlly recreated the smallpox virus. (+1 smallpox)",ircsock)
                        try: money[hostmask][2]["smallpox"] += 1
                        except: money[hostmask][2]["smallpox"] = 1
                    elif prob < 0.98:
                        sendmsg(channel,"Your labatory has invented a working lightsaber. (+1 lightsaber)",ircsock)
                        try: money[hostmask][2]["lightsaber"] += 1
                        except: money[hostmask][2]["lightsaber"] = 1
                    else:
                        sendmsg(channel,"Your labatory has obtained some antimatter. (+1 antimatter)",ircsock)
                        try: money[hostmask][2]["antimatter"] += 1
                        except: money[hostmask][2]["antimatter"] = 1
                elif prob  < 0.52:
                    sendmsg(channel,"Your labatory has created some ice nine. (+1 ice nine)",ircsock)
                    try: money[hostmask][2]["ice nine"] += 1
                    except: money[hostmask][2]["ice nine"] = 1
                else:
                    reason = random.choice(["conducts tests on human psychology.","runs tests on metals.","builds machine prototypes.","sequences potato DNA.","builds a machine gun jetpack."])
                    sendmsg(channel,"Your lab tries to " + reason,ircsock)
                    
            elif item == "mine" and money[hostmask][2]["mine"] > 0:
                prob = random.random()
                if prob < 0.1:
                    reason = random.choice(["Your mine blows up in a horrific accident. (-1 mine)","It's not yours, it's mine! (-1 mine)"])
                    sendmsg(channel,reason,ircsock)
                    money[hostmask][2]["mine"] -= 1
                elif prob < 0.2:
                    action = random.choice(["breeding cows.","enchanting pickaxes.","building over complicated furnace arrays.","a circus.","slapping jacob1."])
                    sendmsg(channel,"Your miners get bored and start " + action,ircsock)
                else:
                    prob = random.random()
                    if prob < 0.4:
                        item = "redstone"
                        try: money[hostmask][2]["redstone"] += 1
                        except: money[hostmask][2]["redstone"] = 1
                    elif prob < 0.7:
                        item = "gold"
                        try: money[hostmask][2]["gold"] += 1
                        except: money[hostmask][2]["gold"] = 1
                    elif prob < 0.95:
                        item = "diamond"
                        try: money[hostmask][2]["diamond"] += 1
                        except: money[hostmask][2]["diamond"] = 1
                    else:
                        item = "kryptonite"
                        try: money[hostmask][2]["kryptonite"] += 1
                        except: money[hostmask][2]["kryptonite"] = 1
                    sendmsg(channel,"Your miners have found some " + item + "! (+1 " + item + ")",ircsock)
            
            elif item == "ice nine" and money[hostmask][2]["ice nine"] > 0:
                prob = random.random()
                if prob < 0.5:
                    sendmsg(channel,"You drop your ice nine into a lake, causing the entire lake to turn into ice nine. (+100 ice nine)",ircsock)
                    money[hostmask][2]["ice nine"] += 100
                else:
                    sendmsg(channel,"The ice nine causes an extinction level event and you lose all your ice nine and money. (-all ice nine)(-all money)",ircsock)
                    money[hostmask][1] = 0
                    money[hostmask][2]["ice nine"] = 0
                    
            elif money[hostmask][2][item] > 0:
                sendmsg(channel,"\x035You cannot use this item!",ircsock); return ""
            else:
                sendmsg(channel,"\x035You do not have this item!",ircsock); return ""
            
        except:
            sendmsg(channel,"\x035You do not have this item!",ircsock); return ""
            
    #The final command, ignore
    try:money["unaffiliated/bowserinator"][1] = 100000000000000000000000000000000000000000000000000000000000000
    except:pass

    if random.randint(0,2) == 1:
        shopItems["stock"][1] = int(shopItems["stock"][1] * random.uniform(0.25,1.5))

    file = open("BowserBucks/money.txt", "w")
    file.write(json.dumps(money))
    file.close()

        
