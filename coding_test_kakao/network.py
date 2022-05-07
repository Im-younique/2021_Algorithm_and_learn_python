def solution(n, computers):
    answer = 1
    stack = []
    visit = [False] * n
    stack.append(0)
    visit[0] = True
    
    while stack or False in visit:
        if len(stack) == 0:
            ff = visit.index(False)
            visit[ff] = True
            stack.append(ff)
            answer += 1
            #visit에서 false인 친구들 찾아서 stack에 넣고 answer 1증가
        node = stack.pop()
        if visit[node] == False:
            visit[node] = True
        for i in range(len(computers[node])):
            if computers[node][i] == 1 and visit[i] == False:
                stack.append(i)
    
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))