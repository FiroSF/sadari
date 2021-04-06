from typing import List


class Player:
    def __init__(self, start: int = 0):
        self.__moveCount = 0
        self.__justPassedBridge = False
        self.__cordi: List[int] = [start, 0]
        self.__history: List[List[int]] = [[start, 0]]
        self.__movedYLength = 0

    def addMoveCount(self):
        self.__moveCount += 1

    def getMoveCount(self):
        return self.__moveCount

    def hasJustPassedBridge(self):
        return self.__justPassedBridge

    def setJustPassedBridge(self, t: bool):
        self.__justPassedBridge = t

    def getHistory(self):
        return self.__history

    def appendToHistory(self, history: List[int]):
        self.__history.append(history)

    def getCordi(self):
        return self.__cordi

    def setCordi(self, cordi: List[int]):
        self.__cordi = cordi

    def getMovedYLength(self):
        return self.__movedYLength

    def addMovedYLength(self):
        self.__movedYLength += 1
