from PyQt5.QtCore import (QThread,pyqtSignal)

from rekall import constants
from rekall import session
from rekall import plugins
import os

class RekallThread(QThread):
    pslistSig = pyqtSignal(str,dict)
    rekallEndSig = pyqtSignal()

    def __init__(self,parent=None):
        super(RekallThread,self).__init__(parent)
       

        
    def Init(self,image_file_name=None):
        profiles_path = os.path.abspath(os.curdir)+"\\profile"
        if( os.path.exists(profiles_path)):
            constants.PROFILE_REPOSITORIES.insert(0,profiles_path)
        if(os.path.isabs(image_file_name) == False):
            image_file_name = os.curdir + "\\"+image_file_name

        self.s = session.Session(
            filename=image_file_name,
            autodetect=["rsds"],
            cache_dir = ".rekall_cache",
            repository_path=constants.PROFILE_REPOSITORIES
            )
        self.EnablePslist = False

    def enablePslist(self,enable = True):
        self.EnablePslist = enable

    def run(self):
        if self.EnablePslist:
            self.pslist()

        self.rekallEndSig.emit()

    def pslist(self):
        self.pslistSig.emit("pslistRuning",dict())
        try:
            for row in self.s.plugins.pslist().collect():
                self.pslistSig.emit("pslistRuning",row)
        except:
            self.pslistSig.emit("pslistEnd",dict())
            return
        

        self.pslistSig.emit("pslistEnd",dict())
        return