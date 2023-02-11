def print_array(a):
    for y in range(len(a)):
        for x in range(len(a[y])):
            print(a[y][x], end='\t')
        print()

def get_empty_array():
    n = int(input())
    a = []
    for y in range(n):
        a.append([])
        for x in range(n):
            a[y].append('_')
    return a

def place_ship():
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split(';'))
        field[y][x] = '#'

def shoot():
    x, y = map(int, input().split(';'))
    if field[y][x] != '#':
        field[y][x] = 'X'
    else:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                field[y + i][x + j] = 'X'
        field[y][x] = '*'

field = get_empty_array()
place_ship()
shoot()
print_array(field)