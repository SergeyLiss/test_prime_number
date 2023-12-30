import datetime
from tpbats import *

prime = PT()

prime_list = [3]

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

generate_prime(5000)

qwerty = 22112825529529666435281085255026230927612089502470015394413748319128822941402001986512729726569746599085900330031400051170742204560859276357953757185954298838958709229238491006703034124620545784566413664540684214361293017694020846391065875914794251435144458199
print(prime(qwerty))
while qwerty != 0:
    for i in prime_list:
        if (qwerty % i) == 0:
            qwerty //= i
            print(i)

start_all = datetime.datetime.now()
start_global = datetime.datetime.now()
for i in prime_list:

    m = 1 << i
    m -= 1

    start = datetime.datetime.now()
    fin = datetime.datetime.now()
    if prime(m):
        finish_global = datetime.datetime.now()
        print(i, "\t--->\t", (fin - start), "\t--->\t", (finish_global - start_global))
        start_global = finish_global
finish_all = datetime.datetime.now()
print("---> ", (finish_all - start_all))



start_all = datetime.datetime.now()
start_global = datetime.datetime.now()
for i in prime_list:

    m = 1 << i
    m -= 1

    start = datetime.datetime.now()
    k = pow(3, (m >> 1), m)
    fin = datetime.datetime.now()
    if (k == 1) | (k == (m-1)):
        finish_global = datetime.datetime.now()
        print(i, "\t--->\t", (fin - start), "\t--->\t", (finish_global - start_global))
        start_global = finish_global
finish_all = datetime.datetime.now()
print("---> ", (finish_all - start_all))