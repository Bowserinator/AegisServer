#The physics
import math

#Classical mechanics
def gravitationMath(m1,m2,d,G=6.673e-11): #Calculates gravity force
    return G * m1 * m2 / d / d
    
def orbitSpeed(mass,radius,G=6.673e-11):
    return math.sqrt(G*mass/radius)
    
def orbitPeriod(mass,radius,G=6.673e-11,pi=3.141592):
    return math.sqrt((4*pi*pi * radius**3) / G / mass)
    
