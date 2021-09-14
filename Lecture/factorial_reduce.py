from functools import reduce
 
def factorial_reduce(n):
     return reduce(lambda x, y: x * y, range(1, n+1))              #lamda는 함수를 간단하게 한줄로 표현한것
                                                    # ex) print((lambda x,y: x + y)(10, 20)) => 30
                                                    #  (lambda 파라미터: 계산식)(파라미터에 따른 변수) 
                                                    #  (lambda 인자 : 표현식) (인자에 따른 변수)

                                                    # reduce(함수, 시퀀스)
                                                    # reduce(lambda x, y: y + x, 'abcde') => 'edcba'
print(factorial_reduce(10))