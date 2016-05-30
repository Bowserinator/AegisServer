conversionsDis = {
"M_TO_KM": 1000.0,
"M_TO_M": 1.0,
"M_TO_CM": 0.01,
"M_TO_MM": 0.001,
"M_TO_MIRCOM": 10e-6,
"M_TO_NM": 10e-9,
"M_TO_MI": 1609.0,
"M_TO_YARD": 1.09361,
"M_TO_FT": 1/3.28084,
"M_TO_IN": 1/39.37008,

"M_TO_KILOMETER": 1000.0,
"M_TO_METER": 1.0,
"M_TO_CENTIMETER": 0.01,
"M_TO_MILLIMETER": 0.001,
"M_TO_MIRCOMETER":10e-6,
"M_TO_NANOMETER": 10e-9,
"M_TO_MILE": 1609.0,
"M_TO_YARD": 1.09361,
"M_TO_FOOT": 1/3.28084,
"M_TO_INCH": 1/39.37008,

"M_TO_DM":0.1,
"M_TO_PM":1e-12,
"M_TO_FM":1e-15,
"M_TO_AM":1e-18,
"M_TO_ZM":1e-21,
"M_TO_YM":1e-24,

"M_TO_DECIMETER":0.1,
"M_TO_PICOMETER":1e-12,
"M_TO_FEMTOMETER":1e-15,
"M_TO_ATTOMETER":1e-18,
"M_TO_ZEPTOMETER":1e-21,
"M_TO_YOCTOMETER":1e-24,

"M_TO_DAM":10, "M_TO_DECAMETER":10,
"M_TO_HM":100, "M_TO_HECTAMETER":100,
"M_TO_MEGAMETER":10e6,
"M_TO_GM":10e9, "M_TO_GIGAMETER":10e9,
"M_TO_TM":10e12, "M_TO_TERAMETER":10e12,
"M_TO_PM":10e15, "M_TO_PETAMETER":10e15,
"M_TO_EM":10e18, "M_TO_EXAMETER":10e18,
"M_TO_ZM":10e21, "M_TO_ZETTAMETER":10e21,
"M_TO_YOTTAMETER":10e24,
"M_TO_LIGHT-YEAR":9.4607 * 10e12 *1000,
"M_TO_AU":1.496e+11
}

#Master unit is bit
conversionsData = {
"BIT_TO_BIT":1,
"BIT_TO_KILOBIT":1000.0,
"BIT_TO_KIBIBIT":1024.0,
"BIT_TO_MEGABIT":1000000.0,
"BIT_TO_MEBIBIT":1.049e+6,
"BIT_TO_GIGABIT":1000000000.0,
"BIT_TO_GIBIBIT":1.074e+9,
"BIT_TO_TERABIT":1e+12,
"BIT_TO_TEBIBIT":1.1e+12,
"BIT_TO_PETABIT":1e+15,
"BIT_TO_PEBIBIT":1.126e+15,

"BIT_TO_BYTE":1*8,
"BIT_TO_KILOBYTE":1000.0*8, "BIT_TO_KB":1000.0*8,
"BIT_TO_KIBIBYTE":1024.0*8, "BIT_TO_KIB":1024.0*8,
"BIT_TO_MEGABYTE":1000000.0*8, "BIT_TO_MB":1000000.0*8,
"BIT_TO_MEBIBYTE":1.049e+6*8, "BIT_TO_MIB":1.049e+6*8,
"BIT_TO_GIGABYTE":1000000000.0*8, "BIT_TO_GB":1000000000.0*8,
"BIT_TO_GIBIBYTE":1.074e+9*8, "BIT_TO_GIB":1.074e+9*8,
"BIT_TO_TERABYTE":1e+12*8, "BIT_TO_TB":1e+12*8,
"BIT_TO_TEBIBYTE":1.1e+12*8,"BIT_TO_TIB":1.1e+12*8,
"BIT_TO_PETABYTE":1e+15*8,"BIT_TO_PB":1e+15*8,
"BIT_TO_PEBIBYTE":1.126e+15*8, "BIT_TO_PIB":1.126e+15*8,


}

#Time units
#http://www.maplesoft.com/support/help/maple/view.aspx?path=Units%2Ftime
#https://en.wikipedia.org/wiki/Unit_of_time
#Master value is Seconds

conversionsTime = {
"S_TO_WINK":0.3333333333*10e-9,
"S_TO_SHAKE":1.1e-8,
"S_TO_SVEDBURG":1.1e-13,
"S_TO_BLINK":0.00001 * 86400,
"S_TO_S":1,
"S_TO_SEC":1,
"S_TO_SECOND":1,
"S_TO_MINUTE":60.0, "S_TO_MIN":60.0,
"S_TO_HOUR":360.0, "S_TO_HR":360.0,
"S_TO_DAY":86400.0,
"S_TO_WEEK":86400*7.0,
"S_TO_YEAR":86400*365.2425, "S_TO_YR":86400*365.2425,
"S_TO_BIENNIUM":86400*365.2425*2,
"S_TO_TRIENNIUM":86400*365.2425*3,
"S_TO_QUADRENNIUM":86400*365.2425*4,
"S_TO_QUINQUENNIUM":86400*365.2425*5,
"S_TO_DECADE":86400*365.2425*10,
"S_TO_CENTURY":86400*365.2425*100,
"S_TO_MILLENNIUM":86400*365.2425*1000,
"S_TO_EON":86400*365.2425*1.1e9,

"S_TO_PENTAD":86400*5,
"S_TO_FORTNIGHT":86400*14,
"S_TO_PLANK-TIME":10e-43,
"S_TO_JIFFY":10e-12*33.3564,
"S_TO_TU":10e-6*1024,
"S_TO_GALACTIC-YEAR":250000000*86400*365.2425,

"S_TO_DECISECOND":0.1,
"S_TO_MILISECOND":0.001,
"S_TO_MIRCOSECOND":1/1000000.0,
"S_TO_NANOSECOND":1/1000000000.0,
"S_TO_PICOSECOND":1e-12,
"S_TO_FESTOSECOND":1e-15,
"S_TO_ATTOSECOND":1e-18,
"S_TO_ZEPTOSECOND":1e-21,
"S_TO_YOCTOSECOND":1e-24,

"S_TO_DASECOND":10, "S_TO_DECASECOND":10,
"S_TO_HS":100, "S_TO_HECTASECOND":100,
"S_TO_MEGASECOND":10e6,
"S_TO_GS":10e9, "S_TO_GIGASECOND":10e9,
"S_TO_TS":10e12, "S_TO_TERASECOND":10e12,
"S_TO_PS":10e15, "S_TO_PETASECOND":10e15,
"S_TO_ES":10e18, "S_TO_EXASECOND":10e18,
"S_TO_ZS":10e21, "S_TO_ZETTASECOND":10e21,
"S_TO_YOTTASECOND":10e24,

}

#Master is degrees
conversionsAngle = {
    "DEG_TO_DEG":1,
    "DEG_TO_DEGREE":1,
    "DEG_TO_RAD":0.0174533,
    "DEG_TO_RADIAN":0.0174533,
    "DEG_TO_GRAD":1.11111,
    "DEG_TO_GRADIAN":1.11111,
    "DEG_TO_TURN":0.00277778
}

#Master is L (L)
conversionsVolume = {
    "L_TO_L":1,
    "L_TO_LITER":1,
    "L_TO_DECILITER":0.1,
    "L_TO_MILILITER":0.001,
    "L_TO_MIRCOLITER":1/1000000.0,
    "L_TO_NANOLITER":1/1000000000.0,
    "L_TO_PICOLITER":1e-12,
    "L_TO_FESTOLITER":1e-15,
    "L_TO_ATTOLITER":1e-18,
    "L_TO_ZEPTOLITER":1e-21,
    "L_TO_YOCTOLITER":1e-24,
    
    "L_TO_DALITER":10, "L_TO_DECALITER":10,
    "L_TO_HL":100, "L_TO_HECTALITER":100,
    "L_TO_MEGALITER":10e6,
    "L_TO_GL":10e9, "L_TO_GIGALITER":10e9,
    "L_TO_TL":10e12, "L_TO_TERALITER":10e12,
    "L_TO_PL":10e15, "L_TO_PETALITER":10e15,
    "L_TO_EL":10e18, "L_TO_EXALITER":10e18,
    "L_TO_ZL":10e21, "L_TO_ZETTALITER":10e21,
    "L_TO_YOTTALITER":10e24,
    
    "L_TO_GALLON":3.78541, "L_TO_GL":3.78541,
    "L_TO_PINT":2.11338,
    "L_TO_QUART":1.0566900005191,
    "L_TO_CUP":4.1666737291666331444,
    "L_TO_OUNCE":33.814080016611200108,
    "L_TO_OZ":33.814080016611200108,
    "L_TO_TABLESPOON":67.628, "L_TO_TB":67.628, "L_TO_TBL":67.628, "L_TO_TBSP":67.628,
    "L_TO_TEASPOON":202.884,"L_TO_TP":202.884,
    "L_TO_CUBIC-METER":0.001,"L_TO_METER^3":0.001,"L_TO_M^3":0.001,
    "L_TO_CUBIC-FOOT":0.0353147,"L_TO_FOOT^3":0.0353147,"L_TO_FT^3":0.0353147,
    "L_TO_CUBIC-INCH":61.0237,"L_TO_INCH^3":61.0237,"L_TO_IN^3":61.0237

}