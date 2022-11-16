#自定义图片测试
import cv2
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import PCA_down
#降维
pca=PCA(n_components=100)
pca.fit(PCA_down.X)
X=pca.transform(PCA_down.X)
#训练模型
model = cv2.face.EigenFaceRecognizer_create()
model.train(X, PCA_down.Y)


def Face_recognize(img):
    img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    imgs=[]
    imgs.append(img)
    #特征矩阵
    image_data=[]
    for i in imgs:
        data=img.flatten()
        image_data.append(data)
    test=np.array(image_data)
    test=pca.transform(test)
    res = model.predict(test)
    return res[0]




