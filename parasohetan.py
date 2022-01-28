# Поиск совершенного набора паросочетаний двудольного графа
# Количество вершин в каждой доле

n, k = 3, 4
g = [[1, 2, 3], [0, 4], [0, 4], [0, 5], [1, 2, 6], [3, 6], [4, 5]]
# g = [[1, 3], [0, 2], [1], [0]]
used = [False for i in range(n+k)]
# Массив для хранения паросочетаний по индексу
mt = [-1 for i in range(n+k)]

def khun(v: int):
    if used[v] == True:
        return False
    used[v] = True

    for i in range(len(g[v])):
        nv = g[v][i]
        if mt[nv] == -1 or khun(mt[nv]) == True:
            mt[nv] = v
            return True

    return False

for v in range(n):
    used = [False for i in range(n+k)]
    khun(v)
for i in range(n+k):
    if mt[i] != -1:
        print(i, mt[i])