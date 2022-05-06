def solution(s):
    my_l = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, v in enumerate(my_l):
        s = s.replace(v, str(i))
    
    answer = int(s)
    return answer

s = "one4seveneight"
print(solution(s))