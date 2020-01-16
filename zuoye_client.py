"""
    学生录入信息客户端
"""
from socket import *
import struct
# def get_info():
# class Student:
#     def __init__(self,id=0,name="",age=0,score=0):
#         self.id=id
#         self.name=name
#         self.age=age
#         self.score=score
#         self.list_st=[]

st=struct.Struct("i20sif")
s=socket(AF_INET,SOCK_DGRAM)
ADDR=(("0.0.0.0",5555))
while True:
    print("================================================")
    id=int(input("录入学生id："))
    name=input("录入学生姓名：")
    age=int(input("录入学生年龄："))
    score=float(input("录入学生分数："))
    data=st.pack(id,name.encode(),age,score)
    s.sendto(data,ADDR)
s.close()