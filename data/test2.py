def decode(str):
    numlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    prev = ''
    result = ''
    for i in range(len(str)):
        if str[i] in numlist:
            result += prev * (int(str[i])-1)
        else:
            result += str[i]
        prev = str[i]
    return result


def caesar(str, n):
    res = ''
    for c in str:
        temp = ord(c) - n
        if temp < 97:
            temp = 123 - (97-temp)
        temp = chr(temp)
        res += temp

    return res


if __name__ == '__main__':
    str = 'a3b2cde'
    print(decode(str))
    print(caesar('fdhvdu', 3))
    print(caesar('qbbatfvy', 13))
    print(max([1]))
