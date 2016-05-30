def getNamesChannel(channel,irc):
    irc.send("NAMES {0}\r\n".format(channel).encode("UTF-8"))
    ircmsg = irc.recv(2048)
    ircmsg = ircmsg.decode("UTF-8")
    ircmsg = ircmsg.strip("\r\n")
    ircmsg = ircmsg.strip(":").split(" :",1)[1].split(" ")
    
    returned = []
    for i in ircmsg:
        if i.startswith("@"):
            returned.append([i.replace("@","",1), "op" ])
        elif i.startswith("+"):
            returned.append([i.replace("+","",1), "voice" ])
        else:
            returned.append([i,"none"])
    return returned

    #weber.freenode.net 353 AegisServer @ ##BWBellairs-bots :
    #@AegisServer ^wolfy @Bowserinator noteness JZTech101 zz JeDa @BWBellairs RadioNeat boxmein @HAL9000 @Andromeda @DZBot CussBot @iovoid @BWBellairs[Bot] @IndigoTiger
    #Returns list of names in an array [["name","op"]]

def gethostmask(nick,irc):
    irc.send("WHO {0}\r\n".format(nick).encode("UTF-8"))
    ircmsg = irc.recv(2048)
    ircmsg = ircmsg.decode("UTF-8")
    ircmsg = ircmsg.strip("\r\n")
    ircmsg = ircmsg.strip(":")
    ircmsg = ircmsg.split()
    print(ircmsg)
    if ircmsg[1] == "352":
        user = ircmsg[4]
        host = ircmsg[5]
        hm = "{0}!{1}@{2}".format(nick, user, host)
        return hm
    else:
        return False

def banmask(nick,ircsock):
    mask = gethostmask(nick,ircsock)
    if not mask:
        return False
    nick = mask.split("!")[0]
    user = mask.split("!")[1].split("@")[0]
    host = mask.split("@")[1]
    if host.startswith("gateway/"):
        if "/irccloud.com/" in host:
            uid = user[1:]
            host = host.split("/")
            host = "/".join(host[:-1])
            bm = "*!*{0}@{1}/*".format(uid, host)
            return bm
        elif "/ip." in host:
            host = host.split("/ip.")
            host = host[1]
            bm = "*!*@*{0}".format(host)
            return bm
        else:
            host = host.split("/")
            host = "/".join(host[:-1])
            bm = "*!{0}@{1}/*".format(user, host)
            return bm
    elif host.startswith("nat/"):
        host = host.split("/")
        host = "/".join(host[:-1])
        bm = "*!{0}@{1}/*".format(user, host)
        return bm
    elif "/" in host:
        bm = "*!*@{0}".format(host)
        return bm
    elif user.startswith("~"):
        bm = "*!*@{0}".format(host)
        return bm
    else:
        bm = "*!{0}@{1}".join(user, host)
        return bm
        
