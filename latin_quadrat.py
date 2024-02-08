a = 10

def p_to_n_m(n, m):
    fact = 1
    for i in range(1, (n+1)):
        fact *= i
    
    x = fact
    temp = fact

    for j in range(1, (m+1)):
        temp //= (n+1-j)
        temp *= (m+1-j)
        temp //= j

        if j & 1:
            x -= temp
        else:
            x += temp

    return x

for p in range(2, a):
    print()
    for k in range((p+1)):
        c = p_to_n_m(p, k)
        print(f"{p}.{k}\t--->\t{c}")




# #
# # max = 8
# len_array = 8

# array = 'ABCDEFGH'

# c = 0

# flag = [False for i in range(len_array)]

# def rotation (arr, box):
#     global c
#     for i in arr:
#         if len((box + i)) == len_array:
#             print(box)
#             c = c + 1
#         else:
#             rotation((arr.replace(i, '')), (box + i))


# rotation(array[:len_array], '')
# print(c)