import string

def anagrams(s):
    if s == "":
        return [s]
    else:
        ans = []
        for an in anagrams(s[1:]):
            for pos in range(len(an)+1):
                ans.append(an[:pos]+s[0]+an[pos:])
        return ans


def unscrambleWord(anagram):
    anaLst = anagrams(anagram)
    diction = dictionary("words2.txt")
    solutions = []
    for ana in anaLst:
        if diction.has_key(ana):
            solutions.append(ana)
            
    return list(set(solutions))

def dictionary(wordlist):
    dict = {}
    infile = open(wordlist, "r")
    for line in infile:
        word = line.split("\n")[0]
        dict[word] = 1
    infile.close()
    return dict 
    
wordlist = open("words2.txt","r").read().split("\n")

def getRhymes(word,wordlist):
    word = word.lower()
    results = []
    for i in wordlist:
        if i.lower().endswith(word[-3:]):
            results.append(i)
    return results
    
def sendmsg(chan, msg,ircsock):
    ircsock.send("PRIVMSG {0} :{1}\n".format(chan, msg))#
    
def runCommands(channel,nick,commandChar,ircmsg,hostmask,ircsock):
    if ircmsg.find(commandChar+"unscramble ") != -1:
        if len(ircmsg.split(commandChar+"unscramble ")[1].replace(" ","")) > 9:
            sendmsg(channel,"Word too long :C",ircsock)
        else:
            result = unscrambleWord(ircmsg.split(commandChar+"unscramble ")[1].replace(" ",""))
            if len(result) == 0:
                sendmsg(channel,"There were no anagrams of the given text.",ircsock)
            else:
                returned = "Results: "
                index = 0
                for i in result:
                    returned = returned + i + ", "
                    index += 1
                    if index > 10:
                        break
                sendmsg(channel,returned[0:420]+"...",ircsock)
                
    elif ircmsg.find(commandChar+"anagram ") != -1:
        if len(ircmsg.split(commandChar+"anagram ")[1].replace(" ","")) > 9:
            sendmsg(channel,"Word too long :C",ircsock)
        else:
            result = unscrambleWord(ircmsg.split(commandChar+"anagram ")[1].replace(" ",""))
            if len(result) == 0:
                sendmsg(channel,"There were no anagrams of the given text.",ircsock)
            else:
                returned = "Results: "
                index = 0
                for i in result:
                    returned = returned + i + ", "
                    index += 1
                    if index > 10:
                        break
                sendmsg(channel,returned[0:420]+"...",ircsock)
                
    elif ircmsg.find(commandChar+"rhyme ") != -1:
        results = getRhymes(ircmsg.split(commandChar+"rhyme ",1)[1] , wordlist)
        if len(results) == 0:
            sendmsg(channel,"There were no rhymes of the given text.",ircsock)
        else:    
            returned = "Results: "
            for i in results:
                returned = returned + i + ", "
            sendmsg(channel,returned[0:310]+"...",ircsock)
            