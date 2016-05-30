import urllib2,re

def define(user,x):
    try:
        x = x.replace("/","").replace("&","").replace("\\","").replace("#","").lower()

        if True:
            if x.lower() == "bowserinator":
                return "Supreme Emperor of the Bowser Empire."

        srch=str(x)
        x=urllib2.urlopen("http://dictionary.reference.com/browse/"+srch+"?s=t")
        x=x.read()
        items=re.findall('<meta name="description" content="'+".*$",x,re.MULTILINE)
        for x in items:
            y=x.replace('<meta name="description" content="','')
            z=y.replace(' See more."/>','')
            m=re.findall('at Dictionary.com, a free online dictionary with pronunciation,              synonyms and translation. Look it up now! "/>',z)
            if m==[]:
                if z.startswith("Get your reference question answered by Ask.com"):
                    return "Word not found! :("
                else:
                    z = z.split("<meta property=\"og:", 1)[0]
                    if z.find("The world's most popular dictionary and thesaurus with definitions") == -1 and z.find("definition at Dictionary.com") == -1:
                        return z.replace('/>','')
                    else:
                        return "Word not found :("
        else:
                return "Word not found! :("
    except:
        return "Word not found! :("


import requests
import json
import re
from HTMLParser import HTMLParser


"""class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        returned = []
        if tag == "a":
           for name, value in attrs:
               if name == "href" and value.find("http") != -1 and value.find("microsoft") == -1 and value.find("msn") == -1:
                    urls.append(value)"""


def getUrls(html):
    import re
    urls = re.findall(r'href=[\'"]?([^\'" >]+)', html)
    urls2 = []
    found = 0
    for u in urls:
        if u.find("http")  != -1 and u.find("microsoft") == -1 and u.find("msn") == -1 and u.find("//") != -1:
            found2 = False
            found2limit = 0
            for x in urls:
                if x.find(u) != -1:
                    found2 = True
                else:
                    found2limit += 1
                if found2limit > 5:
                    break
            if found2 == False:
                urls2.append(u)
        if found > 5:
            break
    return urls2
    
def google(query):
    html = requests.get("http://www.bing.com/search?q=" + query)
    urls = getUrls(html.text)
    return urls[:3]
    
import requests,re, urllib
import urllib2

def translate(to_translate, to_langage="auto", langage="auto"):
	to_translate = to_translate.replace("/","").replace("%","").replace("$","")
	'''Return the translation using google translate
	you must shortcut the langage you define (French = fr, English = en, Spanish = es, etc...)
	if you don't define anything it will detect it or use english by default
	Example:
	print(translate("salut tu vas bien?", "en"))
	hello you alright?'''
	agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
	before_trans = 'class="t0">'
	link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, to_translate.replace(" ", "+"))
	request = urllib2.Request(link, headers=agents)
	page = urllib2.urlopen(request).read()
	result = page[page.find(before_trans)+len(before_trans):]
	result = result.split("<")[0]
	
	result = result.replace("&quot;",'"').replace("&#39;","'").replace("&lt","<").replace("&gt;",">")
	return "Result: " +  result

def attack(user):
    #ACTION test
    attacks = [
        "drops a cool black planet on " + user,
        "eats " + user + " for breakfast.",
        "tackles " + user + " and annihilates " + user + " completely, ending " + user +"'s thoughts of revenge. ",
        "smashes " + user + "'s face through 4 layers of glass.",
        "whacks " + user + " into space.",
        "breathes out a stream of white hot fire, melting " + user + "'s face instantly.",
        "takes out a sharpness V sword and slices " + user + " in half.",
        "detonates an antimatter missile onto " + user + ".",
        "fires the B.E. Space Laser, shooting a beam of death towards " + user + ".",
        "takes the brush and drops some SING near where " + user + " was standing.",
        "borrows a banhammer and smashes it on " + user + "'s skull.",
        "beats " + user + " in a game of chess, causing " + user + " to die of shame.",
        "lands a TARDIS on top of " + user + ".",
        "forces " + user + " to listen to Justin Bieber, causing their eardrums to explode.",
        "shoves " + user + " into a vat of sodium hydroxide.",
        "types /kill @p[Name=" + user + "]",
        "types !set type " + user + " none",
        "straps " + user + " onto a rocket heading towards the sun.",
        "drops an anvil onto " + user + ".",
        "introduces " + user + " to geometry dash, causing " + user + " to die of fustration."
    ]
    
    return  random.choice(attacks)
    
def youtubeSearch(query):
    import urllib
    import urllib2
    from bs4 import BeautifulSoup

    textToSearch = query
    query = urllib.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    returned = []
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        returned.append('https://www.youtube.com' + vid['href'])
    return returned

def modeReference(mode):
    returned = "\x02User Modes: \x0f"
    
    if mode == "D":
        returned = returned + "This prevents you from receiving channel messages. You will probably not want to set this in most cases. (It is used by services.)"
    elif mode == "g":
        returned = returned + "You can set this umode to prevent you from receiving private messages from anyone not on a session-defined whitelist. "
    elif mode == "i":
        returned = returned + "This prevents you from appearing in global WHO/WHOIS by normal users, and hides which channels you are on."
    elif mode == "q":
        returned = returned + "This user mode prevents you from being forwarded to another channel because of channel mode +f (see below) or by a ban (see +b below). Instead of being forwarded to another channel, you'll be given a message as to why you could not join."
    elif mode == "R":
        returned = returned + "This user mode prevents users who are not identified to NickServ from sending you private messages."
    elif mode == "w":
        returned = returned + "This user mode lets you see the wallops announcement system. Important network messages will be sent out via global notices; this is only for non-critical announcements and comments which may be of interest."
    elif mode == "z":
        returned = returned + "You will have this user mode if you connect to freenode with SSL"
        
    returned = returned + " \x02Channel Modes: \x0f"
    if mode == "b":
        returned = returned + "Bans user. /mode #channel +b lists bans. Extbans: /ban $a:account - Bans all accounts identified to account. /ban $j:channel - Bans all users banned in channel from current channel. $r - Bans realname. $x - String parm against full name. $z - bans all SSL. /mode #channel +b [banmask]$#redirectchannel"
    elif mode == "c":
        returned = returned + "Filters out formatting such as color and bold words."
    elif mode == "e":
        returned = returned + "Exempts person from bans, overrides +q and +b bans"
    elif mode == "f":
        returned = returned + "/mode #channel1 +if #channel2 Forwards user to channel2 if not invited"
    elif mode == "F":
        returned = returned + "This mode can be set by any channel operator to allow operators in other channels to set bans to forward clients to their channel, without requiring ops in it."
    elif mode == "g":
        returned = returned + "Allow anyone to invite."
    elif mode == "i":
        returned = returned + "Makes the channel invite only."
    elif mode == "I":
        returned = returned + "Exempts client (Same format as bans) from having to be invited to join."
    elif mode == "j":
        returned = returned + "/mode #channel n:t  Only allows n users to join every t seconds. Invited users can join regardless of this, but are still counted."
    elif mode == "k":
        returned = returned + "Sets a password to join the channel, to join type /join #channel <password>"
    elif mode == "l":
        returned = returned + "Sets limit to how many users can join channel."
    elif mode == "L":
        returned = returned + "Set only by freenode staff, allows a channel to have longer than normal ban, exempt, and invite exemption lists."
    elif mode == "m":
        returned = returned + "When a channel is set +m, only users who are opped or voiced on the channel can send to it. This mode does not prevent users without voice or op from changing nicks."
    elif mode == "n":
        returned = returned + "Users outside the channel may not send messages to it."
    elif mode == "p":
        returned = returned + "When set, the KNOCK command cannot be used on the channel to request an invite, and users will not be shown the channel in whois replies unless they are on it. Unlike on some ircds, +p and +s can be set together."
    elif mode == "P":
        returned = returned + "Only set by freenode staff, makes the channel stay even if there are no users in it."
    elif mode == "q":
        returned = returned + "This mode prevents users who are not identified to NickServ from joining the channel. Users will receive a server notice explaining this if they try to join. /mode #channel +q $~a can be used to prevent unregistered users from speaking in channel while allowing them to join."
    elif mode == "Q":
        returned = returned + "Users will not be able to be forwarded (see +f above) to a channel with +Q."
    elif mode == "r":
        returned = returned + "This mode prevents users who are not identified to NickServ from joining the channel. "
    elif mode == "s":
        returned = returned + "Only users connected via SSL may join the channel while this mode is set. Users already in the channel are not affected. "
    elif mode == "t":
        returned = returned + "When +t is set, only channel operators may modify the topic of the channel. This mode is recommended in larger, more public channels to protect the integrity of the topic."
    elif mode == "z":
        returned = returned + "When +z is set, the effects of +b, +q, and +m are relaxed. For each message, if that message would normally be blocked by one of these modes, it is instead sent to all the users who are currently set +o (channel operator). This is intended for use in moderated debates."
    return returned