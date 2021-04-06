from typing import List
import random as r

from Player import Player
from Bridge import Bridge, AssignedBridge


class Board:
    def __init__(self, player: Player, lineCount: int = 8, bridgeCount: int = 20, yIndex: int = 8, xInterval: int = 100, yInterval: int = 100, edgeSpace: int = 50, blankSpace: int = 50, displayMode: bool = True):
        self.__player = player
        self.__lineCount = lineCount
        # grid[x][y]
        self.__grid = [[None for _ in range(yIndex)] for _ in range(lineCount)]
        # default = max of bridge count, 0 if that line is full
        self.__isLineNotFull = [yIndex for _ in range(lineCount)]
        # list of bridges
        self.__assignedBridges: List[AssignedBridge] = []
        self.__yIndex = yIndex
        self.__xInterval = xInterval
        self.__yInterval = yInterval
        self.__edgeSpace = edgeSpace
        self.displayMode = displayMode
        self.__blankSpace = blankSpace

        # player initialize
        # self.__player.assignBoard(self)
        # bridge initialize
        for i in range(bridgeCount):
            self.makeRandomBridge()

        #self.t = turtle.Turtle() if displayMode else None
        # self.__p = Painter() if displayMode else None
        # if displayMode:
        #     self.displaySadari()

    def getLineCount(self):
        return self.__lineCount

    def getAssignedBridges(self):
        return self.__assignedBridges

    def getYIndex(self):
        return self.__yIndex

    def getXInterval(self):
        return self.__xInterval

    def getYInterval(self):
        return self.__yInterval

    def getEdgeSpace(self):
        return self.__edgeSpace

    def getBlankSpace(self):
        return self.__edgeSpace

    def isDisplayMode(self):
        return self.displayMode

    def setPlayer(self, p: Player):
        self.__player = p

    def makeRandomBridge(self):
        # if not possible to assign bridge, throws exception.
        isPossible = self.__lineCount - 1
        for i in range(self.__lineCount-1):
            if not self.__isLineNotFull[i] or not self.__isLineNotFull[i+1]:
                isPossible -= 1

        if not isPossible:
            raise Exception(
                "not enough space to assign bridge during processing")

        # assign bridge
        x1 = r.randrange(0, self.__lineCount-1)
        y1 = r.randrange(0, self.__yIndex)
        while not self.__isLineNotFull[x1] or not self.__isLineNotFull[x1+1]:
            x1 = r.randrange(0, self.__lineCount-1)
        while self.__grid[x1][y1]:
            y1 = r.randrange(0, self.__yIndex)

        x2 = x1 + 1
        y2 = r.randrange(0, self.__yIndex)
        while self.__grid[x2][y2]:
            # print(self.__grid[x2])
            y2 = r.randrange(0, self.__yIndex)

        bridge1: Bridge = Bridge((x1, y1))
        bridge2: Bridge = Bridge((x2, y2), bridge1)
        bridge1.connectBridge(bridge2)
        self.assignBridge(bridge1, bridge2)

    def assignBridge(self, bridge1: Bridge, bridge2: Bridge):
        """assigns bridges. if it's invalid, raise exception."""
        if bridge1 != bridge2.getConnectedBridge() or bridge2 != bridge1.getConnectedBridge():
            raise Exception("invalid assign")

        for i in (bridge1, bridge2):
            self.__grid[i.getCordi()[0]][i.getCordi()[1]] = i
            self.__isLineNotFull[i.getCordi()[0]] -= 1

        self.__assignedBridges.append(AssignedBridge(bridge1, bridge2))

    def playerMove(self):
        #! I have to modify this method. because this method is too long, and compiling statistics is not this method's task. so it should be separated.
        x, y = self.__player.getCordi()

        if self.__grid[x][y] != None and not self.__player.hasJustPassedBridge():
            # crossing bridge
            current: Bridge = self.__grid[x][y]
            current.addUpsidePassedCount()
            self.__player.appendToHistory([x, y])
            self.__player.addMoveCount()
            self.__player.setJustPassedBridge(True)
            self.__player.setCordi(current.getConnectedBridge().getCordi()[:])

        else:
            # crossing line
            if self.__grid[x][y] != None:
                # crossed bridge (not run at first start)
                current: Bridge = self.__grid[x][y]
                current.addDownsidePassedCount()
                self.__player.appendToHistory([x, y])
                self.__player.addMoveCount()

            while True:
                # go down
                y += 1

                if self.__yIndex <= y:
                    # end of line
                    self.__player.appendToHistory([x, y-1])
                    self.__player.addMoveCount()
                    return False

                self.__player.addMovedYLength()

                if self.__grid[x][y] == None:
                    continue
                break

            # arrive bridge
            self.__player.setJustPassedBridge(False)
            current: Bridge = self.__grid[x][y]
            self.__player.setCordi(current.getCordi()[:])

        return True

    def processed(self):
        # print(self.__player.getCordi())
        pass

    def start(self):
        self.processed()
        while self.playerMove():
            self.processed()
        self.processed()

        return [self.__player.getMoveCount(), self.__player.getMovedYLength(), self.__player.getHistory()[-1][0]]
        # print(f"{self.__player.getMoveCount()} {self.__player.getMovedYLength()}")
        # def displaySadari(self):
        #     self.__p.start()
