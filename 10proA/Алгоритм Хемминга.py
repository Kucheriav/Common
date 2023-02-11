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

import random

word_list = list()
while len(word_list) < 10:
    x = random.randint(0, 100)
    x = from_10_to_n(x, 2)
    x = x.rjust(8, '0')
    if not x in word_list:
        word_list.append(x)
print(word_list)

x = random.randint(0, 100)
x = from_10_to_n(x, 2)
x = x.rjust(8, '0')
print('непонятное слово', x)
min_dist = 8
for word in word_list:
    dist = 8
    for i in range(8):
        if x[i] == word[i]:
            dist -= 1
    if dist < min_dist:
        min_dist = dist
        predicted_word = word
print('скорее всего, это - ', predicted_word)
print('расстояние:', min_dist)