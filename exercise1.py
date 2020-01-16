"""
    服务端，接受图片
"""
from socket import *
sockfd=socket(AF_INET,SOCK_STREAM)
sockfd.bind(("0.0.0.0",2222))
sockfd.listen(3)
g=open("/home/tarena/未命名.jpeg","wb")
while True:
    connfd, addr = sockfd.accept()
    print("接收地址为",addr)
    data=connfd.recv(2**32)
    if not data:
        break
    g.write(data)

sockfd.close()
connfd.close()
g.close()

