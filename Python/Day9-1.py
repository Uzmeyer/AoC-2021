from re import match
from struct import pack

import numpy as np

infile = open('D9_input_example.txt')

lines = infile.readlines()
ymax = len(lines) - 1
xmax = len(lines[0].rstrip()) - 1
hightmap = np.zeros((xmax + 1, ymax + 1), int)


def checkSurroundings(point, _xmax, _ymax):
    x, y = point
    pointhight = hightmap[x][y]
    lowpoint = False
    if x == 0:
        if y == 0: #origin
            if hightmap[x][y+1] > pointhight and hightmap[x+1][y] > pointhight:
                lowpoint = True
        elif y == _ymax: #bottom left corner
            if hightmap[x][y-1] > pointhight and hightmap[x][y+1] > pointhight:
                lowpoint = True
        else: # left edge
            if hightmap[x][y-1] > pointhight and hightmap[x][y+1] > pointhight and hightmap[x+1][y] > pointhight:
                lowpoint = True

    elif x == _xmax:
        if y == 0: #top right corner
            if hightmap[x-1][y] > pointhight and hightmap[x][y+1] > pointhight:
                lowpoint = True
        elif y == _ymax: #bottom right corner
            if hightmap[x][y-1] > pointhight and hightmap[x-1][y] > pointhight:
                lowpoint = True
        else: #right edge
            if hightmap[x][y-1] > pointhight and hightmap[x][y+1] > pointhight and hightmap[x-1][y] > pointhight:
                lowpoint = True

    else:
        if y == 0: #top edge
            if hightmap[x-1][y] > pointhight and hightmap[x+1][y] > pointhight and hightmap[x][y+1] > pointhight:
                lowpoint = True
        elif y == _ymax: #bottom edge
            if hightmap[x-1][y] > pointhight and hightmap[x+1][y] > pointhight and hightmap[x][y-1] > pointhight:
                lowpoint = True
        else: #everything else
            if hightmap[x-1][y] > pointhight and hightmap[x+1][y] > pointhight and hightmap[x][y+1] > pointhight and hightmap[x][y-1] > pointhight:
                lowpoint = True

    return lowpoint



for i in range(xmax + 1):
    for j in range(ymax + 1):
        hightmap[i][j] = int(lines[j][i])

lowpoints = []
for x in range(xmax + 1):
    for y in range(ymax + 1):
        if checkSurroundings((x, y), xmax, ymax):
            lowpoints.append(((x, y), hightmap[x][y]))

danger = 0
for lowpoint in lowpoints:
    danger = danger + lowpoint[1] + 1

print('Danger: ' + str(danger))
print('Welp')