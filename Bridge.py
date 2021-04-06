from typing import Tuple


class Bridge:
    def __init__(self, start: Tuple[int, int], connectedBridge=None):
        self.__cordi = start
        # self.__passCount = 0
        self.__upsidePassedCount = 0
        self.__downsidePassedCount = 0
        if connectedBridge:
            self.connectBridge(connectedBridge)

    def getUpsidePassedCount(self):
        return self.__upsidePassedCount

    def addUpsidePassedCount(self):
        self.__upsidePassedCount += 1

    def getDownsidePassedCount(self):
        return self.__downsidePassedCount

    def addDownsidePassedCount(self):
        self.__downsidePassedCount += 1

    def getCordi(self):
        """get cordinaion."""
        return self.__cordi

    def getConnectedBridge(self):
        """get connected bridge."""
        return self.__connectedBridge

    # def getPassCount(self):
    #     return self.__passCount

    def connectBridge(self, bridge):
        """connect self and bridge, if invalid connection, raise exception."""
        self.__connectedBridge: Bridge = bridge
        if abs(self.__cordi[0] - self.__connectedBridge.getCordi()[0]) != 1:
            raise Exception("invalid bridge connection")


class AssignedBridge:
    def __init__(self, bridge1: Bridge, bridge2: Bridge):
        self.__bridge1 = bridge1
        self.__bridge2 = bridge2

    def getBridges(self):
        return (self.__bridge1, self.__bridge2)

    def getBridge1(self):
        return self.__bridge1

    def getBridge2(self):
        return self.__bridge2
