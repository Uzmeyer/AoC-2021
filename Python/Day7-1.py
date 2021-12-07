import collections
import sys
import time

import numpy as np
from matplotlib import pyplot as plt

def triangularsum(n):
    if n < 0:
        return 0

    return (n*(n+1))/2

scriptstart = time.time()

crabs = np.genfromtxt('D7_input.txt', delimiter=',', dtype=int)
best_position = 0
best_consumption = sys.maxsize
crabcounts = collections.Counter(crabs)
for i in range(crabs.min(), crabs.max()):
    fuelconsumption = 0
    for crab in crabcounts.most_common():
        fuelconsumption = fuelconsumption + (abs(crab[0] - i) * crab[1])
    if fuelconsumption < best_consumption:
        best_position = i
        best_consumption = fuelconsumption

print("Best consumption is at position " + str(best_position) + ": " + str(best_consumption) + " Script took " + str(time.time() - scriptstart) + " seconds")

scriptstart = time.time()
best_position = 0
best_consumption = sys.maxsize
crabcounts = collections.Counter(crabs)
for i in range(crabs.min(), crabs.max()):
    fuelconsumption = 0
    for crab in crabcounts.most_common():
        fuelconsumption = fuelconsumption + (triangularsum(abs(crab[0] - i)) * crab[1])
    if fuelconsumption < best_consumption:
        best_position = i
        best_consumption = fuelconsumption

print("Best consumption for 2 is at position " + str(best_position) + ": " + str(best_consumption) + " Script took " + str(time.time() - scriptstart) + " seconds")

print("welp")

""""
1 step costs 1 = 1
2 step costs 2 = 3
3 step costs 3 = 6
"""