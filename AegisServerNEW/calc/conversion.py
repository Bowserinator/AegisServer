#Unit types:
#Distance: km, m, cm, mm, mircom, nm, mile, yard, foot, inch
#Use m as master unit, first convert to meter, then convert to other units
from __future__ import division
import requests

currencyCodesF = open('calc/currency.txt', 'r')
currencyCodes = []  #Save usernames in format user,channel (Or all),voice/op
for i in currencyCodesF:
    currencyCodes.append(i.replace("\n","").replace("\t"," "))

try:
    execfile("calc/conversion_list.py")
except: #Running locally
    execfile("conversion_list.py")

def convertDis(unit1,unit2,value):
    value = value / conversionsDis["M" + "_TO_" + unit2.upper()]
    value = value * conversionsDis["M_TO_" + unit1.upper()]
    return value

def convertData(unit1,unit2,value):
    value = value / conversionsData["BIT" + "_TO_" + unit2.upper()]
    value = value * conversionsData["BIT_TO_" + unit1.upper()]
    return value
    
def convertTime(unit1,unit2,value):
    value = value / conversionsTime["S" + "_TO_" + unit2.upper()]
    value = value * conversionsTime["S_TO_" + unit1.upper()]
    return value

def convertAngle(unit1,unit2,value):
    value = value / conversionsAngle["DEG" + "_TO_" + unit2.upper()]
    value = value * conversionsAngle["DEG_TO_" + unit1.upper()]
    return value
    
def convertVolume(unit1,unit2,value):
    value = value / conversionsVolume["L" + "_TO_" + unit2.upper()]
    value = value * conversionsVolume["L_TO_" + unit1.upper()]
    return value
    
def convertEnergy(unit1,unit2,value):
    value = value / conversionsEnergy["J" + "_TO_" + unit2.upper()]
    value = value * conversionsEnergy["J_TO_" + unit1.upper()]
    return value
    
    
def convertTemp(unit1,unit2,value):
    #Accepted units: f,c,k,plank-temp
    #Step1: convert to c
    if unit1 == "c":
        value *= 1
    elif unit1 == "f":
        value = (value - 32) * 5/9.0
    elif unit1 == "k":
        value -= 273.15
    elif unit1 == "plank-temp":
        value *= 1.416831963729*10**32 
    
    #Convert value to unit2
    if unit2 == "c":
        return value
    elif unit2 == "f":
        return value*9/5.0 + 32
    elif unit2 == "k":
        return value + 273.15
    elif unit2 == "plank-temp":
        return value / 1.416831963729*10**32 
    1/0

def convertMoney(unit1,unit2,value):
    a = unit1
    a = a.upper()
    b = unit2
    b = b.upper()
    c = float(value)
    
    #If hitler unit first convert to USD
    if unit1 == "hitler":
        return convertMoney("USD",unit2,value * -41400000000000.0) 
    if unit2 == "hitler":
        return convertMoney(unit1,"USD",value) / -41400000000000.0
    
    url = ('https://currency-api.appspot.com/api/%s/%s.json') % (a, b)
    r = requests.get(url)
    urlalt = ('http://themoneyconverter.com/%s/%s.aspx') % (a, b)
    
    #split and strip
    split1 = ('>%s/%s =') % (b, a)
    strip1 = ('</textarea>')
    ralt = requests.get(urlalt)
    d = float(ralt.text.split(split1)[1].split(strip1)[0].strip())

    return c * d

        
#Iovoid's:
#https://raw.githubusercontent.com/brettlangdon/node-units/master/lib/default.units
    
#The final convert Function
#==================================================================
#==================================================================
#==================================================================

def listUnits(convertType):
    try:
        execfile("calc/conversion_list.py")
    except: #Running locally
        execfile("conversion_list.py")
    
    convertType = convertType.lower()
    try:
        if convertType == "distance":
            returned = "\x02Units: \x0f"
            for key in conversionsDis:
                returned = returned + key.split("_")[-1].title() + ", "
            return returned
            
        elif convertType == "data":
            returned = "\x02Units: \x0f"
            for key in conversionsData:
                returned = returned + key.split("_")[-1].title() + ", "
            return returned
            
        elif convertType == "time":
            returned = "\x02Units: \x0f"
            for key in conversionsTime:
                returned = returned + key.split("_")[-1].title() + ", "
            return returned
            
        elif convertType == "angle":
            returned = "\x02Units: \x0f"
            for key in conversionsAngle:
                returned = returned + key.split("_")[-1].title() + ", "
            return returned
            
        elif convertType == "money":
            return "There is no list for this, all valid money codes (ie USD, CAD) apply. Also there's the hitler unit."
            
        elif convertType == "temp":
            return "\x02Units: \x0fC, F, K, PLANK-TEMP"
            
        elif convertType == "volume":
            returned = "\x02Units: \x0f"
            for key in conversionsVolume:
                returned = returned + key.split("_")[-1].title() + ", "
            return returned
            
        elif convertType == "energy":
            returned = "\x02Units: \x0f"
            for key in conversionsEnergy:
                returned = returned + key.split("_")[-1].title() + ", "
            return returned
    except:
        return "That is not a valid catagory."
    return "That is not a valid catagory."
    
def convertUnits(unit1,unit2,value):
    convertType = ""
    for key in conversionsDis:
        if key.split("_")[2].lower() == unit1.lower():
            convertType = "distance";break
    for key in conversionsTime:
        if key.split("_")[2].lower() == unit1.lower():
            convertType = "time";break
    for key in conversionsAngle:
        if key.split("_")[2].lower() == unit1.lower():
            convertType = "angle";break
    for key in conversionsData:
        if key.split("_")[2].lower() == unit1.lower():
            convertType = "data";break 
    for key in conversionsVolume:
        if key.split("_")[2].lower() == unit1.lower():
            convertType = "volume";break 
    for key in conversionsEnergy:
        if key.split("_")[2].lower() == unit1.lower():
            convertType = "energy";break 
        
    for i in currencyCodes:
        if unit1.lower() == i.split(" ")[0].lower():
            convertType = "money"
    if unit1.lower() in ["c","f","k","plank-temp"]:
        convertType = "temp"

    try:
        if convertType == "distance":
            return convertDis(unit1,unit2,value)
        elif convertType == "data":
            return convertData(unit1,unit2,value)
        elif convertType == "time":
            return convertTime(unit1,unit2,value)
        elif convertType == "angle":
            return convertAngle(unit1,unit2,value)
        elif convertType == "money":
            return convertMoney(unit1,unit2,value)
        elif convertType == "temp":
            return convertTemp(unit1,unit2,value)
        elif convertType == "volume":
            return convertVolume(unit1,unit2,value)
        elif convertType == "energy":
            return convertEnergy(unit1,unit2,value)
    except:
        return "\x035Invalid Units found!"
    return "\x035Invalid Units found!"
