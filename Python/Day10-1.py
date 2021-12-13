import collections
import math

infile = open('D10_input.txt')
lines = []
for line in infile:
    lines.append(line.rstrip())


def getClosing(bracket):
    match bracket:
        case '(':
            return ')'
        case '[':
            return ']'
        case '{':
            return '}'
        case '<':
            return '>'
    return 0


def isClosing(opening, closing):
    match opening:
        case '(':
            if closing == ')':
                return 1
        case '[':
            if closing == ']':
                return 1
        case '{':
            if closing == '}':
                return 1
        case '<':
            if closing == '>':
                return 1
    return 0


def checkIllegals(_line):
    chunkstack = collections.deque()
    missingclosing = []
    for i in range(len(_line)):
        currchar = _line[i]
        if currchar in ('(', '[', '{', '<'):
            chunkstack.append(currchar)
        elif currchar in (')', ']', '}', '>'):
            stackchar = chunkstack.pop()
            if not isClosing(stackchar, currchar):
                # print("Expected '" + getClosing(stackchar) + "', but got '" + currchar + "'")
                return currchar, missingclosing

    chunkstack.reverse()
    for bracket in chunkstack:
        missingclosing.append(getClosing(bracket))
    return 0, missingclosing

errorscore = 0
validlines = []
for line in lines:
    error, missing = checkIllegals(line)
    match error:
        case ')':
            errorscore = errorscore + 3
        case ']':
            errorscore = errorscore + 57
        case '}':
            errorscore = errorscore + 1197
        case '>':
            errorscore = errorscore + 25137
        case _:
            validlines.append(line)

print('Errorscore: ' + str(errorscore))
scores = []
for validline in validlines:
    error, missing = checkIllegals(validline)
    if not error:
        score = 0
        for i in range(len(missing)):
            score = score * 5
            bracket = missing[i]
            match bracket:
                case ')':
                    score = score + 1
                case ']':
                    score = score + 2
                case '}':
                    score = score + 3
                case '>':
                    score = score + 4

        scores.append(score)

scores.sort()
solution = scores[math.floor(len(scores)/2)]
print("Solution: " + str(solution))
print('welp')