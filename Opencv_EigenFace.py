#原理：将训练集图像和测试集图像都投影到特征向量空间中，再使用聚类方法（最邻近或者K临近等），
# 得到测试集中的每个图象最近的图像，进行分类
#cv2.face.EigenFaceRecognizer_create()创建人脸识别模型，通过图像数组和对应标签组来训练模型
#predict()函数进行人脸预测，该函数会返回两个元素的数组
#第一个是识别个体的标签
#第二个是置信度，越小匹配度越高，0表示完全匹配
#getEigenValues()获得特征值
#getEigenVectors()获得特征向量
#getMean()获得均值

import cv2
from matplotlib import pyplot as plt
import PCA_down



#模型创建与训练
model=cv2.face.EigenFaceRecognizer_create()
model.train(PCA_down.x_train, PCA_down.y_train)

#测试
def Test1():
    res=model.predict(PCA_down.x_test[0])
    print(res)
    print(PCA_down.y_test[0])

#计算识别率
def rate_Recognize():
    ress=[]
    true=0
    for i in range(len(PCA_down.y_test)):
        res=model.predict(PCA_down.x_test[i])
        if PCA_down.y_test[i]==res[0]:
            true=true+1
        else:
            print(i)
    print("测试集准确度为：%.2f"%(true/len(PCA_down.y_test)))

#平均脸
def Mean_face():
    mean=model.getMean()
    meanFace=mean.reshape(112,92)
    plt.imshow(meanFace)
    plt.show()
    # cv2.imshow("Mean_Face",meanFace)
    # cv2.waitKey(0)


if __name__ == '__main__':
    # 测试
    Test1()
    # 计算识别率
    rate_Recognize()
    # 平均脸
    Mean_face()

