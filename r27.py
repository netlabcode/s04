import psycopg2
from datetime import datetime
import binascii
import _thread
import time
import socket

PORT1 = 8804
 
conn = psycopg2.connect(host="131.180.165.7",database="CRoF",user="postgres", password="crpg")


cursor = conn.cursor()

#Value id 147 - 149
cursor.execute('''SELECT value from objects WHERE id=147''')
result = cursor.fetchone()
record1 = result[0]
cursor.execute('''SELECT value from objects WHERE id=148''')
result = cursor.fetchone()
record2 = result[0]
cursor.execute('''SELECT value from objects WHERE id=149''')
result = cursor.fetchone()
record3 = result[0]

#Value code
cursor.execute('''SELECT code from objects WHERE id=147''')
result = cursor.fetchone()
r1 = result[0]
cursor.execute('''SELECT code from objects WHERE id=148''')
result = cursor.fetchone()
r2 = result[0]
cursor.execute('''SELECT code from objects WHERE id=149''')
result = cursor.fetchone()
r3 = result[0]


try:                   
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
        s1.bind(('',PORT1))
        s1.listen()
        conn1, addr = s1.accept()
        with conn1:
            print('Server 1 from:',addr)
            while True:
                a = 1
                while a < 6:
                    #Format: mu01_id+value
                    cursor.execute('''SELECT value from objects WHERE id=147''')
                    result = cursor.fetchone()
                    if record1 != result[0]:
                        print(result[0])
                        string = "mu01_"+str(r1)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record1 = result[0]

                    cursor.execute('''SELECT value from objects WHERE id=148''')
                    result = cursor.fetchone()
                    if record2 != result[0]:
                        print(result[0])
                        string = "mu02_"+str(r2)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record2 = result[0]

                    cursor.execute('''SELECT value from objects WHERE id=149''')
                    result = cursor.fetchone()
                    if record3 != result[0]:
                        print(result[0])
                        string = "mu03_"+str(r3)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record3 = result[0]

except:
   print ("Error: unable to start thread")

while 1:
   pass

