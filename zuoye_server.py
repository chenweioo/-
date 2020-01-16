"""
    学生录入信息服务端
"""
from socket import *
import struct
sockfd=socket(AF_INET,SOCK_DGRAM)
st=struct.Struct("i20sif")
ADDR=("0.0.0.0",5555)
sockfd.bind(ADDR)
f=open("/home/tarena/student.txt","a")
while True:
    data,ADDR=sockfd.recvfrom(1024)
    word=st.unpack(data)
    if word[3]>90:
        name=word[1].decode().strip("\x00")
        info="%d %s %d %d\n"%(word[0],name,word[2],word[3])
        f.write(info)
        f.flush()


f.close()
sockfd.close()