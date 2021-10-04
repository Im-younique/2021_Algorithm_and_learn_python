def palindrome(s) :     #문자열을 뒤집어서 같은지 확인
    if s==s[::-1]:
        return True
    else:
        return False



str = input().strip()
longest = 0
result = ""

for i in range(0, len(str)):        #i는 0부터 str의 길이까지
    for j in range(i+1, len(str)):  #j는 i+1부터 str의 길이까지 
        substr = str[i:j]           #i부터 j직전까지  
        if palindrome(substr):      #substr이 palindrome인지 확인
            if(len(substr) > longest):  #가장긴 palindrome을 찾기위해 longest와 비교
                longest = len(substr)
                result = substr

print(result)

