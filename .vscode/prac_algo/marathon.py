
def main():
    pati = list(input().strip().split())
    com = list(input().strip().split())
    result = []
    result = list(set(pati) - set(com))
    
    print(*result)

if __name__ == '__main__':
    main()