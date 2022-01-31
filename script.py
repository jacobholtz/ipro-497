# python3 script to listen for files over ftp and send them to the database
# tutorial taken from https://pypi.org/project/pyftpdlib/
import os


# check to see if pyftpdlib is installed
try:
	# try to import the ftp library needed, to see if it's installed on the machine
	import pyftpdlib
	print("pyftpdlib installed")
except ModuleNotFoundError:
	print("pyftpdlib not installed. installing...")
	os.system("pip3 install pyftpdlib")

#check if ftp location is present, if not, create it
if not os.path.isdir("C:\\Windows\\Temp\\ftp"):
	os.system("mkdir C:\\Windows\\Temp\\ftp")

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("test", "password", "C:\\Windows\\Temp\\ftp", perm="elradfmwMT") # no idea what perm does atm

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()