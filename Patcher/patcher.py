import hashlib
import os
import requests
import sys
import subprocess
from time import sleep
import win32com.shell.shell as shell
ASADMIN = 'asadmin'

from PyQt4.QtCore import QObject, QUrl, pyqtSignal, QThread
from PyQt4.QtGui import QApplication
from PyQt4.QtDeclarative import QDeclarativeView

SERVER = "http://ptg.duckdns.org:42140"

class DownloaderThread(QThread):
    def hashfile(self, afile, hasher, blocksize=65536):
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
        return hasher.hexdigest()
        
    def run(self):
        jsonFile = requests.get(SERVER + "/files.json")
        for f in jsonFile.json():
            if os.path.isfile(f['filename']):
                with open(f['filename']) as localFile:
                    if self.hashfile(localFile, hashlib.sha256()) == f['hash']:
                        print "Skipping " + f['filename']
                        continue
                    else:
                        print "Hashes differ. Local is {}, remote is {}.".format(
                            self.hashfile(localFile, hashlib.sha256()),
                            f['hash'])
            if sys.argv[-1] != ASADMIN:
                script = os.path.abspath(sys.argv[0])
                params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
                shell.ShellExecuteEx(lpVerb='runas',
                                     lpFile=sys.executable,
                                     lpParameters=params)
                sys.exit(0)
            print "Downloading " + f['filename']
            r = requests.get(SERVER + "/" + f['filename'])
            directory = os.path.dirname(f['filename'])
            if directory != '' and not os.path.exists(directory):
                os.makedirs(directory)
            with open(f['filename'], 'wb') as localFile:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        localFile.write(chunk)
                        localFile.flush()

if True:#os.path.isfile("gamelobby.exe"):
    app = QApplication(sys.argv)

    view = QDeclarativeView()
    view.setSource(QUrl('patcher.qml'))
    view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
    view.setFixedSize(640, 480)
    view.setWindowTitle("PTG Patcher")

    view.show()

    thread = DownloaderThread()
    thread.finished.connect(app.exit)
    thread.start()

    app.exec_()

print "Opening PTG..."
subprocess.Popen("gamelobby.exe")
