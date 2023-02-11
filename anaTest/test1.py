import sys

N = int(input())
bulbList = list(map(int, sys.stdin.readline().split()))
stateList = list(map(int, sys.stdin.readline().split()))

nowLight = 0
for i in range(len(bulbList)):
    if stateList[i] == 1:
        nowLight += bulbList[i]
result = []
zeroIndexList = []
for s in range(len(stateList)):
    if stateList[s] == 0:
        zeroIndexList.append(s)

if len(zeroIndexList) == 0:
    result.append(-min(bulbList))
elif len(zeroIndexList) == 1:
    result.append(bulbList[zeroIndexList[0]])
else:
    for i in range(len(zeroIndexList)):
        for j in range(i+1, len(zeroIndexList)):
            sum = 0
            for k in range(zeroIndexList[i], zeroIndexList[j]+1):
                if(stateList[k] == 1):
                    sum -= bulbList[k]
                else:
                    sum += bulbList[k]
            result.append(sum)


print(nowLight + max(result))