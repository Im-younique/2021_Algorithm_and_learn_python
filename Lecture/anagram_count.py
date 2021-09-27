#두개의 문자에 써있는 알파벳이 같은지 확인
#알파벳 카운트 방식으로 확인

def is_anagram(s1, s2):
    c1 = [0]*26     #각각 알파벳 카운트 초기화
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a') #ord() 특정한 문자를 아스키 코드 값으로 변환
        c1[pos] += 1                #따라서 a면 c1[0] b면 c1[1] 에 값이 올라감
    for i in range(len(s1)):
        pos = ord(s2[i]) - ord('a') #위와 동일
        c2[pos] += 1                #cf. ord() <-> chr() 아스키 값을 문자로 변환

    stillOK = True
    j = 0
    while j < 26 and stillOK:       #각 문자열의 알파벳의 수가 동일한지 확인
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOK = False
    return stillOK


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