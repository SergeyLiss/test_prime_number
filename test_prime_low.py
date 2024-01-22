a = 30
b = [1,7,11,13,17,19,23,29]

def abc(x,y):
    x = b[x]
    y = b[y]
    temp = f'{x}x{y}='
    x = x * y
    y = x // 30
    x = x % 30

    temp += f'{x}.{y}'
    
    return temp

c = [[abc(i,j) for j in range(8)] for i in range(8)]

for q in range(8):
    print(b[q], ': ', c[q])