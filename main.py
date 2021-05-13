from Board import Board
from DrawableBoard import DrawableBoard
from Player import Player
import matplotlib.pyplot as plt
import time
import numpy
# board = DrawableBoard(Player(), bridgeCount=60, yInterval=20, yIndex=30)
# # board = Board(Player(), bridgeCount=2000, yInterval=1, yIndex=700)
# board.start()
# time.sleep(5)
req = [
    [3, 7*8],
    [4, 20*8],
    [5, 43*8],
    [6, 79*8],
    [7, 130*8]
]

# for ii in req:
#     for jj in [ii[1]//2, ii[1], ii[1]*2]:
#         yInd = 300
#         bridgeC = jj
#         repeat = 10000
#         xInd = ii[0]
#         print(
#             f"다리 개수 {bridgeC}, 라인 개수 {xInd}, y축 길이 {yInd-1}, 시작 위치당 반복횟수 {repeat}")
#         for j in range(xInd):
#             aveMove = 0
#             aveYLen = 0
#             arriveCord = [0 for i in range(xInd)]
#             for i in range(repeat):
#                 board = Board(Player(), bridgeCount=bridgeC,
#                               yInterval=100, yIndex=yInd, lineCount=xInd)
#                 board.setPlayer(Player(j))
#                 # if i % 100 == 0:
#                 #     print(i)
#                 t = board.start()
#                 aveMove += t[0]
#                 aveYLen += t[1]
#                 arriveCord[t[2]] += 1
#             plt.subplot(2, xInd//2+xInd % 2, j+1)
#             plt.title(f"starts at {j + 1}")
#             plt.bar([i for i in range(xInd)], arriveCord)
#             print(
#                 f"{j}에서 {arriveCord}, 평균 이동은 {aveMove / repeat}회, 평균 y축 이동량은 {aveYLen / repeat}칸")
#         plt.savefig(f"fig{xInd}-{bridgeC}")
#         plt.close()
for ii in req:
    for jj in [ii[1]//2, ii[1], ii[1]*2]:
        yInd = 300
        bridgeC = jj
        repeat = 1000
        xInd = ii[0]
        stdv = [0 for i in range(xInd)]
        print(
            f"다리 개수 {bridgeC}, 라인 개수 {xInd}, y축 길이 {yInd-1}, 시작 위치당 반복횟수 {repeat}")
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
            plt.subplot(2, xInd//2+xInd % 2, j+1)
            plt.title(f"starts at {j + 1}")
            plt.bar([i for i in range(xInd)], arriveCord)
            stdv[j] = numpy.std(arriveCord)
            print(
                f"{j}에서 {arriveCord}, 평균 이동은 {aveMove / repeat}회, 평균 y축 이동량은 {aveYLen / repeat}칸, 표준편차는 {stdv[j]}")
        plt.savefig(f"fig{xInd}-{bridgeC}")
        plt.close()
        print(f"편차평균은 {sum(stdv)/xInd}")
# 7 20 43 79 130
