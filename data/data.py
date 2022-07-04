import numpy as np
import matplotlib.pyplot as plt
import os

data = np.load(os.path.join(os.getcwd(), 'data', 'Covid_Decided_Count.npy'))
cnt = np.zeros(9)

for i in range(len(data)):
    num = str(data[i])
    first = num[0]
    cnt[int(first) - 1] += 1

plt.bar([i for i in range(1, 10)], cnt)
plt.show()
