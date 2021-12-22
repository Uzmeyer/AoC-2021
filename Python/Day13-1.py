import numpy as np

infile = open("D13_input.txt", 'r')
lines = infile.readlines()
dotlocations = []
foldinstructions = []
dotsdone = False
xmax = 0
ymax = 0

def printpaper(paper, _xmax, _ymax):
    for y in range(_ymax):
        for x in range(_xmax):
            if paper[x][y] == 1:
                print('#', end="")
            else:
                print('.', end="")
        print("")
    print('\n\n')


def fold(paper, direction, location, _xmax, _ymax):
    if direction == 'x':
        insertposition = location - 1
        for x in range(location + 1, _xmax):
            for y in range(ymax):
                if paper[x][y]:
                    paper[insertposition][y] = paper[x][y]
                    paper[x][y] = 0
            insertposition = insertposition - 1
        _xmax = location
        #np.reshape(paper, (_xmax, _ymax))
    elif direction == 'y':
        insertposition = location - 1
        for y in range(location + 1, _ymax):
            for x in range(xmax):
                if paper[x][y]:
                    paper[x][insertposition] = paper[x][y]
                    paper[x][y] = 0
            insertposition = insertposition - 1
        _ymax = location
        #np.reshape(paper, (_xmax, _ymax))
    return _xmax, _ymax


for line in lines:
    if line == '\n':
        dotsdone = True
        continue
    if not dotsdone:
        dotlocation = line.rstrip().split(',')
        x, y = int(dotlocation[0]), int(dotlocation[1])
        if x + 1 > xmax:
            xmax = x + 1
        if y + 1> ymax:
            ymax = y + 1
        dotlocations.append((x, y))
    else:
        foldinstruction = line.rstrip().lstrip('fold along ').split('=')
        foldinstructions.append((foldinstruction[0], int(foldinstruction[1])))

paper = np.zeros((xmax, ymax))
for dotlocation in dotlocations:
    paper[dotlocation[0]][dotlocation[1]] = 1

printpaper(paper, xmax, ymax)
#xmax, ymax = fold(paper, foldinstructions[0][0], foldinstructions[0][1], xmax, ymax)
#printpaper(paper, xmax, ymax)
#dotcount = np.sum(paper)
#print('Dots after first fold: ' + str(dotcount))
for instruction in foldinstructions:
    xmax, ymax = fold(paper, instruction[0], instruction[1], xmax, ymax)

printpaper(paper, xmax, ymax)

print('welp')