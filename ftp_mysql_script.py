# python3 script to listen for files over ftp and send them to the database
# tutorial taken from https://pypi.org/project/pyftpdlib/
import os, sys

if not len(sys.argv) > 1:
	print("Usage: python3 ftp_mysql_script.py ip_address")
	quit()

# check to see if pyftpdlib is installed
try:
	# try to import the ftp library needed, to see if it's installed on the machine
	import pyftpdlib
	print("pyftpdlib installed")
except ModuleNotFoundError:
	print("pyftpdlib not installed. installing...")
	os.system("sudo pip3 install pyftpdlib")

#check if ftp location is present, if not, create it
if not os.path.isdir("/tmp/ftp"):
	os.system("/tmp/ftp")

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "password", "/tmp/ftp", perm="elradfmwMT") # no idea what perm does atm

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer((sys.argv[1], 21), handler)
server.serve_forever()