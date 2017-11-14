from mainwindow import MainWindow
from PyQt5.QtWidgets import (QApplication)
from PyQt5.QtCore import (QAbstractNativeEventFilter)
from ctypes import wintypes


class WinEventFilter(QAbstractNativeEventFilter):
    def __init__(self, form): 
        super(WinEventFilter, self).__init__()
        self.form = form
    
    def GET_X_LPARAM(self, param):
        return param & 0xffff

    def GET_Y_LPARAM(self, param):
        return param >> 16

    def nativeEventFilter(self, eventType, message):
        msg = wintypes.MSG.from_address(message.__int__())
        if msg.message == 0x84: #WM_NCHITTEST
            if self.form:
                xPos = self.GET_X_LPARAM(msg.lParam) - self.form.frameGeometry().x()
                yPos = self.GET_Y_LPARAM(msg.lParam) - self.form.frameGeometry().y()

                if hasattr(self.form, 'isInTitle') and self.form.isInTitle(xPos, yPos):
                     return True, 0x2 #HTCAPTION

        return False, 0

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    win_event_filter = WinEventFilter(mainWindow)
    app.installNativeEventFilter(win_event_filter) 
    mainWindow.show()
    sys.exit(app.exec_())
