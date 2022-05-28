from select import epoll, EPOLLIN, EPOLLET
from socket import socket, AF_INET, SOCK_STREAM

HOST='0.0.0.0'
PORT=8888
ADDR=(HOST,PORT)
map={}


def connect_client(ep, fd):
    confd,addr=map[fd].accept()
    # 设置套接字为非阻塞
    confd.setblocking(False)
    # 添加对IO的关注,默认是水平触发,但设置成边缘触发
    ep.register(confd,EPOLLIN|EPOLLET)
    map[confd.fileno()]=confd


def handle(ep, fd):
    data=map[fd].recv(1024*10)
    if not data:
        map[fd].close()
        # 从字典里移除
        del map[fd]
        # 取消对IO的关注
        ep.unregister(fd)
        return
    print(data.decode())



def main():
    sock=socket(AF_INET,SOCK_STREAM)
    sock.bind(ADDR)
    sock.listen(5)

    sock.setblocking(False)
    # 创建epoll()对象
    ep=epoll()
    # 初始关注sock套接字
    ep.register(sock,EPOLLIN)
    map[sock.fileno()]=sock
    while True:
        # 监控等待IO事件发生 返回[(),()]
        events=ep.poll()
        for fd,event in events:
            if fd==sock.fileno():
                connect_client(ep,fd)
            else:
                handle(ep,fd)