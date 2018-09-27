__author__ = 'Test-YLL'

"""
TCP socket服务端
"""
import socket

HOST=''
PORT=10888
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr = s.accept()
print('Client\'s Address:',addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Receive Data:",data.decode('utf-8'))
    conn.send(data)
conn.close()

"""
TCP socket客户端
"""
import socket

HOST='localhost'
PORT=10888
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
data = "你好！"
while data:
    s.sendall(data.encode('utf-8'))
    data = s.recv(512)
    print("Receive form server:\n",data.decode('utf-8'))
    data = input('please input a info:\n')
s.close()

"""
UDP socket服务端
"""
import socket

HOST=''
PORT=10888
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT))
data = True
while data:
    data,address = s.recvfrom(1024)
    if data==b'bye':
        break
    print("Received String:",data.decode('utf-8'))
    s.sendto(data,address)
s.close()

"""
UDP socket客户端
"""
import socket

HOST='localhost'
PORT=10888
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data = "你好！"
while data:
    s.sendto(data.encode('utf-8'),(HOST,PORT))
    if data =='bye':
        break
    data,addr = s.recvfrom(512)
    print("Receive form server:\n",data.decode('utf-8'))
    data = input('please input a info:\n')
s.close()


