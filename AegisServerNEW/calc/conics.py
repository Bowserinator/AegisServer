#Color codes

WHITE = "\x030"
BLACK = "\x031"
DARKBLUE = "\x032"
DARKGREEN = "\x033"
RED = "\x034"
DARKRED = "\x035"
DARKVIOLET = "\x036"
ORANGE = "\x037"
YELLOW = "\x038"
LIGHTGREEN = "\x039"
CYAN = "\x0310"
LIGHTCYAN = "\x0311"
BLUE = "\x0312"
VIOLET = "\x0313"
DARKGRAY = "\x0314"
LIGHTGRAY = "\x0315"

BOLD = "\x02"
ITALIC = "\x09"     
RESET = "\x0f"   
UNDERLINE = "\x15"     

import math

def getParabola(ircmsg): #IRCMSG In format a,b,c
    #lactus rectum, y intercept, x intercept"""
    
    returned = ""
    
    coff = ircmsg.split(",")
    if len(coff) != 3:  #Must have 3 coeffients
        return RED + "Input must be inform a,b,c for the quadratic ax^2 + bx + c"
        
    coff = [float(x) for x in coff] #Change string to floats
    a = coff[0]; b = coff[1]; c = coff[2]
    dis = b*b - 4 * a * c
    
    #Get the real roots
    if dis > 0: #2 real roots
        r1 = round((-b + math.sqrt(dis)) /  (2*a),3)
        r2 = round((-b - math.sqrt(dis)) /  (2*a),3)
        returned  = returned + "The roots are: " + str(r1) + " & " + str(r2)
    elif dis == 0: #1 real root
        r1 = round((-b + math.sqrt(dis)) /  (2*a),3)
        returned = returned + "The root is: " + str(r1)
    elif dis < 0:
        returned = returned + "There are no real roots. "
    
    #Get the vertex
    vertx = round(-b/2/a,3)
    verty = a * vertx * vertx + b*vertx+c
    returned = returned + " | The vertex is (" + str(vertx) + "," + str(round(verty,3)) + ")"
    returned = returned + " | The focus is (" + str(vertx) + "," + str(round((1-dis) / 4 / a))+  ")"
    returned = returned + " | The focal length is " + str(round(0.25/a,3))
    returned = returned + " | The y intercept is " + str(c) 
    returned = returned + " | The completed square form is " + str(a) + "(x - " + str(vertx) + ")^2 + " + str(verty)
    
    return returned
    
def getEllipse(ircmsg):
    returned = ""
    
    if len(ircmsg.split(",")) != 2:
        return RED + "Input must be in form a,b for x^2/a^2 + y^2/b^2 = 1 (radii of length a and b)"
    
    coff = ircmsg.split(",")
    coff = [float(x) for x in coff]
    a = coff[0]; b = coff[1]

    f = round(math.sqrt(abs(a*a - b*b)),3)
    returned = returned + "The foci add to " + str(2*a) + " and are (h,k +- " + str(f) + ")"
    returned = returned + " | The eccentricity is " + str(round(f/a,3)) 
    returned = returned + " | The area is " + str(round(a*3.1415926535897*b,3))
    
    #Get the circumfrence
    h = (a-b) * (a-b)  / (a+b) / (a+b)
    c1 = (a+b) * 3.1415926535898
    multi = 1 + (3*h / (10 + math.sqrt(4 - 3*h) ) )
    returned = returned + " | The circumfrence is " + str(round(c1*multi,3))
    return returned

def getHyperbola(ircmsg):
    returned = ""
    
    if len(ircmsg.split(",")) != 2:
        return RED + "Input must be in form a,b for x^2/a^2 - y^2/b^2 = 1 (Axis of length a and b)"
    
    coff = ircmsg.split(",")
    coff = [float(x) for x in coff]
    a = coff[0]; b = coff[1]; c = math.sqrt(abs(a*a-b*b))

    returned = returned + "(Center h,k) The foci are (h +- " + str(c) + ",k)"
    returned = returned + " | The traverse axis length: " + str(2*a)
    returned = returned + " | The conjugate axis length: " + str(2*b)
    returned = returned + " | The conjugate axis endpoints: (h,k +- " + str(b) + ")"
    returned = returned + " | The asymptotes equations are: (+-" + str(b) + "/" + str(a) + ")(x-h)"
    
    return returned
    
