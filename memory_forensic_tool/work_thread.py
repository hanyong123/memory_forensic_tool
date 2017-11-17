from PyQt5.QtCore import (QThread,pyqtSignal)

from rekall import constants
from rekall import session
from rekall import plugins
import os

import logging

logging.basicConfig(level=logging.DEBUG)

class RekallThread(QThread):
    
    rekallEndSig = pyqtSignal()

    pslistSig = pyqtSignal(str,dict)
    svcSig = pyqtSignal(str,dict)
    filescanSig = pyqtSignal(str,dict)

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
            logger=logging.getLogger(),
            repository_path=constants.PROFILE_REPOSITORIES
            )

        self.EnablePslist = False
        self.EnableSvcScan = False
        self.EnableFileScan = False

    def enablePslist(self,enable = True):
        self.EnablePslist = enable

    def enableSvcScan(self,enable = True):
        self.EnableSvcScan = enable

    def enableFileScan(self,enable = True):
        self.EnableFileScan = enable

    def run(self):
        if self.EnablePslist:
            self.pslist()
        
        if self.isInterruptionRequested():
            self.rekallEndSig.emit()
            return

        if self.EnableSvcScan:
            self.svcscan()

        if self.isInterruptionRequested():
            self.rekallEndSig.emit()
            return

        if self.EnableFileScan:
            self.filescan()

        if self.isInterruptionRequested():
            self.rekallEndSig.emit()
            return

        self.rekallEndSig.emit()

    def pslist(self):
        self.pslistSig.emit("pslistRuning",dict())
        try:
            for row in self.s.plugins.pslist().collect():
                if self.isInterruptionRequested():
                    return
                d = {}
                d["process_name"] = str(row["_EPROCESS"].name)
                d["process_id"] = int(row["_EPROCESS"].pid)
                d["ppid"] = int(row["ppid"])
                d["thread_count"] = int(row["thread_count"])
                d["handle_count"] = int(row["handle_count"])
                d["session_id"] = int(row["session_id"])
                d["wow64"] = row["wow64"]
                d["process_create_time"] = str(row["process_create_time"])
                d["process_exit_time"] = str(row["process_exit_time"]) 
                self.pslistSig.emit("pslistRuning",d)
        except:
            self.pslistSig.emit("pslistEnd",dict())
            return
        

        self.pslistSig.emit("pslistEnd",dict())
        return

    def svcscan(self):
        self.svcSig.emit("svcscanRuning",dict())
        try:
            for rec in self.s.plugins.svcscan().calculate():
                if self.isInterruptionRequested():
                    return
                result = {}
                result["Pid"] = int(rec.Pid)
                result["ServiceName"] = unicode(rec.ServiceName.deref())
                result["DisplayName"] = unicode(rec.DisplayName.deref())
                result["Type"] = iter(rec.Type).next()
                result["State"] = str(rec.State)
                result["Binary"] = unicode(rec.Binary)
                self.svcSig.emit("svcscanRuning",result)
        except:
            self.svcSig.emit("svcscanEnd",dict())
            return

        self.svcSig.emit("svcscanEnd",dict())
        return

    def filescan(self):
        self.filescanSig.emit("filescanRuning",dict())
        try:
            for row in self.s.plugins.filescan().collect():
                if self.isInterruptionRequested():
                    return
                d = {}
                d["path"] = row["path"]
                d["ptr_no"] = int(row["ptr_no"])
                d["hnd_no"] = int(row["hnd_no"])
                d["access"] = row["access"]
                self.filescanSig.emit("filescanRuning",d)
        except:
            self.filescanSig.emit("filescanEnd",dict())
            return

        self.filescanSig.emit("filescanEnd",dict())
        return


