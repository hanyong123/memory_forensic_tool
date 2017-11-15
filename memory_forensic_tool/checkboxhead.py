from PyQt5.QtCore import  (Qt,QRect)
from PyQt5.QtWidgets import (QHeaderView,QStyleOptionButton,QStyle)

class CheckBoxHeader(QHeaderView):

    def __init__(self,orientation=Qt.Horizontal,parent = None):
        super(CheckBoxHeader,self).__init__(orientation,parent)

        self.isOn = False


    def paintSection(painter,rect,logicalIndex):

        painter.save()
        super(CheckBoxHeader,self).paintSection(painter,rect,logicalIndex)
        painter.restore()
        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(10,10,10,10)
            if self.isOn:
                option.state = QStyle.State_On
            else:
                option.state = QStyle.State_Off

            self.style().drawPrimitive(QStyle.PE_IndicatorCheckBox,option,painter)

    def mousePressEvent(event):
        if self.isOn:
            self.isOn = False
        else:
            self.isOn = True

        super(CheckBoxHeader,self).mousePressEvent(event)




