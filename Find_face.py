import cv2 as cv
import numpy as np
from PyQt5.QtCore import qDebug
from PyQt5.QtGui import QImage, qRed, qGreen, qBlue, qRgb, QPixmap
from matplotlib import pyplot as plt
from pyqt5_plugins.examplebuttonplugin import QtGui

#人脸检测
face_engine=cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')

#qt图片转化为opencv
def QImage2CV(qimg):
    tmp = qimg

    # 使用numpy创建空的图象
    cv_image = np.zeros((tmp.height(), tmp.width(), 3), dtype=np.uint8)

    for row in range(0, tmp.height()):
        for col in range(0, tmp.width()):
            r = qRed(tmp.pixel(col, row))
            g = qGreen(tmp.pixel(col, row))
            b = qBlue(tmp.pixel(col, row))
            cv_image[row, col, 0] = b
            cv_image[row, col, 1] = g
            cv_image[row, col, 2] = r

    return cv_image



#opencv图片转化为qt
def cvToQImage(data):
    # 8-bits unsigned, NO. OF CHANNELS=1
    if data.dtype == np.uint8:
        channels = 1 if len(data.shape) == 2 else data.shape[2]
    if channels == 3: # CV_8UC3
        # Copy input Mat
        # Create QImage with same dimensions as input Mat
        img = QImage(data, data.shape[1], data.shape[0], data.strides[0], QImage.Format_RGB888)
        return img.rgbSwapped()
    elif channels == 1:
        # Copy input Mat
        # Create QImage with same dimensions as input Mat
        img = QImage(data, data.shape[1], data.shape[0], data.strides[0], QImage.Format_Indexed8)
        return img
    else:
        qDebug("ERROR: numpy.ndarray could not be converted to QImage. Channels = %d" % data.shape[2])
        return QImage()




def Find_faces(img):
    img_=img.copy()
    gray=cv.cvtColor(img_,cv.COLOR_RGB2GRAY)
    faces=face_engine.detectMultiScale(gray)
    for(x,y,w,h) in faces:
        cv.rectangle(img_,(x,y),(x+w,y+h),(0,0,255),3)
        face=img[y:y+w,x:x+h]
    return face


