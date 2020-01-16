"""
    tcp 服务端流传
    重点代码
"""
from socket import*
#创建 套接字
sockfd=socket(AF_INET,SOCK_STREAM)
#绑定网址
sockfd.bind(('0.0.0.0',8888))
#监听套接字
sockfd.listen(3)
#设置端口立即重用
sockfd.setsockopt(SOL_SOCKET,SOCK_STREAM,1)
# g=open("/home/tarena/未命名2.jpeg","wb+")
while True:
#等待客户端链接请求
    print("等待链接")
    connfd,addr=sockfd.accept()
    print("conneck from",addr)
    #消息收发
    while True:
        data=connfd.recv(2**32)
        if not data:# 返回为空 客户端停止
            break
        if data==b"##":
            break
        # g.write(data)
        print("receive:",data)
        n=connfd.send(b"THANK")
        print("发送了%d个字节")

    #关闭套接字和链接
g.close()
sockfd.close()
# connfd.close()