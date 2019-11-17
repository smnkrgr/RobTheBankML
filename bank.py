from counterboy import Counterboy
from guard import Guard
from lock import Lock


class Bank:

    def __init__(self, path):

        self.field = self.readField(path)
        self.agent_start_y, self.agent_start_x = self.setStartingPosition()
        self.agent_y = self.agent_start_y
        self.agent_x = self.agent_start_x

        self.guards = self.initializeGuards()
        self.counterboys = self.initialzeCounterboys()
        self.locks = self.initializeLocks()

        return

    def readField(self, path):

        return

    def setStartingPosition(self):

        return

    def initializeGuards(self):

        return

    def initialzeCounterboys(self):

        return

    def initializeLocks(self):

        return

    
