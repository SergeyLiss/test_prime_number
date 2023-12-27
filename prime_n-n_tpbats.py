# Последовательность из повторяющихся цифр до 100_000 штук в десятиричной системе счисления. Только последовательность цифр: 1. Все остальные являются составными.
import datetime
from tpbats import *

test = PT()

def search_pr(a):
    ab = []
    b = a
    for i in range(2, 100000):
        datetime_now = datetime.datetime.now()
        b = b * 10 + a
        if test(b):
            ab.append(i)
        fin = datetime.datetime.now()
        print('time= ', (fin - datetime_now), "\ti= ", i)
        datetime_now = fin
    
    return ab

def start(c):
    puth = f'D:\Desktop\Теории\Тест простоты\prime_rot_{c}.txt'
    d = search_pr(c)
    with open(puth, '+w') as file:
        file.writelines(str(d))

start(1)