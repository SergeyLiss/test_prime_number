import datetime
import random
import os.path
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

    position = 0x0
    datetime_now = datetime.datetime.now()
    limit = True
    while limit:
        z = False
        x = random.randint(b,c)
        
        if not (x & 1):
            x += 1
        
        while not z:
            x += 2

            z = poisk_prime(x)
            
        position = prime_to_file(start_exp, position, x)
        if position > 0x1ff:
            limit = False
        
def poisk_prime(y):
    z = True

    for j in prime_list:
        if y % j == 0:
            z = False
            break

    if z:
        datetime_now = datetime.datetime.now()
        z = test(y)
        print('\ntime= ', (datetime.datetime.now() - datetime_now))
    else:
        print("#", end="")
    
    return z

def prime_to_file(num1, hex1, prime):
    puth = f'D:\Desktop\Теории\Тест простоты\prime_{num1}\prime_{num1}_'

    p = True
    while p:
        file_puth = puth + str(hex(hex1))[2:] + '.txt'
        if not os.path.isfile(file_puth):
            p = False
            puth = file_puth
        hex1 += 1
    
    with open(puth, '+w') as file:
        file.write(translate(prime, True))
    
    return hex1

generate_prime(2_000_000)
print("prime is ready", len(prime_list))
start_search_prime(13)
print('FINISH')