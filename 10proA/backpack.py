items = [['tape', 3000, 4], ['notebook', 2000, 3], ['guitar', 1500, 1]]
# название, максимизируемое св-во (желаемость 0..10), ограничение
# items = [['процессор', 5, 12500], ['материнская плата', 3, 16700],
#          ['монитор', 7, 11500], ['видеокарта', 7, 31300],
#          ['клавитура', 7, 1050], ['ОЗУ', 2, 800]]
backpack_size = 4
max_sum = 40000


def greedy_alg(items: list, limit: int):
    total_weight = 0
    total_sum = 0
    total_items = []
    items = items[:]
    items.sort(key=lambda x: -x[2])
    for i in range(len(items)):
        if items[i][2] + total_weight <= limit:
            total_weight += items[i][2]
            total_sum += items[i][1]
            total_items.append(items[i][0])
        if total_weight == limit:
            break
    return total_sum, total_items


def dynamic_alg(items: list):
    items = items[:]
    items.sort(key=lambda x: -x[2])
    table = [[['', 0] for x in range(backpack_size)] for y in range(len(items))]
    for x in range(len(table[0])):
        if items[0][2] <= x + 1:
            table[0][x][0] = items[0][0]
            table[0][x][1] = items[0][1]
    for y in range(1, len(table)):
        for x in range(len(table[y])):
            prev = table[y - 1][x]
            if items[y][2] > x + 1:
                table[y][x] = prev
            else:
                this = ['', 0]
                this[0] += items[y][0]
                this[1] += items[y][1]
                if items[y][2] < x + 1:
                    this[0] += ' ' + table[y - 1][x - items[y][2]][0]
                    this[1] += table[y - 1][x - items[y][2]][1]
                table[y][x] = max(prev, this, key=lambda item: item[1])
    print(*table, sep='\n')


dynamic_alg(items)
# res_sum, res_items = greedy_alg(items, max_sum)
# print(res_sum)
# print(res_items)