import numpy as np

infile = open("D5_input.txt", "r")
lines = []
for line in infile:
    lines.append(line.rstrip().replace(' ', ''))

class Faultline:
    xmax = 0
    ymax = 0
    xmin = 0
    ymin = 0

    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.xmax = 0
        self.xmin = 0
        self.ymax = 0
        self.ymin = 0
        self.isvertical = False
        self.ishorizontal = False
        self.isdiagonal = False
        self.points = []

    def parseLine(self, line):
        textpoints = line.split('->')
        x1, y1 = textpoints[0].split(',')
        x2, y2 = textpoints[1].split(',')
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.getOrientation()
        if self.x1 < self.x2:
            self.xmax = self.x2
            self.xmin = self.x1
        else:
            self.xmax = self.x1
            self.xmin = self.x2

        if self.y1 < self.y2:
            self.ymax = self.y2
            self.ymin = self.y1
        else:
            self.ymax = self.y1
            self.ymin = self.y2

        if self.x1 < Faultline.xmin:
            Faultline.xmin = self.x1
        if self.x1 > Faultline.xmax:
            Faultline.xmax = self.x1
        if self.x2 < Faultline.xmin:
            Faultline.xmin = self.x2
        if self.x2 > Faultline.xmax:
            Faultline.xmax = self.x2
        if self.y1 < Faultline.ymin:
            Faultline.ymin = self.y1
        if self.y1 > Faultline.ymax:
            Faultline.ymax = self.y1
        if self.y2 < Faultline.ymin:
            Faultline.ymin = self.y2
        if self.y2 > Faultline.ymax:
            Faultline.ymax = self.y2

    def getOrientation(self):
        if self.x1 == self.x2:
            self.isvertical = True
        elif self.y1 == self.y2:
            self.ishorizontal = True
        else:
            self.isdiagonal = True
            self.calculatePoints()

        return self.ishorizontal, self.isvertical, self.isdiagonal

    def calculatePoints(self):
        if self.isdiagonal:
            x = self.x1
            y = self.y1
            self.points.append((x, y))
            xinc = 1
            yinc = 1
            if self.x1 > self.x2:
                xinc = -1
            if self.y1 > self.y2:
                yinc = -1
            while x != self.x2:
                x = x + xinc
                y = y + yinc
                self.points.append((x, y))


faultlines = []
for line in lines:
    faultline = Faultline()
    faultline.parseLine(line)
    faultlines.append(faultline)

oceanfloormap = np.zeros((Faultline.xmax + 1, Faultline.ymax + 1), dtype=int)

for line in faultlines:
    if line.ishorizontal:
        i = line.xmin
        while i <= line.xmax:
            oceanfloormap[line.ymax][i] = oceanfloormap[line.ymax][i] + 1
            i = i+1

    if line.isvertical:
        i = line.ymin
        while i <= line.ymax:
            oceanfloormap[i][line.xmax] = oceanfloormap[i][line.xmax] + 1
            i = i+1

overlaps = 0
for i in range(Faultline.ymax + 1):
    for j in range(Faultline.xmax + 1):
        if oceanfloormap[i][j] >= 2:
            overlaps = overlaps + 1

print("Overlaping points: " + str(overlaps))
overlaps = 0
for line in faultlines:
    if line.isdiagonal:
        for point in line.points:
            x, y = point
            oceanfloormap[y][x] = oceanfloormap[y][x] + 1

for i in range(Faultline.ymax + 1):
    for j in range(Faultline.xmax + 1):
        if oceanfloormap[i][j] >= 2:
            overlaps = overlaps + 1

print("Overlaping points part 2: " + str(overlaps))
print("welp")