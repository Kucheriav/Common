def crossings():
    #https://acmp.ru/index.asp?main=task&id_task=124
    #количество соединений узла
    n, m = map(int, input().split())
    matrix = [[0 for i in range(n)] for j in range(n)]
    for k in range(m):
        i, j = map(lambda x: int(x) - 1, input().split())
        matrix[i][j] = matrix[j][i] = 1
    for line in matrix:
        print(*line, '\t\t', sum(line))


