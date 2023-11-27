import datetime
from tpbats import *

prime = PT()

test: int
exp: int
constant: list

constant = [0, 0]
exp = 3

for i in range(exp, 10000000, 2):
    if prime(i):
        test = 1 << (i - 1)
        test -= 1
        test //= i
        constant[0] = test % i
        test //= i
        constant[1] = test % i
        constant[1] <<= 1

        test = constant[0] * constant[0] - constant[1]
        test %= i

        flag = False if pow(test, (i >> 1), i) == 1 else True

        if flag:
            # print(i)
            # print(datetime.datetime.now())
            test = 1 << i
            test -= 1

            if prime(test):
                print(i)
