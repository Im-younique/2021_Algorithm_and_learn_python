#문자열을 뒤집었을 때 같은지 확인

def is_palindrome(s):
    return s == s[::-1]     #파이썬 문자열 reverse 표현

def main():
    input_count = int(input())  #Testcase 수
    word_list = []

    word_list = [input().strip() for i in range(0, input_count)]
    #Testcase 만큼 문자열 입력
    for s in word_list: #각 문자열이 palindrome인지 확인
        if(is_palindrome(s)):
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    main()