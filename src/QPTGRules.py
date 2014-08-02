import QPTG

class GameDialogRulesEnforced(QPTG.GameDialog):
    def __init__(self, gameID, parent=None):
        QPTG.GameDialog.__init__(self, gameID, parent)
        self.rulesManager = None
