import re

def is_anagram(str1, str2):
    if ''.join(sorted(str1)) == ''.join(sorted(str2)):
    #sorted는 문자열을 받아 정렬해서 list로 만들어 / join을 써서 다시 문자열로 변경
        return True
    else:
        return False


str_list = list(input().strip().lower().split(' '))

print_list = []

while (len(str_list) != 0):
    do = str_list.pop(0)
    dos = [do]
    deletes = []
    for i in str_list:
        if is_anagram(do, i):
            dos.append(i)
            deletes.append(i)
    dos.sort()                  #그룹내 소팅
    for d in deletes:
        str_list.pop(str_list.index(d))
    print_list.append(dos)

result = sorted(print_list, key=lambda x: (x, len(x)))       # 첫 번째 알파벳 순을 정렬기준으로 둔다. 두 번째 문자열의 길이.
for i in range(0, len(result)):
    print(*result[i])
#my_cord 1
# result = []
# k = 0

# idx = []

# for i in range(0, len(str_list)):
#     result.append([])
#     result[k].append(str_list[i])
#     for j in range(i+1, len(str_list)):
#         if(is_anagram(str_list[i], str_list[j])):
#             result[k].append(str_list[j])
#             idx.append(str_list.index(str_list[j]))
#     for u in range(0, len(idx)):
#         str_list.remove(cp_list[idx[u]])
#     k += 1

# result = result.sort()
# for i in range(len(result)):
#     print(*result[i])

#my_cord 2
# result = []
# m = 0
# k = 0

# idx = []


# for i in range(0, 26):
#     if(len(str_list) == 0):
#         break
#     char_match = list(filter(lambda x: chr(97+i) in x, str_list))
#     if(not char_match):
#         continue
#     char_match.sort()
#     result.append([])
#     result[k].append(char_match[0])
#     if(len(char_match) == 1):
#         str_list.remove(char_match[0])
#     else:
#         for j in range(1, len(char_match)):
#             if(is_anagram(char_match[0], char_match[j])):
#                 idx.append(char_match.index(char_match[j]))
#                 result[k].append(char_match[j])
#             else:
#                 pass
#         str_list.remove(char_match[0])
#         for p in range(len(idx)):
#             str_list.remove(char_match[idx[p]])
#         k += 1
#         idx.clear()

   
# for i in range(len(result)):
#     print(*result[i])


#맨 앞 문자열 / 그 뒤에 문자열들 하나씩 비교하기
#맨 앞 문자열과 아나그램인것 찾으면 같이그룹핑
#없으면 혼자 그룹핑
#


