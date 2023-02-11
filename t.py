import sys
import copy

def dfs(arr, a, b, start):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    stack = copy.deepcopy(start)
    temp = []
    day = 0
    while(stack):
        x, y = stack.pop()
        for i in range(len(dx)):
            if 0 <= dy[i]+y < a and 0 <= dx[i]+x < b and arr[dx[i]+x][dy[i]+y] == '0':  #동서남북
                arr[dx[i]+x][dy[i]+y] = '1'
                temp.append([dx[i]+x, dy[i]+y])
        if stack == [] and temp != []:
            stack = copy.deepcopy(temp)
            temp = []
            day += 1
    for i in range(b):
        if '0' in arr[i]:
            return -1
    return day
        
a, b = map(int, input().strip().split(' '))
arr = []
start = []
for i in range(b):
    line = sys.stdin.readline().strip().split(' ')
    for j in range(len(line)):
        if line[j] == '1':
            start.append([i, j])
    arr.append(line)

print(dfs(arr, a, b, start))