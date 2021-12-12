import sys

def generateTree(N, tree):
    for _ in range(N - 1):
        parent, child = map(int, sys.stdin.readline().split())
        tree[parent].append(child)
        tree[child].append(parent)

def find_lca(child1, child2, tree, N):
    for _ in range(N):
        if(child1 == 1 or child2 == 1):             #최상위 노드가 되었을때
            print(1)
            break
        elif(tree[child1][0] == tree[child2][0]):   #child1과 child2의 부모노드가 같을때
            print(tree[child1][0])
            break
        elif(tree[child1][0] == child2):        #child1의 부모노드가 child2일때
            print(child2)
            break
        elif(tree[child2][0] == child1):        #child2의 부모노드가 child1일때
            print(child1)
            break
        elif(child1 < child2):
            if(tree[child1][0] == 1):
                print(1)
                break
            else:
                child2 = tree[child2][0]
        elif(child1 > child2):
            if(tree[child1][0] == 1):
                print(1)
                break
            else:
                child1 = tree[child1][0]

    

def main():
    N = int(sys.stdin.readline())
    tree = [[] for _ in range(N+1)]
    generateTree(N, tree)

    M = int(sys.stdin.readline())
    for _ in range(M):
        child1, child2 = map(int, sys.stdin.readline().split())
        find_lca(child1, child2, tree, N)


if __name__ == '__main__':
    main()