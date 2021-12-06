import numpy as np

infile = open("D4_input.txt", "r")
textdrawnnumbers = infile.readline().rstrip().split(",")
drawnnumbers  = []
for number in textdrawnnumbers:
    drawnnumbers.append(int(number))

infile.readline()
print(drawnnumbers)
lines = infile.read()


class Bingofield:

    def __init__(self):
        self.numbers = []
        self.checked = []
        self.size = 0
        self.bingo = False
        self.winningnumber = None
        self.winningcolumn = None
        self.winningrow = None


    def parseField(self, field):
        columns = []
        textrows = field.splitlines()
        for textrow in textrows:
            self.size = self.size+1
            row = []
            textnumbers = textrow.split(' ')
            while "" in textnumbers:
                textnumbers.remove("")

            for textnumber in textnumbers:
                row.append(int(textnumber))

            columns.append(row)

        self.numbers = columns
        self.checked = np.zeros_like(self.numbers)


    def drawNumber(self, number):
        for i in range(self.size):
            for j in range(self.size):
                if number == self.numbers[i][j]:
                    self.checked[i][j] = 1
                    if self.checkBingo():
                        self.winningnumber = number
                    return 1

        return 0


    def checkBingo(self):
        for i in range(self.size):
            counter = 0
            for j in range(self.size):
                if self.checked[i][j] == 1:
                    counter = counter + 1

            if counter == self.size:
                self.bingo = True
                self.winningrow = i
                return 1

        for i in range(self.size):
            counter = 0
            for j in range(self.size):
                if self.checked[j][i] == 1:
                    counter = counter + 1

            if counter == self.size:
                self.bingo = True
                self.winningcolumn = i
                return 1

        return 0


    def reset(self):
        self.bingo = False
        self.winningnumber = None
        self.winningcolumn = None
        self.winningrow = None
        for i in range(self.size):
            for j in range(self.size):
                self.checked[i][j] = 0


    def getRow(self, row):
        return self.numbers[row]

    def getColum(self, colum):
        col = []
        for i in range(self.size):
            col.append(self.numbers[i][colum])

        return col

    def getScore(self):
        if not self.bingo:
            return 0
        else:
            accu = 0
            for i in range(self.size):
                for j in range(self.size):
                    if self.checked[i][j] == 0:
                        accu = accu + self.numbers[i][j]

            return accu * self.winningnumber


def playBingo(bingofields, numbers):
    for number in numbers:
        for bingofield in bingofields:
            bingofield.drawNumber(number)
            if bingofield.bingo:
                return bingofield

def playBingoSquid(bingofields, numbers):
    for number in numbers:
        for bingofield in bingofields:
            bingofield.drawNumber(number)

        for bingofield in bingofields:
            if bingofield.bingo:
                if len(bingofields) == 1:
                    return bingofield
                bingofields.remove(bingofield)


bingofields = []
textbingofields = lines.split("\n\n")
for textfield in textbingofields:
    bingofield = Bingofield()
    bingofield.parseField(textfield)
    bingofields.append(bingofield)

winningfield = playBingo(bingofields, drawnnumbers)

print("Score of winning field is " + str(winningfield.getScore()))

for field in bingofields:
    field.reset()

squidfield = playBingoSquid(bingofields, drawnnumbers)

print("Score of last winning field is " + str(squidfield.getScore()))

infile.close()

