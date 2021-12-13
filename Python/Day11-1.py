


class DumboOctopus:

    def __init__(self,  x, y, _xmax, _ymax, octopi=None, initialenergy=0):
        self.energy = initialenergy
        self.flashcount = 0
        self.flashed = False
        self.x = x
        self.y = y
        self.xmax = _xmax
        self.ymax = _ymax
        self.octopi = octopi
        self.adjacentoctopi = self.getadjacent()

    def step(self):
        self.energy = self.energy + 1
        if self.energy > 9:
            self.flash()

    def flash(self):
        if not self.flashed:
            self.flashcount = self.flashcount + 1
            self.flashed = True
            for neighbour in self.adjacentoctopi:
                self.octopi[neighbour[0]][neighbour[1]].getflashedat()

    def flush(self):
        if self.flashed:
            self.flashed = False
            self.energy = 0

    def getflashedat(self):
        self.energy = self.energy + 1
        if not self.flashed and self.energy > 9:
            self.flash()

    def adjacentexists(self, x, y):
        if x == self.x and y == self.y:
            return False
        elif x < 0 or y < 0 or x > self.xmax or y > self.xmax:
            return False
        else:
            return True

    def getadjacent(self):
        adjacent = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.adjacentexists(self.x+i, self.y+j):
                    adjacent.append((self.x+i, self.y+j))

        return adjacent



infile = open('D11_input.txt')
lines = infile.readlines()
ymax = len(lines) - 1
xmax = len(lines[0].rstrip()) - 1
globaloctopi = []
for i in range(xmax+1):
    yoctopi = []
    for j in range(ymax+1):
        octopus = DumboOctopus(i, j, xmax, ymax, globaloctopi, int(lines[j][i]))
        yoctopi.append(octopus)
    globaloctopi.append(yoctopi)

for i in range(100):
    for x in range(xmax+1):
        for y in range(ymax+1):
            globaloctopi[x][y].step()

    for x in range(xmax + 1):
        for y in range(ymax + 1):
            globaloctopi[x][y].flush()

flashcount = 0
for x in range(xmax + 1):
    for y in range(ymax + 1):
       flashcount = globaloctopi[x][y].flashcount + flashcount

print("Part 1 flashcount is " + str(flashcount))

globaloctopi = []
for i in range(xmax+1):
    yoctopi = []
    for j in range(ymax+1):
        octopus = DumboOctopus(i, j, xmax, ymax, globaloctopi, int(lines[j][i]))
        yoctopi.append(octopus)
    globaloctopi.append(yoctopi)

steps = 0
simulflash = False
while not simulflash:
    steps = steps + 1
    for x in range(xmax+1):
        for y in range(ymax+1):
            globaloctopi[x][y].step()

    flashcount = 0
    for x in range(xmax + 1):
        for y in range(ymax + 1):
            if globaloctopi[x][y].flashed:
                flashcount = flashcount + 1

    if flashcount == 100:
        simulflash = True

    for x in range(xmax + 1):
        for y in range(ymax + 1):
            globaloctopi[x][y].flush()


print("Synchorized at step " + str(steps))

print("Welp")
