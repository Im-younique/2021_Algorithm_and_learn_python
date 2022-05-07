def solution(tickets):      #50점
    airport_list = set()
    for t in tickets:
        a, b = t
        airport_list.add(a)
        airport_list.add(b)
    airport_list = list(airport_list)
    matrix = {a:[] for a in airport_list}
    for t in tickets:
        matrix[t[0]].append(t[1])
    for key in matrix:
        matrix[key].sort()
    stack = ['ICN']
    answer = []
    while stack:
        node = stack.pop(0)
        answer.append(node)
        if len(matrix[node]) != 0:
            stack.append(matrix[node].pop(0))
    return answer

#해결못한 케이스..
tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
print(solution(tickets))