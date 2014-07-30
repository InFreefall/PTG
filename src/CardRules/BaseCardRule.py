# Turn has 5 phases:
# - Beginning
#   * Untap
#   * Upkeep
#   * Draw
# - Precombat Main
# - Combat
#   * Beginning of Combat
#   * Declare Attackers
#   * Declare Blockers
#   * Combat Damage
#   * End of Combat
# - Postcombat main
# - Ending
#   * End Step
#   * Cleanup

class BaseCardRule(object):
    def __init__(self):
       self.regenerated = False
       self.types = []
       import inspect; print inspect.getfile(inspect.currentframe())

    def onBeginningPhase(self):
        pass

    def onUntapStep(self):
        pass

    def onUpkeepStep(self):
        pass

    def onDrawStep(self):
        pass

    def onPrecombatMainPhase(self):
        pass

    def onCombatPhase(self):
        pass

    def onBeginningOfCombatStep(self):
        pass

    def onDeclareAttackersStep(self):
        pass

    def onDeclareBlockersStep(self):
        pass

    def onCombatDamageStep(self):
        pass

    def onEndOfCombatStep(self):
        pass

    def onPostcombatMainPhase(self):
        pass

    def onEndingPhase(self):
        pass

    def onEndStep(self):
        self.regenerated = False

    def onCleanupStep(self):
        pass

