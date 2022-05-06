def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        for j in range(len(board)):
            if board[j][m-1] != 0:      #인형이 있을 때
                stack.append(board[j][m-1])
                board[j][m-1] = 0
                break
        #스택에 같은 숫자로 들어왔는지 확인
        num = len(stack)
        if num >= 2:
            a, b = stack[num-1], stack[num-2]
            if a == b:
                stack.pop()
                stack.pop()
                answer += 2
    
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))