from Player import Player
from Painter import Painter
from Board import Board


class DrawableBoard(Board):

    def __init__(self, player: Player, lineCount: int = 8, bridgeCount: int = 20, yIndex: int = 8, xInterval: int = 100, yInterval: int = 100, edgeSpace: int = 50, blankSpace: int = 50, displayMode: bool = True):
        """self, player: Player, lineCount: int = 8, bridgeCount: int = 20, yIndex: int = 8, xInterval: int = 100, yInterval: int = 100, edgeSpace: int = 50, blankSpace: int = 50, displayMode: bool = True"""
        super().__init__(player, lineCount, bridgeCount, yIndex,
                         xInterval, yInterval, edgeSpace, blankSpace, displayMode)
        self.__p = Painter() if self.displayMode else None
        if self.displayMode:
            self.displaySadari()

    def displaySadari(self):
        self.__p.start(self)

    def getPainter(self):
        return self.__p
