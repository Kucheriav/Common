file = open('9.txt')
data = list(map(lambda x: x.strip().split('\t'),file.readlines()))
print(data[:10])