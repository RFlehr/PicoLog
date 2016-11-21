# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 21:54:03 2016

@author: Roman
"""


from pyqtgraph.Qt import QtGui, QtCore
import sys
from numpy import zeros


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        
        self._numChan = 9
        self._Channel = {0:False,
                              1:True,
                              2:False,
                              3:False,
                              4:False,
                              5:False,
                              6:False,
                              7:False,
                              8:False}
        
        self.chanLabels = []
        self.tempLabels = []
        self.temps = zeros(9)
        
        self.createChanLabels()
        self.createTempLabels()
        self.createChanSelection()
        
        l = self.createLayout()
        self.updateChanSelection()
        
        w = QtGui.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)
        
    def createChanSelection(self):
        self.chanSelect = []
        for i in range(self._numChan):
            chB = QtGui.QCheckBox()
            chB.setChecked(self._Channel[i])
            chB.stateChanged.connect(self.updateChanSelection)
            self.chanSelect.append(chB)
        
        
    def createChanLabels(self):
        self.chanLabels = []
        for i in range(self._numChan):
            _str = 'Ch' + str(i) + ':'
            self.chanLabels.append(QtGui.QLabel(text=_str))
    
    def createTempLabels(self):
        self.tempLabels = []
        for i in range(self._numChan):
            self.tempLabels.append(QtGui.QLabel(text='0.00'))
            
    def createLayout(self):
        lay = QtGui.QGridLayout()
        for i in range(self._numChan):
            lay.addWidget(self.chanSelect[i],i,0)
            lay.addWidget(self.chanLabels[i],i,1)
            lay.addWidget(self.tempLabels[i],i,2)
            lay.addWidget(QtGui.QLabel(text=u'\u00b0C'),i,3)
            
            
        return lay
            
    def updateChanSelection(self):
        for i in range(self._numChan):
            if self.chanSelect[i].isChecked():
                self.chanLabels[i].setStyleSheet("color: green")
            else:
                self.chanLabels[i].setStyleSheet("color: red")
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    test = MainWindow()
    test.show()
    app.exec_()