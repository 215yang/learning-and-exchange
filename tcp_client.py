from socket import *

# 服务器地址
ADDR = ("127.0.0.1",8888)

# 创建与服务端相同类型套接字 默认参数
tcp_socket = socket()

# 连接服务端
tcp_socket.connect(ADDR)

# 发送接受
while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())
    # data=tcp_socket.recv(1024*10)
    # print(data.decode())

# 关闭
tcp_socket.close()

