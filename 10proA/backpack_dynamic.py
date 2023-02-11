# предполагается, что вы знакомы с постановкой задачи о рюкзаке из "Грокаем Алгоритмы"


def dynamic_alg(items: list):
    # при работе с аргрументом функции типа список
    # делать полную копию чаще всего жесткая необходимость
    # из-за некоторых особенностей памяти, список передается как ссылка , а не копия
    # изменяя список внутри функции, мы меняем его и во вне.
    # здесь это просто правило хорошего кода.
    items = items[:]
    # формируем таблицу: вложенный список, где элеметом является список
    # из пустой строки и нуля - заготовка для подсчетов названий предметов и суммы их стоимости
    table = [[['', 0] for x in range(backpack_size)] for y in range(len(items))]
    # то же самое можно было записать циклом
    # table = list()
    # for y in range(len(items)):
    #     table.append(list())
    #     for x in range(backpack_size):
    #         table[y].append(['', 0])
    # нулевую строку заполняем отдельно, без оглядки на предыдущие
    for x in range(len(table[0])):
        if items[0][2] <= x + 1:
            table[0][x][0] = items[0][0]
            table[0][x][1] = items[0][1]
    # стартуем не с нулевой строки!
    for y in range(1, len(table)):
        for x in range(len(table[y])):
            # находим предыдущий
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


items = [['guitar', 1500, 1], ['tape', 3000, 4], ['notebook', 2000, 3]]
backpack_size = 4
dynamic_alg(items)
