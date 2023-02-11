# поля:фио, класс, код
file = open('names.csv')
names = list(map(lambda x: x.strip().split(';'), file.readlines()))
# веснушки. косяки с именами
# file = open('vesn_names.csv')
# names = list(map(lambda x: x.strip().split(';'), file.readlines()))
file.close()
# поля: код, результат
file = open('results.csv')
results = dict(list(map(lambda x: (x.strip().split(';')[0], int(x.strip().split(';')[1])), file.readlines())))
file.close()
matching_list = []
for name in names:
    matching_list.append([name[0],name[1],name[2], results.get(name[2], 0)])
# вложенная сортировка: по классу (первые два) и по результату
matching_list.sort(key=lambda x: (x[1][:-1], -x[3]))

print(*matching_list, sep='\n')

# porog = {'7' :200, '8': 240, '9': 180, '10':180, '11':180}
# for pupil in matching_list:
#     if pupil[3] < porog[pupil[1][:-1]]:
#         print(pupil)
file = open('output.csv', 'w')
for line in matching_list:
    file.write(';'.join([str(x) for x in line]) + '\n')
file.close()

