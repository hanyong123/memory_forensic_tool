from PyQt5.QtCore import  (Qt,QRect,QSize,QEvent,QAbstractItemModel,pyqtSignal,QVariant)
from PyQt5.QtWidgets import (QHeaderView,QStyleOptionButton,QStyle,QCheckBox,QTreeWidget,QTreeWidgetItem)
from PyQt5.QtGui import QMouseEvent

class CheckBoxHeader(QHeaderView):

    stateChanged = pyqtSignal(int)
    def __init__(self,orientation=Qt.Horizontal,parent = None):
        super(CheckBoxHeader,self).__init__(orientation,parent)

        self.isOn = False

        self.m_bPressed = False
        self.m_bChecked = False
        self.m_bTristate = False
        self.m_bNoChange = False
        self.m_bMoving = False

        self.setHighlightSections(False)
        self.setMouseTracking(True)

        self.setSectionsClickable(True)

    def onStateChanged(self,state):
        if state == Qt.PartiallyChecked:
            self.m_bTristate = True
            self.m_bNoChange = True
        else:
            self.m_bNoChange = False

        self.m_bChecked = (state != Qt.Unchecked)
        self.update()

    def paintSection(self,painter,rect,logicalIndex):

        painter.save()
        super(CheckBoxHeader,self).paintSection(painter,rect,logicalIndex)
        painter.restore()
        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.initFrom(self)
            option.rect = QRect(5,5,15,15)
            if self.m_bChecked:
                option.state |= QStyle.State_Sunken

            if self.m_bTristate and self.m_bNoChange:
                option.state |= QStyle.State_NoChange
            else:
                option.state |= self.m_bChecked and QStyle.State_On or QStyle.State_Off
           
            if self.testAttribute(Qt.WA_Hover) and self.underMouse():
                if self.m_bMoving :
                    option.state |= QStyle.State_MouseOver;
                else:
                    option.state &= ~QStyle.State_MouseOver;

            
            checkBox = QCheckBox()
            option.iconSize = QSize(20, 20);
            self.style().drawPrimitive(QStyle.PE_IndicatorCheckBox,option,painter,checkBox)

    def mousePressEvent(self,event):
        nColumn = self.logicalIndexAt(event.pos())
        if (event.buttons() & Qt.LeftButton) and (nColumn == 0):
            self.m_bPressed = True
        else:
            super(CheckBoxHeader,self).mousePressEvent(event)
       

    def mouseReleaseEvent(self,event):
         if self.m_bPressed:
             if self.m_bTristate and self.m_bNoChange:
                 self.m_bChecked = True
                 self.m_bNoChange = False
             else:
                 self.m_bChecked = not(self.m_bChecked)

             self.update()

             state = self.m_bChecked and  Qt.Checked or  Qt.Unchecked

             self.stateChanged.emit(state)
         else:
             super(CheckBoxHeader,self).mouseReleaseEvent(event)

         self.m_bPressed = False

    def event(self,e):
        t = e.type()
        if e.type() == QEvent.Enter:
            nColumn = self.logicalIndexAt(e.x())

            if nColumn == 0:
                self.m_bMoving = e.type() == QEvent.Enter

                self.update()
                return True

        return super(CheckBoxHeader,self).event(e)




class CTreeWidgetItemEx(QTreeWidgetItem):

    def __init__(self, parent = None,type = QTreeWidgetItem.Type):
        self.t = parent
        return super(CTreeWidgetItemEx, self).__init__(parent,type)

    def __lt__(self, y):
        column = self.t.sortColumn()
        if self.text(column).isdigit() and y.text(column).isdigit():
            a = int(self.text(column))
            b = int(y.text(column))
            return a < b
        else:
            return cmp(self.text(column),y.text(column))
    
     
   





