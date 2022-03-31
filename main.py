# Import lib socket for connections:
from http import client
import socket

# Colors
GREEN = "\033[0;32m"
RED = "\033[1;31m"
BLUE  = "\033[1;34m"
BOLD    = "\033[;1m"
RESET = "\033[0;0m"

# Target is placed by the user:
print('============================================')
print(BLUE + '# Scanner TCP/IP 0.1 by LucasL1K3Melo' + RESET)
print('============================================')
target = input('# Digite o IP/Domínio: ')

# Loop for TCP connections (65535x) <- number of tcp doors that exist:
for door in range(1, 65535):
    client = socket.socket()
    client.settimeout(0.06)

    # If the door is closed, display then in the screen:
    # Caution: Generate a lot of data in console:
    
    # # #
    # if client.connect_ex((target, door)) != 0:
    #        print(RED + '[!]' + RESET + ' Porta Fechada => ', door)
    # # #

    # If the door is open, print then in the screen:
    if client.connect_ex((target, door)) == 0:
        print(GREEN + '[#]' + RESET + ' Porta Aberta => ', door)

        