import sys

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
    matrix = {  'A': ['B'],                     #주어진 matrix (사실 input으로 만들어야함)
                'B': ['A', 'C', 'H'],
                'C': ['B', 'D'],
                'D': ['C', 'E', 'G'],
                'E': ['D', 'F'],
                'F': ['E'],
                'G': ['D'],
                'H': ['B', 'I', 'J', 'M'],
                'I': ['H'],
                'J': ['H', 'K'],
                'K': ['J', 'L'],
                'L': ['K'],
                'M': ['H']}
    N = 13
    #matrix = {}
    for i in range(N):
        lineinput = sys.stdin.readline().split()        #입력 저장 실패
    #        matrix[lineinput[0]] = lineinput[1:len(lineinput)+1]        #key, value로 저장
            
    print(*bfs(matrix, start))
    print(*dfs(matrix, start))
    

if __name__ == '__main__':
    main()