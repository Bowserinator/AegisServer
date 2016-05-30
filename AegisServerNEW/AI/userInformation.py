import re  
knownUserInformation = {

    "bowserinator":{
            "timeShift":-5, #Shift from UK time
            "ip":"[Not telling]",
            "real_name":"The Emperor King Lord Noble Titan Godly Bowserinator the eternal all seeing overlord, ruler of the universe.",
            "age":1000,
            "brirthday":"[Not telling]",
            "residence":"Bowser Empire" 
        },

        
        
    "bowserbot":{
            "timeShift":0, #Shift from UK time
            "ip":"234.112.197.104.bc.googleusercontent.com",
            "real_name":"BowserBot",
            "age":10000,
            "brirthday":"Unknown",
            "residence":"Mountain View, California, United States" 
        }
}

def phraseDataPersonalInformation(ircmsg,botnick,nick,hostmask): 
    ircmsg = ircmsg.replace(" i "," " + nick + " ").replace(" me "," " + nick+ " ").replace(" you "," bowserbot " )
    
    #Address information
    result = re.findall("where does (.*) live",ircmsg)
    result5 = re.findall("where do (.*) live",ircmsg)
    result2 = re.findall("does (.*) live in the",ircmsg)
    result3 = re.findall("what is (.*)'s address",ircmsg)
    result4 = re.findall("what is (.*)s address",ircmsg)
    addAddress = "Earth, Inner Solar System, Solar system, Local Interstellar Cloud, Local Bubble, Gould Belt, Orion Arm, Milky Way, Local Group, Virgo Supercluster, Laniakea, Universe"
    
    if len(result) > 0 or len(result2) > 0 or len(result3) > 0 or len(result4) > 0  or len(result5) > 0:
        for i in [result,result2,result3,result4,result5]:
            if len(i) > 0:
                nick = i[0]; break
        for key in knownUserInformation:
            if key.lower() == nick.lower():
                return nick + " lives in " + knownUserInformation[key]["residence"] + " (" + addAddress + ")"
        return "I do not know where " + nick + " lives, sorry."
    
    #TODO: GET AGE, ip, real name (aka full name) and time
    
    #how old is [nick] what's nick's [age] 
    result = ircmsg.split("how old is ")
    result2 = ""
    
    