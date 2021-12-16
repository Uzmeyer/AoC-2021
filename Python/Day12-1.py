
infile = open("D12_input.txt", "r")
lines = infile.readlines()


class Cave:

    def __init__(self, name=''):
        self.name = name
        self.isdeadend = True
        if name.islower():
            self.issmall = True
        else:
            self.issmall = False
        if name == 'start':
            self.isstart = True
            self.isend = False
        elif name == 'end':
            self.isstart = False
            self.isend = True
        else:
            self.isstart = False
            self.isend = False
        self.visited = False
        self.connected = []

    def addconnected(self, newcave):
        if cave not in self.connected:
            self.connected.append(newcave)

        if len(self.connected) == 1 and self.connected[0].isupper() or len(self.connected) > 1:
            self.isdeadend = False


def getcave(name, cavelist):
    for cave in cavelist:
        if cave.name == name:
            return cave

    return None

def walkcave(currentcave, cavelist, counter=0):
    print(currentcave.name)
    currentcave.visited = True
    currcount = counter
    if currentcave.isend:
        currentcave.visited = False
        return currcount + 1
    for next in currentcave.connected:
        nextcave = getcave(next, cavelist)
        if nextcave.isstart:
            continue
        if nextcave.issmall and nextcave.isdeadend:
            continue
        if nextcave.issmall and nextcave.visited:
            continue
        currcount = walkcave(nextcave, cavelist, currcount)
        print(currentcave.name)

    currentcave.visited = False
    return currcount


caves = []
for line in lines:
    newcaves = line.rstrip().split("-")
    for newcave in newcaves:
        exists = False
        for cave in caves:
            if newcave == cave.name:
                exists = True
                break

        if not exists:
            freshcave = Cave(newcave)
            caves.append(freshcave)

    for cave in caves:
        if cave.name == newcaves[0]:
            cave.addconnected(newcaves[1])
        if cave.name == newcaves[1]:
            cave.addconnected(newcaves[0])


start = getcave('start', caves)
end = getcave('end', caves)

#paths = []
#allpathsfound = False
#while not allpathsfound:
#    currentpath = []

routecount = walkcave(start, caves)

print("Total path count: " + str(routecount))
print("welp")
