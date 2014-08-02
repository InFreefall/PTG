import smtplib
from email.mime.text import MIMEText
import sys
import traceback
import settingsManager

username = "Unknown"
sender = "ptgcrashsender@gmail.com"
addr = "ptgcrashreports@gmail.com"

lastCrashDescription = ""

def install_excepthook():
    def excepthook(exctype, value, tb):
        print "Sending crash report..."
        s = ''.join(traceback.format_exception(exctype, value, tb))
        msg = MIMEText(s)
        msg['Subject'] = "Crash report from %s" % (str(username))
        msg['From'] = str(username)
        msg['To'] = addr

        print msg.as_string()
        if not settingsManager.settings['reportCrashes']:
            return
        if msg.as_string() == lastCrashDescription:
            return
        lastCrashDescription = msg.as_string()

        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login(sender, "iplayptg")
        s.sendmail(sender, [addr], msg.as_string())
        s.quit()
    
    sys.excepthook = excepthook
