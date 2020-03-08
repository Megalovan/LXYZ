#调档*3，记录当下时间 2020/3/8/22:10
import socket
import time 
HOST = '172.16.0.4'
PORT = 8888

class User:
	empCount = 0
	def __init__(self, time, name, speed, intensity, angle):
		self.time = time
		self.name = name
		self.trainSpeed = speed
		self.trainIntensity = intensity
		self.trainAngle = angle
		User.empCount += 1
	
	def displayUser(self):
		print('Training time:', self.time, '\nUser name:', self.name, '\nTraining speed:', self.trainSpeed, '\nTraining intensity:', self.trainIntensity, '\nTraining angle:', self.trainAngle)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind((HOST, PORT))  
sock.listen(5)
conn, addr = sock.accept()
conn.send('START'.encode())
msg = conn.recv(1024).decode()
if msg:
	if msg[-4:] == 'test':
		name = msg
Time = time.asctime(time.localtime(time.time()))
speed = input('speed>>:')
conn.send(speed.encode())
intensity = input('intensity>>:')
conn.send(intensity.encode())
angle = input('angle>>:')
conn.send(angle.encode())

user1 = User(Time, name, speed, intensity, angle)
user1.displayUser()
while True:
	s = conn.recv(1024).decode()
	if s:
		print('Message from raspi:', s)
	if s == 'quit':
		break;
conn.close;
sock.close;
'''
print('This is centos server. Waiting for connection......')  
conn, addr = sock.accept()
print('Connection seccess!') 
buf = conn.recv(1024)
if buf:
	print(buf.decode())
	conn.send(b'welcome to server, Rasbpi-v-~') 
while True:
	s = 'START'
	print('Send START to the client')
	conn.send(s.encode());
	if s == 'quit':
		break;
	IF conn.recv(1024)
		msg = conn.recv(1024.decode())
	if msg[-4:] == '2020':
		time = msg
	if msg[-4:] == 'test':
		name = msg
	user1 = User(time, name)	
user1.displayUser()
conn.close()
sock.close()'''
