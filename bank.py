from counterboy import Counterboy
from guard import Guard
from lock import Lock


class Bank:

    starting_position_char = "O"
    money_position_char = "$"
    counterboy_char = "C"
    guard_char = "G"
    lock_char = "L"

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

        field = []
        file = open(path, "r")
        columns = file.readlines()

        for column in columns:
            column = column.strip()
            row = [i for i in column]
            field.append(row)
        return field
    
    def getPositionsOf(self, char):

        positions = []

        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if self.field[i][j] == char:
                    positions.append(i, j)

        return positions

    def setStartingPosition(self):

        positions = self.getPositionsOf(self.starting_position_char)
        if len(positions) == 0:
            print("No starting symbol in ascii level. Aborting...")
            exit()
        elif len(positions) > 1:
            print("Multiple starting positions in ascii level. Aborting...")
            exit()
        else:
            return positions[0]

    def initializeGuards(self):

        positions = self.getPositionsOf(self.guard_char)

        return

    def initialzeCounterboys(self):

        return

    def initializeLocks(self):

        return

    
