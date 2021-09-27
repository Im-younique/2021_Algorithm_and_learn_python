#정렬 방식으로 확인

def is_anagram(str1, str2):
    if ''.join(sorted(str1))

def main():
    input_count = int(input())

    for _ in range(0, input_count):
        word1 = input().strip().lower().replace(" ", "")
        word2 = input().strip().lower().replace(" ", "")
        print(word1, word2)
        if(is_anagram(word1, word2)):
            print(1)
        else:
            print(2)

if __name__ == '__main__':
    main()