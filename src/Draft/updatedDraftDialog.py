import os
import statedb
import sys
import Models.QDeck
import cardCrawler
import settingsManager
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from UI_draftUI import Ui_DraftDialog
from QLoadingDialog import QLoadingDialog
from Draft import DraftModel
from expansionPicker import ExpansionPicker
from util import utilities

class CardDownloader(QThread):
    def __init__(self, client, parent=None):
        QThread.__init__(self,parent)
        self.client = client
    def run(self):
        cardList = self.client.getAllCards()
        for i,card in enumerate(cardList):
            if card == "land" or card == "wait":
                continue
            if not os.path.isfile(os.path.join(settingsManager.settings['cardsDir'],card[0],"%s.jpg"%(card[1]))):
                cardCrawler.crawlCardAndInfo(card[0],card[1],addToDB=False,silent=True)
            self.emit(SIGNAL("progress(int)"),int(100.0*(i+1)/len(cardList)))
        self.emit(SIGNAL("doneDownloading()"))

class MockCardDownloader(QThread):
    def __init__(self, seconds):
        QThread.__init__(self, None)
        self.seconds = seconds
    def run(self):
        import time
        for i in range(self.seconds):
            time.sleep(1)
            self.emit(SIGNAL("progress(int)"), int(100.0 / self.seconds * (i+1) ))
            print "Tick: %s" % int(100.0 / self.seconds * (i+1) )
        self.emit(SIGNAL("doneDownloading()"))
        print "Done 'Downloading'"

class DraftDialog(QDialog, Ui_DraftDialog):
    def __init__(self, client, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.lblWaiting.hide()

        self.client = client
        self.deletesListener = False

        self.connect(self.btnAdd, SIGNAL('clicked()'), self.addCard)
        self.connect(self.btnRemove, SIGNAL('clicked()'), self.removeCard)
        self.connect(self.btnPass, SIGNAL('clicked()'), self.passPack)
        self.connect(self.debugButton, SIGNAL('clicked()'), utilities.set_trace)

        self.availableModel = DraftModel.DDraftModel(self)
        self.lvCards.setModel(self.availableModel)

        self.deckModel = DraftModel.DDraftModel(self)
        self.lvDeck.setModel(self.deckModel)

        self.readyForNextPack = False
        self.pickingLand = False
        self.packsWaiting = []
        self.cardThatWasPicked = None
        self.lblSender.setText("You opened:")

        self.loadDialog = QLoadingDialog()
        self.loadDialog.setLabel("Waiting for players")
        self.loadDialog.setProgress(.5)
        self.loadDialog.show()

        self.checkForReadyTimer = QTimer()
        self.checkForReadyTimer.setInterval(250)
        self.checkForPackTimer = QTimer()
        self.checkForPackTimer.setInterval(250)
        self.connect(self.checkForPackTimer, SIGNAL("timeout()"), self.checkForPack)
        self.connect(self.checkForReadyTimer, SIGNAL("timeout()"), self.checkForReady)
        self.client.signalReady()
        self.checkForReadyTimer.start()

    def doneLoading(self):
        self.availableModel.endResetModel()
        self.loadDialog.accept()

    def displayLoadingDialog(self, testing=False):
        if not testing:
            self.downloadThread = CardDownloader(self.client, self)
        else:
            self.downloadThread = MockCardDownloader(10)
        self.availableModel.beginResetModel()
        self.connect(self.downloadThread,SIGNAL("doneDownloading()"),self.doneLoading)
        self.connect(self.downloadThread,SIGNAL("progress(int)"),self.loadDialog.progressBar.setValue)
        self.downloadThread.start()
        self.loadDialog.setLabel("Downloading cards...")

    def checkForReady(self):
        if self.client.everyoneReady():
            self.checkForReadyTimer.stop()
            self.displayLoadingDialog()
            print "Ready!"
            self.checkForPackTimer.start()

    def checkForPack(self):
        print "Checking for pack..."
        pack = self.client.getCurrentPack()
        if pack == ['wait']:
            return

        if pack == ['land']:
            print "Need land"
            self.checkForPackTimer.stop()
            self.availableModel.list = Models.QDeck.basicLand
            self.availableModel.reset()
            self.pickingLand = True
            self.btnPass.setText("Done")
        else:
            self.checkForPackTimer.stop()
            self.availableModel.list = pack
            self.availableModel.reset()
        self.btnAdd.setEnabled(True)
        self.btnRemove.setEnabled(False)
        self.btnPass.setEnabled(True)
        self.lblWaiting.hide()
        self.lvCards.show()

    def setExpansions(self, expansions):
        self.expansions = expansions
        self.expansions.append('land')
        self.nextExpansion()

    def nextExpansion(self):
        self.readyForNextPack = False
        if not self.expansions[0] == "land":
            self.availableModel.list = Models.QDeck.QDeck(None,True).makeBoosterFromAbbreviation(self.expansions[0], False)
            self.availableModel.reset()
            del self.expansions[0]
            self.lblRemaining.setText("Remaining Packs: %s" % (' '.join(self.expansions)))
        else:
            self.availableModel.list = Models.QDeck.basicLand
            self.availableModel.reset()
            self.pickingLand = True
            self.btnPass.setText("Done")

    def addCard(self):
        if not self.pickingLand:
            self.btnAdd.setEnabled(False)
            self.btnRemove.setEnabled(True)
        if self.cardThatWasPicked is not None and not self.pickingLand:
            return
        for index in self.lvCards.selectedIndexes():
            item = self.availableModel.list[index.row()]
            self.deckModel.addItem(item)
            if not self.pickingLand:
                self.availableModel.removeItem(item)
            self.cardThatWasPicked = item

    def removeCard(self):
        if not self.pickingLand:
            self.btnAdd.setEnabled(True)
            self.btnRemove.setEnabled(False)
        if self.cardThatWasPicked is None and not self.pickingLand:
            return
        for index in self.lvDeck.selectedIndexes():
            item = self.deckModel.list[index.row()]
            if item is not self.cardThatWasPicked:
                return
            self.deckModel.removeItem(item)
            if not self.pickingLand:
                self.availableModel.addItem(item)
            self.cardThatWasPicked = None

    def passPack(self):
        if self.pickingLand:
            print "Done drafting"
            db = statedb.Database()
            filename = "Draft"
            with open(os.path.join('src','userdata','decks',filename), 'w') as f:
                for card in self.deckModel.list:
                    f.write(db.nameForAbbreviationIndex(card[0], card[1]) + "\n")
            QMessageBox.information(self.parent(), "Draft Done!", "Now you must run PTG and select the 'Draft' deck.", buttons=QMessageBox.Ok, defaultButton=QMessageBox.Ok)
            self.accept()
            return

        if self.cardThatWasPicked is None:
            return

        if len(self.availableModel.list) == 1:
            # On the last card of this expansion
            self.btnPass.setText("Open Next Pack")
        if len(self.availableModel.list) == 0:
            self.btnPass.setText("Pass Pack")
        self.client.pickCard(self.cardThatWasPicked)
        self.lblWaiting.show()
        self.lvCards.hide()
        self.cardThatWasPicked = None
        self.checkForPackTimer.start()
        self.btnPass.setEnabled(False)

    def setExpansionFromString(self, expansion):
        # Format is: ["abbreviation,index","abbreviation,index",...]
        if expansion == ["wait"]:
            self.lblWaiting.show()
            self.lvCards.hide()
        else:
            self.lblWaiting.hide()
            self.lvCards.show()
        result = []
        for card in expansion:
            parts = card.split(',')
            if len(parts) < 2:
                continue
            result.append((parts[0],parts[1]))
        self.availableModel.list = result
        self.availableModel.reset()

    def stringForExpansion(self):
        return ':'.join(["%s,%s" % (abbreviation,index) for abbreviation,index in self.availableModel.list])

    def closeEvent(self, event):
        if QMessageBox.question(self, "Do you wish to exit?", "If you exit now, your deck will not be saved.", buttons=QMessageBox.Yes | QMessageBox.Cancel, defaultButton=QMessageBox.Cancel) == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def gameWasCanceled(self):
        pass # To eliminate a crash report sent from Will

if __name__ == '__main__':
    app = QApplication([])
    class MockClient:
        def __init__(self):
            self.counter = 0
        def signalReady(self):
            pass
        def getCurrentPack(self):
            return ['wait']
        def getAllCards(self):
            return [('m13','1'),('m13','2'),('m13','3'),('m13','4'),('m13','5'),('m13','6'),('m13','7'),('m13','8'),('m13','9'),('m13','10')]
        def everyoneReady(self):
            self.counter += 1
            if self.counter > 40:
                return True
            return False
    dialog = DraftDialog(MockClient())
    dialog.displayLoadingDialog(testing=False)
    app.exec_()
