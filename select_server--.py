from select import select
from socket import socket, AF_INET, SOCK_STREAM

HOST='0.0.0.0'
PORT=8888
ADDR=(HOST,PORT)
def connect_client(sock,rlist):
    confd, addr = sock.accept()
    confd.setblocking(False)
    rlist.append(confd)
def send_recv(con,rlist):
    data = con.recv(1024 * 10)
    if not data:
        rlist.remove(con)
        con.close()
        return
    print(data.decode())
    con.send(b'ok ok')

def main():
    sock=socket(AF_INET,SOCK_STREAM)
    sock.bind(ADDR)
    sock.listen(5)
    rlist=[sock]
    wlist=[]
    xlist=[]
    # 设置sock为非阻塞IO事件
    sock.setblocking(False)
    while True:
        rs,ws,xs=select(rlist,wlist,xlist)
        for r in rs:
            if r is sock:
                connect_client(r,rlist)
            else:
                send_recv(r,rlist)








if __name__ == '__main__':
    main()