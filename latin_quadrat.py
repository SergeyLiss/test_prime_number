#
# max = 8
len_array = 8

array = 'ABCDEFGH'

c = 0

flag = [False for i in range(len_array)]

def rotation (arr, box):
    global c
    for i in arr:
        if len((box + i)) == len_array:
            print(box)
            c = c + 1
        else:
            rotation((arr.replace(i, '')), (box + i))


rotation(array[:len_array], '')
print(c)