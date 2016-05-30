#Help for all commands

def getHelp(command,commandChar):
    command = command.replace(commandChar,"")
    
    if command == "me":
        return "Stay calm, help will arrive soon!"
    elif command == "help":
        return "help <command> - You're using it right now!"
        
    #General Module
    elif command == "echo":
        return "echo <phrase> - Echo a phrase, use [b] Bold [i] Italic [u] Underline [r] Reset [nick] User [channel] Channel"
    elif command == "echo.echo":
        return "echo.echo <phrase> - Echo a phrase (Exact Phrase)"
        
    elif command == "filter.lookalike":
        return "filter.lookalike <phrase> - Replaces some characters with similar looking ones."
    elif command == "filter.toMorse":
        return "filter.toMorse <phrase> - Convert phrase to morse."
    elif command == "filter.unMorse":
        return "filter.unMorse <phrase> - Convert phrase from morse."
    elif command == "filter.toBinary":
        return "filter.toBinary <phrase> - Convert phrase to binary."
    elif command == "filter.unBinary":
        return "filter.unBinary <phrase> - Convert phrase from binary."
    elif command == "filter.toHex":
        return "filter.toHex <phrase> - Convert phrase to hexdecimal."
    elif command == "filter.unHex":
        return "filter.unHex <phrase> - Convert phrase from hexdecimal."
    elif command == "filter.reverse":
        return "filter.reverse <phrase> - Reverse the phrase."
    elif command == "filter.shuffle":
        return "filter.shuffle <phrase> - Shuffle the phrase."
    elif command == "filter.rainbow":
        return "filter.rainbow <phrase> - Return rainbow phrase."
        
    #Math module
    ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=##
    ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=##
    ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=##
    elif command == "calc":
        return "calc <math> - Calculate math, supports trig, sqrt and factorial (Use factorial(x))"
    elif command == "convert":
        return "convert <value> <from unit> to <to unit> - Convert value from unit 1 to 2."
    elif command == "calc.getParabola":
        return "calc.getParabola a,b,c - Gets parabola information for parabola ax^2 + bx + c"
    elif command == "calc.getHyperbola":
        return "calc.getHyperbola a,b - Gets hyperbola information for hyperbola x^2/a^2 - y^2/b^2 = 1"
    elif command == "calc.getEllipse":
        return "calc.getEllipse a,b - Gets ellipse information for ellipse x^2/a^2 + y^2/b^2 = 1"
    elif command == "calc.average":
        return "calc.average a,b,c... - Gets averages and statistics on data set."
    elif command == "calc.gravitation":
        return "calc.gravitation <mass1>,<mass2>,<distance> - Calculate gravity between 2 masses."
    elif command == "calc.getG":
        return "calc.getG <mass>,<distance> - Get gravitational acceleration on mass at distance."
    elif command == "calc.orbitSpeed":
        return "calc.orbitSpeed <mass>,<r> - Get orbit speed when orbiting planet of mass m at radius r."
    elif command == "wolf":
        return "wolf <math> - Query wolfram alpha"
    elif command == "calc.sequence":
        return "calc.sequence <seq type> <data> - Calculate sequence information."
    elif command == "calc.chembalance":
        return "calc.chembalance <chem equation> - Use wolfram alpha's chemical equation balancer."
    elif command == "calc.base":
        return "calc.base <base 10 num>,<new base> - Convert number to base."
    elif command == "calc.equation":
        return "calc.equation <equation> - Solve equation for x."
    elif command == "calc.getPolyData":
        return "calc.getPolyData <number> - Get information for n sided polygon."
    elif command == "calc.getPolyName":
        return "calc.getPolyName <number> - Get name for n sided polygon."
    elif command == "calc.getName":
        return "calc.getName <number> - Get name for number."
        
    #Ops and stuff
    ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=##
    ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=##
    ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=##
    elif command == "kickme":
        return "kickme - Kick yourself!"
    elif command == "kick":
        return "kick <user1,user2...> <reason> - Kick user(s) with reason (optional)."
    elif command == "kban":
        return "kban <user1,user2...> <reason> - Kick and ban user(s) with reason (optional)."
    elif command == "ban":
        return "ban <user1,user2...> - Ban user(s)."
    elif command == "unban":
        return "unban <user1,user2...> - Unban user(s)."
    elif command == "stab":
        return "stab <user1,user2...> - Quiet user(s)."
    elif command == "unstab":
        return "unstab <user1,user2...> - Unquiet user(s)."
    elif command == "op":
        return "op <user1,user2...> - Op user(s)."
    elif command == "deop":
        return "deop <user1,user2...> - Deop user(s)."
        
    #Bowserbucks
    ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=##
    ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=##
    ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=## ##=##=##=##=##=##=##
    elif command == "news":
        return "news - Get random news headline."
    elif command == "bal":
        return "bal - Get your balance, or register your account."
    elif command == "lottery":
        return "lottery - Bet the lottery for 1-1.5 billion."
    elif command == "burnmoney":
        return "burnmoney <amount> - Burn your BowserBucks."
    elif command == "give":
        return "give <user> <amount> - Give user <amount>."
    elif command == "flip":
        return "flip <bet> - 50% chance to win double or lose"
    elif command == "burnitem":
        return "burnitem <item> - Burn item"
    elif command == "inv":
        return "inv - Get your inventory"
    elif command == "buy":
        return "buy <item> <amount=1> - Buy item."
    elif command == "sell":
        return "sell <item> <amount=1> - Sell items."
    return "Command Not found!"