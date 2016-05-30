import math, re, cmath
import traceback

def fact(n):
    if n < 0:
        raise ValueError('Negative factorials do not exist dumbass')
    if n < 2:
        return 1
    else:
        return n * fact(n-1)
    
def text2int(textnum, numwords={}):
    if textnum.replace(" ","") == "":
        return ""
    
    negative = False
    if "negative " in textnum:
        textnum = textnum.replace("negative ","")
        negative = True
        
    #Changes the words into numbers
    if not numwords:
        units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]
        
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        
        scales = ["hundred", "thousand", "million", "billion", "trillion","quadrillion","quintillion","sixtillion","septillion","octillion"]
        
        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):    numwords[word] = (1, idx)
        for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            return textnum #It's already a number or just a bad word

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0
    if negative:
        return -(result + current)
    return result+current
    
def splitPhrase(msg):
    #Splits the message among math operations
    return msg.replace("+","=").replace("-","=").replace("/","=").replace("*","=").replace("fact","=").replace("sqrt","=").replace("^","=").replace("@","=").replace("#","=").replace("!","=").replace("$",'=').replace('%','=').replace('&','=').replace('[','=').replace(']','=').replace('~','=').replace('`','=').replace('_','=').replace(".","=").split("=")

def calcPhrase(msg):
    #Operations: +,-,/,*,^,!, sqrt
    #English: plus, minus, times/multiplied, divided, to the power , factorial, square root
    #Delete by, of the
    #Then split by those symbols and try to translate to numbers
    #Form a string and evaluate it.
    
    msg = msg.lower()

    msg = msg.replace("calculate","").replace("calc","")

    msg = msg.replace("by","").replace("of","").replace("the","").replace("by","").replace('with','').replace("to","").replace("is","")
    msg = msg.replace("plus","+").replace("minus","-").replace("divided","/")
    msg = msg.replace("point",".")
    msg = msg.replace("over","/").replace("times","*").replace("multiplied","*")
    msg = msg.replace("power","^") #CHANGE THIS LATER!!
    msg = msg.replace("square root","@").replace("factorial","#").replace("sqrt","@").replace("squareroot","@").replace("fact","#")
    
        
    #Inverse Sin, acos, atan
    msg = msg.replace("arcsine","[").replace("asin","[").replace("arcsin","[")
    msg = msg.replace("arccosine","]").replace("acos","]").replace("arccos","]")
    msg = msg.replace("arctangent","~").replace("atan","~").replace("arctan","~")
    
    #Sin, cos, tan
    msg = msg.replace("sine","!").replace("sin","!")
    msg = msg.replace("cosine","$").replace("cos","$")
    msg = msg.replace("tangent","&").replace("tan","&")
    
    #Log and abs
    msg = msg.replace("log","`").replace("abs","_")

    #Get the order of the operations (Not the actual PEDMAS or whatever, the order they appear in the string)
    order = []
    for i in msg:
        if i in ["^",'+','-','*','/','#','@','!','%','$','&','[',']','~','`','_','.']: #,'S','F','Q','W','A','q','w','a'
            order.append(i)
    new_msg = splitPhrase(msg)
    newer_msg = "" #Need better varaible names
    
    index = 0
    for i in new_msg:
        if i.replace(" ","") != "":
            newer_msg = newer_msg + "(" + str(text2int(i)) + ")"
        try: newer_msg = newer_msg + order[index]
        except: pass
        index += 1

    #Ok now replace S with the proper square root function and F with the proper factorial function
    newer_msg = newer_msg.replace("#","fact")
    newer_msg = newer_msg.replace("@","cmath.sqrt")
    newer_msg = newer_msg.replace("!","math.sin")
    newer_msg = newer_msg.replace("$","math.cos")
    newer_msg = newer_msg.replace("&","math.tan")
    newer_msg = newer_msg.replace("[","math.asin")
    newer_msg = newer_msg.replace("]","math.acos")
    newer_msg = newer_msg.replace("~","math.atan")
    
    newer_msg = newer_msg.replace("`","math.log")
    newer_msg = newer_msg.replace("_","abs")
    
    #Now evalulate the phrase
    msg = newer_msg
        
    msg = msg.replace("pi","3.1415926535897")
    msg = msg.replace("e","2.71828")
    
    msg = msg.replace("^","**").replace(").(",".")
    msg = re.sub(r"(?<!\.)(\b\d+\b)(?!\.)", r"\1.0", msg) 
    msg = msg.replace("()","")
    msg = msg.replace(" ","")

    try: return "\x02Input:\x0f " + msg.replace(" ","").replace("math.","").replace("csqrt","sqrt") + " \x02Solution: \x0f" + str(eval(msg))
    except ArithmeticError: return "\x02 Input: \x0f" + msg.replace(" ","").replace("math.","") + " \x02Solution: \x0f The answer is too large or undefined."
    except Exception as e: 
        return None
    
