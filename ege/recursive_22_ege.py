def find_time(x):
    if data[x][2] == [0]:
        return data[x][1]
    else:
        return data[x][1] + max([find_time(i - 1) for i in data[x][2]])

file = open('24.txt')
data = []
counter = 0
for line in file:
    n, time, prevs = line.split('\t')
    prevs = list(map(int, prevs.split(';')))
    data.append([int(n), int(time), prevs, 0])
for i in range(len(data)):
    data[i][3] = find_time(i)

print(max(map(lambda x: x[3], data)))
