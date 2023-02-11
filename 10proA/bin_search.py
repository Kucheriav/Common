import random

numbers = list()
for i in range(10000):
    a = random.randint(1, 1000000)
    numbers.append(a)
numbers.sort()
print(numbers)
left = 0
right = len(numbers) - 1
mid = (left + right) // 2
x = 42
while numbers[mid] != x and left <= right:
    if x > numbers[mid]:
        left = mid + 1
    else:
        right = mid - 1
    mid = (left + right) // 2
if numbers[mid] == x:
    print("Ура, нашлось")
else:
    print("Ой, не нашлось")