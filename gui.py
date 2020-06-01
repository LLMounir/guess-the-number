# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(774, 515)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 10, 741, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 20, 16, 441))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 450, 741, 21))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(750, 20, 16, 441))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.lbl_title = QtGui.QLabel(self.centralwidget)
        self.lbl_title.setEnabled(True)
        self.lbl_title.setGeometry(QtCore.QRect(20, 20, 741, 51))
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(18, 80, 741, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lcd_bottom = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcd_bottom.setSmallDecimalPoint(False)
        self.lcd_bottom.setDigitCount(3)
        self.lcd_bottom.setProperty("intValue", 0)
        self.lcd_bottom.setObjectName(_fromUtf8("lcd_bottom"))
        self.horizontalLayout_2.addWidget(self.lcd_bottom)
        self.lcd_secret = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcd_secret.setEnabled(True)
        self.lcd_secret.setDigitCount(3)
        self.lcd_secret.setObjectName(_fromUtf8("lcd_secret"))
        self.horizontalLayout_2.addWidget(self.lcd_secret)
        self.lcd_top = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcd_top.setDigitCount(3)
        self.lcd_top.setProperty("intValue", 100)
        self.lcd_top.setObjectName(_fromUtf8("lcd_top"))
        self.horizontalLayout_2.addWidget(self.lcd_top)
        self.btn_guess = QtGui.QPushButton(self.centralwidget)
        self.btn_guess.setGeometry(QtCore.QRect(510, 241, 111, 31))
        self.btn_guess.setObjectName(_fromUtf8("btn_guess"))
        self.lineedit_input = QtGui.QLineEdit(self.centralwidget)
        self.lineedit_input.setGeometry(QtCore.QRect(390, 242, 113, 30))
        self.lineedit_input.setObjectName(_fromUtf8("lineedit_input"))
        self.lbl_too_high = QtGui.QLabel(self.centralwidget)
        self.lbl_too_high.setEnabled(False)
        self.lbl_too_high.setGeometry(QtCore.QRect(40, 184, 330, 260))
        self.lbl_too_high.setObjectName(_fromUtf8("lbl_too_high"))
        self.lbl_too_low = QtGui.QLabel(self.centralwidget)
        self.lbl_too_low.setGeometry(QtCore.QRect(40, 210, 330, 260))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lbl_too_low.setFont(font)
        self.lbl_too_low.setObjectName(_fromUtf8("lbl_too_low"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lbl_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Guess The Number !</span></p></body></html>", None))
        self.btn_guess.setText(_translate("MainWindow", "Guess !", None))
        self.lbl_too_high.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600; color:#c50000;\">TOO HIGH !</span></p></body></html>", None))
        self.lbl_too_low.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600; color:#c50000;\">TOO LOW</span></p><p><br/></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
