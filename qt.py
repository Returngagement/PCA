import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyqt5_plugins.examplebutton import QtWidgets
import Start_the_screen
import cv2 as cv
import sys
import Photo
import attendance_interface
import sign_in



class Start(QMainWindow, Start_the_screen.Ui_Start_Window):
    def __init__(self):
        super(Start,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    start=Start()
    start.show()
    window = Photo.mywindow()
    Face_window= sign_in.mywindow()
    start.pushButton.clicked.connect(window.open)
    start.pushButton_2.clicked.connect(Face_window.open)
    sys.exit(app.exec_())


