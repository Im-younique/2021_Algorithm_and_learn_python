import sys

def main():
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()

    len1 = len(str1)
    len2 = len(str2)

    matrix = [[0 for _ in range(len1+1)] for _ in range(len2 + 1)]
    for i in range(1, len2+1):
        for j in range(1, len1+1):
            if str2[i-1] == str1[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    
    print(matrix[-1][-1])

if __name__ == '__main__':
    main()