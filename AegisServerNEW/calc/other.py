import math

def gravitation(ircmsg):
    ircmsg = ircmsg.split(",")
    return gravitationMath(float(ircmsg[0]),float(ircmsg[1]),float(ircmsg[2]))
    
def gravitationMath(m1,m2,d):
    return 6.673e-11 * m1 * m2 / d / d
    
def getG(ircmsg):
    ircmsg=ircmsg.split(",")
    #In format mass, d
    return float(ircmsg[0]) * 6.673e-11 / float(ircmsg[1]) / float(ircmsg[1])
    
def orbitSpeed(ircmsg):
    m = float(ircmsg.split(",")[0])
    r =  float(ircmsg.split(",")[1])
    return math.sqrt(6.673e-11 * m / r)

def getNameSmall(number):
    #Returns name of number from 1 - 1000
    ones = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen",
    "fifteen","sixteen","seventeen","eighteen","nineteen",""]
    tens = ["twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    if number == 0:
        return ""
    if number < 20:
        return ones[number-1]
    if number >= 20:
        return tens[number/10-2] + " " + ones[number%10-1]
    

def NumberToWords(number):
    number=  int(number)
    if (number == 0):
        return "zero"
    if (number < 0):
        return "minus " + NumberToWords(abs(number))
    words = ""
    if (int(number / 1000000000000000000000000000000000) > 0):
        words += NumberToWords(number / 1000000000000000000000000000000000) + " duodecillion "
        number %= 1000000000000000000000000000000000
    if (int(number / 1000000000000000000000000000000) > 0):
        words += NumberToWords(number / 1000000000000000000000000000000) + " undecillion "
        number %= 1000000000000000000000000000000
    if (int(number / 1000000000000000000000000000) > 0):
        words += NumberToWords(number / 1000000000000000000000000000) + " decillion "
        number %= 1000000000000000000000000000
    if (int(number / 1000000000000000000000000) > 0):
        words += NumberToWords(number / 1000000000000000000000000) + " nonillion "
        number %= 1000000000000000000000000
    if (int(number / 1000000000000000000000) > 0):
        words += NumberToWords(number / 1000000000000000000000) + " octillion "
        number %= 1000000000000000000000
    if (int(number / 1000000000000000000) > 0):
        words += NumberToWords(number / 1000000000000000000) + " septillion "
        number %= 1000000000000000000
    if (int(number / 1000000000000000000) > 0):
        words += NumberToWords(number / 1000000000000000000) + " sextillion "
        number %= 1000000000000000
    if (int(number / 1000000000000000) > 0):
        words += NumberToWords(number / 1000000000000000) + " quintillion "
        number %= 1000000000000000
    if (int(number / 1000000000000000) > 0):
        words += NumberToWords(number / 1000000000000000) + " quadrillion "
        number %= 1000000000000000
    if (int(number / 1000000000000) > 0):
        words += NumberToWords(number / 1000000000000) + " trillion "
        number %= 1000000000000
    if (int(number / 1000000000) > 0):
        words += NumberToWords(number / 1000000000) + " billion "
        number %= 1000000000
    if (int(number / 1000000) > 0):
        words += NumberToWords(number / 1000000) + " million "
        number %= 1000000
    if (int(number / 1000) > 0):
        words += NumberToWords(number / 1000) + " thousand "
        number %= 1000
    if (int(number / 100) > 0):
        words += NumberToWords(number / 100) + " hundred "
        number %= 100
    if (number > 0):
        if (words != ""):
            words += "and "
        unitsMap =  [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]
        tensMap = [ "zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]

        if (number < 20):
            words += unitsMap[int(number)]
        else:
            words += tensMap[int(number / 10)]
            if ((number % 10) > 0):
                words += "-" + unitsMap[int(number % 10)]
    return words

def calcRot(x,y,angle,tx,ty):
    a = angle/57.2958
    xnew = (y+ty)*math.cos(a) - (x+tx)*math.sin(a)
    ynew = (y+ty)*math.sin(a) + (x+tx)*math.cos(a)

    return [round(xnew)-tx,round(ynew)-ty]
    
def columbLaw(c1,c2,distance):
    c1 = float(c1)
    c2 = float(c2)
    distance = float(distance)
    return 9*10**9 * c1 * c2 / distance / distance
    
def components(x,y,value):
    x = float(x)
    y = float(y)
    value = float(value)
    a = math.atan(y/x)
    return "\x02X comp: \x0f" + str(math.cos(a) * value) + "\x02 Y comp: \x0f" + str(math.sin(a) * value) 