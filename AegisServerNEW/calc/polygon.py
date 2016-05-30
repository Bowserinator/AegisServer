import math


def getPolyInfo(num):
    #Returns angle sum, exteriror angle, interior angle,
    diag = num*(num-3)/2
    Sum = 180*(num-2)
    ext = 360/num
    inner = 180-ext
    return "Diagionals: " + str(diag) + " | Angle sum: " + str(Sum) + " | Exterior: " + str(ext) + " | Interior: " + str(inner)
    
    
def getName(num):
    #Returns [ name , alt names ]
    if num == 1:
        return ["monogon","None"]
    if num == 2:
        return ["Digon","None"]
        
    if num == 3: #triangle, also known as trigon
    #Equalaterial, right, isoloes, scalene, acute, obtuse
        return ["Triangle","None"]
    
    #Quads
    if num == 4:
        return ["Quadilateral","None"]
    
    elif num == 5: #Quintalaterial or pentagon
        return ["Pentagon","Quintrilateral"]
    elif num == 6:
        return ["Irregular Hexagon","None"]
    elif num == 7:
        return ["Irregular Heptagon","Irregular Septagon"]
    elif num == 8:
        return ["Irregular Octogon","None"]
    elif num == 9:
        return ["Irregular Nonagon","Irregular Enneagon"]
    elif num == 10:
        return ["Irregular Decagon","None"]
    elif num == 11:
        return ["Irregular Hendecagon","Irregular Undecagon"]
    elif num == 12:
        return ["Irregular Dodecagon","Irregular Duodecagon"]
    elif num == 13:
        name = "Tridecagon "
        name2 = "Triskaidecagon"
        return [ name,  name2]
    elif num == 14:
        name = "Tetradecagon "
        name2 = "Tetrakaidecagon"
        return [ name,  name2]
    #Array of elements from 15 - 20, should've done this earlier.
    name1 = ["Pentadecagon","Hexadecagon","Heptadecagon","Octadecagon","Enneadecagon","Icosagon"]
    name2 = ["Pentakaidecagon","Hexakaidecagon","Heptakaidecagon","Octakaidecagon","Enneakaidecagon","None"]
    if num > 14 and num <= 20:
        return [ name1[num - 15], name2[num-15]]
    
    tens = ["icosi","triaconta","tetraconta","pentaconta","hexaconta","heptaconta","octaconta","enneaconta"]
    ones = ["","hena","di","tri","tetra","penta","hexa","hepta","octa","ennea",""]
    if num > 20 and num < 100:
        a = num
        tens = tens[int(a/10) - 2]
        ones = ones[a % 10 ]
        return [ tens + "kai" + ones + "gon","None"]

    return [ str(num) + "-gon","None"]


#

import math

def getDis(p1,p2):
    a = p2[0]-p1[0]
    b = p2[1]-p1[1]
    return math.sqrt(a*a + b*b)
    
def getDiag(verts):
    n = len(verts)
    return n * (n-3) / 2

def getPolySides(verts): #gets side lengths
    side_lengths = []
    size = len(verts)
    
    for i in range(0,len(verts)-1):
        side_lengths.append(getDis(verts[i],verts[i+1]))
    side_lengths.append(getDis(verts[0],verts[size-1]))
    return side_lengths
    
def getPolyArea(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area
    
def getPolyPerm(verts):
    sides = getPolySides(verts)
    total = 0
    for i in sides:
        total += i
    return total

def isEqualaterial(verts):
    sides_old = getPolySides(verts)
    sides= []
    for i in sides_old:
        sides.append(round(i, 1))
    return len(set(sides)) <= 1
    
def isConvex(verts):
    angles = getAngles(verts)
    convex = True
    for i in angles:
        if i >= 180:
            convex=False
    return convex
    
def isEqualangular(verts):
    sides_old = getAngles(verts)
    sides= []
    for i in sides_old:
        sides.append(round(i, 1))
    return len(set(sides)) <= 1

def calcDis(x1,y1,x2,y2):
    return math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
    
def calcAngle(x1,y1,x2,y2,x3,y3): #x2,y2 are vert
    try:
        a = getDis([x1,y1],[x2,y2])
        b = getDis([x3,y3],[x2,y2])
        c = getDis([x3,y3],[x1,y1])
        #(a^2 + b^2  - c^2)/2ab = cos(C)
        angle = math.acos((a*a + b*b - c*c) / 2 / a/b)
        
        if round(angle,1) == round(3.1415926535/2,1):
            return True
        return False
    except:
        return False
    
def getAngle(x1,y1,x2,y2,x3,y3): #x2,y2 are vert
    try:
        a = getDis([x1,y1],[x2,y2])
        b = getDis([x3,y3],[x2,y2])
        c = getDis([x3,y3],[x1,y1])
        #(a^2 + b^2  - c^2)/2ab = cos(C)
        angle = math.acos((a*a + b*b - c*c) / 2 / a/b)
        
        return angle
    except:
        return 0
    
def getAngles(verts):
    angles = []
    angles.append(round(getAngle(verts[len(verts)-1][0],verts[len(verts)-1][1],verts[0][0],verts[0][1],verts[1][0],verts[1][1]) * 57.2958,1))
    for i in range(1,len(verts) - 1):
        a = getAngle(verts[i-1][0],verts[i-1][1],verts[i][0],verts[i][1],verts[i+1][0],verts[i+1][1])
        a *= 57.2958
        angles.append(round(a,1))
    angles.append(round(getAngle(verts[len(verts)-2][0],verts[len(verts)-2][1],verts[len(verts)-1][0],verts[len(verts)-1][1],verts[0][0],verts[0][1]) * 57.2958,1))
    return angles

def isParallel(x1,y1,x2,y2,x3,y3,x4,y4): #x2,y2 are vert
    slopea = (y2 - y1)/(x2 - x1)
    slopeb = (y4 - y3)/(x4-x3)
    if slopea == slopeb:
        return True
    else:
        return False


#qu = qu to u, etc...
#qu, ua, ad, dq
def getName2(verts):
    #Returns [ name , alt names ]
    if len(verts) == 1:
        return ["monogon","None"]
    if len(verts) == 2:
        return ["Digon","None"]
        
    if len(verts) == 3: #triangle, also known as trigon
    #scalene, acute, obtuse
        angles = getAngles(verts)
        if round(angles[0],1) == 60 and round(angles[1],1) == 60:
            return ["Equilateral triangle","Equilateral trigon"]
        if round(angles[0],1) == round(angles[1],1) or round(angles[1],1) == round(angles[2],1) or round(angles[2],1) == round(angles[0],1):
            return ["Isosceles triangle","Isosceles trigon"]
            
        for i in angles:
            if round(i,2) == 90:
                return ["Right triangle","Right trigon"]
            elif round(1,2) > 90:
                return ["Obtuse triangle","Obtuse trigon"]
        return ["Acute triangle","Acute trigon"]

    
    #Quads
    if len(verts) == 4:
        q = verts[0]; u = verts[1]
        a = verts[2]; d = verts[3]

        sides = getPolySides(verts)
        qu = round(sides[0],3); ua = round(sides[1],3)
        ad = round(sides[2],3); dq = round(sides[3],3)
        
        if qu == ad or ua == dq:
            if qu == ad == ua ==dq:
                if calcAngle(q[0],q[1],u[0],u[1],a[0],a[1]):
                    return ["Square","None"]
                else:
                    return ["Rhombus","None"]
            elif calcAngle(q[0],q[1],u[0],u[1],a[0],a[1]):
                return ["Rectangle","Right parallelogram"]
            elif isParallel(q[0],q[1],u[0],u[1],a[0],a[1],d[0],d[1]):
                return ["Parallelogram","None"]
        
        elif isParallel(q[0],q[1],u[0],u[1],a[0],a[1],d[0],d[1]) or isParallel(u[0],u[1],a[0],a[1],d[0],d[1],q[0],q[1]):
            if ad == qu or ua == dq:
                return ["Isosceles Trapezoid","Isosceles Trapezium"]
            else:
                return ["Trapezoid","Trapezium"]
        elif dq == qu and ua == ad:
            return ["Kite","Deltoid"]
        elif qu == ua and ad == dq:
            return ["Kite","Deltoid"]
        else:
            return ["Irregular Quadlaterial","Irregular Tetragon"]
    
    elif len(verts) == 5: #Quintalaterial or pentagon
        if isEqualaterial(verts):
            return ["Regular Pentagon","Regular Quintrilateral"]
        return ["Irregular Pentagon","Irregular Quintrilateral"]
    elif len(verts) == 6:
        if isEqualaterial(verts):
            return ["Regular Hexagon","None"]
        return ["Irregular Hexagon","None"]
    elif len(verts) == 7:
        if isEqualaterial(verts):
            return ["Regular Heptagon","Regular Septagon"]
        return ["Irregular Heptagon","Irregular Septagon"]
    elif len(verts) == 8:
        if isEqualaterial(verts):
            return ["Regular Octogon","None"]
        return ["Irregular Octogon","None"]
    elif len(verts) == 9:
        if isEqualaterial(verts):
            return ["Regular Nonagon","Regular Enneagon"]
        return ["Irregular Nonagon","Irregular Enneagon"]
    elif len(verts) == 10:
        if isEqualaterial(verts):
            return ["Regular Decagon","None"]
        return ["Irregular Decagon","None"]
    elif len(verts) == 11:
        if isEqualaterial(verts):
            return ["Regular Hendecagon","Regular Undecagon"]
        return ["Irregular Hendecagon","Irregular Undecagon"]
    elif len(verts) == 12:
        if isEqualaterial(verts):
            return ["Regular Dodecagon","Regular Duodecagon"]
        return ["Irregular Dodecagon","Irregular Duodecagon"]
    elif len(verts) == 13:
        name = "Tridecagon "
        name2 = "Triskaidecagon"
        if isEqualaterial(verts):
            return ["Regular " + name,"Regular " +  name2]
        return ["Irregular " + name,"Irregular " +  name2]
    elif len(verts) == 14:
        name = "Tetradecagon "
        name2 = "Tetrakaidecagon"
        if isEqualaterial(verts):
            return ["Regular " + name,"Regular " +  name2]
        return ["Irregular " + name,"Irregular " +  name2]
    #Array of elements from 15 - 20, should've done this earlier.
    name1 = ["Pentadecagon","Hexadecagon","Heptadecagon","Octadecagon","Enneadecagon","Icosagon"]
    name2 = ["Pentakaidecagon","Hexakaidecagon","Heptakaidecagon","Octakaidecagon","Enneakaidecagon","None"]
    if len(verts) > 14 and len(verts) <= 20:
        if isEqualaterial(verts):
            return ["Regular " + name1[len(verts) - 15],"Regular " + name2[len(verts)-15]]
        return ["Irregular " + name1[len(verts) - 15],"Irregular " + name2[len(verts)-15]]
    
    tens = ["icosi","triaconta","tetraconta","pentaconta","hexaconta","heptaconta","octaconta","enneaconta"]
    ones = ["","hena","di","tri","tetra","penta","hexa","hepta","octa","ennea"]
    if len(verts) > 20 and len(verts) < 100:
        a = len(verts)
        tens = tens[int(a/10) - 2]
        ones = ones[a - (a%10+1)*10]
        
        if isEqualaterial(verts):
            return ["Regular " + tens + "kai" + ones + "gon","None"]
        return ["Irregular " + tens + "kai" + ones + "gon","None"]
    if isEqualaterial(verts):
        return ["Regular " + str(len(verts)) + "-gon","None"]
    return ["Irregular " + str(len(verts)) + "-gon","None"]
    
    

#Returns the final string for data
def getPolyDataCord(verts):
    returned = []
    
    #add name
    returned.append("\x02Name: \x0f" + getName2(verts)[0])
    returned.append("\x02Other names: \x0f" + getName2(verts)[1])
    returned.append("")
    
    #Return lenght of each side
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    side_length_str = ""
    side_lengths = getPolySides(verts)
    if len(verts) <= 26:
        for i in range(0,len(side_lengths)):
            side_length_str = side_length_str + alphabet[i] + alphabet[i+1] + ": " + str(side_lengths[i]) + "  "
    else:
        for i in range(0,len(side_lengths)):
            side_length_str = side_length_str + "P" + str(i) + ": " + str(side_lengths[i]) + "  "
    returned.append(side_length_str)

    
    #Return the permeiter
    returned.append("\x02Perimeter: \x0f" + str(getPolyPerm(verts)))
    #Return the area
    returned.append("\x02Area: \x0f" + str(getPolyArea(verts)))
    #Number of diagionals
    returned.append("\x02Diagionals: \x0f" + str(getDiag(verts)))
    returned.append("")
    
    #Is it equalaterial?
    returned.append("\x02Equilateral: \x0f" + str(isEqualaterial(verts)))
    #Is it equalangular?
    returned.append("\x02Equilangular: \x0f" + str(isEqualangular(verts)))

    returned.append("")
    #Angle sum
    returned.append("\x02Angle sum: \x0f" + str(len(verts)*180-360))
        
    #Angles - getAngles(verts)
    angles_str = ""
    angles = getAngles(verts)
    for i in angles:
        angles_str = angles_str + str(i) + " | " 
    returned.append("\x02Angles (Degrees): \x0f" + angles_str)
    returned.append("\x02Is convex: \x0f" + str(isConvex(verts)))
    
    return returned