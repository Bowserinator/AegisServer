execfile("MC/crafting.py")
execfile("MC/enchant.py")
execfile("MC/dynmap.py")
execfile("MC/wikiscraper.py")
execfile("MC/brewing.py")
import json
from mcstatus import MinecraftServer

import urllib, requests
import urllib, urllib2

brewing = brew()
server = MinecraftServer.lookup("mc.starcatcher.us")

def tinyurl(url):
    tiny = "http://tinyurl.com/api-create.php?url=%s" %(url)
    page = urllib2.urlopen(tiny)
    tiny = page.read()
    page.close()
    return tiny

recipies_raw = open("MC/recipies.txt", "r").read()
recipies = json.loads(recipies_raw)

def sendmsg(chan, msg,ircsock):
    ircsock.send("PRIVMSG {0} :{1}\n".format(chan, msg))#
    
def runCommands(ircmsg,commandChar,ircsock,channel,hostmask,nick):
    message = ircmsg
    user = nick
    
    usersF = open('MC/data.txt', 'r').read()
    if usersF == "":
        users = {}
    else:
        users = json.loads(usersF)
    
    if commandChar+"mcstatus" in message.lower():
        status = server.status()
        sendmsg(channel, "The server has {0} players and replied in {1} ms".format(status.players.online, status.latency),ircsock)
        
    elif(message.lower().find(commandChar + "mcuserstats ") != -1):
        try:
            query =  message.split(commandChar + "mcuserstats ")[1].lower().encode('utf8')
            for i in users:
                if query in i:
                    query = i; break
        
            returned = "\x02Deaths: \x0f" + str(users[query]["deaths"])
            returned = returned + " \x02Logins: \x0f" + str(users[query]["logins"])
            returned = returned + " \x02Quits: \x0f" + str(users[query]["quits"])
            sendmsg(channel, returned,ircsock)
        except:
            sendmsg(channel,"Could not get data for that user.",ircsock)
    
    elif(message.lower().find(commandChar + "enchant possible ") != -1):
        try:
            x = message.split(commandChar+"enchant possible ")[1]
            y = x.split(",")
            returned = ""
            for e in getPossibleEnchants(y[0],int(y[1]),int(y[2])): #Possible enchants at slot
                returned = returned + e.name + " " + str(e.level) + " | "
            sendmsg(channel,"\x02Possible enchants: \x0f" + returned,ircsock)
        except Exception as e:
            sendmsg(channel, "\x034" +"Invalid Input, use format " + commandChar + "enchant possible [item],[slot],[book shelves] .",ircsock)
            
    elif(message.lower().find(commandChar + "enchant prob ") != -1):
        try:
            x = message.split(commandChar+"enchant prob ")[1]
            y = x.split(",")
            prob = getProbEnchant(y[0],y[1],int(y[2]),int(y[3]))
            sendmsg(channel,
            str(prob * 100) + "% chance of getting " + y[0] + " on slot " + y[2] + " with " + y[3] + " books.",
            ircsock)
        except Exception as e:
            sendmsg(channel, "\x034" +"Invalid Input, use format " + commandChar + "enchant prob [enchant],[item],[slot],[books]  .",ircsock)

    elif(message.lower().find(commandChar + "enchant best slot ") != -1):
        try:
            x = message.split(commandChar+"enchant best slot ")[-1]
            y = x.split(",")
            slot = getBestSlot(y[0],y[1],int(y[2]))
            slots = ["Top","Middle","Bottom"]
            sendmsg(channel, slots[slot[0]-1] + " is the best slot with " + str(slot[1]*100) + "% chance.",ircsock)
        except Exception as e:
            sendmsg(channel,"\x034" +"Invalid Input, use format " + commandChar + "enchant best slot [enchant],[item],[books] .",ircsock)

    elif(message.lower().find(commandChar + "enchant best ") != -1):
        try:
            x = message.split(commandChar+"enchant best ")[-1]
            y = x.split(",")
            slot = getBestLevel(y[0],y[1])
            
            slots = ["Top","Middle","Bottom"]
            sendmsg(channel, slots[slot[1]-1] + " slot with " + str(slot[0]) + " books yeilds " + str(slot[2]*100) + "% chance.",ircsock)
        except Exception as e:
            sendmsg(channel, "\x034" +"Invalid Input, use format " + commandChar + "enchant best [enchant],[item] .",ircsock)
    
    elif (message.lower().find(commandChar + "enchant") != -1):
        sendmsg(channel,"enchant best [enchant],[item], enchant best slot [enchant],[item],[books], enchant prob [enchant],[item],[slot],[books], enchant possible [item],[slot],[book shelves]",ircsock)
        
    elif(message.lower().find(commandChar + "craftcalc ") != -1):
        try:
            x = message.split(commandChar+"craftcalc ")[-1]
            y = x.split(",")
            y[0] = y[0].lower()
            slot = RecipieCalc(y[0],recipies, int(y[1]))

            sendmsg(channel,"\x02Resources: \x0f" + slot,ircsock)
        except Exception as e:
            sendmsg(channel, "\x034" +"Invalid Input, use format " + commandChar + "craftcalc [item],[amount] .",ircsock)

    elif(message.lower().find(commandChar + "toolstats ") != -1):
        try:
            x = message.split(commandChar+"toolstats ")[-1]
            y = x.split("|")
            result = getToolStats(y[0],y[1])
            for x in result:
                sendmsg(channel,x,ircsock)
            
        except Exception as e:
            sendmsg(channel, "\x034" +"Invalid Input, use format " + commandChar + "toolstats [tool]|[enchants seperated with ,] .",ircsock)
    
    elif ircmsg.lower().find(commandChar + "craft ") != -1:
        try:
            a = message.split(commandChar + "craft ", 1)[1]
            r = getRecipieStr(a,recipies)
            sendmsg(channel, r[0],ircsock)
            sendmsg(channel, r[1],ircsock)
            sendmsg(channel, r[2],ircsock)
        except Exception as e:
            sendmsg(channel, "\x034" +"Recipe not found, try !search/" + commandChar + "search.",ircsock)
            
    elif ircmsg.lower().find(commandChar + "search ") != -1:
        try:
            a = message.split(commandChar + "search ", 1)[1]
            r = searchRecipie(a,recipies)
            if r.replace(" ","") == "":
                sendmsg(channel,"No matches found.",ircsock)
            sendmsg(channel, r,ircsock)
        except Exception as e:
            sendmsg(channel, "No matches found..",ircsock)
            
    # elif(message.lower().find(commandChar + "getnwc") != -1):
    #     try:
    #         x = message.split(channel + ' :', 1)[-1].split(" ")
    #         x = x[x.index(commandChar + "getnwc") + 1].split(",")
    #         if(len(x) == 3):
    #             sendmsg(channel, str(float(x[0]) / 8) + "," + str(float(x[1])) + "," + str(float(x[2]) / 8),ircsock)
    #         elif(len(x) == 2):
    #             sendmsg(channel, str(float(x[0]) / 8) + "," + str(float(x[1]) / 8),ircsock)
    #     except:
    #         sendmsg(channel,"\x034" +"Invalid Input Found.",ircsock)
    
    # elif message.lower().find(commandChar + "getmap p") != -1:  # Gets map at coords
    #     message = message.replace("layer","",1)
    #     gen = message.split(channel + ' :', 1)[-1]
    #     x = gen.split(commandChar + 'getmap p ', 1)[1]
    #     a = getPlayerData(x)
        
    #     if getPlayerData(x) != "":
    #         if a.world == "world_nether":
    #             sendmsg(channel, tinyurl("http://dynmap.starcatcher.us/?worldname=world_nether&mapname=flat&zoom=6&x="+str(a.x)+"&y=64&z="+str(a.z)) , ircsock)
    #         elif a.world == "world_the_end":
    #             sendmsg(channel, tinyurl("http://dynmap.starcatcher.us/?worldname=world_the_end&mapname=flat&zoom=6&x="+str(a.x)+"&y=64&z="+str(a.y)), ircsock)
    #         else:
    #             sendmsg(channel, tinyurl("http://dynmap.starcatcher.us/?worldname=world&mapname=flat&zoom=6&x="+str(a.x)+"&y=64&z="+str(a.z)), ircsock)
    #     else:
    #         sendmsg(channel, "Player not found", ircsock)
    
    # elif message.lower().find(commandChar + "get_time") != -1:  
    #     sendmsg(channel, "The current MC time is " + getTime(), ircsock)
    # elif message.lower().find(commandChar + "get_server_time") != -1:  
    #     sendmsg(channel, "" + getTimeTick(), ircsock)
    # elif message.lower().find(commandChar + "get_weather") != -1:  
    #     sendmsg(channel, "" + getWeather() + " (THIS COMMAND NO WORK)",ircsock)
        
    # elif message.lower().find(commandChar + "get_player") != -1:
    #     temp = message.split(commandChar + 'get_player ', 1)[1]
    #     play = getPlayerData(temp)

    #     if play != "":
    #         if play.world == "world_nether":
    #             sendmsg(channel, temp + " is in the nether at " + str(int(play.x)) + "," + str(int(play.y)) + "," + str(int(play.z)) + " and has " + str(int(play.health)) + " health and " + str(int(play.armor)) + " armor.", ircsock)
    #         elif play.world == "world_the_end":
    #             sendmsg(channel, temp + " is in the end at " + str(int(play.x)) + "," + str(int(play.y)) + "," + str(int(play.z))+ " and has " + str(int(play.health)) + " health and " + str(int(play.armor)) + " armor.", ircsock)
    #         else:
    #             sendmsg(channel, temp + " is at " + str(int(play.x)) + "," + str(int(play.y)) + "," + str(int(play.z))+ " and has " + str(int(play.health)) + " health and " + str(int(play.armor)) + " armor.", ircsock)
    #     if play == "":
    #         sendmsg(channel, "Player not found. (Possibly hidden?)",ircsock)
            
    
    # elif message.lower().find(commandChar + "getmap") != -1:  # Gets map at coords
    #     try:
    #         gen = message.split(channel + ' :', 1)[-1]
    #         x = gen.split(commandChar + 'getmap', 1)[-1]
            
    #         if(x.lower().find("nether") != -1):
    #             x = x.replace("nether","").replace(" ","").split(",")
    #             sendmsg(channel, "\x0312" + tinyurl("http://dynmap.starcatcher.us/?worldname=world_nether&mapname=flat&zoom=6&x="+x[0]+"&y=64&z="+x[1]),ircsock)
    #         elif(x.lower().find("end") != -1):
    #             x = x.replace("end","").replace(" ","").split(",")
    #             sendmsg(channel, "\x0312" +tinyurl("http://dynmap.starcatcher.us/?worldname=world_the_end&mapname=flat&zoom=6&x="+x[0]+"&y=64&z="+x[1]),ircsock)
    #         else:
    #             x = x.replace(" ","").split(",")
    #             sendmsg(channel, "\x0312" +tinyurl("http://dynmap.starcatcher.us/?worldname=world&mapname=flat&zoom=6&x="+x[0]+"&y=64&z="+x[1]),ircsock)
                        
    #     except:
    #         sendmsg(channel, "\x034" +"Invalid input found.",ircsock)

    elif message.lower().find(commandChar + "mcwiki ") != -1:
        try:
            gen = message.split(channel + ' :', 1)[-1]
            a = gen.split(commandChar + "mcwiki ", 1)[-1].replace(" ", "+")
            
            sendmsg(channel, "\x02Url: \x0f\x0312" + tinyurl("https://minecraft.gamepedia.com/index.php?search=" + a + "&title=Special%3ASearch&go=Go"),ircsock)
        except:
            sendmsg(channel,"\x034" +"Invalid input found.",ircsock)
    
    elif message.lower().find(commandChar + "brew ") != -1:
        try:
            query = message.lower().split(commandChar+"brew ")[1]
            result = brewing.brew(query)
            if result["possible"]:
                sendmsg(channel,"\x02Steps: \x0f" + ",".join(result["steps"]) + " \x02Time: \x0f" + str(result["time"]) + " seconds.",ircsock)
            else:
                sendmsg(channel,"This potion is impossible to brew in vanilla Minecraft",ircsock)
        except:
            sendmsg(channel,"\x034" +"Invalid input found.",ircsock)


import json

def phraseText(ircmsg,commandChar,botnick,user,hostmask,channel): #RUN ONLY IF USER IF POTATORELAY
    if user == "potatorelay":
        usersF = open('MC/data.txt', 'r').read()
        if usersF == "":
            users = {}
        else:
            users = json.loads(usersF)
            
        if "disconnected]" in ircmsg or "connected]" in ircmsg:
            minecraftNick = ircmsg.split(" :",1)[1].split(" ")[0].replace("[","",1).replace("14","",1).lower().encode('ascii').replace("0003","").decode("UTF-8")
            print(minecraftNick)
            
            if userExist(minecraftNick,users) == True:
                if "disconnected]" in ircmsg:
                    users[minecraftNick]["quits"] += 1
                elif "connected]" in ircmsg:
                    users[minecraftNick]["logins"] += 1
            else:
                if userExist(minecraftNick,users) == False:
                    users[minecraftNick.lower()] = {
                        "logins":0,
                        "quits":0,
                        "deaths":0
                    }
    
        for key in users:
            if checkDeath(key.lower(),ircmsg.split(" :",1)[1]):
                users[key.lower()]["deaths"] += 1
            
        file = open("MC/data.txt", "w")
        file.write(json.dumps(users, sort_keys=True, indent=4, separators=(',', ': ')))
        file.close()

def userExist(name,users):
    for key in users:
        if key.lower() == name.lower():
            return True
    return False
    
def checkDeath(username,ircmsg):
    if ircmsg.lower().find(username.lower()[4:]) != -1 and ircmsg.find("<") == -1:
        for i in ["drowned","slain","shot","died","pricked","kinetic","blew","blown",
        "hit the ground","fell off","doomed to fall","shot off some vines","shot off a ladder","blown from",
        "squashed by","went up in flames","burned to death","walked into a fire","burnt to a crisp",
        "tried to swim in lava","struck by lightning","got finished off by","was fireballed by",
        "by magic","using magic","starved to death","suffocated in a wall","fell out of the world",
        "withered away","was pummeled by"]:
            if i in ircmsg.lower():
                return True