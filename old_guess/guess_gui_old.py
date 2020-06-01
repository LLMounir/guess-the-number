import sys
import random
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))

        mainWindow.resize(601, 341)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.title_fix = QtGui.QLabel(self.centralwidget)
        self.title_fix.setGeometry(QtCore.QRect(-135, -20, 860, 161))
        self.title_fix.setObjectName(_fromUtf8("title_fix"))

        self.guess = QtGui.QPushButton(self.centralwidget)
        self.guess.setGeometry(QtCore.QRect(110, 170, 380, 26))
        self.guess.setObjectName(_fromUtf8("guess"))

        self.input_user = QtGui.QLineEdit(self.centralwidget)
        self.input_user.setGeometry(QtCore.QRect(110, 130, 381, 27))
        self.input_user.setText(_fromUtf8(""))
        self.input_user.setObjectName(_fromUtf8("input_user"))

        self.display_range = QtGui.QLabel(self.centralwidget)
        self.display_range.setGeometry(QtCore.QRect(-90, 80, 601, 51))
        self.display_range.setObjectName(_fromUtf8("display_range"))

        self.abandonner = QtGui.QPushButton(self.centralwidget)
        self.abandonner.setGeometry(QtCore.QRect(470, 280, 111, 26))
        self.abandonner.setObjectName(_fromUtf8("abandonner"))
        self.abandonner.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.number_bottom = QtGui.QLCDNumber(self.centralwidget)
        self.number_bottom.setGeometry(QtCore.QRect(360, 95, 64, 23))
        self.number_bottom.setObjectName(_fromUtf8("number_bottom"))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(426, 65, 21, 80))
        self.label.setObjectName(_fromUtf8("label"))

        self.number_top = QtGui.QLCDNumber(self.centralwidget)
        self.number_top.setGeometry(QtCore.QRect(450, 95, 64, 23))
        self.number_top.setObjectName(_fromUtf8("number_top"))

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 280, 231, 26))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.guess, self.input_user)
        mainWindow.setTabOrder(self.input_user, self.abandonner)
        mainWindow.setTabOrder(self.abandonner, self.pushButton)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Guess the number !", None))
        self.title_fix.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">Devinez le nombre secret !</span></p></body></html>", None))
        self.guess.setText(_translate("mainWindow", "Guess", None))
        self.display_range.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Le nombre secret se trouve entre 0 et 100</span></p></body></html>", None))
        self.abandonner.setText(_translate("mainWindow", "Abandonner", None))
        self.label.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">et</span></p></body></html>", None))
        self.pushButton.setText(_translate("mainWindow", "Ce bouton ne sert à rien", None))


class Guess:
    def __init__(self,minimum,maximum,essais):
        self.essais = essais
        self.bottom = minimum
        self.top = maximum
        self.secret = random.randint(self.bottom,self.top)

    def set_bottom(self,new):
        self.bottom = new

    def set_top(self,new):
        self.top = new


def main():
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    partie = Guess()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
