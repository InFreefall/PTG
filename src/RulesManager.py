import Constants as c

class RulesManager:
    def __init__(self, client):
        self.client = client
        self.client.addMapping(c.EventPhaseChanged, self.eventPhaseChanged)
        self.client.addMapping(c.EventStepChanged, self.eventStepChanged)
        self.currentPhase = c.PhaseBeginning
        self.currentStep = c.StepUntap

    def eventPhaseChanged(self, event):
        pass

    def eventStepChanged(self, event):
        pass
