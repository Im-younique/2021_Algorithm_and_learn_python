def main():
    N = int(input())
    n_list = list(map(int, input().split()))
    M = int(input())
    m_list = list(map(int, input().split()))

    find = False
    for i in range(M):
        find = False
        for j in range(N):
            if n_list[j] == m_list[i]:
                find = True
                print(1)
                break
        if find == False:
            print(0)
    
if __name__ == '__main__':
    main()