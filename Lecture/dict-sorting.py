#길이가 짧은것부터, 길이가 같으면 사전순으로 정렬하는 알고리즘
def multiple_sort(input_list):
    result = sorted(input_list, key=lambda x: (len(x), x))       #첫 번째로 문자열의 길이를 정렬기준으로 두고 / 두 번째 알파벳 순을 정렬기준으로 둔다.
    #result = sorted() 정렬한다. input_list배열에 대해 키 값을 x로 두고 len(x) : 길이순으로 정렬하고, x값을 받아 알파벳 순으로 정렬한다.
    return (result)

def main() :
    input_list = list(input().split(' '))
    print(*multiple_sort(input_list))

if __name__ == '__main__':
    main()