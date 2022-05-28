"""
IO多路复用
"""
from select import select
from socket import socket, AF_INET, SOCK_STREAM
HOST='0.0.0.0'
PORT=8888
ADDR=(HOST,PORT)
def recv_send(confd,rlist,wlist):
    data = confd.recv(1024 * 20)
    if not data:
        # remove 只是从列表里把对象移除,并没有真正删除对象
        rlist.remove(confd)
        print(confd)
        confd.close()
        return
    print(data.decode())
    # confd.send(b'0k')
    wlist.append(confd)

def connect_client(sock,rlist):
    confd,addr=sock.accept()
    confd.setblocking(False)
    rlist.append(confd)

def main():
    sock=socket(AF_INET,SOCK_STREAM)
    sock.bind(ADDR)
    sock.listen(5)
    # 设置套接字为非阻塞io
    sock.setblocking(False)
    rlist=[sock]        #初始化监听套接字
    wlist=[]
    xlist=[]
    while True:
        rs,ws,xs=select(rlist,wlist,xlist)
        for r in rs:
            # 判断对象用is最合适的
            if r is sock:
                connect_client(sock,rlist)
                 # 处理客户端连接,创建套接字
                # confd, addr = r.accept()
                # # 设置套接字为非阻塞io
                # confd.setblocking(False)
                # rlist.append(confd)
            else:
                recv_send(r,rlist,wlist)
                # 这里不能写死循环
                # while True:
                    # 客户端发送请求,接受请求
                    # data=r.recv(1024*20)
                    # if not data:
                    #     rlist.remove(r)
                    #     r.close()
                    #     continue
                    # print(data.decode())
                    # r.send(b'0k')

        # 这个写操作可有可无
        for w in ws:
            w.send(b'ok')
            wlist.remove(w)

if __name__ == '__main__':
    main()