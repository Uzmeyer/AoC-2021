import numpy as np
import time

scriptstart = time.time()
lanternfish = np.genfromtxt('Day6_input_example.txt', delimiter=',', dtype=int)

for i in range(256):
    start = time.time()
    newfish = 0
    for j, fish in enumerate(lanternfish):
        lanternfish[j] = lanternfish[j] - 1
        if lanternfish[j] < 0:
            newfish = newfish + 1
            lanternfish[j] = 6

    lanternfish = np.append(lanternfish, np.full(newfish, 8))
    print("Day " + str(i) + " took " + str(time.time() - start) + " seconds, current fish: " + str(len(lanternfish)))

print("Number of Lanternfish after 80 days: " + str(len(lanternfish)) + " Script took " + str(time.time() - scriptstart) + " seconds")


print("welp")