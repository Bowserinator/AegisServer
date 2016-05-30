#Timebomb
#1 time bomb per bot, timer reaches 0
import math

#Puzzle 1 - Get inital v given x distance, angle in radians and inital height and gravity, must calculate to nearest integer
def getVi(xdis,angle,h,g):
    """This uses a fancy formula: 1/cos(angle) * sqrt((0.5g*x^2)/(xtan(angle) + h)"""
    var1 = 1 / math.cos(angle)
    var2 = 0.5*g*xdis*xdis
    var3 = math.tan(angle) * xdis + h
    return var1 * math.sqrt(var2/var3)
    

#Other puzzles?
"""How much would could a woodchuck...
"""