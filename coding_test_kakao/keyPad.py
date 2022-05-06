def solution(numbers, hand):
    lt = [3, 0]
    rt = [3, 2]
    phone = [['0','0','0'], ['0','0','0'], ['0','0','0'], ['L','0','R']]
    answer = []
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer.append('L')
            phone[lt[0]][lt[1]] = '0'
            phone[int(n/3)][0] = 'L'
            lt = [int(n/3), 0]
        elif n == 3 or n == 6 or n == 9:
            answer.append('R')
            phone[rt[0]][rt[1]] = '0'
            phone[int(n/3)-1][2] = 'R'
            rt = [int(n/3)-1, 2]
        elif n == 2:
            sumL = abs(lt[0]-0) + abs(lt[1]-1)
            sumR = abs(rt[0]-0) + abs(rt[1]-1)
            if sumL > sumR or (sumL==sumR and hand == "right"):
                answer.append('R')
                phone[rt[0]][rt[1]] = '0'
                phone[0][1] = 'R'
                rt = [0, 1]
            elif sumL < sumR or (sumL==sumR and hand == "left"):
                answer.append('L')
                phone[lt[0]][lt[1]] = '0'
                phone[0][1] = 'L'
                lt = [0, 1]
        elif n == 5:
            sumL = abs(lt[0]-1) + abs(lt[1]-1)
            sumR = abs(rt[0]-1) + abs(rt[1]-1)
            if sumL > sumR or (sumL==sumR and hand == "right"):
                answer.append('R')
                phone[rt[0]][rt[1]] = '0'
                phone[1][1] = 'R'
                rt = [1, 1]
            elif sumL < sumR or (sumL==sumR and hand == "left"):
                answer.append('L')
                phone[lt[0]][lt[1]] = '0'
                phone[1][1] = 'L'
                lt = [1, 1]
        elif n == 8:
            sumL = abs(lt[0]-2) + abs(lt[1]-1)
            sumR = abs(rt[0]-2) + abs(rt[1]-1)
            if sumL > sumR or (sumL==sumR and hand == "right"):
                answer.append('R')
                phone[rt[0]][rt[1]] = '0'
                phone[2][1] = 'R'
                rt = [2, 1]
            elif sumL < sumR or (sumL==sumR and hand == "left"):
                answer.append('L')
                phone[lt[0]][lt[1]] = '0'
                phone[2][1] = 'L'
                lt = [2, 1]
        elif n == 0:
            sumL = abs(lt[0]-3) + abs(lt[1]-1)
            sumR = abs(rt[0]-3) + abs(rt[1]-1)
            if sumL > sumR or (sumL==sumR and hand == "right"):
                answer.append('R')
                phone[rt[0]][rt[1]] = '0'
                phone[3][1] = 'R'
                rt = [3, 1]
            elif sumL < sumR or (sumL==sumR and hand == "left"):
                answer.append('L')
                phone[lt[0]][lt[1]] = '0'
                phone[3][1] = 'L'
                lt = [3, 1]
    
    answer = ''.join(answer)
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))