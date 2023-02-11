n = int(input())
floor = n // 7 +1
if n % 7 == 0:
    floor -= 1
print(floor)