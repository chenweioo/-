"""
    udp套接字服务端
    重点代码
"""
from socket import *


def get_word(word):
    f=open("dict.txt")
    for line in f:
        w = line.split(" ", 1)[0]  # 提取单词
        if w > word:
            f.close()
            return "没有该单词"

        elif w == word:
            f.close()
            return line
    else:
        f.close()
        return ">>没有找到该单词"
#创建套接字
sockfd=socket(AF_INET,SOCK_DGRAM)
#绑定地址
server_addr=("127.0.0.1",2222)
sockfd.bind(server_addr)

#循环收发消息

while True:
    data,addr=sockfd.recvfrom(1024)
    word=get_word(data.decode())
    print("收到消息:",data.decode())
    sockfd.sendto(word.encode(),addr)

sockfd.close()