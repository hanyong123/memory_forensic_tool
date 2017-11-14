# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_widget.ui'
#
# Created: Fri Nov 10 17:53:04 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MyButton import ImageButton

class Ui_mainWidget(object):
    def setupUi(self, mainWidget):
        mainWidget.setObjectName("mainWidget")
        mainWidget.resize(900, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWidget.sizePolicy().hasHeightForWidth())
        mainWidget.setSizePolicy(sizePolicy)
        mainWidget.setStyleSheet("QToolButton#menuButton:hover{\n"
"image:url(:/images/00006[27x22x8BPP].png);\n"
"}\n"
"\n"
"QToolButton#menuButton:pressed{\n"
"image:url(:/images/00008[27x22x8BPP].png);\n"
"}\n"
"\n"
"QToolButton#minButton:hover{\n"
"image:url(:/images/00004[27x22x8BPP].png);\n"
"}\n"
"\n"
"QToolButton#minButton:pressed{\n"
"image:url(:/images/00002[27x22x8BPP].png);\n"
"}\n"
"\n"
"\n"
"QToolButton#closeButton:hover{\n"
"image:url(:/images/00005[27x22x8BPP].png);\n"
"}\n"
"\n"
"\n"
"QToolButton#closeButton:pressed{\n"
"image:url(:/images/00009[27x22x8BPP].png);\n"
"}\n"
"\n"
"\n"
"QToolButton#selectImageButton:hover{\n"
"image:url(:/images/00034[72x28x8BPP].png);\n"
"}\n"
"\n"
"\n"
"QToolButton#selectImageButton:pressed{\n"
"image:url(:/images/00035[70x26x8BPP].png);\n"
"}\n"
"\n"
"\n"
"QToolButton#runButton:hover{\n"
"image:url(:/images/00034[72x28x8BPP].png);\n"
"}\n"
"\n"
"QToolButton#runButton:pressed{\n"
"image:url(:/images/00035[70x26x8BPP].png);\n"
"}\n"
"\n"
"QToolButton#stopButton:hover{\n"
"image:url(:/images/00034[72x28x8BPP].png);\n"
"}\n"
"\n"
"QToolButton#stopButton:pressed{\n"
"image:url(:/images/00035[70x26x8BPP].png);\n"
"}\n"
"\n"
"QToolButton#returnButton:hover{\n"
"image:url(:/images/00034[72x28x8BPP].png);\n"
"}\n"
"\n"
"QToolButton#returnButton:pressed{\n"
"image:url(:/images/00035[70x26x8BPP].png);\n"
"}\n"
"\n"
"QToolButton#exportButton{\n"
"border:none;\n"
"border-image: url(:/images/00036[72x28x8BPP].png);\n"
"}\n"
"QToolButton#exportButton:hover{\n"
"border-image:url(:/images/00034[72x28x8BPP].png);\n"
"}\n"
"\n"
"QToolButton#exportButton:pressed{\n"
"border-image:url(:/images/00035[70x26x8BPP].png);\n"
"}\n"
"\n"
"QPushButton#selectallButton:hover{\n"
"color: rgba(85, 170, 255,50%);\n"
"}\n"
"\n"
"QProgressBar{\n"
"border:none;\n"
"border-image: url(:/images/00042[100x13x8BPP].png);\n"
"}\n"
"QProgressBar::chunk {\n"
"border-image: url(:/images/00044[120x12x8BPP].png);\n"
"}\n"
"")
        self.titleBar = QtWidgets.QWidget(mainWidget)
        self.titleBar.setGeometry(QtCore.QRect(0, 0, 900, 50))
        self.titleBar.setStyleSheet("background-image: url(:/images/00001[1175x50x24BPP].jpg);")
        self.titleBar.setObjectName("titleBar")
        self.label = QtWidgets.QLabel(self.titleBar)
        self.label.setGeometry(QtCore.QRect(10, 10, 32, 32))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/00003[64x64x8BPP].png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.titleBar)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 101, 31))
        self.label_2.setObjectName("label_2")
        self.menuButton = QtWidgets.QToolButton(self.titleBar)
        self.menuButton.setGeometry(QtCore.QRect(820, 5, 27, 22))
        self.menuButton.setStyleSheet("border:0px;\n"
"background: transparent;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/00001[27x22x8BPP].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QtCore.QSize(27, 22))
        self.menuButton.setObjectName("menuButton")
        self.minButton = QtWidgets.QToolButton(self.titleBar)
        self.minButton.setGeometry(QtCore.QRect(845, 5, 27, 22))
        self.minButton.setStyleSheet("border:0px;\n"
"background: transparent;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/00007[27x22x8BPP].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minButton.setIcon(icon1)
        self.minButton.setIconSize(QtCore.QSize(27, 22))
        self.minButton.setObjectName("minButton")
        self.closeButton = QtWidgets.QToolButton(self.titleBar)
        self.closeButton.setGeometry(QtCore.QRect(870, 5, 27, 22))
        self.closeButton.setStyleSheet("border:0px;\n"
"background: transparent;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/00010[27x22x8BPP].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QtCore.QSize(27, 24))
        self.closeButton.setObjectName("closeButton")
        self.stackedWidget = QtWidgets.QStackedWidget(mainWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 50, 900, 550))
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setEnabled(True)
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.line = QtWidgets.QFrame(self.stackedWidgetPage1)
        self.line.setGeometry(QtCore.QRect(0, 75, 900, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.stackedWidgetPage1)
        self.line_2.setGeometry(QtCore.QRect(0, 500, 900, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label_3.setGeometry(QtCore.QRect(20, 25, 61, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.stackedWidgetPage1)
        self.lineEdit.setGeometry(QtCore.QRect(90, 23, 600, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.selectImageButton = QtWidgets.QToolButton(self.stackedWidgetPage1)
        self.selectImageButton.setGeometry(QtCore.QRect(710, 20, 72, 28))
        self.selectImageButton.setStyleSheet("border:0px;\n"
"background-image: url(:/images/00036[72x28x8BPP].png);")
        self.selectImageButton.setIconSize(QtCore.QSize(72, 28))
        self.selectImageButton.setObjectName("selectImageButton")
        self.runButton = QtWidgets.QToolButton(self.stackedWidgetPage1)
        self.runButton.setGeometry(QtCore.QRect(810, 20, 72, 28))
        self.runButton.setStyleSheet("border:0px;\n"
"background-image: url(:/images/00036[72x28x8BPP].png);")
        self.runButton.setIconSize(QtCore.QSize(72, 28))
        self.runButton.setObjectName("runButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.stackedWidgetPage1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 90, 801, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.netscanButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.netscanButton.setStyleSheet("border:0px;\n"
"background: transparent;\n"
"\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/00022[72x72x8BPP].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.netscanButton.setIcon(icon3)
        self.netscanButton.setIconSize(QtCore.QSize(72, 72))
        self.netscanButton.setCheckable(True)
        self.netscanButton.setChecked(True)
        self.netscanButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.netscanButton.setObjectName("netscanButton")
        self.gridLayout.addWidget(self.netscanButton, 0, 4, 1, 1)
        self.svcscanButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.svcscanButton.setStyleSheet("border:0px;\n"
"background: transparent;\n"
"\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/00027[72x72x8BPP].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.svcscanButton.setIcon(icon4)
        self.svcscanButton.setIconSize(QtCore.QSize(72, 72))
        self.svcscanButton.setCheckable(True)
        self.svcscanButton.setChecked(True)
        self.svcscanButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.svcscanButton.setObjectName("svcscanButton")
        self.gridLayout.addWidget(self.svcscanButton, 0, 1, 1, 1)
        self.filescanButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.filescanButton.setStyleSheet("border:0px;\n"
"background: transparent;\n"
"\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/00024[72x72x8BPP].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filescanButton.setIcon(icon5)
        self.filescanButton.setIconSize(QtCore.QSize(72, 72))
        self.filescanButton.setCheckable(True)
        self.filescanButton.setChecked(True)
        self.filescanButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.filescanButton.setObjectName("filescanButton")
        self.gridLayout.addWidget(self.filescanButton, 0, 2, 1, 1)
        self.dlllistButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.dlllistButton.setStyleSheet("border:0px;\n"
"background: transparent;\n"
"\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/00013[72x72x8BPP].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dlllistButton.setIcon(icon6)
        self.dlllistButton.setIconSize(QtCore.QSize(72, 72))
        self.dlllistButton.setCheckable(True)
        self.dlllistButton.setChecked(True)
        self.dlllistButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.dlllistButton.setObjectName("dlllistButton")
        self.gridLayout.addWidget(self.dlllistButton, 0, 3, 1, 1)
        self.deviceButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.deviceButton.setStyleSheet("border:0px;\n"
"background: transparent;\n"
"\n"
"")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/00014[86x72x8BPP].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deviceButton.setIcon(icon7)
        self.deviceButton.setIconSize(QtCore.QSize(72, 72))
        self.deviceButton.setCheckable(True)
        self.deviceButton.setChecked(True)
        self.deviceButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.deviceButton.setObjectName("deviceButton")
        self.gridLayout.addWidget(self.deviceButton, 1, 0, 1, 1)
        self.driverscanButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.driverscanButton.setStyleSheet("border:0px;\n"
"background: transparent;\n"
"\n"
"")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/00015[72x72x8BPP].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.driverscanButton.setIcon(icon8)
        self.driverscanButton.setIconSize(QtCore.QSize(72, 72))
        self.driverscanButton.setCheckable(True)
        self.driverscanButton.setChecked(True)
        self.driverscanButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.driverscanButton.setObjectName("driverscanButton")
        self.gridLayout.addWidget(self.driverscanButton, 1, 1, 1, 1)
        self.socketsButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.socketsButton.setStyleSheet("border:0px;\n"
"background: transparent;\n"
"\n"
"")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/00025[72x72x8BPP].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.socketsButton.setIcon(icon9)
        self.socketsButton.setIconSize(QtCore.QSize(72, 72))
        self.socketsButton.setCheckable(True)
        self.socketsButton.setChecked(True)
        self.socketsButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.socketsButton.setObjectName("socketsButton")
        self.gridLayout.addWidget(self.socketsButton, 1, 2, 1, 1)
        self.truecryptButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.truecryptButton.setStyleSheet("border:0px;\n"
"background: transparent;\n"
"\n"
"")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/00020[72x72x8BPP].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.truecryptButton.setIcon(icon10)
        self.truecryptButton.setIconSize(QtCore.QSize(72, 72))
        self.truecryptButton.setCheckable(True)
        self.truecryptButton.setChecked(True)
        self.truecryptButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.truecryptButton.setObjectName("truecryptButton")
        self.gridLayout.addWidget(self.truecryptButton, 1, 3, 1, 1)
        self.bitlockerButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.bitlockerButton.setStyleSheet("border:0px;\n"
"background: transparent;\n"
"\n"
"")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/00019[72x72x8BPP].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bitlockerButton.setIcon(icon11)
        self.bitlockerButton.setIconSize(QtCore.QSize(72, 72))
        self.bitlockerButton.setCheckable(True)
        self.bitlockerButton.setChecked(True)
        self.bitlockerButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.bitlockerButton.setObjectName("bitlockerButton")
        self.gridLayout.addWidget(self.bitlockerButton, 1, 4, 1, 1)
        self.pslistButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        #self.pslistButton = ImageButton(self.gridLayoutWidget)
        self.pslistButton.setAccessibleDescription("")
        self.pslistButton.setStyleSheet("\n"
"border:none;\n"
"background: transparent;\n"
"\n"
"\n"
"\n"
"")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/00018[72x72x8BPP].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pslistButton.setIcon(icon12)
        self.pslistButton.setIconSize(QtCore.QSize(72, 72))
        self.pslistButton.setCheckable(True)
        self.pslistButton.setChecked(True)
        self.pslistButton.setAutoExclusive(False)
        self.pslistButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.pslistButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.pslistButton.setObjectName("pslistButton")
        self.gridLayout.addWidget(self.pslistButton, 0, 0, 1, 1)
        self.selectallButton = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.selectallButton.setGeometry(QtCore.QRect(730, 520, 75, 23))
        self.selectallButton.setStyleSheet("\n"
"\n"
"QPushButton#selectallButton:hover{\n"
"color: rgba(85, 170, 255,50%);\n"
"}\n"
"\n"
"border:0px;\n"
"color: rgb(85, 170, 255);\n"
"background: transparent;")
        self.selectallButton.setObjectName("selectallButton")
        self.disselectallButton = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.disselectallButton.setGeometry(QtCore.QRect(800, 520, 75, 23))
        self.disselectallButton.setStyleSheet("\n"
"\n"
"\n"
"\n"
"QPushButton#disselectallButton:hover{\n"
"color: rgba(85, 170, 255,50%);\n"
"}\n"
"\n"
"border:0px;\n"
"color: rgb(85, 170, 255);\n"
"background: transparent;\n"
"")
        self.disselectallButton.setObjectName("disselectallButton")
        self.label_4 = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label_4.setGeometry(QtCore.QRect(20, 510, 161, 31))
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QtWidgets.QWidget()
        self.stackedWidgetPage2.setObjectName("stackedWidgetPage2")
        self.line_3 = QtWidgets.QFrame(self.stackedWidgetPage2)
        self.line_3.setGeometry(QtCore.QRect(0, 75, 900, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_5 = QtWidgets.QLabel(self.stackedWidgetPage2)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 48, 48))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/images/00045[48x48x8BPP].png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.progressBar = QtWidgets.QProgressBar(self.stackedWidgetPage2)
        self.progressBar.setGeometry(QtCore.QRect(100, 30, 600, 16))
        self.progressBar.setProperty("value", 50)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.stopButton = QtWidgets.QToolButton(self.stackedWidgetPage2)
        self.stopButton.setGeometry(QtCore.QRect(760, 20, 72, 28))
        self.stopButton.setStyleSheet("border:0px;\n"
"background-image: url(:/images/00036[72x28x8BPP].png);")
        self.stopButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.stopButton.setObjectName("stopButton")
        self.label_7 = QtWidgets.QLabel(self.stackedWidgetPage2)
        self.label_7.setGeometry(QtCore.QRect(100, 10, 131, 16))
        self.label_7.setStyleSheet("color: rgb(108, 108, 108);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.stackedWidgetPage2)
        self.label_8.setGeometry(QtCore.QRect(110, 50, 54, 12))
        self.label_8.setStyleSheet("color: rgb(108, 108, 108);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.stackedWidgetPage2)
        self.label_9.setGeometry(QtCore.QRect(170, 50, 71, 16))
        self.label_9.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_9.setObjectName("label_9")
        self.treeWidget = QtWidgets.QTreeWidget(self.stackedWidgetPage2)
        self.treeWidget.setGeometry(QtCore.QRect(0, 75, 900, 525))
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.headerItem().setText(1, "2")
        self.treeWidget.headerItem().setText(2, "3")
        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        self.stackedWidgetPage3 = QtWidgets.QWidget()
        self.stackedWidgetPage3.setObjectName("stackedWidgetPage3")
        self.line_4 = QtWidgets.QFrame(self.stackedWidgetPage3)
        self.line_4.setGeometry(QtCore.QRect(0, 75, 900, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_10 = QtWidgets.QLabel(self.stackedWidgetPage3)
        self.label_10.setGeometry(QtCore.QRect(90, 20, 40, 40))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/images/00012[40x40x8BPP].png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.stackedWidgetPage3)
        self.label_11.setGeometry(QtCore.QRect(140, 31, 381, 21))
        self.label_11.setObjectName("label_11")
        self.returnButton = QtWidgets.QToolButton(self.stackedWidgetPage3)
        self.returnButton.setGeometry(QtCore.QRect(670, 30, 72, 28))
        self.returnButton.setStyleSheet("border:0px;\n"
"background-image: url(:/images/00036[72x28x8BPP].png);")
        self.returnButton.setObjectName("returnButton")
        self.tabWidget = QtWidgets.QTabWidget(self.stackedWidgetPage3)
        self.tabWidget.setGeometry(QtCore.QRect(0, 80, 900, 420))
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"border:none\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"font-weight:300;\n"
"color: rgb(85, 170, 255);\n"
"border:none;\n"
"border-right:1px solid #C4C4C3;\n"
"padding-top: 5px;\n"
"padding-bottom:5px;\n"
"padding-right:20px;\n"
"padding-left:20px;\n"
"}\n"
"QTabBar::tab:hover {\n"
"color: rgba(85, 170, 255, 50%);\n"
"}\n"
"QTabBar::tab:selected {\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.pslist = QtWidgets.QWidget()
        self.pslist.setObjectName("pslist")
        self.tabWidget.addTab(self.pslist, "")
        self.svc = QtWidgets.QWidget()
        self.svc.setObjectName("svc")
        self.tabWidget.addTab(self.svc, "")
        self.file = QtWidgets.QWidget()
        self.file.setObjectName("file")
        self.tabWidget.addTab(self.file, "")
        self.dlllist = QtWidgets.QWidget()
        self.dlllist.setObjectName("dlllist")
        self.tabWidget.addTab(self.dlllist, "")
        self.netcon = QtWidgets.QWidget()
        self.netcon.setObjectName("netcon")
        self.tabWidget.addTab(self.netcon, "")
        self.device = QtWidgets.QWidget()
        self.device.setObjectName("device")
        self.tabWidget.addTab(self.device, "")
        self.driver = QtWidgets.QWidget()
        self.driver.setObjectName("driver")
        self.tabWidget.addTab(self.driver, "")
        self.sockets = QtWidgets.QWidget()
        self.sockets.setObjectName("sockets")
        self.tabWidget.addTab(self.sockets, "")
        self.truecrypt = QtWidgets.QWidget()
        self.truecrypt.setObjectName("truecrypt")
        self.tabWidget.addTab(self.truecrypt, "")
        self.bitlocker = QtWidgets.QWidget()
        self.bitlocker.setObjectName("bitlocker")
        self.tabWidget.addTab(self.bitlocker, "")
        self.line_5 = QtWidgets.QFrame(self.stackedWidgetPage3)
        self.line_5.setGeometry(QtCore.QRect(0, 500, 900, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.exportButton = QtWidgets.QToolButton(self.stackedWidgetPage3)
        self.exportButton.setGeometry(QtCore.QRect(700, 510, 141, 28))
        self.exportButton.setStyleSheet("")
        self.exportButton.setIconSize(QtCore.QSize(141, 28))
        self.exportButton.setAutoRepeat(False)
        self.exportButton.setObjectName("exportButton")
        self.stackedWidget.addWidget(self.stackedWidgetPage3)

        self.retranslateUi(mainWidget)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(mainWidget)

    def retranslateUi(self, mainWidget):
        _translate = QtCore.QCoreApplication.translate
        mainWidget.setWindowTitle(_translate("mainWidget", "Form"))
        self.label_2.setText(_translate("mainWidget", "<html><head/><body><p><span style=\" color:#ffffff;\">内存镜像解析工具</span></p></body></html>"))
        self.menuButton.setText(_translate("mainWidget", "..."))
        self.minButton.setText(_translate("mainWidget", "..."))
        self.closeButton.setText(_translate("mainWidget", "..."))
        self.label_3.setText(_translate("mainWidget", "内存镜像："))
        self.selectImageButton.setText(_translate("mainWidget", "选择镜像"))
        self.runButton.setText(_translate("mainWidget", "开始解析"))
        self.netscanButton.setText(_translate("mainWidget", "\n"
"网络连接\n"
"解析网络连接信息"))
        self.svcscanButton.setText(_translate("mainWidget", "\n"
"服务\n"
"解析加载的服务信息"))
        self.filescanButton.setText(_translate("mainWidget", "\n"
"文件\n"
"解析已打开文件信息"))
        self.dlllistButton.setText(_translate("mainWidget", "\n"
"动态链接库\n"
"解析动态链接库信息"))
        self.deviceButton.setText(_translate("mainWidget", "\n"
"设备\n"
"解析加载设备信息"))
        self.driverscanButton.setText(_translate("mainWidget", "\n"
"驱动\n"
"解析加载驱动信息"))
        self.socketsButton.setText(_translate("mainWidget", "\n"
"Sockets\n"
"解析Sockets信息"))
        self.truecryptButton.setText(_translate("mainWidget", "\n"
"TrueCrypt\n"
"搜索TrueCrypt密钥"))
        self.bitlockerButton.setText(_translate("mainWidget", "\n"
"BitLocker\n"
"搜索BitLocker密钥"))
        self.pslistButton.setText(_translate("mainWidget", "\n"
"进程\n"
"解析进程列表信息"))
        self.selectallButton.setText(_translate("mainWidget", "全选"))
        self.disselectallButton.setText(_translate("mainWidget", "全不选"))
        self.label_4.setText(_translate("mainWidget", "<html><head/><body><p><span style=\" font-size:12pt; color:#6b6b6b;\">已选择</span><span style=\" font-size:18pt; font-weight:600; color:#00aa00;\">10</span><span style=\" font-size:12pt; color:#6b6b6b;\">项解析类型</span></p></body></html>"))
        self.stopButton.setText(_translate("mainWidget", "停止"))
        self.label_7.setText(_translate("mainWidget", "正在解析进程列表信息..."))
        self.label_8.setText(_translate("mainWidget", "已用时间："))
        self.label_9.setText(_translate("mainWidget", "00：00：00"))
        self.label_11.setText(_translate("mainWidget", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#484848;\">解析被终止，已发现</span><span style=\" font-size:12pt; font-weight:600; color:#00aa00;\">871</span><span style=\" font-size:12pt; font-weight:600; color:#535353;\">项结果，用时</span><span style=\" font-size:12pt; font-weight:600; color:#ff5500;\">00：00：12</span></p></body></html>"))
        self.returnButton.setText(_translate("mainWidget", "返回"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pslist), _translate("mainWidget", "进程"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.svc), _translate("mainWidget", "服务"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.file), _translate("mainWidget", "文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dlllist), _translate("mainWidget", "动态链接库"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.netcon), _translate("mainWidget", "网络连接"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.device), _translate("mainWidget", "设备"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.driver), _translate("mainWidget", "驱动"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sockets), _translate("mainWidget", "Sockets"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.truecrypt), _translate("mainWidget", "TrueCrypt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bitlocker), _translate("mainWidget", "BitLocker"))
        self.exportButton.setText(_translate("mainWidget", "导出勾选列表"))

import images_rc
