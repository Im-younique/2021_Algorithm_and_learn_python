from collections import defaultdict
n = int(input())
edge = defaultdict(lambda: [])
indegree = defaultdict(lambda: 0)
for _ in range(n):
    x, y = map(str, input().split())
    edge[x].append(y)
    indegree[y] += 1
q = []
ans = []
for i in edge:
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.pop(0)
    ans.append(cur)
    for i in edge[cur]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(*ans)