import datetime
from tpbats import *

prime = PT()

test: int
exp: int

directoria = 'D:\Desktop\Теории\Тест простоты\Mersenne_prime.txt'

with open(directoria, 'r') as file:
    exp = int(file.readlines()[-1])

while True:
    z = False
    test = 1

    while not z:
        exp += 2
        z = prime(exp)
    
    test <<= exp
    test -= 1

    z = prime(test)

    if z:
        print(exp)
        with open(directoria, 'a') as file:
            file.write(f'{exp}\n')