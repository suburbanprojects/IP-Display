import socket
import urllib.request
from pyfiglet import Figlet

def localip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    localIP = s.getsockname()[0]
    return localIP

def publicip():
    external_ip = urllib.request.urlopen('http://myip.dnsomatic.com').read().decode('utf8')
    return external_ip

f = Figlet(font='cybermedium')
print(f.renderText('Display IP'))
print("1. Show local IP ")
print("2. Show public IP")
print("3. Quit")

while True:
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        print(localip())

    if choice == '2':
        print(publicip())

    if choice == '3':
        break 
