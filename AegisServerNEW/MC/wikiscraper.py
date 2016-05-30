import requests, re
from bs4 import BeautifulSoup

def getWiki(query):
    try:
        a = requests.get("http://minecraft.gamepedia.com/"+query.replace(" ","_")).text.split('<ul class="gallery mw-gallery-traditional">')[0]
        b = re.findall("<p>(.*)</p>",a)

        result1 = blockInfo(b)
        if result1:
            return result1
        
        result2 = mobInfo(b)
        if result2 != None:
            return result2
    except:
        pass

def mobInfo(urlData):
    health = urlData[0].split('<span class="nowrap">')[1].split(" ")[0]
    spawn = urlData[1]
    xp = urlData[4]
    
    returned = "\x02Health: \x0f" + health
    returned = returned + "\x02 Spawn: \x0f" + spawn
    returned = returned + "\x02 XP: \x0f" + xp
    return returned
    
def blockInfo(urlData):
    #Gets information on blocks only!
    block = False
    tools = ["shear","pickaxe","sword","shovel","spade","tool","axe","hoe"]
    tool = ""
    
    for i in tools:
        if urlData[6].lower().find(i) != -1:
            block = True; 
            tool = i
            break
    
    if block == False:
        return False
        
    #Return the block type, physics, transparency, luminance, blast resistance, harndess, tool
    #renwable, stackable, flammable, [ignore], drops, data, name
    returned = "\x02Block type: \x0f" + urlData[0]
    returned = returned + "\x02 Physics: \x0f" + urlData[1]
    returned = returned + "\x02 Transparency: \x0f" + urlData[2]
    returned = returned + "\x02 Luminance: \x0f" + urlData[3]
    returned = returned + "\x02 Blast Res: \x0f" + urlData[4]
    returned = returned + "\x02 Hardness: \x0f" + urlData[5]
    returned = returned + "\x02 Tool: \x0f" + tool.title()
    returned = returned + "\x02 Renewable: \x0f" + urlData[7]
    returned = returned + "\x02 Stackable: \x0f" + urlData[8]
    returned = returned + "\x02 Flammable: \x0f" + urlData[9]
    returned = returned + "\x02 Drops: \x0f" + urlData[11]
    returned = returned + "\x02 Name: \x0f" + urlData[13]
    
    return returned

a = getWiki("creeper")
#print(a)