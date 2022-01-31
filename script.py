#TODO: add database connections and extract data from front-end
# python3 script to listen for files over ftp and send them to the database
# tutorial taken from https://pypi.org/project/pyftpdlib/
import os, sys

# print usage statement if no ip address is specified
if (len(sys.argv)) < 2:
	print("Usage: python3 script.py ip_address")
	quit()

# check to see if libraries needed are installed
try:
	# try to import the libraries needed, to see if they are installed on the machine
	import pyftpdlib
	print("pyftpdlib installed")
except ModuleNotFoundError:
	print("pyftpdlib not installed. installing...")
	os.system("pip3 install pyftpdlib socket")

#check if ftp location is present, if not, create it
if not os.path.isdir("C:\\Windows\\Temp\\ftp"):
	os.system("mkdir C:\\Windows\\Temp\\ftp")

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "password", "C:\\Windows\\Temp\\ftp", perm="elradfmwMT") # no idea what perm does atm

handler = FTPHandler
handler.authorizer = authorizer

print(len(sys.argv))
server = FTPServer((sys.argv[1], 21), handler)

server.serve_forever()