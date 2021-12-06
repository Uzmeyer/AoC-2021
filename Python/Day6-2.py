import collections

import numpy as np
import time
from matplotlib import pyplot as plt

scriptstart = time.time()

lanternfish = np.genfromtxt('Day6_input.txt', delimiter=',', dtype=int)

timercount = collections.Counter(lanternfish)
fishtracker = collections.deque()
for i in range(7):
   fishtracker.append(timercount[i])

seveneight = collections.deque()
seveneight.append(0)
seveneight.append(0)
fishtracker.rotate(-1)

for i in range(256):
    fishtracker.rotate(-1)
    seveneight.append(fishtracker[6])
    fishtracker[6] = fishtracker[6] + seveneight.popleft()

fishcount =  0
for i in range(7):
    fishcount = fishcount + fishtracker[i]

fishcount = fishcount + seveneight[0]


print("Number of Lanternfish after 80 days: " + str(fishcount) + " Script took " + str(time.time() - scriptstart) + " seconds")
print("welp")