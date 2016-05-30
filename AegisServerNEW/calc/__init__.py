#The calculation module
#Use import Calc - Then use calc.funct name, etc...
from __future__ import division
import math, ast, re, time
import random as rand
execfile("calc/conics.py")
execfile("calc/conversion.py")
execfile("calc/base.py")
execfile("calc/average.py")
execfile("calc/sequence.py")
execfile("calc/chemequation.py")
execfile("calc/other.py")
execfile("calc/calcphrase.py")
execfile("calc/polygon.py")

def sendmsg(chan, msg,ircsock):
    ircsock.send("PRIVMSG {0} :{1}\n".format(chan, msg))#
    
class Floatify(ast.NodeTransformer):
    def visit_Num(self, node):
        return ast.Num(float(node.n))
        
def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]
    
def runCommands(channel,nick,commandChar,ircmsg,ircsock):
    #if ircmsg.find(commandChar + "calc ") != -1:
        #ircmsg = ircmsg.split(commandChar + "calc ")[1]
        #sendmsg(channel, phraseText(ircmsg), ircsock)

    
    if ircmsg.find(commandChar+"wolf") != -1 and ircmsg.find(commandChar+"wolf ") == -1:
        sendmsg(channel,"Output: There were no results for that query.",ircsock) ; return ""
        
    elif ircmsg.find(commandChar + "wolf ") != -1:
        inp = ircmsg.split(commandChar+"wolf ")[1]
        o = wolfram(inp).replace("    ","").replace("\n","  ")
        sendmsg(channel,"Output: " + o[:300].encode("utf8"),ircsock)   
    
    elif ircmsg.find(commandChar + "unit ") != -1:
        query = ircmsg.split(commandChar + "unit ")[1]
        string = listUnits(query)

        sendmsg(channel,string,ircsock)
        
    elif ircmsg.find(commandChar + "convert ") != -1: #[number] [unit] to [unit2]
        try:
            ircmsg2 = ircmsg.split(commandChar+"convert ", 1)[1].split(" ")
            unit1 = ircmsg2[1]
            unit2 = ircmsg2[3]
            if unit1.lower().endswith("s") and unit1.lower() != "s":
                unit1 = unit1[:-1]
            if unit2.endswith("s") and unit2.lower() != "s":
                unit2 = unit2[:-1]
            result = convertUnits(unit1,unit2,float(ircmsg2[0]))   
            if result != "\x035Invalid Units found!":
                sendmsg(channel,ircmsg2[0] + " " + unit1 + " is " + str(result) + " " + unit2,ircsock)
            else:
                1/0
        except:
            sendmsg(channel,"\x035Invalid Units found!",ircsock)
    
    #calc.commands
    commandChar = commandChar + "calc."
    #try:
    if ircmsg.find(commandChar + "getParabola ") != -1:
        sendmsg(channel,getParabola(ircmsg.split(commandChar+"getParabola ")[1]),ircsock)
    elif ircmsg.find(commandChar + "getHyperbola ") != -1:
        sendmsg(channel,getHyperbola(ircmsg.split(commandChar+"getHyperbola ")[1]),ircsock)
    elif ircmsg.find(commandChar + "getEllipse ") != -1:
        sendmsg(channel,getEllipse(ircmsg.split(commandChar+"getEllipse")[1]),ircsock)
        
    elif ircmsg.find(commandChar + "getAngle ") != -1:
        result = ircmsg.split(commandChar+"getAngle ")[1].split(',')
        result = calcRot(float(result[0]),float(result[1]),float(result[2]),float(result[3]),float(result[4]))
        sendmsg(channel,result,ircsock)
        
    elif ircmsg.find(commandChar + "average ") != -1:
        sendmsg(channel,computeAverages(ircmsg.split(commandChar+"average")[1]),ircsock)
    elif ircmsg.find(commandChar + "gravitation ") != -1:
        sendmsg(channel,"Gravity force: " + str(gravitation(ircmsg.split(commandChar+"gravitation ")[1])),ircsock)
    elif ircmsg.find(commandChar + "getG ") != -1:
        sendmsg(channel,"Gravity acceleration: " + str(getG(ircmsg.split(commandChar+"getG ")[1])),ircsock)
    elif ircmsg.find(commandChar + "orbitSpeed ") != -1:
        sendmsg(channel,"Orbital Speed: " + str(orbitSpeed(ircmsg.split(commandChar+"orbitSpeed ")[1])),ircsock)   
        
    elif ircmsg.find(commandChar + "getPolyName") != -1:
        try:
            result = getName(int(ircmsg.split(commandChar+"getPolyName ")[1]))
            sendmsg(channel,"\x02Name:   \x0f" + result[0] + "   \x02Other:   \x0f" + result[1],ircsock)   
        except:
            sendmsg(channel,"\x035Invalid polygon number!",ircsock)
            
    elif ircmsg.find(commandChar + "getPolyData ") != -1:
        try:
            result = getPolyInfo(int(ircmsg.split(commandChar+"getPolyData ")[1]))
            sendmsg(channel,result,ircsock)   
        except:
            sendmsg(channel,"\x035Invalid polygon number!",ircsock)
    
    elif ircmsg.find(commandChar + "sequence ") != -1:
        args = ircmsg.split(commandChar+"sequence ")[1].split(" ")
        sendmsg(channel,calcSequence(args[0],args[1]),ircsock)
        
    elif ircmsg.find(commandChar + "equation ") != -1:
        args = ircmsg.split(commandChar+"equation ")[1]
        sendmsg(channel,solveEquation(args),ircsock)
        
    elif ircmsg.find(commandChar + "chembalance ") != -1:
        args = ircmsg.split(commandChar+"chembalance ")[1]
        sendmsg(channel,solveChemEquation(args),ircsock)
        
    elif ircmsg.find(commandChar + "getName ") != -1:
        args = ircmsg.split(commandChar+"getName ")[1].replace(",","")
        sendmsg(channel,NumberToWords(int(float(args))),ircsock)
        
    elif commandChar + "charge " in ircmsg:
        args = ircmsg.split(commandChar+"charge ")[1].replace(',',' ').split(" ")
        sendmsg(channel,"\x02Result: \x0f" + str(columbLaw(args[0],args[1],args[2])),ircsock)
        
    elif commandChar + "comp " in ircmsg:
        args = ircmsg.split(commandChar+"comp ")[1].replace(',',' ').split(" ")
        sendmsg(channel,str(components(args[0],args[1],args[2])),ircsock)

    elif ircmsg.find(commandChar + "base ") != -1: #Number,x
        ircmsg=  ircmsg.split(commandChar + "base ")[1].split(",")
        a = int2base(int(ircmsg[0]),int(ircmsg[1]))
        a = stripZero(str(a))
        sendmsg(channel,"The conversion is: " + str(a),ircsock)

    elif commandChar+"getPolyDataCord " in ircmsg:
        #getPolyData(verts)
        ircmsg = ircmsg.split(commandChar + "getPolyDataCord ")[1]
        data = ircmsg.split("),(")
        returned = []
        for i in data:
            returned.append([float(i.split(',')[0].replace("(","").replace(")","")),float(i.split(',')[1].replace("(","").replace(")",""))])
        
        result = getPolyDataCord(returned)
        final = ""
        for i in result:
            final = final + i + " "
        sendmsg(channel,final,ircsock)
        
    #NumberToWords
    #except:
        #sendmsg(channel,"\x035An error has occured, sorry.")
    
#The math functions
#===========================                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        =========================================

def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)



