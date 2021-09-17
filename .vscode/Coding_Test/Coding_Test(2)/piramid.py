def pira(n) :
    two = 2
    return two ** n

n = int(input())
sum = 0
for i in range(n):
    sum += pira(i)

print(sum)