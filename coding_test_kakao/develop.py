import copy

def solution(progresses, speeds):
    answer = []
    queue = copy.deepcopy(progresses)
    now = 0
    while queue:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        for j in range(now, len(progresses)):
            if progresses[j] >= 100:
                queue.pop(0)
                cnt += 1
                now += 1
            else:
                break
        if cnt > 0:
            answer.append(cnt)
    return answer

progress = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progress, speeds))