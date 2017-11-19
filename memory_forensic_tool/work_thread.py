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
    dlllistSig =  pyqtSignal(str,dict)
    netscanSig =  pyqtSignal(str,dict)
    devscanSig = pyqtSignal(str,dict)
    driverscanSig = pyqtSignal(str,dict)
    socketsSig =  pyqtSignal(str,dict)
    tcSig  = pyqtSignal(str,dict)
    bitlockerSig = pyqtSignal(str,dict)

    def __init__(self,parent=None):
        super(RekallThread,self).__init__(parent)
        self.bInit = False
        
        
    def Init(self,image_file_name=None):
        if self.bInit == False:
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
            self.bInit = True

        self.devscan_drv = {}
        self.devscan_dev = {}

        self.EnablePslist = False
        self.EnableSvcScan = False
        self.EnableFileScan = False
        self.EnableDllList = False
        self.EnableNetScan = False
        self.EnableDevScan = False
        self.EnableDriverScan = False
        self.EnableSockets = False
        self.EnableTc = False
        self.EnableBitLocker = False

    def enableBitlocker(self,enable = True):
        self.EnableBitLocker = enable

    def enableTc(self,enable = True):
        self.EnableTc = enable

    def enbaleSockets(self,enable =  True):
        self.EnableSockets = enable

    def enableDriverscan(self,enable = True):
        self.EnableDriverScan = enable

    def enableNetScan(self,enable = True):
        self.EnableNetScan  = enable

    def enableDllList(self,enable = True):
        self.EnableDllList = enable

    def enablePslist(self,enable = True):
        self.EnablePslist = enable

    def enableSvcScan(self,enable = True):
        self.EnableSvcScan = enable

    def enableFileScan(self,enable = True):
        self.EnableFileScan = enable

    def enableDevScan(self,enable = True):
        self.EnableDevScan = enable

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

        if self.EnableDllList:
            self.dlllist()

        if self.isInterruptionRequested():
            self.rekallEndSig.emit()
            return

        if self.EnableNetScan:
            self.netscan()

        if self.isInterruptionRequested():
            self.rekallEndSig.emit()
            return

        if self.EnableDevScan:
            self.devscan()

        if self.isInterruptionRequested():
            self.rekallEndSig.emit()
            return

        

        if self.EnableDriverScan:
            self.driverscan()

        if self.isInterruptionRequested():
            self.rekallEndSig.emit()
            return

        if self.EnableSockets:
            self.sockets()

        if self.isInterruptionRequested():
            self.rekallEndSig.emit()
            return

        if self.EnableTc:
            self.tcscan()

        if self.isInterruptionRequested():
            self.rekallEndSig.emit()
            return

        if self.EnableBitLocker:
            self.bitlocker()

        if self.isInterruptionRequested():
            self.rekallEndSig.emit()
            return

        self.rekallEndSig.emit()
    
    def devscan(self):
        self.devscanSig.emit("devscanRuning",dict())

        try:
            for item in self.s.plugins.devicetree().collect():
                if self.isInterruptionRequested():
                    return

                if item["depth"] == 0 and self.devscan_drv == {}:
                    self.devscan_drv["Name"] = unicode(item["Name"])
                    self.devscan_drv["devs"] = []
                elif item["depth"] == 0 and self.devscan_drv != {}:
                     self.devscanSig.emit("devscanRuning",self.devscan_drv)
                     self.devscan_drv = {}
                     self.devscan_drv["Name"] = unicode(item["Name"])
                     self.devscan_drv["devs"] = []


                if item["depth"] == 1 and self.devscan_dev == {}:
                    self.devscan_dev["Name"] = unicode(item["Name"])
                    self.devscan_dev["atts"] = []
                    self.devscan_drv["devs"].append(self.devscan_dev)
                elif item["depth"] == 1 and self.devscan_dev != {}:
                    self.devscan_dev = {}
                    self.devscan_dev["Name"] = unicode(item["Name"])
                    self.devscan_dev["atts"] = []
                    self.devscan_drv["devs"].append(self.devscan_dev)


                if item["depth"] > 1:
                    att = {}
                    att["Name"] = unicode(item["Name"])
                    self.devscan_dev["atts"].append(att)
        
        except:
             self.devscanSig.emit("devscanEnd",dict())
             return

        self.devscanSig.emit("devscanEnd",dict())
        return


    def driverscan(self):
        self.driverscanSig.emit("driverscanRuning",dict())
        try:
            for row in self.s.plugins.driverscan().collect():
                if self.isInterruptionRequested():
                    return

                d = {}
                d["name"] = row["name"]
                d["servicekey"] = row["servicekey"]
                d["path"] = row["path"]
                d["size"] = int(row["size"])
                d["ptr_no"] = int(row["ptr_no"])
                d["hnd_no"] = int(row["hnd_no"])
                self.driverscanSig.emit("driverscanRuning",d)
        except:
            self.driverscanSig.emit("driverscanEnd",dict())
            return

        self.driverscanSig.emit("driverscanEnd",dict())
        return

    def bitlocker(self):
        self.bitlockerSig.emit("bitlockerRuning",dict())
        try:
            for pool, fvek, tweak in s.plugins.bitlockerscan().collect():
                if self.isInterruptionRequested():
                    return
                d = {}
                d["Cipher"] = "AES-{0}".format(len(fvek) * 8)
                fvek = 'FVEK    : {}\n'.format(''.join('{:02x}'.format(ord(i)) for i in fvek))
                tweak = 'TWEAK   : {}\n'.format(''.join('{:02x}'.format(ord(i)) for i in tweak))
                name = "{0:#010x}.bitlocker".format(pool.obj_offset)
                keyfile = os.path.join(os.path.abspath(os.curdir),name)
                key = fvek + tweak
                with open(keyfile, "w") as handle:
                         handle.write(key)
                d["keyfile"] = keyfile
                self.bitlockerSig.emit("bitlockerRuning",d)

        except:
            self.bitlockerSig.emit("bitlockerEnd",dict())
            return

        self.bitlockerSig.emit("bitlockerEnd",dict())
        return


    def tcscan(self):
        self.tcSig.emit("tcscanRuning",dict())
        try:
            for t in self.s.plugins.truecryptmaster().collect():
                if self.isInterruptionRequested():
                    return

                d = {}
                d["Volume"] = unicode(t[0])
                d["ea"] =  str(t[1])
                d["mode"] = str(t[2])
                d["keyfile"] = t[3]
                self.tcSig.emit("tcscanRuning",d)
        except:
            self.driverscanSig.emit("tcscanEnd",dict())
            return

        self.driverscanSig.emit("tcscanEnd",dict())
        return

    def sockets(self):
        self.socketsSig.emit("socketsRuning",dict())
        version = self.s.profile.metadata("version")
        if version == 5.1: #winxp
            try:
                for row in self.s.plugins.sockets().collect():
                    if self.isInterruptionRequested():
                        return
                    d = {}
                    d["pid"] = int(row["pid"])
                    d["address"] = str(row["address"])
                    d["port"] = int(row["port"])
                    d["proto"] = row["proto"]
                    d["protocol"] = str(row["protocol"])
                    d["create_time"] = str(row["create_time"])

                    self.socketsSig.emit("socketsRuning",d)
            except:
                self.socketsSig.emit("socketsEnd",dict())
                return

        self.socketsSig.emit("socketsEnd",dict())
        return

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

    def dlllist(self):
        self.dlllistSig.emit("dlllistRuning",dict())
        try:
            for task in self.s.plugins.dlllist().collect():
                if task.Peb:
                    d = {}
                    d["UniqueProcessId"] = int(task.UniqueProcessId)
                    d["CommandLine"] = str(task.Peb.ProcessParameters.CommandLine)
                    d["dlls"] = []
                    for m in  task.get_load_modules():
                        d["dlls"].append(unicode(m.FullDllName))

                    self.dlllistSig.emit("dlllistRuning",d)
        except:
            self.dlllistSig.emit("dlllistEnd",dict())
            return

        self.dlllistSig.emit("dlllistEnd",dict())
        return

    def netscan(self):
        self.netscanSig.emit("netscanRuning",dict())
        version = self.s.profile.metadata("version")
        
        try:
            if version == 5.1: #winxp
                for t in self.s.plugins.connscan().collect():
                    d = {}
                    d["local"] = t[1]
                    d["remote"] = t[2]
                    d["pid"] = int(t[3])
                    self.netscanSig.emit("netscanRuning",d)
            else:
                for t in self.s.plugins.netscan().collect():
                    d = {}
                    d["local"] = t[2]
                    d["remote"] = t[3]
                    d["pid"] = int(t[5])
                    self.netscanSig.emit("netscanRuning",d)
        except:
            self.netscanSig.emit("netscanEnd",dict())
            return

        self.netscanSig.emit("netscanEnd",dict())
        return


    





