a = 10000

def p_to_n(n):
    f = 1
    for i in range(1, (n+1)):
        f *= i
    x = f
    for j in range(1, (n+1)):
        if j & 1:
            m = -1
        else:
            m = 1
        for k in range(1, (j+1)):
            m *= k
        x += (f // m)
    return x

b = p_to_n(a)
print(f"{a} ---> {b}")




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