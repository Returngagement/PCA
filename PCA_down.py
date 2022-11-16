import matplotlib.pyplot as plt
import numpy as np
import Read_face
import cv2 as cv
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split


faces_addr,labels= Read_face.read_addr('./Photos')
images=[]
for face in faces_addr:
    image=cv.imread(face,0)
    images.append(image)
#将图片矩阵转化为一行数据
image_data=[]
for image in images:
    data=image.flatten()
    image_data.append(data)

#转换为np
X=np.array(image_data)
Y=np.array(labels)
# print(labels)


#画出特征矩阵
data=pd.DataFrame(X)
data.head()



#划分数据集
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2)
#训练PCA模型
pca=PCA(n_components=100)
# pca=PCA(n_components=100)
pca.fit(x_train)

#返回测试集和训练集降维后的数据集
x_train_pca=pca.transform(x_train)
x_test_pca=pca.transform(x_test)
# print(x_train_pca.shape)
# print(x_test_pca.shape)

#画出特征脸
def Characteristic_face():
    V=pca.components_
    # print(V.shape)
    fig,axes=plt.subplots(10,10
                          ,figsize=(15,15)
                          ,subplot_kw={"xticks":[],"yticks":[]}#不显示坐标轴
                          )
    #填充图像
    for i,ax in enumerate(axes.flat):
        ax.imshow(V[i,:].reshape(112,92),cmap="gray")
    plt.show()

#查看降维后每个新特征向量所占信息占原始数据总信息量的百分比
#又叫做可解释方差贡献率
def rate_information():
    print(pca.explained_variance_ratio_)
    #返回特征所携带的数据信息比
    print(pca.explained_variance_ratio_.sum())

#画出特征个数和所携带信息数的曲线图
def Dimension_information():
    explained_variance_ratio=[]
    for i in range(1,151):
        pca=PCA(n_components=i).fit(x_train)
        explained_variance_ratio.append(pca.explained_variance_ratio_.sum())
    plt.plot(range(1,151),explained_variance_ratio)
    plt.show()



if __name__ == '__main__':
    Characteristic_face()#画出特征脸

    # 查看降维后每个新特征向量所占信息占原始数据总信息量的百分比
    # 又叫做可解释方差贡献率
    rate_information()

    # 画出特征个数和所携带信息数的曲线图
    Dimension_information()