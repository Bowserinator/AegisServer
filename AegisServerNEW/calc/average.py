import math
from collections import Counter

def computeAverages(ircmsg):
    returned = ""
    num = [float(x) for x in ircmsg.split(",")]
    num.sort()
    
    mean = reduce(lambda x, y: x + y, num) / len(num)
    median1 = num[int(math.floor(len(num)/2))]
    median2 = num[int(math.ceil(len(num)/2))] #Upper median
    median = (median1+median2)/2.0
    
    counter = Counter(num)
    max_count = max(counter.values())
    mode = [k for k,v in counter.items() if v == max_count]
    
    rangeNum  = max(num) - min(num)
    maxNum = max(num)
    minNum = min(num)
    geoMean = reduce(lambda x, y: x*y, num) ** (1.0/len(num))
    
    returned = returned + "Mean: " + str(mean)
    returned = returned + " | Geometric Mean: " + str(geoMean)
    returned = returned + " | Median (High): " + str(median2)
    returned = returned + " | Median (Low): " + str(median1)
    returned = returned + " | Median (Avg): " + str(median)
    returned = returned + " | Mode: " + str(mode)
    returned = returned + " | Range: " + str(rangeNum)
    returned = returned + " | Largest: " + str(maxNum)
    returned = returned + " | Smallest: " + str(minNum)
    returned = returned + " | Length of list: " + str(len(num))
    return returned
    