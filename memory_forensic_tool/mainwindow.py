﻿# -*- coding: utf-8 -*-
from PyQt5 import (QtWidgets,QtGui)

from main_widget import Ui_mainWidget

from PyQt5.QtCore import  (Qt,QTimer)
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import (QMenu,QFileDialog,QTreeWidgetItem)

from work_thread import RekallThread

class MainWindow(QtWidgets.QWidget,Ui_mainWidget):
    def __init__(self, app=None,parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint | Qt.FramelessWindowHint)
        self.createContextMenu()

        self.closeButton.clicked.connect(self.close);
        self.minButton.clicked.connect(self.showMinimized);
        self.menuButton.clicked.connect(self.showAuboutMenu);

        self.pslistButton.clicked.connect(self.pslistClick)
        self.bpslistButton = True

        self.svcscanButton.clicked.connect(self.svcscanClick)
        self.bsvcscan = True

        self.filescanButton.clicked.connect(self.filescanClick)
        self.bfilescan = True

        self.dlllistButton.clicked.connect(self.dlllistClick)
        self.bdlllist = True

        self.netscanButton.clicked.connect(self.netscanClick)
        self.bnetscan = True

        self.deviceButton.clicked.connect(self.deviceClick)
        self.bdevice = True

        self.driverscanButton.clicked.connect(self.driverscanClick)
        self.bdriverscan = True

        self.socketsButton.clicked.connect(self.socketsClick)
        self.bsockets = True

        self.truecryptButton.clicked.connect(self.truecryptButtonClick)
        self.btruecrypt = True

        self.bitlockerButton.clicked.connect(self.bitlockerButtonClick)
        self.bbitlocker = True

        self.disselectallButton.clicked.connect(self.disallselect)
        self.selectallButton.clicked.connect(self.selectall)
        self.count = 10
        self.updateCount()

        self.Image_filename = None
        self.selectImageButton.clicked.connect(self.showFileDialog)
        self.runButton.clicked.connect(self.startRun)
        self.pslistResultCount= 0

        self.rekall_thread = RekallThread()
    
    def pslistParse(self,status,result):
        if status == "pslistRuning":
            self.pslistItem.setText(2,'解析中...')
            if result != {}:
                self.pslistResultCount = self.pslistResultCount + 1;
                text = "共{0}项结果".format(self.pslistResultCount)
                self.pslistItem.setText(1,text)
        elif status == "pslistEnd":
            self.pslistItem.setText(2,'解析成功')

    def startRun(self):
        if self.Image_filename:
            self.stackedWidget.setCurrentIndex(1)
            self.progressBar.setProperty("value", 0)
            self.treeWidget.headerItem().setText(0, "解析项目")
            self.treeWidget.headerItem().setText(1, "解析结果")
            self.treeWidget.headerItem().setText(2, "解析状态")
            
            self.rekall_thread.Init(self.Image_filename)
            if self.bpslistButton:
                self.pslistItem = QTreeWidgetItem(self.treeWidget)
                self.pslistItem.setText(0,'进程列表信息')
                self.pslistItem.setText(1,'共0项结果')
                self.pslistItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.pslistItem)
               
                self.rekall_thread.enablePslist();
                self.rekall_thread.pslistSig.connect(self.pslistParse)
                self.rekall_thread.start()
            if self.bsvcscan:
                self.svclistItem = QTreeWidgetItem(self.treeWidget)
                self.svclistItem.setText(0,'加载服务信息')
                self.svclistItem.setText(1,'共0项结果')
                self.svclistItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.svclistItem)
            if self.bfilescan:
                self.fileItem = QTreeWidgetItem(self.treeWidget)
                self.fileItem.setText(0,'已打开文件信息')
                self.fileItem.setText(1,'共0项结果')
                self.fileItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.fileItem)
            if self.bdlllist:
                self.dlllistItem = QTreeWidgetItem(self.treeWidget)
                self.dlllistItem.setText(0,'动态链接库信息')
                self.dlllistItem.setText(1,'共0项结果')
                self.dlllistItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.dlllistItem)
            if self.bnetscan:
                self.netscanItem = QTreeWidgetItem(self.treeWidget)
                self.netscanItem.setText(0,'网络连接信息')
                self.netscanItem.setText(1,'共0项结果')
                self.netscanItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.netscanItem)
            if self.bdevice:
                self.deviceItem = QTreeWidgetItem(self.treeWidget)
                self.deviceItem.setText(0,'加载设备信息')
                self.deviceItem.setText(1,'共0项结果')
                self.deviceItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.deviceItem)
            if self.bdriverscan:
                self.driverItem = QTreeWidgetItem(self.treeWidget)
                self.driverItem.setText(0,'加载驱动信息')
                self.driverItem.setText(1,'共0项结果')
                self.driverItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.driverItem)
            if self.bsockets:
                self.socketsItem = QTreeWidgetItem(self.treeWidget)
                self.socketsItem.setText(0,'Sockets信息')
                self.socketsItem.setText(1,'共0项结果')
                self.socketsItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.socketsItem)
            if self.btruecrypt:
                self.truecryptItem = QTreeWidgetItem(self.treeWidget)
                self.truecryptItem.setText(0,'TrueCrypt密钥')
                self.truecryptItem.setText(1,'共0项结果')
                self.truecryptItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.truecryptItem)
            if self.bbitlocker:
                self.bitlockerItem = QTreeWidgetItem(self.treeWidget)
                self.bitlockerItem.setText(0,'BitLocker密钥')
                self.bitlockerItem.setText(1,'共0项结果')
                self.bitlockerItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.bitlockerItem)

            self.timer = QTimer(self)
            self.sencond = 0
            self.minutes = 0
            self.hour = 0

            self.timer.timeout.connect(self.updateTime)
            self.timer.start(1000)

    def updateTime(self):
        self.sencond = self.sencond + 1
        if self.sencond == 60 :
            self.sencond = 0
            self.minutes = self.minutes + 1
        if self.minutes == 60:
            self.minutes = 0
            self.hour = self.hour + 1

        text = "{0:02d}:{1:02d}:{2:02d}".format(self.hour,self.minutes,self.sencond)
        self.label_9.setText(text)

    def showFileDialog(self):
        self.Image_filename,  _ = QFileDialog.getOpenFileName(self, 'Open file', './')
        self.lineEdit.setText(self.Image_filename)

    def updateCount(self):
       if self.count < 0 :
           self.count = 0
       if self.count > 10:
           self.count = 10
       s =  "<html><head/><body><p><span style=\" font-size:12pt; color:#6b6b6b;\">已选择</span><span style=\" font-size:18pt; font-weight:600; color:#00aa00;\">{0}</span><span style=\" font-size:12pt; color:#6b6b6b;\">项解析类型</span></p></body></html>".format(self.count)
       self.label_4.setText(s)

    def createContextMenu(self):
        self.aboutMenu = QMenu(self)

        self.actionA = self.aboutMenu.addAction('关于')
        self.actionE = self.aboutMenu.addAction('退出')

        self.actionE.triggered.connect(self.close)
    
    def selectall(self):
        self.bbitlocker = False
        self.btruecrypt = False
        self.bsockets = False
        self.bdriverscan = False
        self.bdevice = False
        self.bnetscan = False
        self.bdlllist = False
        self.bfilescan = False
        self.bsvcscan = False
        self.bpslistButton = False
        self.bitlockerButtonClick()
        self.truecryptButtonClick()
        self.socketsClick()
        self.driverscanClick()
        self.deviceClick()
        self.netscanClick()
        self.dlllistClick()
        self.filescanClick()
        self.svcscanClick()
        self.pslistClick()

    def disallselect(self):
        self.bbitlocker = True
        self.btruecrypt = True
        self.bsockets = True
        self.bdriverscan = True
        self.bdevice = True
        self.bnetscan = True
        self.bdlllist = True
        self.bfilescan = True
        self.bsvcscan = True
        self.bpslistButton = True
        self.bitlockerButtonClick()
        self.truecryptButtonClick()
        self.socketsClick()
        self.driverscanClick()
        self.deviceClick()
        self.netscanClick()
        self.dlllistClick()
        self.filescanClick()
        self.svcscanClick()
        self.pslistClick()

    def bitlockerButtonClick(self):
        if self.bbitlocker:
            pix = QtGui.QPixmap(":/images/00021[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.bitlockerButton.setIcon(icon)
            self.bbitlocker = False
            self.count = self.count - 1
        else:
            pix = QtGui.QPixmap(":/images/00019[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.bitlockerButton.setIcon(icon)
            self.bbitlocker = True
            self.count = self.count + 1
        self.updateCount()

    def truecryptButtonClick(self):
        if self.btruecrypt:
            pix = QtGui.QPixmap(":/images/00016[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.truecryptButton.setIcon(icon)
            self.btruecrypt = False
            self.count = self.count -1 
        else:
            pix = QtGui.QPixmap(":/images/00020[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.truecryptButton.setIcon(icon)
            self.btruecrypt = True
            self.count = self.count + 1
        self.updateCount()

    def socketsClick(self):
        if self.bsockets:
            pix = QtGui.QPixmap(":/images/00030[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.socketsButton.setIcon(icon)
            self.bsockets = False
            self.count = self.count - 1
        else:
            pix = QtGui.QPixmap(":/images/00025[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.socketsButton.setIcon(icon)
            self.bsockets = True
            self.count = self.count + 1
        self.updateCount()

    def driverscanClick(self):
        if self.bdriverscan:
            pix = QtGui.QPixmap(":/images/00026[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.driverscanButton.setIcon(icon)
            self.bdriverscan = False
            self.count = self.count -1
        else:
            pix = QtGui.QPixmap(":/images/00015[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.driverscanButton.setIcon(icon)
            self.bdriverscan = True
            self.count = self.count + 1
        self.updateCount()

    def deviceClick(self):
        if self.bdevice:
            pix = QtGui.QPixmap(":/images/00031[86x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.deviceButton.setIcon(icon)
            self.bdevice = False
            self.count = self.count - 1
        else:
            pix = QtGui.QPixmap(":/images/00014[86x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.deviceButton.setIcon(icon)
            self.bdevice = True
            self.count = self.count + 1
        self.updateCount()

    def netscanClick(self):
        if self.bnetscan:
            pix = QtGui.QPixmap(":/images/00017[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.netscanButton.setIcon(icon)
            self.bnetscan = False
            self.count = self.count - 1
        else:
            pix = QtGui.QPixmap(":/images/00022[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.netscanButton.setIcon(icon)
            self.bnetscan = True
            self.count = self.count + 1
        self.updateCount()

    def dlllistClick(self):
        if self.bdlllist:
            pix = QtGui.QPixmap(":/images/00032[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.dlllistButton.setIcon(icon)
            self.bdlllist = False
            self.count = self.count - 1
        else:
            pix = QtGui.QPixmap(":/images/00013[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.dlllistButton.setIcon(icon)
            self.bdlllist = True
            self.count = self.count + 1
        self.updateCount()

    def filescanClick(self):
        if self.bfilescan:
            pix = QtGui.QPixmap(":/images/00028[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.filescanButton.setIcon(icon)
            self.bfilescan = False
            self.count = self.count - 1
        else:
            pix = QtGui.QPixmap(":/images/00024[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.filescanButton.setIcon(icon)
            self.bfilescan = True
            self.count = self.count + 1
        self.updateCount()

    def svcscanClick(self):
        if self.bsvcscan:
            pix = QtGui.QPixmap(":/images/00029[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.svcscanButton.setIcon(icon)
            self.bsvcscan = False
            self.count = self.count - 1
        else:
            pix = QtGui.QPixmap(":/images/00027[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.svcscanButton.setIcon(icon)
            self.bsvcscan = True
            self.count = self.count + 1
        self.updateCount()


    def pslistClick(self):
        if self.bpslistButton:
            pix = QtGui.QPixmap(":/images/00023[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.pslistButton.setIcon(icon)
            self.bpslistButton = False
            self.count = self.count - 1
        else:
            pix = QtGui.QPixmap(":/images/00018[72x72x8BPP].png")
            icon = QtGui.QIcon()
            icon.addPixmap(pix)
            self.pslistButton.setIcon(icon)
            self.bpslistButton = True
            self.count = self.count + 1
        self.updateCount()

    def showAuboutMenu(self, pos):
         self.aboutMenu.exec_(QCursor.pos())
      
    def isInTitle(self, xPos, yPos):
        return yPos < 30 and xPos < 695