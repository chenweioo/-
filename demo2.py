"""
    tcp客户端流程
"""
from socket import *
# 默认情况就是tcp套接字
sockfd=socket()
#链接服务器
server_addr=('172.40.91.244',8888)
sockfd.connect(server_addr)
#发送 接收
# f=open("timg.jpeg","rb")
while True:
    # p=f.read()
    msg=input(">>")
    # msg=f.read()
    if not msg:
        break
    sockfd.send(msg.encode())
    if msg=="##":
        break
    data=sockfd.recv(2**32)
    print("from server:",data.decode())


sockfd.close()