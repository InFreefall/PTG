import os
import subprocess

class FileServer:
    def __init__(self, port):
        self.port = port
        self._started = False

    # Elegant, right?
    def start(self):
        subprocess.Popen(["python", "-m", "SimpleHTTPServer", str(self.port)],
                         cwd=os.path.join('..','..','dist','PTG'))
        self.started = True

    def started(self):
        return self._started
