import sys

N = int(sys.stdin.readline())
myList = list(map(int, sys.stdin.readline().split()))
myMap = {}
for l in range(len(myList)):
    myMap[l] = myList[l]
cnt = 0

postKey = None
nowMax = max(myMap, key=myMap.get)

while(myMap[nowMax] != 0):
    myMap[nowMax] -= 1
    cnt += 1
    postKey = nowMax
    nowMax = max(myMap, key= lambda x : myMap.get)

print(cnt)