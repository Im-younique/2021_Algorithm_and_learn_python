def pira(n):
    if n==1:
        return 1
    else:
        return pira(n-1)*2 + 1
        
def main():
    n = int(input())
    print(pira(n))
    
if __name__ == '__main__':
    main()