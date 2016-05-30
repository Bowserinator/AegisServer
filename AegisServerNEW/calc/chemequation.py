import urllib
import requests
import xml.etree.ElementTree as ET

#http://api.wolframalpha.com/v2/query?input=sqrt+2&appid=APLTT9-9WG78GYE65"

def solveChemEquation(phrase):
    phrase = phrase.replace("+","+%2B+")

    xml_data=requests.get("http://api.wolframalpha.com/v2/query?input="+phrase+"&appid=APLTT9-9WG78GYE65").text
    root = ET.fromstring(xml_data.encode('utf-8')) #.encode('ascii','ignore')

    for child in root:
        if child.get("title") == "Balanced equation":
            for pod in root.findall('.//pod'):
                for pt in pod.findall('.//plaintext'):
                    if pt.text:
                        answer = pt.text
                        answer = answer.replace("_","")
                        answer = answer.replace("   ","")
                        return "The balanced equation is " + answer
    return "\x035Invalid equation was given!"

def wolfram(phrase):
    #e^i * x + 1 - 10 / 10 + 10! = e%5Ei+*+x+%2B+1+-+10+%2F+10+%2B+10%21
    #^ = %5E  + = +*+  - = +-+ / = %2F * = +*+ ! = %21
    if phrase == "":
        return "There was no result for the query."
    phrase = phrase.replace("^","%5E").replace("!","%21").replace("+","%2B")
    phrase = phrase.replace("/","%2F").replace("#","").replace("\\","").replace(" ","+")
    try:
        xml_data=requests.get("http://api.wolframalpha.com/v2/query?input="+phrase+"&appid=APLTT9-9WG78GYE65").text
        #xml_data=requests.get("http://api.wolframalpha.com/v2/query?input="+phrase+"&appid=VWJ4LK-PGJTQQEK63").text #MY OWN APP ID ADD SWITCH COMMAND
        root = ET.fromstring(xml_data.encode('utf-8')) #.encode('ascii','ignore')
    
        amount = 0
        returned = ""
        for child in root:
            if amount < 1:
                amount += 1
                returned = returned + "\x02" + child.get("title") + "\x0f "
                for pod in root.findall('.//pod'):
                    for pt in pod.findall('.//plaintext'):
                        if pt.text:
                            if pt.text.replace(" ","") != "":
                                returned = returned + pt.text + " | "
        if returned == "":
            return "There was no result for the query."
        return returned[:300]
    except:
        return "There was no result for the query."

def solveEquation(phrase):
    #e^i * x + 1 - 10 / 10 + 10! = e%5Ei+*+x+%2B+1+-+10+%2F+10+%2B+10%21
    #^ = %5E  + = +*+  - = +-+ / = %2F * = +*+ ! = %21
    phrase = phrase.replace("^","%5E").replace("!","%21").replace("+","%2B")
    phrase = phrase.replace("/","%2F").replace("#","").replace("\\","").replace(" ","+")
    
    xml_data=requests.get("http://api.wolframalpha.com/v2/query?input="+phrase+"&appid=APLTT9-9WG78GYE65").text
    root = ET.fromstring(xml_data.encode('utf-8')) #.encode('ascii','ignore')

    amount = 0
    returned = ""
    for child in root:
        if amount < 1:
            amount += 1
            for pod in root.findall('.//pod'):
                for pt in pod.findall('.//plaintext'):
                    if pt.text:
                        if pt.text.find("x = ") != -1 and pt.text.find("Input") == -1:
                            returned = returned + pt.text + "    "
    if returned == "":
        return "Invalid equation or no solution found"
    return returned