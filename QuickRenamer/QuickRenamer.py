# -*- coding: utf-8 -*-
import re
from maya import cmds
from PySide2.QtWidgets import * 
from PySide2.QtGui import *
from PySide2.QtCore import * 
from PySide2.QtCore import Qt
from shiboken2 import wrapInstance
from maya import OpenMayaUI
#-------------------------------------------------------
# Base
#-------------------------------------------------------
def baseWindow():
    mainWindow = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(mainWindow), QWidget)
#-------------------------------------------------------
# Main
#-------------------------------------------------------  
class Gui(QDialog):
    
    def __init__(self, parent=baseWindow()):
        super(Gui, self).__init__(parent)
        self.palette()
        self.alphaBox()
        self.design()
    #---------------------------------------------------
    # Design
    #---------------------------------------------------
    def design(self):
        self.setWindowTitle('Quick Renamer for Maya')
        self.setWindowFlags(QtCore.Qt.Dialog|QtCore.Qt.WindowCloseButtonHint)
        self.setStyleSheet(self.backColor)
        self.setFixedSize(257, 315)
        self.numberBox = []
        self.groupBox = []
        self.layoutBox = []
        self.labelBox = []
        self.labelTextBox = [" Name", " Prefix", " Suffix", " Search", " Replace"]
        self.editBox = []
        self.outputLayout = QVBoxLayout(self)
        for i in range(6):
            self.groupBox.append(QGroupBox())
            self.groupBox[i].setFixedSize(235, 40)
            self.layoutBox.append(QHBoxLayout())
            self.groupBox[i].setLayout(self.layoutBox[i]) 
            self.outputLayout.addWidget(self.groupBox[i])

            self.groupBox[i].setStyleSheet(self.groupColor)
            if i == 0:
                self.numberBox.append(QComboBox())
                self.numberBox[i].addItems(["Default", "Number", "ALPHABET", "alphabet"])
                self.numberBox[i].setStyleSheet(self.labelColor)
                self.layoutBox[i].addWidget(self.numberBox[i])
                
            else:
                self.labelBox.append(QLabel(self.labelTextBox[i-1]))
                self.labelBox[i-1].setFixedSize(60, 20)
                self.labelBox[i-1].setAlignment(Qt.AlignLeft | Qt.AlignLeft)
                self.labelBox[i-1].setStyleSheet(self.labelColor)

                self.editBox.append(QLineEdit())
                self.editBox[i-1].setStyleSheet(self.editColor)
                self.layoutBox[i].addWidget(self.labelBox[i-1])
                self.layoutBox[i].addWidget(self.editBox[i-1])

        # Instance
        self.numberBox = self.numberBox[0]
        self.nameEdit = self.editBox[0]
        self.prefixEdit = self.editBox[1]
        self.suffixEdit = self.editBox[2]
        self.searchEdit = self.editBox[3]
        self.replaceEdit = self.editBox[4]
        # Connect
        self.nameEdit.textEdited.connect(lambda:self.callBackColor(self.changeColor, 
        self.editColor, self.editColor, self.editColor, self.editColor))
        self.prefixEdit.textEdited.connect(lambda:self.callBackColor(self.editColor, 
        self.changeColor, self.editColor, self.editColor, self.editColor))
        self.suffixEdit.textEdited.connect(lambda:self.callBackColor(self.editColor, 
        self.editColor, self.changeColor, self.editColor, self.editColor))
        self.searchEdit.textEdited.connect(lambda:self.callBackColor(self.editColor, 
        self.editColor, self.editColor, self.changeColor, self.editColor))
        self.replaceEdit.textEdited.connect(lambda:self.callBackColor(self.editColor, 
        self.editColor, self.editColor, self.editColor, self.changeColor))
        self.nameEdit.returnPressed.connect(self.nameSet)
        self.prefixEdit.returnPressed.connect(self.prefixSet)
        self.suffixEdit.returnPressed.connect(self.suffixSet)
        self.replaceEdit.returnPressed.connect(self.replaceSet)
    #---------------------------------------------------
    # Parameter
    #---------------------------------------------------
    def palette(self):
        self.backColor = "background:qlineargradient(x2:1, y1:0, x2:1, y2:1, stop:0.3#aa4b6b, stop:0.5#6b6b83 stop:0.8#3b8d99)"
        self.groupColor = "background:rgba(158, 200, 226, 0.2);color:#f5f5f5;border-style:solid;border-width:0.2px;border-color:#f5f5f5;border-radius:4px"
        self.labelColor = "background:rgba(255, 255, 255, 0);color:#f5f5f5;border-color:#f5f5f5;font-weight:bold"
        self.editColor = "background:rgba(158, 200, 226, 0.2);color:#f5f5f5;border-color:#f5f5f5;font-weight:bold"
        self.changeColor = "background:rgba(158, 200, 226, 0.5);color:#f5f5f5;border-color:#f5f5f5;font-weight:bold"
    
    def alphaBox(self):
        self.ALPHALIST = [chr(i) for i in range(65,65+26)]
        self.alphalist = [chr(i) for i in range(97,97+26)]
    #---------------------------------------------------
    # Processing
    #---------------------------------------------------
    def callBackColor(self, color0, color1, color2, color3, color4):
        self.nameEdit.setStyleSheet(color0)
        self.prefixEdit.setStyleSheet(color1)
        self.suffixEdit.setStyleSheet(color2)
        self.searchEdit.setStyleSheet(color3)
        self.replaceEdit.setStyleSheet(color4)
          
    def nameSet(self):
        cmds.undoInfo(openChunk=True)
        selection = cmds.ls(sl=True)
        if self.numberBox.currentText() == 'Default':
            for i in range(len(selection)):
                cmds.rename(self.nameEdit.text())
                
        elif self.numberBox.currentText() == 'Number':
            for i in range(len(selection)):
                cmds.rename('{}{}'.format(self.nameEdit.text(), str(i)))
                
        elif self.numberBox.currentText() == 'ALPHABET':
            for i in range(len(selection)):
                cmds.rename('{}{}'.format(self.nameEdit.text(), self.ALPHALIST[i]))
                
        elif self.numberBox.currentText() == 'alphabet':
            for i in range(len(selection)):
                cmds.rename('{}{}'.format(self.nameEdit.text(), self.alphalist[i]))
        
        cmds.undoInfo(closeChunk=True)
    
    def prefixSet(self):
        cmds.undoInfo(openChunk=True)
        selection = cmds.ls(sl=True)
        if self.numberBox.currentText() == 'Default':
            for i in range(len(selection)):
                cmds.rename('{}{}'.format(self.prefixEdit.text(), 
                selection[i].split("|")[-1:][0]))
                
        elif self.numberBox.currentText() == 'Number':
            for i in range(len(selection)):
                cmds.rename('{}{}'.format(self.prefixEdit.text() + str(i), 
                selection[i].split("|")[-1:][0]))
                
        elif self.numberBox.currentText() == 'ALPHABET':
            for i in range(len(selection)):
                cmds.rename('{}{}'.format(self.prefixEdit.text() + self.ALPHALIST[i], 
                selection[i].split("|")[-1:][0]))
                
        elif self.numberBox.currentText() == 'alphabet':
            for i in range(len(selection)):
                cmds.rename('{}{}'.format(self.prefixEdit.text() + self.alphalist[i], 
                selection[i].split("|")[-1:][0]))
        
        cmds.undoInfo(closeChunk=True)
        
    def suffixSet(self):
        cmds.undoInfo(openChunk=True)
        selection = cmds.ls(sl=True)
        if self.numberBox.currentText() == 'Default':
            for i in range(len(selection)):
                cmds.rename('{}{}'.format(selection[i].split("|")[-1:][0], 
                self.suffixEdit.text()))
                    
        elif self.numberBox.currentText() == 'Number':
            for i in range(len(selection)):
                cmds.rename('{}{}'.format(selection[i].split("|")[-1:][0], 
                self.suffixEdit.text() + str(i)))
                
        elif self.numberBox.currentText() == 'ALPHABET':
            for i in range(len(selection)):
                cmds.rename('{}{}'.format(selection[i].split("|")[-1:][0], 
                self.suffixEdit.text() + self.ALPHALIST[i]))
                
        elif self.numberBox.currentText() == 'alphabet':
            for i in range(len(selection)):
                cmds.rename('{}{}'.format(selection[i].split("|")[-1:][0], 
                self.suffixEdit.text() + self.alphalist[i]))
        
        cmds.undoInfo(closeChunk=True)
        
    def replaceSet(self):
        cmds.undoInfo(openChunk=True)
        selection = cmds.ls(sl=True)
        if self.numberBox.currentText() == 'Default':
            for i in range(len(selection)):
                replaceName = re.sub(self.searchEdit.text(), self.replaceEdit.text(), selection[i].split("|")[-1:][0])
                cmds.rename(replaceName)
            
        elif self.numberBox.currentText() == 'Number':
            for i in range(len(selection)):
                replaceNum = self.replaceEdit.text() + str(i)
                replaceName = re.sub(self.searchEdit.text(), replaceNum, selection[i].split("|")[-1:][0])
                cmds.rename(replaceName)
            
        elif self.numberBox.currentText() == 'ALPHABET':
            for i in range(len(selection)):
                replaceALPHA = self.replaceEdit.text() + self.ALPHALIST[i]
                replaceName = re.sub(self.searchEdit.text(), replaceALPHA, selection[i].split("|")[-1:][0])
                cmds.rename(replaceName)
            
        elif self.numberBox.currentText() == 'alphabet':
            for i in range(len(selection)):
                replaceALPHA = self.replaceEdit.text() + self.alphalist[i]
                replaceName = re.sub(self.searchEdit.text(), replaceALPHA, selection[i].split("|")[-1:][0])
                cmds.rename(replaceName)
            
        cmds.undoInfo(closeChunk=True)
#-------------------------------------------------------
# Show
#-------------------------------------------------------
def main():
    
    G = Gui()
    G.show()

if __name__ == '__main__':
    
    G = Gui()
    G.show()
