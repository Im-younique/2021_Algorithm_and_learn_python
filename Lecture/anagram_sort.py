#두개의 문자에 써있는 알파벳이 같은지 확인
#정렬 방식으로 확인

def is_anagram(str1, str2):
    if ''.join(sorted(str1)) == ''.join(sorted(str2)):
    #sorted는 문자열을 받아 정렬해서 list로 만들어 / join을 써서 다시 문자열로 변경
        return True
    else:
        return False


def main():
    input_count = int(input())

    for _ in range(0, input_count):
        word1 = input().strip().lower().replace(" ", "")    #앞, 뒤 및 중간 공백 처리 및 소문자 정렬
        word2 = input().strip().lower().replace(" ", "")
        print(word1, word2)
        if(is_anagram(word1, word2)):
            print(1)
        else:
            print(2)

if __name__ == '__main__':
    main()