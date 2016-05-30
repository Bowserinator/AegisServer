def getList(module):
    if module == " calc":
        return "\x02Commands: \x0fcalc, convert, wolf. \x02calc.<command name>: \x0fgetParabola, getHyperbola, getEllipse, average, gravitation, getG, orbitSpeed, sequence, chembalance, base, equation, getName, getPolyName, getPolyData, getAngle, getPolyDataCord, charge, comp"
    elif module == " bowserbucks":
        return "\x02Commands: \x0fbal, buy, give, sell, burnitem, burnmoney, use, info, news, flip, flipall, lottery, shop.list"
    elif module == " general":
        return "\x02Commands: \x0fhelp, list, echo, echo.echo, google, define, translate, geoip, unscramble, wiki, time, ctime, wcalc, rhyme, ping, about, youtube, modeReference. \x02filter.<command name>:\x0f lookalike, toMorse, unMorse, toBinary, unBinary, toHex, unHex, toBase64, unBase64, reverse, shuffle, rainbow."
    elif module == " op":
        return "\x02Commands: \x0fkickme, kick, kban, ban, unban, stab, unstab, op, deop, remotekick, remotekban, remoteban, remoteunban, remotestab, remoteunstab, remoteop, remotedeop"
    elif module == " word":
        return "\x02Commands: \x0fdefine, translate, unscramble, synonym, antonym, rhyme"
    elif module == " stats":
        return "\x02Commands: \x0fuserstats"
    elif module == " games":
        return "\x02Commands: \x0fcoin, dice, 8ball, rand, roulette, time"
    elif module == " mc":
        return "\x02Commands: \x0f enchant possible, enchant prob, enchant best slot, enchant best, craftcalc, toolstats, craft, search, getnwc, getowc, getmap, getmap player, get_time, get_server_time, mcwiki, get_weather, brew, mcuserstats, mcstatus"
    return "\x02Do list <module name>. Modules: \x0f calc, bowserbucks, general, op, word, stats, mc, games"