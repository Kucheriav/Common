import random

numbers = list()
for i in range(10):
    a = random.randint(1, 10000)
    numbers.append(a)
numbers.sort(key=lambda x: len(str(x)))
print(numbers)
# for i in range(len(numbers) - 1):
#     for j in range(len(numbers) - 1 - i):
#         if numbers[j] % 2 == 0:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#     print(numbers)