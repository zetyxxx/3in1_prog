from gui import *
import sys

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.camera_mode_btn.clicked.connect(self.tab_1)
        self.neuro_mode_btn.clicked.connect(self.tab_2)
        self.threeD_mode_btn.clicked.connect(self.tab_3)

    def tab_1(self):
        self.tabWidget.setCurrentIndex(0)

    def tab_2(self):
        self.tabWidget.setCurrentIndex(1)

    def tab_3(self):
        self.tabWidget.setCurrentIndex(2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()

    sys.exit(app.exec())