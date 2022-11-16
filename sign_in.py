import os
import sys

from PyQt5.QtMultimedia import QCamera, QCameraImageCapture
from pyqt5_plugins.examplebutton import QtWidgets
from pyqt5_plugins.examplebuttonplugin import QtGui
import cv2 as cv
import Find_face
import Recognize_face
import attendance_interface

class mywindow(QtWidgets.QMainWindow, attendance_interface.Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)



    def open(self):
        self.show()
        # 创建摄像头实例
        self.camer = QCamera()

        # 设置摄像头的捕获模式
        # 拍照模式 QCamera.CaptureMode.CaptureStillImage
        # 取景器模式 QCamera.CaptureMode.CaptureViewfinder
        # 视频录制模式 QCamera.CaptureMode.CaptureVideo
        self.camer.setCaptureMode(QCamera.CaptureMode.CaptureStillImage)

        # 将摄像头实例放入相对应的组件中
        self.camer.setViewfinder(self.widget)

        # 创建一个用于摄像头拍照的类
        self.capture = QCameraImageCapture(self.camer)

        # 开启摄像机
        self.camer.start()

        # 给签到按钮绑定函数
        self.pushButton.clicked.connect(self.save_img)

    def save_img(self):
        # 拍摄图片
        self.capture.capture()
        # 把拍摄的图像保存到缓存
        self.capture.setCaptureDestination(QCameraImageCapture.CaptureDestination.CaptureToBuffer)
        # 如果成功保存到缓存，会自动发送一个imageCapture信号
        self.capture.imageCaptured.connect(self.message_save)

    def message_save(self, id, img: QtGui.QImage):
        # 人脸检测
        img1 = Find_face.QImage2CV(img)
        face = Find_face.Find_faces(img1)
        face1 = cv.resize(face, (112, 92))
        res = Recognize_face.Face_recognize(face1)
        if len(str(res)) == 0:
            print("打开失败")
        else:
            print("工号", res, "打卡成功")
            self.close()
        self.capture.imageCaptured.disconnect(self.message_save)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())