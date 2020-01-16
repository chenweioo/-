"""
    udp客户端流程
"""
from socket import *
#服务器地址
ADDR=('127.0.0.1',2222)
#创建套接字
sockfd=socket(AF_INET,SOCK_DGRAM)

#循环发送消息
while True:
    data=input('>>')
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr=sockfd.recvfrom(1024)
    print("from server:",msg.decode())

sockfd.close()



