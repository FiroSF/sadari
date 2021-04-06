import tkinter

from Board import Board
from Bridge import AssignedBridge


class Painter(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Sadari  S I M U L A T O R - by 30226")
        self.geometry("1600x900+100+100")
        self.__canvas = tkinter.Canvas(self, width="1280",
                                       height="720", relief="solid", bd=2)
        self.__board: Board = None

    def drawLine(self, i: int):
        x1 = self.__board.getEdgeSpace() + i * self.__board.getXInterval()
        y1 = self.__board.getEdgeSpace()
        x2 = self.__board.getEdgeSpace() + i * self.__board.getXInterval()
        y2 = self.__height - self.__board.getEdgeSpace()
        self.__canvas.create_line(x1, y1, x2, y2)

    def drawBridge(self, bridge: AssignedBridge):
        cordi = [*bridge.getBridge1().getCordi(),
                 *bridge.getBridge2().getCordi()]

        # modify interval
        for i in range(len(cordi)):
            if i % 2 == 1:
                cordi[i] *= self.__board.getYInterval()
                cordi[i] += (self.__board.getBlankSpace() +
                             self.__board.getEdgeSpace())
                #y is opposite
                #cordi[i] = self.__height - cordi[i]

            else:
                cordi[i] *= self.__board.getXInterval()
                cordi[i] += self.__board.getBlankSpace()

        self.__canvas.create_line(*cordi)

    def start(self, board: Board):
        self.__board: Board = board
        self.__height = (self.__board.getEdgeSpace() * 2 + self.__board.getYInterval()
                         * (self.__board.getYIndex() - 1) + self.__board.getBlankSpace() * 2)
        for i in range(board.getLineCount()):
            self.drawLine(i)
        for i in board.getAssignedBridges():
            self.drawBridge(i)

        self.__canvas.pack(fill="both", expand=True)
        self.update()

    # def process(self):

    # def move(self):
