"""
    客户端，发送图片
"""
from socket import *
sockfd=socket(AF_INET,SOCK_STREAM)
sockfd.connect(("0.0.0.0",2222))
f=open("timg.jpeg","rb")
while True:
    data=f.read(2**32)
    if not data:
        break
    sockfd.send(data)
f.close()
sockfd.close()