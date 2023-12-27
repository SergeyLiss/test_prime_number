import datetime
from tpbats import *

prime = PT()

exp = 5

proof = 3

print(pow(2047,4095,8191))

for i in range(exp, 100000, 2):
    j = 1 << i
    j -= 1

    k = j >> 1

    x = pow(proof, k, j)
    if (x == 1) | (x == (j-1)):
        print(i)


# for i in range(exp, 100000, 2):
#     j = 1 << i
#     j -= 1

#     k = 1 << (i -2)

#     x = pow(proof, k, j)

#     y = pow(x, 2, j)

#     if y == proof:
#         print(i)