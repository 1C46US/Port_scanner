import socket
from colorama import init, Fore


init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX


def port_checker(host, port):
    x = socket.socket()
    x.settimeout(0.2)
    try:
        x.connect((host, port))
    except:
        return False
    else:
        return True


host = input("Enter the host ip here: ")


for port in range(1, 1024):
    if port_checker(host, port):
        print(f'{GREEN}[+]{host}:{port} is open  {RESET}')
    else:
        print(f'{GRAY}[!]{host}:{port} is closed  {RESET}')
