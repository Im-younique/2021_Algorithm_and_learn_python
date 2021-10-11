import collections

def compareCollections(p, c):
    i = collections.Counter(p) - collections.Counter(c)     #i는 해쉬 키 밸류의 쌍.
    return list(i.keys())                                   #키 값을 모아놓은 list return

def main():
    a = input().split()
    b = input().split()
    print(*compareCollections(a, b))

if __name__ == '__main__':
    main()