def find_time(line):
    if line[2] == [0]:
        return line[1]
    else:
        prev_lines = list(filter(lambda x: x[0] in line[2], data))
        return line[1] + max(find_time(x) for x in prev_lines)


file = open('input.txt')
data = []
for line in file:
    n, time, prevs = line.strip().split('\t')
    if prevs[-1] != '?':
        prevs = list(map(int, prevs.split(';')))
    else:
        prevs = [-1]
    data.append([int(n), int(time), prevs, 0])
dependent_lines = []
for line in data:
    if 18 in line[2]:
        dependent_lines.append(line[0])
for i in range(0, 20):
    if