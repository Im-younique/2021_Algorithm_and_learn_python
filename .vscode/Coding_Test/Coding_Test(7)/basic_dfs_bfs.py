import sys
from collections import defaultdict

def bfs(matrix, start):                     #queue로 bfs 구현
    visit = list()
    queue = list()
    
    queue.append(start)
    while queue:
        V = queue.pop(0)
        if V not in visit:
            visit.append(V)
            queue.extend(matrix[V])
    
    return visit
        
def dfs(matrix, start):                     #stack으로 dfs 구현
    visit = list()
    stack = list()
    
    stack.append(start)
    while stack:
        V = stack.pop()
        if V not in visit:
            visit.append(V)
            stack.extend(matrix[V])
            
    return visit


def main():
    start = input()
    matrix = defaultdict(lambda: 0)
    N = 13
    for i in range(N):
        lineinput = sys.stdin.readline().split()        #입력 저장 성공
        my_k = lineinput.pop(0)
        matrix[my_k] = lineinput
            
    print(*bfs(matrix, start))
    print(*dfs(matrix, start))
    

if __name__ == '__main__':
    main()