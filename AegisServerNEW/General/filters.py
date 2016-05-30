import random, re, base64

letter_to_morse = {
    "a" : ".-",     "b" : "-...",     "c" : "-.-.",
    "d" : "-..",    "e" : ".",        "f" : "..-.",
    "g" : "--.",    "h" : "....",     "i" : "..",
    "j" : ".---",   "k" : "-.-",      "l" : ".-..",
    "m" : "--",     "n" : "-.",       "o" : "---",
    "p" : ".--.",   "q" : "--.-",     "r" : ".-.",
    "s" : "...",    "t" : "-",        "u" : "..-",
    "v" : "...-",   "w" : ".--",      "x" : "-..-",
    "y" : "-.--",   "z" : "--..",     " " : "/",
    "?": "", "!": "", "#":"","$":"","%":"","^":""
}

morse_to_letter = {morse: letter for letter, morse in letter_to_morse.items()}

charLookAlike = {"0":"O","1":"I","2":"Z","3":"8","4":"H","5":"S","6":"G","7":"Z","8":"3","9":"6",
"b":"d","c":"s","d":"b","e":"c","f":"t","g":"q","h":"n","i":"j","j":"i",
"k":"h","l":"1","m":"n","n":"m","o":"c","p":"q","q":"p",
"r":"n","s":"c","t":"f","u":"v","v":"w","w":"vv","x":"X","z":"Z",
"A":"&","B":"8","C":"O","D":"0","E":"F","F":"E","G":"6","H":"4","I":"l",
"J":"U","K":"H","L":"J","M":"N","N":"M","O":"0","P":"R","R":"P",
"S":"5","T":"t","U":"V","V":"U","W":"VV","X":"x","Y":"V","Z":"2",
"!":"1","@":"&","#":"H","$":"S","^":"/\\","&":"8","(":"{",")":"}","-":":",":":"-",
"{":"(","}":")","\"":"'","'":"\"","/":"\\","\\":"/","`":"'","~":"-",
}

def lookAlike(text):
    returned = ''
    for i in text:
        try:
            if random.random() < 0.5:
                returned = returned + charLookAlike[i]
            else:
                returned = returned + i
        except:
            returned = returned + i
    return returned


def decode_morse(morse_code):
    return ''.join(morse_to_letter[code] for code in morse_code.split())

def encode_morse(text):
    text = text.lower()
    return ' '.join(letter_to_morse[letter] for letter in text)
    
def reverse(text):
    return text[::-1]
    
def toBinary(text):
    returned = ' '.join(format(ord(x), 'b') for x in text)
    if len(returned) > 2000:
        return "\x035Error: String too long"
    return returned

def unBinary(text):
    returned = ""
    for i in range(0,len(text)/8):
        returned = returned + chr(int(text[i*8:i*8+8], base=2)) 
    return returned

def toHex(s):
    return s.encode("hex")
    
def unHex(s):
    return s.decode("hex")
    
def letterShuffle(text):
    l = list(text)
    random.shuffle(l)
    return ''.join(l)
    
def rainbow(text):
    returned = "\x02"
    colors = ["\x031","\x032","\x033","\x034","\x035","\x036","\x037","\x038","\x039","\x0310","\x0311","\x0312"]
    for i in text:
        returned = returned+colors[text.index(i) % len(colors)] + i
    return returned
    
def cowSay(text,cowType="normal"):
    if cowType == "normal":
        return [
"<" + text + ">",
"----------------------------------------",
"        \   ^__^ ",
"         \  (oo)\_______",
"            (__)\       )\/",
"               ||----w | ",
"               ||     ||"]
    elif cowType == "dead":
        return [
"<" + text + ">",
"----------------------------------------",
"        \   ^__^ ",
"         \  (XX)\_______",
"            (__)\       )\/",
"               ||----w | ",
"               ||     ||"]



def echoPhrase(nick,channel,text):
    text = text.lower()
    text = text.replace("[b]","\x02")
    text = text.replace("[i]","\x09")
    text = text.replace("[r]","\x0f")
    text = text.replace("[u]","\x15")
    text = text.replace("[nick]",nick)
    text = text.replace("[channel]",channel)
    
    #f*ck with 42 uses, sh*t with 33 uses, b*tch with 21 uses, d*mn with 13 uses, f*g with 4 uses 
    
    text = text.replace("fuck", "f*ck") ;
    text = text.replace("bitch", "b*tch");
    text = text.replace("shit", "sh*t");
    text = text.replace("damn", "d*mn");
    text = text.replace("fug", "f*g");
    text = text.replace("nigga", "n*gga");
    text = text.replace("dick", "d*ck");
    text = text.replace("asshole", "a**hole");

    text = text.replace("[white]", "\x030");
    text = text.replace("[black]", "\x031");
    text = text.replace("[dark blue]", "\x032");
    text = text.replace("[dark green]", "\x033");
    text = text.replace("[red]", "\x034 ");
    text = text.replace("[dark red]", "\x035");
    text = text.replace("[dark violet]", "\x036");
    text = text.replace("[orange]", "\x037");
    text = text.replace("[yellow]", "\x038");
    text = text.replace("[light green]", "\x039");
    text = text.replace("[cyan]", "\x0310");
    text = text.replace("[light cyan]", "\x0311");
    text = text.replace("[blue]", "\x0312");
    text = text.replace("[violet]", "\x0313");
    text = text.replace("[dark gray]", "\x0314");
    text = text.replace("[light gray]", "\x0315")
    return text
    
def toBase64(string):
    return base64.b64encode(string)
    
    
def unBase64(string):
    return base64.b64decode(string)