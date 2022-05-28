

from socket import socket
from time import ctime, sleep

sock=socket()
sock.bind(('0.0.0.0',4567))
sock.listen(5)
# 设置非阻塞
sock.setblocking(False)
log=open('log.txt','a')
while True:
    try:
        # 没有客户端连接不会阻塞,然后报错
        con,addr=sock.accept()
    except  BlockingIOError as b:
        # ctime()当前时间
        log.write(f'{ctime()} {b}\n')
        # 刷新缓冲区
        log.flush()
        sleep(2)
    else:
        data=con.recv(1024)
        print(data.decode())

