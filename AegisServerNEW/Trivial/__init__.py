#Birthdays
import datetime

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

def birthday(nick,BWBellairsTrue):
    #BWBellairs is January 23
    now = datetime.datetime.now()
    if nick == "Bowserinator" and BWBellairsTrue == True:
        return [""]
    return False

