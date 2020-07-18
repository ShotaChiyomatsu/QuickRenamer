# -*- coding: utf-8 -*-
import re
from maya import cmds
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Qt
from shiboken2 import wrapInstance
from maya import OpenMayaUI
#-------------------------------------------------------
# Base
#-------------------------------------------------------
def baseWindow():
    mainWindow = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(mainWindow), QtWidgets.QWidget)
#-------------------------------------------------------
# Main
#-------------------------------------------------------  
class Gui(QtWidgets.QDialog):
    def __init__(self, parent=baseWindow()):
        super(Gui, self).__init__(parent)
        self.design()
    #---------------------------------------------------
    # Design
    #---------------------------------------------------
    def design(self):
        # Component
        self.setWindowTitle('Quick Renamer')
        self.setFixedSize(257, 315)
        self.setWindowFlags(QtCore.Qt.Dialog|QtCore.Qt.WindowCloseButtonHint)
        # Number
        numberBox = QtWidgets.QComboBox()
        numberBox.addItems(['Default', 'Number', 'ALPHABET', 'alphabet'])
        numberSpace = QtWidgets.QLabel()
        numberSpace.setFixedSize(0, 0)
        numberLayout = QtWidgets.QHBoxLayout()
        numberGroup = QtWidgets.QGroupBox()
        numberGroup.setLayout(numberLayout)
        numberGroup.setFixedSize(235, 40)
        numberLayout.addWidget(numberBox)
        numberLayout.addWidget(numberSpace)
        # Name
        nameLabel = QtWidgets.QLabel(' Name')
        nameLabel.setFixedSize(60, 20)
        nameEdit = QtWidgets.QLineEdit()
        nameSpace = QtWidgets.QLabel()
        nameSpace.setFixedSize(0, 0)
        nameLayout = QtWidgets.QHBoxLayout()
        nameGroup = QtWidgets.QGroupBox()
        nameGroup.setLayout(nameLayout)
        nameGroup.setFixedSize(235, 40)
        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(nameEdit)
        nameLayout.addWidget(nameSpace)
        # Prefix
        prefixLabel = QtWidgets.QLabel(' Prefix')
        prefixLabel.setFixedSize(60, 20)
        prefixEdit = QtWidgets.QLineEdit()
        prefixSpace = QtWidgets.QLabel()
        prefixSpace.setFixedSize(0, 0)
        prefixLayout = QtWidgets.QHBoxLayout()
        prefixGroup = QtWidgets.QGroupBox()
        prefixGroup.setLayout(prefixLayout)
        prefixGroup.setFixedSize(235, 40)
        prefixLayout.addWidget(prefixLabel)
        prefixLayout.addWidget(prefixEdit)
        prefixLayout.addWidget(prefixSpace)
        # Suffix
        suffixLabel = QtWidgets.QLabel(' Suffix')
        suffixLabel.setFixedSize(60, 20)
        suffixEdit = QtWidgets.QLineEdit()
        suffixSpace = QtWidgets.QLabel()
        suffixSpace.setFixedSize(0, 0)
        suffixLayout = QtWidgets.QHBoxLayout()
        suffixGroup = QtWidgets.QGroupBox()
        suffixGroup.setLayout(suffixLayout)
        suffixGroup.setFixedSize(235, 40)
        suffixLayout.addWidget(suffixLabel)
        suffixLayout.addWidget(suffixEdit)
        suffixLayout.addWidget(suffixSpace)
        # Search
        searchLabel = QtWidgets.QLabel(' Search')
        searchLabel.setFixedSize(60, 20)
        searchEdit = QtWidgets.QLineEdit()
        searchSpace = QtWidgets.QLabel()
        searchSpace.setFixedSize(0, 0)
        searchLayout = QtWidgets.QHBoxLayout()
        searchGroup = QtWidgets.QGroupBox()
        searchGroup.setLayout(searchLayout)
        searchGroup.setFixedSize(235, 40)
        searchLayout.addWidget(searchLabel)
        searchLayout.addWidget(searchEdit)
        searchLayout.addWidget(searchSpace)
        # Replace
        replaceLabel = QtWidgets.QLabel(' Replace')
        replaceLabel.setFixedSize(60, 20)
        replaceEdit = QtWidgets.QLineEdit()
        replaceSpace = QtWidgets.QLabel()
        replaceSpace.setFixedSize(0, 0)
        replaceLayout = QtWidgets.QHBoxLayout()
        replaceGroup = QtWidgets.QGroupBox()
        replaceGroup.setLayout(replaceLayout)
        replaceGroup.setFixedSize(235, 40)
        replaceLayout.addWidget(replaceLabel)
        replaceLayout.addWidget(replaceEdit)
        replaceLayout.addWidget(replaceSpace)
        # OutputLayout
        outputLayout = QtWidgets.QVBoxLayout(self)
        outputLayout.addWidget(numberGroup)
        outputLayout.addWidget(nameGroup)
        outputLayout.addWidget(prefixGroup)
        outputLayout.addWidget(suffixGroup)
        outputLayout.addWidget(searchGroup)
        outputLayout.addWidget(replaceGroup)
        # Palette
        backColor = "background:qlineargradient(x2:1, y1:0, x2:1, y2:1, stop:0.3#aa4b6b, stop:0.5#6b6b83 stop:0.8#3b8d99)"
        groupColor = "background:rgba(158, 200, 226, 0.2);color:#f5f5f5;border-style:solid;border-width:0.2px;border-color:#f5f5f5;border-radius:4px"
        labelColor = "background:rgba(255, 255, 255, 0);color:#f5f5f5;border-color:#f5f5f5;font-weight:bold"
        editColor = "background:rgba(158, 200, 226, 0.2);color:#f5f5f5;border-color:#f5f5f5;font-weight:bold"
        changeColor = "background:rgba(158, 200, 226, 0.5);color:#f5f5f5;border-color:#f5f5f5;font-weight:bold"
        # Color
        self.setStyleSheet(backColor)
        numberGroup.setStyleSheet(groupColor)
        nameGroup.setStyleSheet(groupColor)
        prefixGroup.setStyleSheet(groupColor)
        suffixGroup.setStyleSheet(groupColor)
        searchGroup.setStyleSheet(groupColor)
        replaceGroup.setStyleSheet(groupColor)
        numberBox.setStyleSheet(labelColor)
        nameLabel.setStyleSheet(labelColor)
        nameEdit.setStyleSheet(editColor)
        prefixLabel.setStyleSheet(labelColor)
        prefixEdit.setStyleSheet(editColor)
        suffixLabel.setStyleSheet(labelColor)
        suffixEdit.setStyleSheet(editColor)
        searchLabel.setStyleSheet(labelColor)
        searchEdit.setStyleSheet(editColor)
        replaceLabel.setStyleSheet(labelColor)
        replaceEdit.setStyleSheet(editColor)
        # Instance
        self.numberBox = numberBox
        self.editColor = editColor
        self.nameEdit = nameEdit
        self.prefixEdit = prefixEdit
        self.suffixEdit = suffixEdit
        self.searchEdit = searchEdit
        self.replaceEdit = replaceEdit
        self.editColor = editColor 
        self.changeColor = changeColor 
        # List
        self.ALPHALIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
        'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        # Connect
        nameEdit.textEdited.connect(self.nameSelect)
        prefixEdit.textEdited.connect(self.prefixSelect)
        suffixEdit.textEdited.connect(self.suffixSelect)
        searchEdit.textEdited.connect(self.searchSelect)
        replaceEdit.textEdited.connect(self.replaceSelect)
        nameEdit.returnPressed.connect(self.nameSet)
        prefixEdit.returnPressed.connect(self.prefixSet)
        suffixEdit.returnPressed.connect(self.suffixSet)
        replaceEdit.returnPressed.connect(self.replaceSet)
    #---------------------------------------------------
    # Processing
    #---------------------------------------------------
    def nameSelect(self):
        self.nameEdit.setStyleSheet(self.changeColor)
        self.prefixEdit.setStyleSheet(self.editColor)
        self.suffixEdit.setStyleSheet(self.editColor)
        self.searchEdit.setStyleSheet(self.editColor)
        self.replaceEdit.setStyleSheet(self.editColor)
    
    def prefixSelect(self):
        self.nameEdit.setStyleSheet(self.editColor)
        self.prefixEdit.setStyleSheet(self.changeColor)
        self.suffixEdit.setStyleSheet(self.editColor)
        self.searchEdit.setStyleSheet(self.editColor)
        self.replaceEdit.setStyleSheet(self.editColor)

    def suffixSelect(self):
        self.nameEdit.setStyleSheet(self.editColor)
        self.prefixEdit.setStyleSheet(self.editColor)
        self.suffixEdit.setStyleSheet(self.changeColor)
        self.searchEdit.setStyleSheet(self.editColor)
        self.replaceEdit.setStyleSheet(self.editColor)
    
    def searchSelect(self):
        self.nameEdit.setStyleSheet(self.editColor)
        self.prefixEdit.setStyleSheet(self.editColor)
        self.suffixEdit.setStyleSheet(self.editColor)
        self.searchEdit.setStyleSheet(self.changeColor)
        self.replaceEdit.setStyleSheet(self.editColor)
    
    def replaceSelect(self):
        self.nameEdit.setStyleSheet(self.editColor)
        self.prefixEdit.setStyleSheet(self.editColor)
        self.suffixEdit.setStyleSheet(self.editColor)
        self.searchEdit.setStyleSheet(self.editColor)
        self.replaceEdit.setStyleSheet(self.changeColor)
        
    def nameSet(self):
        cmds.undoInfo(openChunk=True)
        selection = cmds.ls(sl=True)
        try:   
            if self.numberBox.currentText() == 'Default':
                for i in range(len(selection)):
                    cmds.rename(selection[i], self.nameEdit.text())
                
            elif self.numberBox.currentText() == 'Number':
                for i in range(len(selection)):
                    cmds.rename(selection[i], 
                    '{}{}'.format(self.nameEdit.text(), str(i)))
                
            elif self.numberBox.currentText() == 'ALPHABET':
                for i in range(len(selection)):
                    cmds.rename(selection[i], 
                    '{}{}'.format(self.nameEdit.text(), self.ALPHALIST[i]))
                
            elif self.numberBox.currentText() == 'alphabet':
                for i in range(len(selection)):
                    cmds.rename(selection[i], 
                    '{}{}'.format(self.nameEdit.text(), self.alphalist[i]))
            
        except Exception as e:
            print '同名のノードがあります / There is a node with the same name',
        
        cmds.undoInfo(closeChunk=True)
    
    def prefixSet(self):
        cmds.undoInfo(openChunk=True)
        selection = cmds.ls(sl=True)
        try:
            if self.numberBox.currentText() == 'Default':
                for i in range(len(selection)):
                    cmds.rename(selection[i], 
                    '{}{}'.format(self.prefixEdit.text(), selection[i].split("|")[-1:][0]))
                
            elif self.numberBox.currentText() == 'Number':
                for i in range(len(selection)):
                    cmds.rename(selection[i], 
                    '{}{}'.format(self.prefixEdit.text() + str(i), selection[i].split("|")[-1:][0]))
                
            elif self.numberBox.currentText() == 'ALPHABET':
                for i in range(len(selection)):
                    cmds.rename(selection[i], 
                    '{}{}'.format(self.prefixEdit.text() + self.ALPHALIST[i], selection[i].split("|")[-1:][0]))
                
            elif self.numberBox.currentText() == 'alphabet':
                for i in range(len(selection)):
                    cmds.rename(selection[i], 
                    '{}{}'.format(self.prefixEdit.text() + self.alphalist[i], selection[i].split("|")[-1:][0]))
            
        except Exception as e:
            print '同名のノードがあります / There is a node with the same name',
        
        cmds.undoInfo(closeChunk=True)
        
    def suffixSet(self):
        cmds.undoInfo(openChunk=True)
        selection = cmds.ls(sl=True)
        try:
            if self.numberBox.currentText() == 'Default':
                for i in range(len(selection)):
                    cmds.rename(selection[i], 
                    '{}{}'.format(selection[i].split("|")[-1:][0], self.suffixEdit.text()))
                
            elif self.numberBox.currentText() == 'Number':
                for i in range(len(selection)):
                    cmds.rename(selection[i], 
                    '{}{}'.format(selection[i].split("|")[-1:][0], self.suffixEdit.text() + str(i)))
                
            elif self.numberBox.currentText() == 'ALPHABET':
                for i in range(len(selection)):
                    cmds.rename(selection[i], 
                    '{}{}'.format(selection[i].split("|")[-1:][0], self.suffixEdit.text() + self.ALPHALIST[i]))
                
            elif self.numberBox.currentText() == 'alphabet':
                for i in range(len(selection)):
                    cmds.rename(selection[i], 
                    '{}{}'.format(selection[i].split("|")[-1:][0], self.suffixEdit.text() + self.alphalist[i]))

        except Exception as e:
            print '同名のノードがあります / There is a node with the same name',
        
        cmds.undoInfo(closeChunk=True)
        
    def replaceSet(self):
        cmds.undoInfo(openChunk=True)
        selection = cmds.ls(sl=True)
        try:
            if self.numberBox.currentText() == 'Default':
                for i in range(len(selection)):
                    replaceName = re.sub(self.searchEdit.text(), self.replaceEdit.text(), selection[i])
                    cmds.rename(selection[i], replaceName)
            
            elif self.numberBox.currentText() == 'Number':
                for i in range(len(selection)):
                    replaceNum = self.replaceEdit.text() + str(i)
                    replaceName = re.sub(self.searchEdit.text(), replaceNum, selection[i])
                    cmds.rename(selection[i], replaceName)
            
            elif self.numberBox.currentText() == 'ALPHABET':
                for i in range(len(selection)):
                    replaceALPHA = self.replaceEdit.text() + self.ALPHALIST[i]
                    replaceName = re.sub(self.searchEdit.text(), replaceALPHA, selection[i])
                    cmds.rename(selection[i], replaceName)
            
            elif self.numberBox.currentText() == 'alphabet':
                for i in range(len(selection)):
                    replaceALPHA = self.replaceEdit.text() + self.alphalist[i]
                    replaceName = re.sub(self.searchEdit.text(), replaceALPHA, selection[i])
                    cmds.rename(selection[i], replaceName)
            
        except Exception as e:
            print '同名のノードがあります / There is a node with the same name',
        
        cmds.undoInfo(closeChunk=True)
     
#-------------------------------------------------------
# Show
#-------------------------------------------------------  
if __name__ == '__main__':
    
    G = Gui()
    G.show()