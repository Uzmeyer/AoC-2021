from re import match
from struct import pack

import numpy as np

infile = open('D9_input_example.txt')

lines = infile.readlines()
ymax = len(lines) - 1
xmax = len(lines[0].rstrip()) - 1
hightmap = np.zeros((xmax + 1,ymax + 1), int)
def checkSurroundings(point):
    x, y = point
    pointhight = hightmap[x][y]
    lowpoint = False
    match point:
        case (0, 0): ##Origin
            if hightmap[x][y+1] > pointhight and hightmap[x+1][y] > pointhight:
                lowpoint = True

        case (0, ymax): ##bottom left corner
            if hightmap[x][y-1] > pointhight and hightmap[x][y+1] > pointhight:
                lowpoint = True

        case (xmax, 0): ##top right corner
            if hightmap[x-1][y] > pointhight and hightmap[x][y+1] > pointhight:
                lowpoint = True

        case (xmax, ymax): ##bottom right corner
            if hightmap[x][y-1] > pointhight and hightmap[x-1][y] > pointhight:
                lowpoint = True

        case (0, y): ##Left edge
            if hightmap[x][y-1] > pointhight and hightmap[x][y+1] > pointhight and hightmap[x+1][y] > pointhight:
                lowpoint = True

        case (x, 0): ##top edge
            if hightmap[x-1][y] > pointhight and hightmap[x+1][y] > pointhight and hightmap[x][y+1] > pointhight:
                lowpoint = True

        case (xmax, y): ##right edge
            if hightmap[x][y-1] > pointhight and hightmap[x][y+1] > pointhight and hightmap[x+1][y] > pointhight:
                lowpoint = True

        case (x, ymax): ##bottom edge
            if hightmap[x-1][y] > pointhight and hightmap[x+1][y] > pointhight and hightmap[x][y+1] > pointhight:
                lowpoint = True

        case _: ##everything else
            if hightmap[x-1][y] > pointhight and hightmap[x+1][y] > pointhight and hightmap[x][y+1] > pointhight and hightmap[x][y-1] > pointhight:
                lowpoint = True

    return lowpoint



for i in range(xmax + 1):
    for j in range(ymax + 1):
        hightmap[i][j] = int(lines[j][i])

lowpoints = []
for i in range(xmax + 1):
    for j in range(ymax + 1):
        if checkSurroundings((i, j)):
            lowpoints.append(((i, j), hightmap[i][j]))

print('Welp')