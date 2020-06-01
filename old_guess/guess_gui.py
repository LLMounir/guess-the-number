"""
Guess the number !
GUI version 2
"""
import sys
import random
from PyQt4 import QtGui

def window():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    b = QtGui.QLabel(w)
    
    b.setText("Hello World!")
    
    w.setGeometry(1000,500,200,50)
    b.move(50,20)
    w.setWindowTitle("HELLO WORLD!")
    w.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    window()