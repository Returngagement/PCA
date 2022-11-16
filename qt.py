import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import Start_the_screen
import cv2 as cv

#录入按钮被点击
def handleCalc1():
    import cv2
    import numpy as np

    def video_demo():
        print('开始')
        cap = cv2.VideoCapture(0)  # 电脑自身摄像头
        i = 0  # 定时装置初始值
        photoname = 1  # 文件名序号初始值
        while True:
            i = i + 1
            reg, frame = cap.read()
            frame = cv2.flip(frame, 1)  # 图片左右调换
            cv2.imshow('window', frame)

            if i == 50:  # 定时装置，定时截屏，可以修改。

                filename = str(photoname) + '.png'  # filename为图像名字，将photoname作为编号命名保存的截图
                cv2.imwrite('E:/PCA/' + filename, frame)  # 截图保存 frame为此时的图像
                print(filename + '保存成功')  # 打印保存成功
                i = 0  # 清零
                photoname = photoname
                if photoname >= 10:  # 最多截图10张 然后退出（如果调用photoname = 1 不用break为不断覆盖图片）
                    # photoname = 1
                    break
                photoname = photoname+1
            if cv2.waitKey(1) & 0xff == ord('q'):
                break
        # 释放资源
        cap.release()

    video_demo()
    cv2.destroyAllWindows()


#打卡签到按钮被点击
def handleCalc2():
    pass






if __name__ == '__main__':
    app=QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui= Start_the_screen.Ui_mainWindow()
    ui.setupUi(mainWindow)
    ui.retranslateUi(mainWindow)
    ui.showtime()
    ui.pushButton.clicked.connect(handleCalc1)
    ui.pushButton.clicked.connect(handleCalc2)
    mainWindow.show()
    sys.exit(app.exec_())
