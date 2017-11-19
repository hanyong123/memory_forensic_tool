from PyQt5 import (QtWidgets,QtGui)

from main_widget import Ui_mainWidget

from PyQt5.QtCore import  (Qt,QTimer,pyqtSignal,QVariant,QPointF)
from PyQt5.QtGui import (QCursor,QPainter)
from PyQt5.QtWidgets import (QMenu,QFileDialog,QTreeWidgetItem)

from work_thread import RekallThread
from checkboxhead import (CheckBoxHeader,CTreeWidgetItemEx)


class MainWindow(QtWidgets.QWidget,Ui_mainWidget):

    def __init__(self, app=None,parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint | Qt.FramelessWindowHint)
        self.createContextMenu()

        self.timer = QTimer(self)       #任务计算时器
        self.timer.timeout.connect(self.updateTime)

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
        
        self.rekall_thread = RekallThread()
        self.rekall_thread.rekallEndSig.connect(self.parseComplete)
        self.rekall_thread.pslistSig.connect(self.pslistParse)
        self.rekall_thread.svcSig.connect(self.svcscanParse)
        self.rekall_thread.filescanSig.connect(self.filescanParse)
        self.rekall_thread.dlllistSig.connect(self.dlllistParse)
        self.rekall_thread.netscanSig.connect(self.netscanParse)
        self.rekall_thread.devscanSig.connect(self.devscanParse)
        self.rekall_thread.driverscanSig.connect(self.driverscanParse)
        self.rekall_thread.socketsSig.connect(self.socketsParse)
        self.rekall_thread.tcSig.connect(self.tcscanParse)
        self.rekall_thread.bitlockerSig.connect(self.bitlockerParse)

        self.pslistResultCount= 0
        self.pslistWidgetHead = CheckBoxHeader()
        self.pslistWidgetHead.stateChanged.connect(self.pslist_headCheckClicked)
        self.pslistWidgetHead.sortSig.connect(self.pslist_sortAfter)
        self.pslistWidget.setHeader(self.pslistWidgetHead)
        self.pslistWidget.headerItem().setText(0,"序号")
        self.pslistWidget.headerItem().setText(1,"进程名称")
        self.pslistWidget.headerItem().setText(2,"进程ID")
        self.pslistWidget.headerItem().setText(3,"父进程ID")
        self.pslistWidget.headerItem().setText(4,"线程数")
        self.pslistWidget.headerItem().setText(5,"句柄数")
        self.pslistWidget.headerItem().setText(6,"会话ID")
        self.pslistWidget.headerItem().setText(7,"wow64")
        self.pslistWidget.headerItem().setText(8,"创建时间")
        self.pslistWidget.headerItem().setText(9,"退出时间")
        self.pslistWidget.itemClicked.connect(self.pslist_ItemClicked)
        self.pslistWidget.setSortingEnabled(True)
        self.pslistWidget.sortByColumn(0,Qt.AscendingOrder)

        self.stopButton.clicked.connect(self.stopParse)
        self.isStop = False

        self.progressBarCount = 0
        self.completeProgressCount = 0

        self.returnButton.clicked.connect(self.returnHomePage)

        self.svcscantResultCount= 0

        self.svcscanWidgetHead = CheckBoxHeader()
        self.svcscanWidgetHead.stateChanged.connect(self.svcscan_headCheckClicked)
        self.svcscanWidgetHead.sortSig.connect(self.svcscan_sortAfter)
        self.treeWidget_2.setHeader(self.svcscanWidgetHead)
        
        self.treeWidget_2.headerItem().setText(0,"序号")
        self.treeWidget_2.headerItem().setText(1,"服务名称")
        self.treeWidget_2.headerItem().setText(2,"进程ID")
        self.treeWidget_2.headerItem().setText(3,"服务描述")
        self.treeWidget_2.headerItem().setText(4,"服务类型")
        self.treeWidget_2.headerItem().setText(5,"服务状态")
        self.treeWidget_2.headerItem().setText(6,"启动路径")
        self.treeWidget_2.itemClicked.connect(self.svcscan_ItemClicked)
        self.treeWidget_2.setSortingEnabled(True)
        self.treeWidget_2.sortByColumn(0,Qt.AscendingOrder)

        self.filescanResultCount = 0
        self.filescanWidgetHead = CheckBoxHeader()
        self.filescanWidgetHead.stateChanged.connect(self.filescan_headCheckClicked)
        self.filescanWidgetHead.sortSig.connect(self.filescan_sortAfter)
        self.treeWidget_3.setHeader(self.filescanWidgetHead)

        self.treeWidget_3.headerItem().setText(0,"序号")
        self.treeWidget_3.headerItem().setText(1,"文件名称")
        self.treeWidget_3.headerItem().setText(2,"指针数")
        self.treeWidget_3.headerItem().setText(3,"句柄数")
        self.treeWidget_3.headerItem().setText(4,"读写权限")
        self.treeWidget_3.itemClicked.connect(self.filescan_ItemClicked)
        self.treeWidget_3.setSortingEnabled(True)
        self.treeWidget_3.sortByColumn(0,Qt.AscendingOrder)

        self.dlllistResultCount = 0
        self.treeWidget_4.headerItem().setText(0,"[进程ID]进程名称")

        self.netscanResultCount = 0
        self.netscanWidgetHead = CheckBoxHeader()
        self.netscanWidgetHead.stateChanged.connect(self.netscan_headCheckClicked)
        self.netscanWidgetHead.sortSig.connect(self.netscan_sortAfter)
        self.treeWidget_5.setHeader(self.netscanWidgetHead)

        self.treeWidget_5.headerItem().setText(0,"序号")
        self.treeWidget_5.headerItem().setText(1,"进程ID")
        self.treeWidget_5.headerItem().setText(2,"本地IP地址")
        self.treeWidget_5.headerItem().setText(3,"远程IP地址")
        self.treeWidget_5.itemClicked.connect(self.netscan_ItemClicked)
        self.treeWidget_5.setSortingEnabled(True)
        self.treeWidget_5.sortByColumn(0,Qt.AscendingOrder)

        self.devscanResultCount = 0
        self.treeWidget_6.headerItem().setText(0,"名称")
        self.treeWidget_6.headerItem().setText(1,"类型")

        self.driverscanResultCount = 0
        self.driverscanWidgetHead = CheckBoxHeader()
        self.driverscanWidgetHead.stateChanged.connect(self.driverscan_headCheckClicked)
        self.driverscanWidgetHead.sortSig.connect(self.driverscan_sortAfter)
        self.treeWidget_7.setHeader(self.driverscanWidgetHead)

        self.treeWidget_7.headerItem().setText(0,"序号")
        self.treeWidget_7.headerItem().setText(1,"显示名称")
        self.treeWidget_7.headerItem().setText(2,"服务名称")
        self.treeWidget_7.headerItem().setText(3,"驱动名称")
        self.treeWidget_7.headerItem().setText(4,"驱动大小")
        self.treeWidget_7.headerItem().setText(5,"指针数")
        self.treeWidget_7.headerItem().setText(6,"句柄数")
        self.treeWidget_7.itemClicked.connect(self.driverscan_ItemClicked)
        self.treeWidget_7.setSortingEnabled(True)
        self.treeWidget_7.sortByColumn(0,Qt.AscendingOrder)

        self.socketsResultCount = 0
        self.socketsWidgetHead = CheckBoxHeader()
        self.socketsWidgetHead.stateChanged.connect(self.sockets_headCheckClicked)
        self.socketsWidgetHead.sortSig.connect(self.sockets_sortAfter)
        self.treeWidget_8.setHeader(self.socketsWidgetHead)

        self.treeWidget_8.headerItem().setText(0,"序号")
        self.treeWidget_8.headerItem().setText(1,"进程ID")
        self.treeWidget_8.headerItem().setText(2,"IP地址")
        self.treeWidget_8.headerItem().setText(3,"端口号")
        self.treeWidget_8.headerItem().setText(4,"协议号")
        self.treeWidget_8.headerItem().setText(5,"协议名称")
        self.treeWidget_8.headerItem().setText(6,"创建时间")
        self.treeWidget_8.itemClicked.connect(self.sockets_ItemClicked)
        self.treeWidget_8.setSortingEnabled(True)
        self.treeWidget_8.sortByColumn(0,Qt.AscendingOrder)

        self.tcscanResultCount = 0
        self.tcscanWidgetHead = CheckBoxHeader()
        self.tcscanWidgetHead.stateChanged.connect(self.tcscan_headCheckClicked)
        self.tcscanWidgetHead.sortSig.connect(self.tcscan_sortAfter)
        self.treeWidget_9.setColumnCount(5)
        self.treeWidget_9.setHeader(self.tcscanWidgetHead)

        self.treeWidget_9.headerItem().setText(0,"序号")
        self.treeWidget_9.headerItem().setText(1,"卷名称")
        self.treeWidget_9.headerItem().setText(2,"加密算法")
        self.treeWidget_9.headerItem().setText(3,"加密模式")
        self.treeWidget_9.headerItem().setText(4,"密钥文件")
        self.treeWidget_9.itemClicked.connect(self.tcscan_ItemClicked)
        self.treeWidget_9.setSortingEnabled(True)
        self.treeWidget_9.sortByColumn(0,Qt.AscendingOrder)

        self.bitlockerResultCount = 0
        self.bitlockerWidgetHead = CheckBoxHeader()
        self.bitlockerWidgetHead.stateChanged.connect(self.bitlocker_headCheckClicked)
        self.tcscanWidgetHead.sortSig.connect(self.bitlocker_sortAfter)
        self.treeWidget_10.setColumnCount(3)
        self.treeWidget_10.setHeader(self.bitlockerWidgetHead)

        self.treeWidget_10.headerItem().setText(0,"序号")
        self.treeWidget_10.headerItem().setText(1,"加密算法")
        self.treeWidget_10.headerItem().setText(2,"密钥文件")
        self.treeWidget_10.itemClicked.connect(self.bitlocker_ItemClicked)
        self.treeWidget_10.setSortingEnabled(True)
        self.treeWidget_10.sortByColumn(0,Qt.AscendingOrder)
        #self.stackedWidget.setCurrentIndex(2)
    
    def bitlocker_headCheckClicked(self,state):
        nCount = self.treeWidget_10.topLevelItemCount()
        for i in range(0,nCount):
            item = self.treeWidget_10.topLevelItem(i)
            item.setCheckState(0,state)

    def bitlocker_sortAfter(self):
        nCount = self.treeWidget_10.topLevelItemCount()
        for i in range(0,nCount):
            item = self.treeWidget_10.topLevelItem(i)
            oldIndex = int(item.text(0))
            index = self.treeWidget_10.indexOfTopLevelItem(item)
            if oldIndex != index:
                item.setText(0,"{0}".format(index))

    def bitlocker_ItemClicked(self,item,column):
        if column == 0:
            nCount = self.treeWidget_10.topLevelItemCount()
            nCheckedCount = 0
            state = Qt.Unchecked
            for i in range(0,nCount):
                item = self.treeWidget_10.topLevelItem(i)
                if item.checkState(0) == Qt.Checked:
                    nCheckedCount = nCheckedCount + 1

            if nCheckedCount >= nCount:
                state = Qt.Checked
            elif nCheckedCount > 0:
                state = Qt.PartiallyChecked

            self.bitlockerWidgetHead.onStateChanged(state)


    def tcscan_headCheckClicked(self,state):
        nCount = self.treeWidget_9.topLevelItemCount()
        for i in range(0,nCount):
            item = self.treeWidget_9.topLevelItem(i)
            item.setCheckState(0,state)
    
    def tcscan_sortAfter(self):
        nCount = self.treeWidget_9.topLevelItemCount()
        for i in range(0,nCount):
            item = self.treeWidget_9.topLevelItem(i)
            oldIndex = int(item.text(0))
            index = self.treeWidget_9.indexOfTopLevelItem(item)
            if oldIndex != index:
                item.setText(0,"{0}".format(index))

    def tcscan_ItemClicked(self,item,column):
        if column == 0:
            nCount = self.treeWidget_9.topLevelItemCount()
            nCheckedCount = 0
            state = Qt.Unchecked
            for i in range(0,nCount):
                item = self.treeWidget_9.topLevelItem(i)
                if item.checkState(0) == Qt.Checked:
                    nCheckedCount = nCheckedCount + 1

            if nCheckedCount >= nCount:
                state = Qt.Checked
            elif nCheckedCount > 0:
                state = Qt.PartiallyChecked

            self.tcscanWidgetHead.onStateChanged(state)

    def sockets_headCheckClicked(self,state):
        nCount = self.treeWidget_8.topLevelItemCount()
        for i in range(0,nCount):
            item = self.treeWidget_8.topLevelItem(i)
            item.setCheckState(0,state)
     
    def sockets_sortAfter(self):
        nCount = self.treeWidget_8.topLevelItemCount()
        for i in range(0,nCount):
            item = self.treeWidget_8.topLevelItem(i)
            oldIndex = int(item.text(0))
            index = self.treeWidget_8.indexOfTopLevelItem(item)
            if oldIndex != index:
                item.setText(0,"{0}".format(index))

    def sockets_ItemClicked(self,item,column):
        if column == 0:
            nCount = self.treeWidget_8.topLevelItemCount()
            nCheckedCount = 0
            state = Qt.Unchecked
            for i in range(0,nCount):
                item = self.treeWidget_8.topLevelItem(i)
                if item.checkState(0) == Qt.Checked:
                    nCheckedCount = nCheckedCount + 1

            if nCheckedCount >= nCount:
                state = Qt.Checked
            elif nCheckedCount > 0:
                state = Qt.PartiallyChecked

            self.socketsWidgetHead.onStateChanged(state)

    def driverscan_headCheckClicked(self,state):
        nCount = self.treeWidget_7.topLevelItemCount()
        for i in range(0,nCount):
            item = self.treeWidget_7.topLevelItem(i)
            item.setCheckState(0,state)
    
    def driverscan_sortAfter(self):
        nCount = self.treeWidget_7.topLevelItemCount()
        for i in range(0,nCount):
            item = self.treeWidget_7.topLevelItem(i)
            oldIndex = int(item.text(0))
            index = self.treeWidget_7.indexOfTopLevelItem(item)
            if oldIndex != index:
                item.setText(0,"{0}".format(index))

    def driverscan_ItemClicked(self,item,column):
        if column == 0:
            nCount = self.treeWidget_7.topLevelItemCount()
            nCheckedCount = 0
            state = Qt.Unchecked
            for i in range(0,nCount):
                item = self.treeWidget_7.topLevelItem(i)
                if item.checkState(0) == Qt.Checked:
                    nCheckedCount = nCheckedCount + 1

            if nCheckedCount >= nCount:
                state = Qt.Checked
            elif nCheckedCount > 0:
                state = Qt.PartiallyChecked

            self.driverscanWidgetHead.onStateChanged(state)


    def netscan_headCheckClicked(self,state):
        nCount = self.treeWidget_5.topLevelItemCount()
        for i in range(0,nCount):
            item = self.treeWidget_5.topLevelItem(i)
            item.setCheckState(0,state)

    def netscan_sortAfter(self):
        nCount = self.treeWidget_5.topLevelItemCount()
        for i in range(0,nCount):
            item = self.treeWidget_5.topLevelItem(i)
            oldIndex = int(item.text(0))
            index = self.treeWidget_5.indexOfTopLevelItem(item)
            if oldIndex != index:
                item.setText(0,"{0}".format(index))

    def netscan_ItemClicked(self,item,column):
        if column == 0:
            nCount = self.treeWidget_5.topLevelItemCount()
            nCheckedCount = 0
            state = Qt.Unchecked
            for i in range(0,nCount):
                item = self.treeWidget_5.topLevelItem(i)
                if item.checkState(0) == Qt.Checked:
                    nCheckedCount = nCheckedCount + 1

            if nCheckedCount >= nCount:
                state = Qt.Checked
            elif nCheckedCount > 0:
                state = Qt.PartiallyChecked

            self.netscanWidgetHead.onStateChanged(state)
        

    def filescan_ItemClicked(self,item,column):
        if column == 0:
            nCount = self.treeWidget_3.topLevelItemCount()
            nCheckedCount = 0
            state = Qt.Unchecked
            for i in range(0,nCount):
                item = self.treeWidget_3.topLevelItem(i)
                if item.checkState(0) == Qt.Checked:
                    nCheckedCount = nCheckedCount + 1

            if nCheckedCount >= nCount:
                state = Qt.Checked
            elif nCheckedCount > 0:
                state = Qt.PartiallyChecked

            self.filescanWidgetHead.onStateChanged(state)
           
    def filescan_sortAfter(self):
        nCount = self.treeWidget_3.topLevelItemCount()
        for i in range(0,nCount):
            item = self.treeWidget_3.topLevelItem(i)
            oldIndex = int(item.text(0))
            index = self.treeWidget_3.indexOfTopLevelItem(item)
            if oldIndex != index:
                item.setText(0,"{0}".format(index))

    def filescan_headCheckClicked(self,state):
        nCount = self.treeWidget_3.topLevelItemCount()
        for i in range(0,nCount):
            item = self.treeWidget_3.topLevelItem(i)
            item.setCheckState(0,state)

    def svcscan_sortAfter(self):
        nCount = self.treeWidget_2.topLevelItemCount()
        for i in range(0,nCount):
            item = self.treeWidget_2.topLevelItem(i)
            oldIndex = int(item.text(0))
            index = self.treeWidget_2.indexOfTopLevelItem(item)
            if oldIndex != index:
                item.setText(0,"{0}".format(index))

    def svcscan_headCheckClicked(self,state):
        nCount = self.treeWidget_2.topLevelItemCount()
        for i in range(0,nCount):
            item = self.treeWidget_2.topLevelItem(i)
            item.setCheckState(0,state)
    
    def svcscan_ItemClicked(self,item,column):
        if column == 0:
            nCount = self.treeWidget_2.topLevelItemCount()
            nCheckedCount = 0
            state = Qt.Unchecked
            for i in range(0,nCount):
                item = self.treeWidget_2.topLevelItem(i)
                if item.checkState(0) == Qt.Checked:
                    nCheckedCount = nCheckedCount + 1

            if nCheckedCount >= nCount:
                state = Qt.Checked
            elif nCheckedCount > 0:
                state = Qt.PartiallyChecked

            self.svcscanWidgetHead.onStateChanged(state)
    
    def devscanParse(self,status,result):
        if status == "devscanRuning":
            self.deviceItem.setText(2,'解析中...')
            if result != {}:
                self.devscanResultCount = self.devscanResultCount + 1
                text = "共{0}项结果".format(self.netscanResultCount)
                self.deviceItem.setText(1,text)

                item = QTreeWidgetItem(self.treeWidget_6)
                item.setText(0,result["Name"])
                item.setText(1,"驱动")
                for dev in result["devs"]:
                    item1 = QTreeWidgetItem(item)
                    item1.setText(0,dev["Name"])
                    item1.setText(1,"内置设备")

                    item1.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable )
                    item1.setCheckState(0,Qt.Unchecked)
                    item.addChild(item1)

                    for att in dev["atts"]:
                        item2 = QTreeWidgetItem(item1)
                        item2.setText(0,att["Name"])
                        item2.setText(1,"外接设备")

                        item2.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable )
                        item2.setCheckState(0,Qt.Unchecked)
                        item1.addChild(item2)
                
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable )
                item.setCheckState(0,Qt.Unchecked)
                self.treeWidget_6.addTopLevelItem(item)

        if status == "devscanEnd":
            self.completeProgressCount = self.completeProgressCount + 1
            value =(100/ self.progressBarCount)*self.completeProgressCount
            self.progressBar.setProperty("value", value)
            self.deviceItem.setText(2,'解析成功')


    def netscanParse(self,status,result):
        if status == "netscanRuning":
            self.netscanItem.setText(2,'解析中...')
            if result != {}:
                self.netscanResultCount = self.netscanResultCount + 1
                text = "共{0}项结果".format(self.netscanResultCount)
                self.netscanItem.setText(1,text)

                item = CTreeWidgetItemEx(self.treeWidget_5)
                item.setText(0,"{0}".format(self.netscanResultCount))
                item.setText(2,result["local"])
                item.setText(3,result["remote"])
                item.setText(1,"{0}".format(result["pid"]))
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable )
                item.setCheckState(0,Qt.Unchecked)
                self.treeWidget_5.addTopLevelItem(item)

        if status == "netscanEnd":
            self.completeProgressCount = self.completeProgressCount + 1
            value =(100/ self.progressBarCount)*self.completeProgressCount
            self.progressBar.setProperty("value", value)
            self.netscanItem.setText(2,'解析成功')

    
    def socketsParse(self,status,result):
        if status == "socketsRuning":
            self.socketsItem.setText(2,'解析中...')
            if result != {}:
                self.socketsResultCount = self.socketsResultCount + 1
                text = "共{0}项结果".format(self.socketsResultCount)
                self.socketsItem.setText(1,text)

                item = CTreeWidgetItemEx(self.treeWidget_8)
                item.setText(0,"{0}".format(self.socketsResultCount))
                item.setText(1,str(result["pid"]))
                item.setText(2,result["address"])
                item.setText(3,str(result["port"]))
                item.setText(4,str(result["proto"]))
                item.setText(5,result["protocol"])
                item.setText(6,result["create_time"])

                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable )
                item.setCheckState(0,Qt.Unchecked)
                self.treeWidget_8.addTopLevelItem(item)

        if status == "socketsEnd":
            self.completeProgressCount = self.completeProgressCount + 1
            value =(100/ self.progressBarCount)*self.completeProgressCount
            self.progressBar.setProperty("value", value)
            self.socketsItem.setText(2,'解析成功')

    def driverscanParse(self,status,result):
        if status == "driverscanRuning":
            self.driverItem.setText(2,'解析中...')
            if result != {}:
                self.driverscanResultCount = self.driverscanResultCount + 1
                text = "共{0}项结果".format(self.dlllistResultCount)
                self.driverItem.setText(1,text)

                item = CTreeWidgetItemEx(self.treeWidget_7)
                item.setText(0,"{0}".format(self.driverscanResultCount))
                item.setText(1,result["name"])
                item.setText(2,result["servicekey"])
                item.setText(3,result["path"])
                item.setText(4,str(result["size"]))
                item.setText(5,str(result["ptr_no"]))
                item.setText(6,str(result["hnd_no"]))

                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable )
                item.setCheckState(0,Qt.Unchecked)
                self.treeWidget_7.addTopLevelItem(item)
        if status == "driverscanEnd":
            self.completeProgressCount = self.completeProgressCount + 1
            value =(100/ self.progressBarCount)*self.completeProgressCount
            self.progressBar.setProperty("value", value)
            self.driverItem.setText(2,'解析成功')



    def dlllistParse(self,status,result):
        if status == "dlllistRuning":
            self.dlllistItem.setText(2,'解析中...')
            if result != {}:
                self.dlllistResultCount = self.dlllistResultCount + 1
                text = "共{0}项结果".format(self.dlllistResultCount)
                self.dlllistItem.setText(1,text)

                item = QTreeWidgetItem(self.treeWidget_4)
                item.setText(0,"[{0}]{1}".format(result["UniqueProcessId"],result["CommandLine"]))

                for dll in result["dlls"]:
                    if dll != "":
                        child = QTreeWidgetItem(item)
                        child.setText(0,dll)
                        child.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable )
                        child.setCheckState(0,Qt.Unchecked)
                        item.addChild(child)

                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable )
                item.setCheckState(0,Qt.Unchecked)
                self.treeWidget_4.addTopLevelItem(item)

        if status == "filescanEnd":
            self.completeProgressCount = self.completeProgressCount + 1
            value =(100/ self.progressBarCount)*self.completeProgressCount
            self.progressBar.setProperty("value", value)
            self.dlllistItem.setText(2,'解析成功')

    def filescanParse(self,status,result):
        if status == "filescanRuning":
            self.fileItem.setText(2,'解析中...')
            if result != {}:
                self.filescanResultCount = self.filescanResultCount + 1
                text = "共{0}项结果".format(self.filescanResultCount)
                self.fileItem.setText(1,text)

                item = CTreeWidgetItemEx(self.treeWidget_3)
                item.setText(0,"{0}".format(self.filescanResultCount))
                item.setText(1,result["path"])
                
                item.setText(2,str(int(result["ptr_no"])))
                item.setText(3,str(int(result["hnd_no"])))
              
                item.setText(4,result["access"])

                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable )
                item.setCheckState(0,Qt.Unchecked)
                self.treeWidget_3.addTopLevelItem(item)
        if status == "filescanEnd":
            self.completeProgressCount = self.completeProgressCount + 1
            value =(100/ self.progressBarCount)*self.completeProgressCount
            self.progressBar.setProperty("value", value)
            self.fileItem.setText(2,'解析成功')

    def svcscanParse(self,status,result):
        if status == "svcscanRuning":
            self.svclistItem.setText(2,'解析中...')
            if result != {}:
                self.svcscantResultCount = self.svcscantResultCount + 1
                text = "共{0}项结果".format(self.svcscantResultCount)
                self.svclistItem.setText(1,text)

                item = CTreeWidgetItemEx(self.treeWidget_2)
                item.setText(0,"{0}".format(self.svcscantResultCount))
                item.setText(1,result["ServiceName"])
                item.setText(2,"{0}".format(result["Pid"]))
                item.setText(3,result["DisplayName"])
                item.setText(4,result["Type"])
                item.setText(5,result["State"])
                item.setText(6,result["Binary"])

                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable )
                item.setCheckState(0,Qt.Unchecked)
                self.treeWidget_2.addTopLevelItem(item)

        if status == "svcscanEnd":
            self.completeProgressCount = self.completeProgressCount + 1
            value =(100/ self.progressBarCount)*self.completeProgressCount
            self.progressBar.setProperty("value", value)
            self.svclistItem.setText(2,'解析成功')

    def pslist_sortAfter(self):
        nCount = self.pslistWidget.topLevelItemCount()
        for i in range(0,nCount):
            item = self.pslistWidget.topLevelItem(i)
            oldIndex = int(item.text(0))
            index = self.pslistWidget.indexOfTopLevelItem(item)
            if oldIndex != index:
                item.setText(0,"{0}".format(index))

    def pslist_ItemClicked(self,item,column):
        if column == 0:
            nCount = self.pslistWidget.topLevelItemCount()
            nCheckedCount = 0
            state = Qt.Unchecked
            for i in range(0,nCount):
                item = self.pslistWidget.topLevelItem(i)
                if item.checkState(0) == Qt.Checked:
                    nCheckedCount = nCheckedCount + 1

            if nCheckedCount >= nCount:
                state = Qt.Checked
            elif nCheckedCount > 0:
                state = Qt.PartiallyChecked

            self.pslistWidgetHead.onStateChanged(state)

    def pslist_headCheckClicked(self,state):
        nCount = self.pslistWidget.topLevelItemCount()
        for i in range(0,nCount):
            item = self.pslistWidget.topLevelItem(i)
            item.setCheckState(0,state)

    def returnHomePage(self):
         self.stackedWidget.setCurrentIndex(0)
         

    def stopParse(self):
        self.timer.stop()
        self.rekall_thread.requestInterruption()
        self.isStop = True
    
    def tcscanParse(self,status,result):
        if status == "tcscanRuning":
            self.truecryptItem.setText(2,'解析中...')
            if result != {}:
                self.tcscanResultCount = self.tcscanResultCount + 1
                text = "共{0}项结果".format(self.tcscanResultCount)
                self.truecryptItem.setText(1,text)

                item = CTreeWidgetItemEx(self.treeWidget_9)
                item.setText(0,"{0}".format(self.tcscanResultCount))
                item.setText(1,result["Volume"])
                item.setText(2,result["ea"])
                item.setText(3,result["mode"])
                item.setText(4,result["keyfile"])

                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable )
                item.setCheckState(0,Qt.Unchecked)
                self.treeWidget_9.addTopLevelItem(item)

        elif status == "tcscanEnd":
            self.completeProgressCount = self.completeProgressCount + 1
            value =(100/ self.progressBarCount)*self.completeProgressCount
            self.progressBar.setProperty("value", value)
            self.truecryptItem.setText(2,'解析成功')
    
    def bitlockerParse(self,status,result):
        if status == "bitlockerRuning":
            self.bitlockerItem.setText(2,'解析中...')
            if result != {}:
                self.bitlockerResultCount = self.bitlockerResultCount + 1
                text = "共{0}项结果".format(self.bitlockerResultCount)
                self.bitlockerItem.setText(1,text)

                item = CTreeWidgetItemEx(self.treeWidget_10)
                item.setText(0,"{0}".format(self.bitlockerResultCount))
                item.setText(1,result["Cipher"])
                item.setText(2,result["keyfile"])

                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable )
                item.setCheckState(0,Qt.Unchecked)
                self.treeWidget_10.addTopLevelItem(item)

        elif status == "bitlockerEnd":
            self.completeProgressCount = self.completeProgressCount + 1
            value =(100/ self.progressBarCount)*self.completeProgressCount
            self.progressBar.setProperty("value", value)
            self.bitlockerItem.setText(2,'解析成功')

    def pslistParse(self,status,result):
        if status == "pslistRuning":
            self.pslistItem.setText(2,'解析中...')
            if result != {}:
                self.pslistResultCount = self.pslistResultCount + 1;
                text = "共{0}项结果".format(self.pslistResultCount)
                self.pslistItem.setText(1,text)
                
                item = CTreeWidgetItemEx(self.pslistWidget)
                item.setText(0,"{0}".format(self.pslistResultCount))
                item.setText(1,result["process_name"])
                item.setText(2,"{0}".format(result["process_id"]))
                item.setText(3,"{0}".format(result["ppid"]))
                item.setText(4,"{0}".format(result["thread_count"]))
                item.setText(5,"{0}".format(result["handle_count"]))
                item.setText(6,"{0}".format(result["session_id"]))
                item.setText(7,"{0}".format(result["wow64"]))
                item.setText(8,result["process_create_time"])
                item.setText(9,result["process_exit_time"])
               
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable )
                item.setCheckState(0,Qt.Unchecked)
                self.pslistWidget.addTopLevelItem(item)

        elif status == "pslistEnd":
            self.completeProgressCount = self.completeProgressCount + 1
            value =(100/ self.progressBarCount)*self.completeProgressCount
            self.progressBar.setProperty("value", value)
            self.pslistItem.setText(2,'解析成功')
    
    def parseComplete(self):
        self.timer.stop()
        self.stackedWidget.setCurrentIndex(2)
       
        total = 0 
        total = total + self.pslistResultCount
        total = total + self.svcscantResultCount  
        total = total + self.filescanResultCount 
        total = total + self.dlllistResultCount 
        total = total + self.netscanResultCount
        total = total + self.devscanResultCount
        total = total + self.driverscanResultCount
        total = total + self.socketsResultCount
        total = total + self.tcscanResultCount
        total = total + self.bitlockerResultCount

        text = ""
        pix = None
        if self.isStop == False:
            pix = QtGui.QPixmap(":/images/00011[40x40x8BPP].png")
            text = "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#484848;\">解析已完成，共发现</span><span style=\" font-size:12pt; font-weight:600; color:#00aa00;\">{0}</span><span style=\" font-size:12pt; font-weight:600; color:#535353;\">项结果，用时</span><span style=\" font-size:12pt; font-weight:600; color:#ff5500;\">{1}</span></p></body></html>".format(total,self.useTimetext)
        else:
            pix = QtGui.QPixmap(":/images/00012[40x40x8BPP].png")
            text = "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#484848;\">解析被终止，已发现</span><span style=\" font-size:12pt; font-weight:600; color:#00aa00;\">{0}</span><span style=\" font-size:12pt; font-weight:600; color:#535353;\">项结果，用时</span><span style=\" font-size:12pt; font-weight:600; color:#ff5500;\">{1}</span></p></body></html>".format(total,self.useTimetext)
            self.isStop = False

        self.label_11.setText(text)
        self.label_10.setPixmap(pix)

    def startRun(self):
        self.treeWidget.clear()
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
               
                self.rekall_thread.enablePslist()
                self.pslistResultCount = 0
                self.pslistWidget.clear()
                self.progressBarCount = self.progressBarCount + 1

            if self.bsvcscan:
                self.svclistItem = QTreeWidgetItem(self.treeWidget)
                self.svclistItem.setText(0,'加载服务信息')
                self.svclistItem.setText(1,'共0项结果')
                self.svclistItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.svclistItem)
                
                self.rekall_thread.enableSvcScan()
                self.svcscantResultCount = 0
                self.treeWidget_2.clear()
                self.progressBarCount = self.progressBarCount + 1

            if self.bfilescan:
                self.fileItem = QTreeWidgetItem(self.treeWidget)
                self.fileItem.setText(0,'已打开文件信息')
                self.fileItem.setText(1,'共0项结果')
                self.fileItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.fileItem)

                self.rekall_thread.enableFileScan()
                self.filescanResultCount = 0
                self.treeWidget_3.clear()
                self.progressBarCount = self.progressBarCount + 1

            if self.bdlllist:
                self.dlllistItem = QTreeWidgetItem(self.treeWidget)
                self.dlllistItem.setText(0,'动态链接库信息')
                self.dlllistItem.setText(1,'共0项结果')
                self.dlllistItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.dlllistItem)

                self.rekall_thread.enableDllList()
                self.dlllistResultCount = 0
                self.treeWidget_4.clear()
                self.progressBarCount = self.progressBarCount + 1

            if self.bnetscan:
                self.netscanItem = QTreeWidgetItem(self.treeWidget)
                self.netscanItem.setText(0,'网络连接信息')
                self.netscanItem.setText(1,'共0项结果')
                self.netscanItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.netscanItem)

                self.rekall_thread.enableNetScan()
                self.netscanResultCount = 0
                self.treeWidget_5.clear()
                self.progressBarCount = self.progressBarCount + 1
            if self.bdevice:
                self.deviceItem = QTreeWidgetItem(self.treeWidget)
                self.deviceItem.setText(0,'加载设备信息')
                self.deviceItem.setText(1,'共0项结果')
                self.deviceItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.deviceItem)

                self.rekall_thread.enableDevScan()
                self.devscanResultCount = 0
                self.treeWidget_6.clear()
                self.progressBarCount = self.progressBarCount + 1
            if self.bdriverscan:
                self.driverItem = QTreeWidgetItem(self.treeWidget)
                self.driverItem.setText(0,'加载驱动信息')
                self.driverItem.setText(1,'共0项结果')
                self.driverItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.driverItem)

                self.rekall_thread.enableDriverscan()
                self.driverscanResultCount = 0
                self.treeWidget_7.clear()
                self.progressBarCount = self.progressBarCount + 1
            if self.bsockets:
                self.socketsItem = QTreeWidgetItem(self.treeWidget)
                self.socketsItem.setText(0,'Sockets信息')
                self.socketsItem.setText(1,'共0项结果')
                self.socketsItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.socketsItem)

                self.rekall_thread.enbaleSockets()
                self.socketsResultCount = 0
                self.treeWidget_8.clear()
                self.progressBarCount = self.progressBarCount + 1
            if self.btruecrypt:
                self.truecryptItem = QTreeWidgetItem(self.treeWidget)
                self.truecryptItem.setText(0,'TrueCrypt密钥')
                self.truecryptItem.setText(1,'共0项结果')
                self.truecryptItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.truecryptItem)

                self.rekall_thread.enableTc()
                self.tcscanResultCount = 0
                self.treeWidget_9.clear()
                self.progressBarCount = self.progressBarCount + 1
            if self.bbitlocker:
                self.bitlockerItem = QTreeWidgetItem(self.treeWidget)
                self.bitlockerItem.setText(0,'BitLocker密钥')
                self.bitlockerItem.setText(1,'共0项结果')
                self.bitlockerItem.setText(2,'等待解析...')
                self.treeWidget.addTopLevelItem(self.bitlockerItem)

                self.rekall_thread.enableBitlocker()
                self.bitlockerResultCount = 0
                self.treeWidget_10.clear()
                self.progressBarCount = self.progressBarCount + 1

            self.rekall_thread.start()
           
            self.sencond = 0
            self.minutes = 0
            self.hour = 0

            
            self.timer.start(1000)

    def updateTime(self):
        self.sencond = self.sencond + 1
        if self.sencond == 60 :
            self.sencond = 0
            self.minutes = self.minutes + 1
        if self.minutes == 60:
            self.minutes = 0
            self.hour = self.hour + 1

        self.useTimetext = "{0:02d}:{1:02d}:{2:02d}".format(self.hour,self.minutes,self.sencond)
        self.label_9.setText(self.useTimetext)

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

    def paintEvent(self, event):
        painter2 = QPainter(self)
        painter2.setPen(Qt.gray)
        painter2.drawPolyline(QPointF(0, 100), QPointF(0, self.height() - 1), QPointF(self.width() - 1, self.height() - 1), QPointF(self.width() - 1, 100))
        painter2.end()
          