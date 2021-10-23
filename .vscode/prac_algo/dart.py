import re

def score(my_dart):
    myre = re.compile("([0-9]+)([a-zA-Z])([\*|\#])?")
    score_list = myre.findall(my_dart)
    
    hasOption = False
    result_list = []
    for score in score_list:
        num = score[0]
        bonus = score[1]
        option = score[2]
        if bonus == "S":
            bonus = 1
        elif bonus == "D":
            bonus = 2
        elif bonus == "T":
            bonus = 3
        if option == "*":
            if hasOption == False:
                result = int(num) ** bonus * 2
                hasOption = True
            else:
                result = int(num) ** bonus * 4
                hasOption = True
        elif option == "#":
            if hasOption == False:
                result = -(int(num) ** bonus)
                hasOption = False
            else:
                result = int(num) ** bonus * -2
                hasOption = False
        else:
            if hasOption == False:
                result = int(num) ** bonus
                hasOption = False
            else:
                result = int(num) ** bonus * 2
                hasOption = False
        result_list.append(result)
    
    sum = 0
    for i in range(len(result_list)):
        sum += result_list[i]
    
    return sum
    

def main():
    my_dart = input()
    print(score(my_dart))
    
if __name__ == '__main__':
    main()