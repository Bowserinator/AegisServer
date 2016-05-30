import string
digs = string.digits + string.letters
digs = digs.upper()

def int2base(x, base):
  if base < 2:
    return "\x035Error invalid base!"
  elif base > 36:
    return "\x035Error base too large!"
  x = int(x)
  if x < 0: sign = -1
  elif x == 0: return digs[0]
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[int(x % base)])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)

def stripZero(string):
  returned = ""
  found = False
  for i in string:
    if found == False and i == "0":
      pass
    elif i != "0" and found == False:
      found = True
      returned = returned + i
      
    elif found == True:
      returned = returned + i
  return returned