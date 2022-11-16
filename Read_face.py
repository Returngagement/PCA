import glob
import os
import cv2 as cv




#读取地址
def read_addr(filename):
    faces_addr=[]
    labels=[]
    Name=os.listdir(filename)
    #读取记录每个人脸的地址
    for i in Name:
        Name_addr=filename+'/'+i+'/*'
        addr = glob.glob(Name_addr)
        for j in addr:
            faces_addr.append(j)
    for i in range(1,len(faces_addr)+1):
        labels.append(int((i+9)/10))
    return faces_addr,labels







