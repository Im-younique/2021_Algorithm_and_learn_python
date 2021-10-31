global count
count = 0

def merge(my_input, find, AD, basic_list):
    global count
    if len(basic_list)==1:
        return basic_list
    
    middle = int(len(basic_list)/2)
    left = basic_list[0:middle]
    right = basic_list[middle:]
    
    left = merge(my_input, find, AD, left)
    right = merge(my_input, find, AD, right)
    
    result = mergesort(left, right, AD)
    idx = []
    for i in result:
        idx.append(my_input.index(i))
    idx.sort()
    for j in range(len(idx)):
        my_input.remove(result[j])
    my_input.insert(idx[0], result)
    count += 1
    if count == find:
        print(result)
        
    return result
    
def mergesort(left, right, AD):
    merged_list = []
    i = 0
    j = 0
    while (len(left) != 0) and (len(right) != 0):
        if AD == 'A':
            if left[i] <= right[j]:
                m = left.pop(0)
                merged_list.append(m)
            else:
                m = right.pop(0)
                merged_list.append(m)
        elif AD == 'D':
            if left[i] >= right[j]:
                m = left.pop(0)
                merged_list.append(m)
            else:
                m = right.pop(0)
                merged_list.append(m)
    
    while (len(left) != 0):
        m = left.pop(0)
        merged_list.append(m)
        
    while (len(right) != 0):
        m = right.pop(0)
        merged_list.append(m)
        
    return merged_list
                
    

def main():
    n, find, AD = map(str, input().strip().split())
    n = int(n)
    find = int(find)
    basic_list = list(input().strip().split())
    
    merge(basic_list, find, AD, basic_list)
    
if __name__ == '__main__':
    main()