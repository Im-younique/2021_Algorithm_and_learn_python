
global sorted
global my_count
global idx 
idx = []
sorted = []
my_count = 0

def mergesort(mainlist_1, aord, mainlist, know):
    global sorted
    global my_count
    global idx
    middle = int(len(mainlist_1)/2)
    left = []
    right = []
    if(int(len(mainlist_1)) == 1):
        return mainlist_1
    left = mergesort(mainlist_1[0:middle], aord, mainlist, know) #left
    right = mergesort(mainlist_1[middle:], aord, mainlist, know)  #right
    sorted = merge(left, right, aord)
    for p in sorted:                        #머지된 값들을 mainlist의 인덱스들을 찾아냄
        idx.append(mainlist.index(p))       #찾아낸 인덱스들을 idx배열에 저장
    idx.sort()                              #인덱스들 작은 값부터 정렬
    mainlist[idx[0]:idx[len(idx)-1]+1] = sorted[0:]   #메인 리스트에 찾아낸 인덱스 처음부터 끝까지 sorted된 값으로 바꿔준다.
    my_count += 1
    if(my_count == int(know)):
        print(*mainlist)
    idx.clear()                             #한번 해내면 초기화
    return sorted

def merge(left, right, aord):
    result = []
    i = 0
    j = 0

    while(i < int(len(left)) and j < int(len(right))):
        if(aord == 'A'):
            if(left[i] < right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif(aord == 'D'):
            if(left[i] > right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    while(i < int(len(left))):
        result.append(left[i])
        i += 1
    while(j < int(len(right))):
        result.append(right[j])
        j += 1

    return result
    

def main():
    f_input = list(input().split()) #f_input[2] 'A' or 'D'

    mainlist = list(input().split())
    if(int(f_input[1]) == 0):
        print(*mainlist)
    mergesort(mainlist, f_input[2], mainlist, f_input[1])

    
if __name__ == '__main__':
    main()
