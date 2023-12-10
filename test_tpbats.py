import datetime
import random
from tpbats import *
from tp_array import *
from numeral_system_2_10 import *

prime_list = [3]
test = PT()
translate = NumSys()

def generate_prime(prime_limit):
    size_pl = 1
    for i in range(5, prime_limit, 2):
        temp = True
        j = 0
        while temp:
            if i % prime_list[j] == 0:
                temp = False
            j += 1
            if j == size_pl:
                size_pl += 1
                prime_list.append(i)
                temp = False


def start_search_prime(start_exp):
    b = (1 << (1 << start_exp))
    start_exp += 1
    c = (1 << (1 << start_exp))
    start_exp -= 1

    datetime_now = datetime.datetime.now()
    
    for i in range(1, 100):
        z = False
        x = random.randint(b,c)
        
        if not (x & 1):
            x += 1
        
        while not z:
            x += 2

            z = poisk_prime(x)
            fin = datetime.datetime.now()
            print('time= ', (fin - datetime_now))
            datetime_now = fin
            
        prime_to_file(start_exp, i, x)

        fin = datetime.datetime.now()
        print('time= ', (fin - datetime_now))
        datetime_now = fin

def poisk_prime(y):
    z = True

    for j in prime_list:
        if y % j == 0:
            z = False

    if z:
        z = test(y)
    
    return z


def prime_to_file(num1, num2, prime):
    puth = f'D:\Desktop\Теории\Тест простоты\prime_{num1}_{num2}.txt'
    
    with open(puth, '+w') as file:
        file.write(translate(prime, True))
    

generate_prime(1000)
start_search_prime(15)