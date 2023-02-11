def greedy_alg(items: list, limit: int):
    total_sum = 0
    total_items = []
    items = items[:]
    items.sort(key=lambda x: -x[1])
    for i in range(len(items)):
        if items[i][1] + total_sum <= limit:
            total_sum += items[i][1]
            total_items.append(items[i][0])
        if total_sum == limit:
            break
    return total_sum, total_items

def f(x):
    return x[1]

# название,  ограничение
items = [['процессор', 12500], ['материнка', 16700],
         ['монитор', 11500], ['видеокарта', 31300],
         ['клавиатура', 1050], ['ОЗУ', 800]]
items.sort(key=lambda x: -x[1])
items.reverse()
max_sum = 50_000
cur_sum = 0
names = list()
for i in range(len(items)):
    if cur_sum + items[i][1] <= max_sum:
        cur_sum += items[i][1]
        names.append(items[i][0])
print(cur_sum)
print(names)






# max_sum = 40000
#
# items.sort(key=lambda item: item[1])
# res_items = []
# res_sum = 0
# for i in range(len(items)):
#     if res_sum + items[i][1] <= max_sum:
#         res_sum += items[i][1]
#         res_items.append(items[i][0])
# print(res_items)
# print(res_sum)








# res_sum, res_items = greedy_alg(items, max_sum)
# print(res_sum)
# print(res_items)