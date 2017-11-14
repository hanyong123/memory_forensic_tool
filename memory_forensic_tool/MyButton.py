from PyQt5 import  QtWidgets
from PyQt5.QtGui import QPainter

class ImageButton( QtWidgets.QToolButton):

    def __init__(self,parent = None):
        super(ImageButton,self).__init__(parent)


    def paintEvent(self,event):
        super(ImageButton,self).paintEvent(event)
        


