import random
p_all = 100_000_000
p_circle = 0
for i in range(p_all):
    x = random.random()
    y = random.random()
    if (x ** 2 + y ** 2) < 1:
        p_circle += 1
S_circle = 4 * p_circle / p_all
print(S_circle)