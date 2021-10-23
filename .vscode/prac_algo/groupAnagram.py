import copy

def anagram(st1, st2):
    if ''.join(sorted(st1.lower())) == ''.join(sorted(st2.lower())):
        return True
    else:
        return False

def main():
    my_list = list(map(str, input().strip().split()))
    group = list()
    delete = list()
    result = []
    
    while len(my_list) != 0:
        st1 = my_list.pop(0)
        group.append(st1)
        for i in range(len(my_list)):
            if anagram(st1, my_list[i]):
                group.append(my_list[i])
                delete.append(my_list[i])
        
        for j in delete:
            my_list.remove(j)
        
        group.sort()
        result.append(copy.deepcopy(group))
        group.clear()
        delete.clear()
    
    result = sorted(result, key = lambda x : (x, len(x)))
    for i in result:
        print(*i)
                
if __name__ == '__main__':
    main()