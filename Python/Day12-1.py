
infile = open("D12_input_example.txt", "r")
lines = infile.readlines()

class Cave:

    def __init__(self, name=''):
        self.name = name
        if name.islower():
            self.issmall = True
        else:
            self.issmall = False
        if name == 'start':
            self.isstart = True
            self.isend = False
        if name == 'end':
            self.isstart = False
            self.isend = True
        self.visited = False
        self.connected = []

caves = []
for line in lines:
    caves = line.rstrip().split("-")




print("welp")
