import os
# Host name
import platform
print(platform.node())

# Or
import socket
print(socket.gethostname())

# IP ADDRESS
import socket
print(socket.gethostbyname(socket.gethostname()))

# COMPUTER NAME
import os
print(os.environ["COMPUTERNAME"])