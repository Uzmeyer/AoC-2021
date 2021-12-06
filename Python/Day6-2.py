import numpy as np
import time
from matplotlib import pyplot as plt

scriptstart = time.time()
##lanternfish = np.genfromtxt('Day6_input_example.txt', delimiter=',', dtype=int)
lanternfish = np.zeros(1)
fishcount = []
for i in range(50):
    start = time.time()
    newfish = 0
    for j, fish in enumerate(lanternfish):
        lanternfish[j] = lanternfish[j] - 1
        if lanternfish[j] < 0:
            newfish = newfish + 1
            lanternfish[j] = 6

    lanternfish = np.append(lanternfish, np.full(newfish, 8))
    fishcount.append(len(lanternfish))

plt.plot(fishcount)
plt.show()