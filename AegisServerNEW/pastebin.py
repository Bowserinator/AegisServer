#Gets pastebin title, user, post, file size, expire date
import requests,re
import lxml, urllib
from lxml import etree
import json


def getPaste(url):
    page = requests.get(url)
    try:
        page = page.text

        user = re.search('a href="/u/(.*)img src=', page).group(1).replace('"><',"")
        title = re.search('div class="paste_box_line1" title=(.*)"><h1>', page).group(1).replace('"',"")
        date_posted = re.search('<img src="/i/t.gif" class="img_line t_da" alt=""> <span title="(.*)">', page).group(1).replace('"',"")
        expires = re.search('title="When this paste gets automatically deleted">(.*)</div>',page.replace("\n","")).group(1).split("<div")[0].replace(" ","",1).replace("</div>","")
        size = re.search('<span class="h_640"><a href="/archive/text" class="buttonsm" style="margin:0">text</a></span> (.*)</div>',page.replace("\n","")).group(1).split("<div")[0].replace(" ","",1).replace("</div>","")
        
        returned = "Pastebin is "
        returned = returned + title
        returned = returned + " by " + user
        returned = returned + " posted on " + date_posted
    
        returned = returned + " The paste will expire in " + str(expires) 
        return returned
    except:
        return ""

def getYoutube(url):
    youtube = etree.HTML(urllib.urlopen(url).read()) #enter your youtube url here
    video_title = youtube.xpath("//span[@id='eow-title']/@title") #get xpath using firepath firefox addon
    return 'Video is: '.join(video_title)
    
def getTPT(saveId):
    page = requests.get("http://powdertoy.co.uk/Browse/View.html?ID=" + str(saveId))
    try:
        if page != None:
            page = page.text
    
            title = re.search('<meta property="og:title" content=(.*) />',page).group(1).replace('"',"")
            likesTotal = re.search('<span class="ScoreLike badge badge-success">(.*)</span>',page).group(1).split('</span>&nbsp;/&nbsp;<span class="ScoreDislike badge badge-important">')
            likes = likesTotal[0]
            dislikes = likesTotal[1]
            return "Save " + saveId + " is " + title + " and has " + likes + " likes and " + dislikes + " dislikes."
    except:
        return ""


def getThread(threadId):
    threadId = threadId.replace(":","").replace(".","")
    jsonD = requests.get("http://powdertoy.co.uk/Discussions/Thread/View.json?Thread="+str(threadId)).text
    if jsonD == '{"Status":"0","Error":"The thread you have tried to view does not exist"}':
        return ""
    data = json.loads(jsonD)
    returned = "Thread is '"

    topic = data["Info"]["Topic"]
    returned = returned + topic["Title"] + "' by " + topic["Author"]
    returned = returned + " has " + str(topic["PostCount"]) + " posts and " + str(topic["ViewCount"]) + " views. Last post by " + topic["LastPoster"] + " on " + str(topic["Date"]) 
    return returned
