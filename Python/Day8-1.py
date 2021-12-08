from math import acos


class Entry:

    def __init__(self, line):
        self.input, self.output = line.rstrip().split(" | ")
        self.inputsignals = self.input.split(' ')
        self.outputsingals = self.output.split(' ')


infile = open("D8_input.txt", "r")
lines = infile.readlines()
entries = []
for line in lines:
    entries.append(Entry(line))

acumulator = 0
for entry in entries:
    for output in entry.outputsingals:
        if len(output) == 2: acumulator = acumulator + 1
        if len(output) == 3: acumulator = acumulator + 1
        if len(output) == 4: acumulator = acumulator + 1
        if len(output) == 7: acumulator = acumulator + 1



print(str(acumulator))
print("welp")