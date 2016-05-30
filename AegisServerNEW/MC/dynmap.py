import urllib
import json
import math

def getTimeTick():
    link = "http://dynmap.starcatcher.us/up/world/world/"
    f = urllib.urlopen(link)
    data = f.read() #Gets the data
    decoded = json.loads(data)
    time = str(decoded["servertime"])
    return "The current server time is " + time
    
def getWeather():
    link = "http://dynmap.starcatcher.us/up/world/world/"
    f = urllib.urlopen(link)
    data = f.read() #Gets the data
    decoded = json.loads(data)
    
    rain = str(decoded["hasStorm"])
    thunder = str(decoded["isThundering"])
    
    if thunder == "true":
        return "There is currently a thunderstorm."
    elif rain == "true":
        return "It is currently raining."
    else:
        return "It is currently clear."

def getTime():
    link = "http://dynmap.starcatcher.us/up/world/world/"
    f = urllib.urlopen(link)
    data = f.read() #Gets the data
    decoded = json.loads(data)
    time = int(decoded["servertime"])
    str_time = ""
    
    hours = time / 1000.0

    hours += 6
    if hours > 24:
        hours -= 24
        
    mins = (hours - math.floor(hours)) * 60
    hours = int(hours)
    hours = str(hours)

    if mins >= 10:
        str_time = hours + ":" + str(int(mins))
    if mins < 10:
        str_time = hours + ":0" + str(int(mins))
        
    if time >= 12541 and time <= 23458:
        str_time = str_time + " (You can sleep)"
    elif decoded["isThundering"] == "true":
        str_time = str_time + " (You can sleep)"
    return str_time
    

def getPlayers():
    link = "http://dynmap.starcatcher.us/up/world/world/"
    f = urllib.urlopen(link)
    data = f.read() #Gets the data
    
    decoded = json.loads(data)
    players = decoded["players"]
    return players

def getPlayerData(name):
    p = getPlayers()
    
    for i in p:
        if i["name"].lower() == name.lower():
            return Player(i)
    return ""

class Player:
    def __init__(self,data):
        self.name = data["account"]
        self.x = data["x"]
        self.y = data["y"]
        self.z = data["z"]
        self.health = data["health"]
        self.armor = data["armor"]
        self.world = data["world"]

