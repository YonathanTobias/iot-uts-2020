import socket
from threading import Thread


#MultiThreaded Python Server class ClientThread(Thread):
def init (self,ip,port): Thread. init (self) self.ip = ip
self.port = port

def run(self): while True:
try:
data = conn.recv(1024).decode("utf-8") character_remove = "\r\n"
if len(data) == 0: break
print("Length :
{}".format(len(data.replace(character_remove,""))))
 
print("Server Received data : {}".format(data)) print(data)
MESSAGE = "OK\n"
conn.send(MESSAGE.encode("utf-8")) except Exception as e:
print(e) break

#ganti alamat IP TCP_IP = "192.168.1.6"
TCP_PORT = 2004
BUFFER_SIZE = 20

tcpServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM) tcpServer.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
tcpServer.bind((TCP_IP,TCP_PORT))
threads = []

while True:
tcpServer.listen(4)
print("Server starte on {} port {}".format(TCP_IP,str(TCP_PORT))) (conn,(ip,port)) = tcpServer.accept()
newthread = ClientThread(ip,port) newthread.start() threads.append(newthread)

for t in threads: t.join()
