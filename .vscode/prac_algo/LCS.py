import sys

def lcs(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    matrix = [[0 for _ in range(len1+1)] for _ in range(len2+1)]
    #비교하는 문자열이 마지막만 일치하는지 확인하는 것이 핵심
    for i in range(1, len2+1):
        for j in range(1, len1+1):
            if str2[i-1] == str1[j-1]:      #끝부분이 일치하면 10시방향 대각선에서 1을 더해준 값 적용
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:   #아니면 서쪽과 북쪽중 큰 값을 가져옴
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
    
    return matrix[-1][-1]
                
            
def main():
    str1 = sys.stdin.readline().strip()     #개행문자 제거
    str2 = sys.stdin.readline().strip()
    print(lcs(str1, str2))

if __name__ == "__main__":
    main()