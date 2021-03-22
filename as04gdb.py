import binascii
import _thread
import time
import socket
import psycopg2


HOST1 = '100.4.0.11'
HOST2 = '100.4.0.12'
HOST3 = '100.4.0.13'
HOST4 = '100.4.0.14'
HOST5 = '100.4.0.15'
HOST6 = '100.4.0.16'
PORT1 = 993
PORT2 = 994
PORTS1 = 881
PORTS2 = 883


#Database Connection
conn = psycopg2.connect(host="131.180.165.7",database="CRoF", user="postgres", password="crpg")
conn.autocommit = True
cursor = conn.cursor()

# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST1, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g
    		)

			cursor.execute(" INSERT INTO s04m1(dtime, cb_ctrl, cb_res, i_res, p_res, q_res, v_res) VALUES (%s,%s,%s,%s,%s,%s,%s)", inserted_values)

			print("1")

def serverTwo():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST2, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g
    		)

			cursor.execute(" INSERT INTO s04m2(dtime, cb_ctrl, cb_res, i_res, p_res, q_res, v_res) VALUES (%s,%s,%s,%s,%s,%s,%s)", inserted_values)

			print("2")


def serverThree():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST3, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g,h = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g,
        		h
    		)

			cursor.execute(" INSERT INTO s04m3(dtime, cb_ctrl, cb_res, f_res, i_res, p_res, q_res, v_res) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", inserted_values)

			print("3")

def serverFour():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST4, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g,h,i,j,k,l,m,n = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g,
        		h,
        		i,
        		j,
        		k,
        		l,
        		m,
        		n
    		)

			cursor.execute(" INSERT INTO s04m4(dtime, cb_ctrl, cb_res, f_res, hv_p_res, hv_q_res, ld_res, lv_p_res, lv_q_res, tap, tap_ctrl, tap_mode, tap_res, v_res) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", inserted_values)


			print("4")

def serverFive():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST5, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c= strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c
    		)

			cursor.execute(" INSERT INTO s04m5(dtime, cb_ctrl, cb_res) VALUES (%s,%s,%s)", inserted_values)

			print("5")

def serverSix():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST6, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g,h,i,j= strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g,
        		h,
        		i,
        		j
    		)

			cursor.execute(" INSERT INTO s04m6(dtime, cb_ctrl, cb_res, f_res, ld_res, p_ctrl, p_res, q_res, v_ctrl, v_res) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", inserted_values)

			print("6")


# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )
   _thread.start_new_thread( serverThree, ( ) )
   _thread.start_new_thread( serverFour, ( ) )
   _thread.start_new_thread( serverFive, ( ) )
   _thread.start_new_thread( serverSix, ( ) )

except:
   print ("Error: unable to start thread")

while 1:
   pass