import sys

def main():
    N = int(input())
    myList = []
    for i in range(N):
        age, name = sys.stdin.readline().split()
        myList.append([int(age), name, i])

    myList.sort(key=lambda x : (x[0], x[2]))

    for a, n, l in myList:
        print(a, n)

    

if __name__ == '__main__':
    main()