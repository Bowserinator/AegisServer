import urllib, requests

import sys
import urllib, urllib2
import re

def tinyurl(url):
    tiny = "http://tinyurl.com/api-create.php?url=%s" %(url)
    page = urllib2.urlopen(tiny)
    tiny = page.read()
    page.close()
    return tiny
    
def gethostmask(nick,irc):
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
        
def phraseIP(ip,ircsock):
    host = gethostmask(ip,ircsock)
    if  host != False:
        #It's an user, test hostmask for ip
        try: 
            result = getLoc(host.split('@',1)[1])
    
            returned = "\x02City: \x0f" + result["city"] + "\x02 Region: \x0f" + result["region_name"]
            returned = returned + "\x02 Country: \x0f" + result["country"]
            returned = returned + "\x02 Timezone: \x0f" + result["time_zone"]
            returned = returned + "\x02 Ip: \x0f" + result["ip"]
            returned = returned + "\x02 Zip: \x0f" + result["zip"]
            returned = returned + "\x02 Google maps: \x0f" + result["google_url"]
            return returned
        except:
            return "Hostmask found, could not determine ip address."
    
    result = getLoc(ip)
    
    returned = "\x02City: \x0f" + result["city"] + "\x02 Region: \x0f" + result["region_name"]
    returned = returned + "\x02 Country: \x0f" + result["country"]
    returned = returned + "\x02 Timezone: \x0f" + result["time_zone"]
    returned = returned + "\x02 Ip: \x0f" + result["ip"]
    returned = returned + "\x02 Zip: \x0f" + result["zip"]
    returned = returned + "\x02 Google maps: \x0f" + result["google_url"]
    return returned


"""Bowserlnator [Bowserlnator!4072de72@gateway/web/freenode/ip.64.114.222.114] * h114.222.114.64.cablerocket.net/64.114.222.114 
Bad: iovoid [iovoid!~iovoid@unaffiliated/iovoid] * iovoid """

    
import requests

FREEGEOPIP_URL = 'http://freegeoip.net/json/'

def getLoc(ip):
    ip = ip.replace(" ","",1)
    url = '{}/{}'.format(FREEGEOPIP_URL, ip)
    response = requests.get(url)
    json = response.json()
    
    #The json as city, region code, region name, ip, tmezone, longitude, latatude, country name and zip code
    #For longitude/latatuide use google maps
    final  = ""
    returned = {
        "city":json["city"],
        "region_name":json["region_name"],
        "ip":json["ip"],
        "time_zone":json["time_zone"],
        "long":json["longitude"],
        "lat":json["latitude"],
        "country":json["country_name"],
        "zip":json["zip_code"],
        "google_url":tinyurl("https://www.google.com/maps/place/"+ str(round(float(json["longitude"]))) + ',' +  str(round(float(json["latitude"]))) )
        }
    return returned
        
