prime_list = [3]
thirty: list

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

generate_prime(2_000)

thirty = [(i%30) for i in prime_list]

for i in range(len(prime_list)):
    print(f'{prime_list[i]} ---> {thirty[i]}')



















# a = 30
# b = [1,7,11,13,17,19,23,29]

# def abc(x,y):
#     x = b[x]
#     y = b[y]
#     temp = f'{x}x{y}='
#     x = x * y
#     y = x // 30
#     x = x % 30

#     temp += f'{x}.{y}'
    
#     return temp

# c = [[abc(i,j) for j in range(8)] for i in range(8)]

# for q in range(8):
#     print(b[q], ': ', c[q])