from Board import Board
from DrawableBoard import DrawableBoard
from Player import Player
import time
# board = DrawableBoard(Player(), bridgeCount=60, yInterval=20, yIndex=30)
# # board = Board(Player(), bridgeCount=2000, yInterval=1, yIndex=700)
# board.start()
# time.sleep(5)

yInd = 300
bridgeC = 600
repeat = 1000
xInd = 8
print(f"다리 개수 {bridgeC}, 라인 개수 {xInd}, y축 길이 {yInd-1}, 시작 위치당 반복횟수 {repeat}")
for j in range(xInd):
    aveMove = 0
    aveYLen = 0
    arriveCord = [0 for i in range(xInd)]
    for i in range(repeat):
        board = Board(Player(), bridgeCount=bridgeC,
                      yInterval=100, yIndex=yInd, lineCount=xInd)
        board.setPlayer(Player(j))
        # if i % 100 == 0:
        #     print(i)
        t = board.start()
        aveMove += t[0]
        aveYLen += t[1]
        arriveCord[t[2]] += 1

    print(f"{j}에서 {arriveCord}, 평균 이동은 {aveMove / repeat}회, 평균 y축 이동량은 {aveYLen / repeat}칸")
