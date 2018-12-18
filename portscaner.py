import socket
import subprocess
import sys
from datetime import datetime 


subprocess.call("clear")


remoteserver = input("Enter your ip :")
remoteserverip =socket.gethostbyname(remoteserve)


print("-"*60)
print("pleas waite :")
print("-"*60)

t1 =datetime.now()

try:
    for port in range(1,50):
        sock = socket.socket(socket.AF_INET,sock_stream)
        natije = sock.connect_ex((remoteserverip,port))

        if natije == o:
            print("port {} :              open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("you enter ctrl + z")
    sys.exit()
except socket.gaierror:
    print("is not difinde")                
except socket.error:
    print("server error")
    sys.exit()



t2 = datetime.now()



t3 = t2 -t1


print("scan finish in :" ,t3)


