import binascii
import _thread
import time
import socket
import time
import sqlite3
from sqlite3 import Error
import datetime

#Predefined parameters
MU01 = '100.14.0.11'
MU02 = '100.14.0.12'
MU03 = '100.14.0.13'
PORT1 = 991
PORT2 = 992


def serverXMUCC():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx1:
		sx1.connect((MU01, PORT2))

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx2:
			sx2.connect((MU02, PORT2))

			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx3:
				sx3.connect((MU03, PORT2))


				bx = 1
				value2x=0
				while bx < 6:
					#covert inetger to string
					print("Format: mu01_id+value")
					stringx = str(input("Command entry: "))
					print(stringx)
					part1,part2 = stringx.split("_")
	
					if 'mu01' in stringx:
						part1,part2 = stringx.split("_")
						part2x = part2.encode()
						print(part2x)
						sx1.sendall(part2x)
					elif 'mu02' in stringx:
						part1,part2 = stringx.split("_")
						print(part2)
						part2x = part2.encode()
						sx2.sendall(part2x)
					elif 'mu03' in stringx:
						part1,part2 = stringx.split("_")
						print(part2)
						part2x = part2.encode()
						sx3.sendall(part2x)
					else:
						print(".")
					time.sleep(1)
					#sx2.close()
												


# Create two threads as follows
try:
   _thread.start_new_thread( serverXMUCC, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
