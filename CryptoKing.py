#!/usr/bin/env python3
#https://github.com/emrekybs
import string,os
from time import sleep

print("""
\033[1;33m
▁ ▂ ▄ ▅ ▆ ▇ █ ℭ𝔯𝔶𝔭𝔯𝔱𝔬𝔎𝔦𝔫𝔤 █ ▇ ▆ ▅ ▄ ▂ ▁
\033[1;24m                      𝓔𝓶𝓡𝓔 𝓚𝓸𝔂𝓑𝓪𝓼𝓲 
https://github.com/emrekybs
""")

special = [
'ł',
'€',
'¶',
'ŧ',
'←',
'↓',
'→',
'ø',
'þ',
'æ',
'ß',
'ð',
'đ',
'ŋ',
'ħ',
'ĸ',
'ł',
'~',
'«',
'»',
'¢',
'“',
"'",
'µ',
'ñ',
'!',
'@',
'$', 
'%', 
'^', 
'&', 
'*', 
'(',
')', 
'-', 
'.', 
'+', 
'=', 
'_', 
',', 
'|', 
'?', 
'>', 
'<', 
'/',
'º',
'ª',
'"',
'¬',
'~',
'Ñ',
'·',
'Ł',
'{',
'}',
']',
'm',
'[',
" \ ",
'½',
'',
'\\',
'#']
numbers = [
'0',
'1',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
'9']

list = list(string.ascii_letters) + numbers + special 

def encoder():
    keyinput = input('\033[1;33m\nMESSAGE : \033[1;39m')
    keyinput2 = eval(input('\033[1;33m\nKEY [1,2,3,4,5,6,7,8,9,0] : \033[1;39m'))
    sleep(2)
    code = ''
    def encoder2(message):
        j = list.index(message)
        i = (j+keyinput2)%(len(list) - 1)
        return i
    for k in keyinput:
      if k == ' ':
         code += ' '
      else:
         l = encoder2(k)
         code += list[l]
    print('\033[1;32m\n\t\t\t[ENCRYPTING]  ')
    print("\n"+code)
    print("\n")
    optionss()

def decoder():
    keyinput = input('\033[1;33m\nCODE : \033[1;39m')
    keyinput2 = eval(input('\033[1;33m\nKEY [1,2,3,4,5,6,7,8,9,0] : \033[1;39m'))
    sleep(2)
    message = ''
    for k in keyinput:
      if k == ' ':
         message += ' '
      else:
         r = list.index(k)
         l = (r - keyinput2)%(len(list) - 1)
         message += list[l]
    print('\033[1;32m\n\t\t\t[DECRYPTING]  ')
    print("\n"+message)
    print("\n")
    optionss()
def optionss():
    print('\033[1;33m1)\033[1;39mENCODING ')
    print('\n\033[1;33m2)\033[1;39mDECODING  ')
    print('\n\033[1;33m3)\033[1;39mEXIT')
    opt= int(input("\033[1;33m\nOPTIONS : "))
    if opt == 1:
       encoder()
    elif opt == 2:
       decoder()
    else:
       exit()
optionss()
