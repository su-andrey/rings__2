import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 10, 141, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Сгенерировать"))


class Main(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setting = False
        self.colors = ['Red', 'Blue', 'Orange', 'Yellow', 'Black', 'Green', 'Purple', 'Brown', 'Magenta']
        self.pushButton.clicked.connect(self.cond)

    def cond(self):
        self.setting = True
        self.update()

    def paintEvent(self, event):
        if self.setting:
            qp = QPainter()
            qp.begin(self)
            self.draw_element(qp)
            qp.end()

    def draw_element(self, qp):
        qp.setBrush(QColor(random.choice(self.colors)))
        x, y = random.randint(1, 600), random.randint(1, 600)
        if x >= 300:
            max_x = 600 - x
        else:
            max_x = x
        if y >= 300:
            max_y = 600 - y
        else:
            max_y = y
        r = min(max_x, max_y)
        qp.drawEllipse(x, y, r, r)
        self.setting = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    exit(app.exec())
