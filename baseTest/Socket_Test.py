__author__ = 'Test-YLL'

"""
socket服务端
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
socket客户端
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