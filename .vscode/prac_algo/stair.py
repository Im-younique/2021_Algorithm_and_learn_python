# 1계단 혹은 2계단 올라갈 때 10개단까지 가는 경우의 수 갯수

def stair_count(destination):       #경우의 수의 갯수 출력
    if destination ==1:
        return 1 
    elif destination == 2:
        return 2
    else:
        return (stair_count(destination-1) + stair_count(destination-2))
    
dest = int(input())
print(stair_count(dest))
