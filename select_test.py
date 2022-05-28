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
sock.bind(('0.0.0.0',5555))
sock.listen(5)

# 监控IO

rs,ws,xs=select([sock,file],[udp],[])
print('rlist',rs)
print('wlist',ws)
print('xlist',xs)

