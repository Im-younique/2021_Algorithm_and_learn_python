#logest palidrome substring
#table은 서브스트링을 나열하는 표를 나타낸다. LPS_example.png참고

def longest_palindrome(s):
    table = [[False for i in range(len(s))] for j in range(len(s))]
    longest = 0     #초기화
    #한 글자는 모두 palindrome이 된다.
    for i in range(len(s)): #i는 가로행 
        for j in range(len(s) - i): #j는 세로열
            if i < 2:   #i(문자열)(이)가 작을 때(2)는 옆에 table과 비교 (T,F초기화)
                if s[j] == s[i+j]:  #2글자 문자인데 같으면 True 아니면 False
                    table[j][i+j] = True
                    longest = i + 1
                else:
                    table[j][i+j] = False
            else:   #문자열의 길이가 3이상 일 때는 오른쪽 대각선으로 올라가면서 비교
                #table기준 찾으려는 문자열의 7시방향 대각선이 반드시 True여야  True일 수 있다(아닐 수 도 있음).
                if s[j] == s[i+j] and table[j+1][i+j-1]:
                    table[j][i+j] = True
                    longest = i + 1
                else :
                    table[j][i+j] = False
    return longest

def main():
    input_count = int(input())          #Testcase 갯수 입력

    for _ in range(0, input_count):
        str = input().strip().lower()   #앞 뒤 공백제거, 소문자 정렬
        print(longest_palindrome(str))  

if __name__ == '__main__':
    main()