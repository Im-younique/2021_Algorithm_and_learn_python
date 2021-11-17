import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order(tree, root):      #root, left, right순 탐색
    print(root, end="")
    for i in range(len(tree)):
        if tree[i].data == root:
            root = tree[i]
            break
    if root.left != None:
        pre_order(tree, root.left)
    if root.right != None:
        pre_order(tree, root.right)

def in_order(tree, root):       #left, root, right순 탐색
    temp = root
    for i in range(len(tree)):
        if tree[i].data == root:
            root = tree[i]
            break
    if root.left != None:
        in_order(tree, root.left)
    print(temp, end="")
    if root.right != None:
        in_order(tree, root.right)

def post_order(tree, root):     #left, right, root순 탐색
    temp = root
    for i in range(len(tree)):
        if tree[i].data == root:
            root = tree[i]
            break
    if root.left != None:
        post_order(tree, root.left)
    if root.right != None:
        post_order(tree, root.right)
    print(temp, end='')

def main():
    N = int(input())
    tree = []
    for _ in range(N):
        root, left, right = sys.stdin.readline().split()
        node = Node(root)
        if(left != "."):
            node.left = left
        if(right != "."):
            node.right = right
        tree.append(node)

    pre_order(tree, 'A')        #루트는 'A'부터 시작.
    print()
    in_order(tree, 'A')
    print()
    post_order(tree, 'A')

if __name__ == '__main__':
    main()