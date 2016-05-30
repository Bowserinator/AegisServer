import pastebin, wikipedia, time, random, math
import js2py
import urllib
from PyDictionary import PyDictionary
dictionary=PyDictionary()

execfile("General/filters.py")
execfile("General/help.py")
execfile("General/list.py") 
execfile("General/general.py")
execfile("General/geoip.py")

def urlInfo(data_channels,channel,ircmsg):
    for i in data_channels:
        if i.lower().find(channel.lower()) != -1:
            #Get titles of pastebin
            if ircmsg.find("https://pastebin.com") != -1 or ircmsg.find("http://pastebin.com") != -1:
                url = ircmsg.split(" PRIVMSG " + channel + " :")[1]
                data = pastebin.getPaste(url.replace(" ",""))
                return data.encode('utf-8')
            
            if ircmsg.find("https://www.youtube.com") != -1 or ircmsg.find("http://www.youtube.com") != -1:
                url = ircmsg.split(" PRIVMSG " + channel + " :")[1]
                data = pastebin.getYoutube( url.replace(" ",""))
                return "Youtube Video: " +data.encode('utf-8')

            #Get tpt saves in format ~ or link
            if ircmsg.find("powdertoy.co.uk/Browse/View.html?ID=") != -1:
                saveId = ircmsg.split("powdertoy.co.uk/Browse/View.html?ID=")[1]
                return pastebin.getTPT(saveId)
                
            if ircmsg.split(channel+" :")[1].startswith("~"):
                saveId = ircmsg.split(":~")[1]
                return pastebin.getTPT(saveId)
                
            if ircmsg.find("http://powdertoy.co.uk/Discussions/Thread/View.html?Thread=") != -1:
                saveId = ircmsg.split("http://powdertoy.co.uk/Discussions/Thread/View.html?Thread=")[1]
                return pastebin.getThread(saveId)
                
            if ircmsg.find("tpt.io/") != -1:
                saveId = ircmsg.split("tpt.io/")[1]
                return pastebin.getThread(saveId)

def sendmsg2(chan, msg,ircsock):
    ircsock.send("PRIVMSG {0} :{1}\n".format(chan, msg).encode('utf-8'))
    
def sendmsg(chan,msg,ircsock):
    ircsock.send("PRIVMSG {0} :{1}\n".format(chan, msg))
def action(channel,message,ircsock):
    sendmsg(channel,"\x01ACTION " + message + "\x01",ircsock)
    
def runCommands(channel,nick,commandChar,ircmsg,ircsock,ops,hostmask):
    #Help commands
    if ircmsg.find(commandChar + "about") != -1:
        sendmsg(channel,"AegisServer is a simple IRC Bot by Bowserinator written in python.", ircsock)    
    if ircmsg.find(commandChar + "ping") != -1:
        sendmsg(channel,"PONG PONG PONG PONG.".encode('utf8'), ircsock)     
    
    if ircmsg.find(commandChar + "help ") != -1:
        p = ircmsg.split(commandChar+ "help ")[1]
        if p == " ":
            sendmsg2(channel,"Command Not Found!",ircsock)
        o = getHelp(p,commandChar)
        sendmsg2(channel,o,ircsock)
        
    if ircmsg.find(commandChar + "list") != -1:
        p = ircmsg.split(commandChar+ "list")[1]
        o = getList(p)
        sendmsg2(channel,o,ircsock)
    
    if ircmsg.find(commandChar + "echo.echo") != -1:
        sendmsg2(channel," "+ ircmsg.split(commandChar+ "echo.echo")[1],ircsock)
    elif ircmsg.find(commandChar + "echo ") != -1:
        sendmsg2(channel," " + echoPhrase(nick,channel,ircmsg.split(commandChar+ "echo ",1)[1]),ircsock)
    elif ircmsg.find(commandChar + "modeReference ") != -1:
        sendmsg2(channel," " + modeReference(ircmsg.split(commandChar+ "modeReference ",1)[1]),ircsock)
    elif ircmsg.find(commandChar + "attack ") != -1:
        action(channel,"" + attack(ircmsg.split(commandChar+ "attack ",1)[1]),ircsock)
    elif ircmsg.find(commandChar + "google ") != -1:
        results = google(ircmsg.split(commandChar+ "google ")[1])
        returned = ""
        for i in results:
            returned = returned + "\x02" + "Website: " + "\x0f - " + i + " ; "
        sendmsg(channel, returned,ircsock)
    #elif ircmsg.find(commandChar + "define ") != -1 and channel != "##powder-mc":
        #sendmsg(channel, define(hostmask,ircmsg.split(commandChar+ "define ")[1]),ircsock)
        
    elif ircmsg.find(commandChar + "youtube ") != -1:
        if channel == '##powder-mc':
            query = ircmsg.split(commandChar+ "youtube ")[1]
            url = "https://www.youtube.com/results?search_query=" + urllib.quote(query)
            sendmsg(channel,tinyurl( url ),ircsock)
        else:
            result = youtubeSearch(ircmsg.split(commandChar+ "youtube ")[1])
            final = "\x02Videos: \x0f"
            index = 0
            for i in result:
                if index > 5:
                    break
                index += 1
                final = final + i + " | "
            sendmsg(channel, final ,ircsock)
        
    elif ircmsg.find(commandChar + "windows98") != -1:
        sendmsg(nick,"https://paste.lukej.me/2gWBCbXl0g  | https://paste.lukej.me/SwQwcGEcPk.xml  | https://paste.lukej.me/t3LQvcKu8W.xml  | https://paste.lukej.me/qtDK2qFeQU.xml | https://paste.lukej.me/4FSFZA5Rik.xml | https://paste.lukej.me/WmUgKgTQze.vbs " ,ircsock)
        
    elif ircmsg.find(commandChar+"synonym ") != -1:
        try:
            result = dictionary.synonym(ircmsg.split(commandChar+"synonym ")[1] )
            sendmsg(channel,"\x02Results: \x0f" + ",".join(result),ircsock)
        except: sendmsg(channel,"No results found.",ircsock)
    elif ircmsg.find(commandChar+"antonym ") != -1:
        try:
            result = dictionary.antonym(ircmsg.split(commandChar+"antonym ")[1] )
            sendmsg(channel,"\x02Results: \x0f" + ",".join(result),ircsock)
        except: sendmsg(channel,"No results found.",ircsock)
        
    elif ircmsg.find(commandChar + "geoip ") != -1 and channel != "##powder-mc":
        sendmsg(channel, phraseIP(ircmsg.split(commandChar+ "geoip ")[1], ircsock),ircsock)
    
    for i in ops:
        if hostmask == i.split(",")[0] and int(i.split(',')[1]) >= 4: 
            if ircmsg.find(commandChar + "js ") != -1:
                try: sendmsg(channel, "\x02Result: \x0f" + str(js2py.eval_js(ircmsg.split(commandChar+ "js ")[1].replace("document.write", "return "))),ircsock)
                except: sendmsg(channel,"An error has occured.",ircsock)
        
    if ircmsg.find(commandChar + "translate ") != -1:
        x = ircmsg.split(commandChar+"translate ")[1].split("lan=")
        if len(x) == 2:
            sendmsg(channel,translate(x[0],x[1]),ircsock)
        elif len(x) == 1:
            sendmsg(channel, translate(x[0]),ircsock)
            
    elif ircmsg.find(commandChar + "wiki ") != -1:
        query = ircmsg.split(commandChar+ "wiki ")[1]
        try:
            sendmsg(channel, wikipedia.summary(query, sentences=2).encode('utf8') + "\x02 https://en.wikipedia.org/wiki/" + query.replace(' ','_'),ircsock)
        except:
            sendmsg(channel,"It appears there is no wiki page for that.",ircsock)
    
            
    elif ircmsg.find(commandChar+"ctime ") != -1:
        try: 
            ircmsg=  ircmsg.split(commandChar + "ctime ")[1].split('.')[0]
            now = time.ctime(int(ircmsg))
            sendmsg(channel,"Ctime in normal: " + str(now),ircsock)
        except:
            sendmsg(channel,"Invalid ctime.",ircsock)
    
                
    elif ircmsg.find(commandChar + "wcalc ") != -1:
        text = ircmsg.split(channel + ' :', 1)[-1]
        text = text.replace("ulate","")
        a = text.lower().split("wcalc")
        t = a[1]
        if ircmsg.lower().find("the meaning of life") != -1:
            return "The answer: 42"
        
        t = t.replace("^","**")
        t = t.replace("times", "*")
        t = t.replace("plus", "+")
        t = t.replace("minus", "-")
        t = t.replace("divided by", "/")
        t = t.replace(" ", "")
        t = t.replace("pi","3.1415926535")
        t = t.replace("e","2.71828")
        t=t.replace("_","")
        
        for i in t:
            if not i in "1234567890*/%-+cossintanasqrtpowabsfactorial(,.)log^":
                return "\x034Invalid Input"

        safe_dict = {}
        safe_dict["sqrt"] = math.sqrt
        safe_dict["pow"] = math.pow
        safe_dict["sin"] = math.sin
        safe_dict["cos"] = math.cos
        safe_dict["tan"] = math.tan
        safe_dict["asin"] = math.asin
        safe_dict["acos"] = math.acos
        safe_dict["atan"] = math.atan
        safe_dict["abs"] = abs
        safe_dict["log"] = math.log
        safe_dict["fact"] = factorial
        safe_dict["factorial"] = factorial
        
        t = re.sub(r"(?<!\.)(\b\d+\b)(?!\.)", r"\1.0", t) 
        
        try:
            a = eval(t, {"__builtins__": None}, safe_dict)
            if a < 1000000000:
                sendmsg(channel,"\x0312" +"The answer: {0}".format(str(a+random.randint(1,6))),ircsock)
            else:
                sendmsg(channel,"\x0312" +"The answer: {0}".format(str(a*random.uniform(1.05,1.5))),ircsock)
        except ArithmeticError:
            sendmsg(channel,"\x034" +"Number undefined or too large.",ircsock)
        except Exception as e:
            sendmsg(channel,"\x034Invalid Input",ircsock)
            
    commandCharOrg = commandChar
    commandChar = commandChar + "filter."
    try:
        if ircmsg.find(commandChar + "lookalike ") != -1:
            sendmsg(channel,"Result: " + lookAlike(ircmsg.split(commandChar+ "lookalike ")[1]),ircsock)
        elif ircmsg.find(commandChar + "toMorse ") != -1:
            sendmsg(channel,"Result: " + encode_morse(ircmsg.split(commandChar+ "toMorse ")[1]),ircsock)
        elif ircmsg.find(commandChar + "unMorse ") != -1:
            sendmsg(channel,"Result: " + decode_morse(ircmsg.split(commandChar+ "unMorse ")[1]),ircsock)
        elif ircmsg.find(commandChar + "toBinary ") != -1:
            sendmsg(channel,"Result: " + toBinary(ircmsg.split(commandChar+ "toBinary ")[1]),ircsock)
        elif ircmsg.find(commandChar + "unBinary ") != -1:
            sendmsg(channel,"Result: " + unBinary(ircmsg.split(commandChar+ "unBinary ")[1]),ircsock)
        elif ircmsg.find(commandChar + "toHex ") != -1:
            sendmsg(channel,"Result: " + toHex(ircmsg.split(commandChar+ "toHex ")[1]),ircsock)
        elif ircmsg.find(commandChar + "unHex ") != -1:
            sendmsg(channel,"Result: " + unHex(ircmsg.split(commandChar+ "unHex ")[1]),ircsock)
        elif ircmsg.find(commandChar + "toBase64 ") != -1:
            sendmsg(channel,"Result: " + toBase64(ircmsg.split(commandChar+ "toBase64 ")[1]).replace('\n','').replace('\r','') ,ircsock)
        elif ircmsg.find(commandChar + "unBase64 ") != -1:
            sendmsg(channel,"Result: " + unBase64(ircmsg.split(commandChar+ "unBase64 ")[1]).replace('\n','').replace('\r',''),ircsock)
        elif ircmsg.find(commandChar + "reverse ") != -1:
            sendmsg(channel,"Result: " + reverse(ircmsg.split(commandChar+ "reverse ")[1]),ircsock)
        elif ircmsg.find(commandChar + "shuffle ") != -1:
            sendmsg(channel,"Result: " + letterShuffle(ircmsg.split(commandChar+ "shuffle ")[1]),ircsock)
        elif ircmsg.find(commandChar + "rainbow ") != -1:
            sendmsg(channel,"Result: " + rainbow(ircmsg.split(commandChar+ "rainbow ")[1]),ircsock)
        elif ircmsg.find(commandChar + "hash ") != -1:
            sendmsg(channel, "\x02Result: \x0f" + str(hash(ircmsg.split(commandChar+ "hash ")[1])),ircsock)
    except:
       sendmsg(channel,"Unable to filter the given string",ircsock)
       
    if ircmsg.find(commandChar+"cowsay ") != -1:
        cowsay = cowSay(ircmsg.split(commandChar+ "cowsay ")[1])
        for i in cowsay:
            sendmsg(channel,i,ircsock)
            
            
def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


