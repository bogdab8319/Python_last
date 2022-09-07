

import datetime
import random

start= int(input(" input 1"))
end= int(input(" input 2"))
import time


def myDekorator(fn):
    def function (start, end):
        start = datetime.datetime.now()
        result = fn(start, end)
        print("Время", datetime.datetime.now()-start)
        return result
    return function


def simple_num(start ,end):
    list = []
    count = 0
    for i in range(2, end//2):
        if end % i == 0:
            list.append(i)
            return True
        for i in range(start, end):
            if simple_num(i):
                return False
    return list

def performance(fun):
    start= time.time()
    res = fun()
    end = time.time()
    print( f' Simple number : {res}\n Performance: {end}')
    performance_simple_range = performance(simple_num)
    performance_simple_range()


print(" Задание № 3")

income= [random.randrange(100,1000) for i in range (25)]
comsumption = [random.randrange(100,1000) for i in range(25)]


# test 2 test 2