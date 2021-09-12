import numpy as np
import time
from random import *
import matplotlib.pyplot as plt

findMaxSortingTimes = []
findMaxTime = []

def find_max_sorting(alist):
    alist.sort()
    return alist[len(alist)-1]

def find_max(alist):
    maxsofar = alist[0]
    for i in alist :
        if i > maxsofar:
            maxsofar = i
    return maxsofar

for listSize in range(1000000, 10000000, 2000000):
    alist = [randrange(1000) for x in range(listSize)]

    start = time.time()
    find_max_sorting(alist)
    end = time.time()
    runTime = end - start
    findMaxSortingTimes.append(runTime)

    start = time.time()
    find_max(alist)
    end = time.time()
    runTime = end - start
    findMaxTime.append(runTime)

sizes = range(1000000, 10000000, 2000000)
plt.figure(figsize=(8,5))
plt.plot(sizes, findMaxSortingTimes, marker='x',c='r',label='findMaxSotring')
plt.plot(sizes, findMaxTime, marker='x',c='g',label='findMax')
plt.xlabel("Input size")
plt.ylabel("Time (Second)")
plt.grid()
plt.title("Complexity")
plt.savefig('complexity.png', bbox_inches='tight')