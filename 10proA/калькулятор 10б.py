def from_10_to_n(x, n):
    ost = []
    hex_dict = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    while x >= n:
        temp = str(x % n)
        if int(temp) > 9:
            temp = hex_dict[int(temp)]
        ost.append(temp)
        x = x // n
    ost.append(str(x))
    ost.reverse()
    res = ''.join(ost)
    return res


a = from_10_to_n(43, 2)
print(a)