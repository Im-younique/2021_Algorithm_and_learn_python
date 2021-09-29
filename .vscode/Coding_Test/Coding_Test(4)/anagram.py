
def anagram(str1, str2):
    if ''.join(sorted(str1)) == ''.join(sorted(str2)):
    #sorted는 문자열을 받아 정렬해서 list로 만들어 / join을 써서 다시 문자열로 변경
    #''은 구분자
        return True
    else:
        return False

str = input().lower().strip().split(" ")
#소문자 정렬, 앞뒤 공백제거후 공백 별로 str배열에 저장


print(anagram(str[0], str[1]))