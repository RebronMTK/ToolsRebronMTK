# author : @RebronMTK
# -*- coding: utf-8 -*-

import os
import sys
import fileinput

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'

banner = """
\033[1;33m◈➢Credits by  : RebronMTK
\033[1;31m██████╗░███████╗██████╗░██████╗░░█████╗░███╗░░██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗░██║
██████╔╝█████╗░░██████╦╝██████╔╝██║░░██║██╔██╗██║
\033[1;37m██╔══██╗██╔══╝░░██╔══██╗██╔══██╗██║░░██║██║╚████║  
██║░░██║███████╗██████╦╝██║░░██║╚█████╔╝██║░╚███║
╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝
\033[1;36m◈➢TG CH: @RebronMTKV1
"""

banner2 = """
   {}[{}1{}]{} \033[35mEncript      {}[{}2{}]{} \033[1;34mDecrypt
""".format(G,W,G,W,G,W,G,W)

print banner
print banner2

def dekrip():
   try:
       sc = raw_input(ask + W + "Script " + G + "> " + W)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       out = raw_input(ask + W + "Output" + G + " > " + W)
       f = open(out,'w')
       f.write(newdata)
       f.close()

       os.system("touch tes.sh")
       os.system("bash " + out + " > tes.sh")
       os.remove(out)
       os.system("mv -f tes.sh " + out)
       print (sukses + "Done..")

   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Not Found!")

def enkrip():
   try:
       script = raw_input(ask + W + "Script " + G + "> " + W)
       output = raw_input(ask + W + "Output " + G + "> " + W)
       os.system("bash-obfuscate " + script + " -o " + output )
       print (sukses + "Done..")
   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Not Found!")


takok = raw_input(W + "Choose" + G + " > ")

if takok == "1" or takok == "01":
   enkrip()
elif takok == "2" or takok == "02":
   dekrip()
else:
   print (eror + " Wrong input")
