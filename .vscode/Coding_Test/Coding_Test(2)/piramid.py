def pira(n) :
    two = 2
    return two ** n         #각 층마다 2 ** n 배로 무게가 쌓여간다.

n = int(input())
sum = 0                     #각 층의 무게의 값을 저장
for i in range(n):
    sum += pira(i)          #각 층의 무게를 더한다. 

print(sum)