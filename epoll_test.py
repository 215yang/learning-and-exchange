"""
多路复用方法      select
"""
from select import *
from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM
# 创建IO对象
file=open('log.txt','rb')       #具备读写事件
# 有写事件
udp=socket(AF_INET,SOCK_DGRAM)
# 监听套接字只有读事件
sock=socket(AF_INET,SOCK_STREAM)
sock.bind(('0.0.0.0',8888))
sock.listen(5)
print(sock.fileno())        #文件描述符

map={}
# 创建epoll对象
ep=epoll()
# 关注IO对象的读事件
ep.register(sock,EPOLLIN)
ep.register(udp,EPOLLIN)
# epoll()不关注文件对象
# ep.register(file,EPOLLIN)
map[sock.fileno()]=sock         #文件描述符作为键,IO对象作为值.


print('开始监控')
events=ep.poll()        #阻塞等待
print('events:',events)         #[(5, 1)]

for e in events:
    confd,addr=map[e[0]].accept()



