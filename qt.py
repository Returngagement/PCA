import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyqt5_plugins.examplebutton import QtWidgets
import LuRu
import Start_the_screen
import cv2 as cv
import sys



# def Luru():
#     app = QApplication(sys.argv)
#     mainWindow = QMainWindow()
#     u = LuRu.Ui_LuRu_Window()
#     u.setupUi(mainWindow)
#     u.retranslateUi(mainWindow)
#     mainWindow.show()
#     sys.exit(app.exec_())

class Start(QMainWindow, Start_the_screen.Ui_Start_Window):
    def __init__(self):
        super(Start,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

class Child(QMainWindow, LuRu.Ui_LuRu_Window):
    def __init__(self):
        super(Child,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def Open(self):
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    # mainWindow = QMainWindow()
    # ui = Start_the_screen.Ui_Start_Window()
    # ui.setupUi(mainWindow)
    # ui.retranslateUi(mainWindow)
    # ui.showtime()
    # mainWindow.show()
    # sys.exit(app.exec_())
    start=Start()
    child=Child()
    start.show()
    start.pushButton.clicked.connect(child.Open)
    sys.exit(app.exec_())


