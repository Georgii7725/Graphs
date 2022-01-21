# Задача:
# Найти наибольший путь между двумя данными вершинами в данном неориентированном графе

# Список смежности
g = []

# N, M - количество вершин и рёбер в графе соответственно
with open('input.txt') as file:
    N, M = map(int, file.readline().split())
    g = [[] for i in range(N)] # [0, 1, 2, 3, 4, 5, 6]
    for i in range(M):
        v1, v2 = map(int, file.readline().split())
        g[v1-1].append(v2-1)
        g[v2-1].append(v1-1)
        g[v1-1].sort()
        g[v2-1].sort()
    # Ищему путь между вершинами start и end
    start, end = map(int, file.readline(-1).split())
    start, end = start - 1, end - 1

# Поюзанные вершины
used = [False for i in range(len(g))]
# Дефолтное расстояние между вершинами, чтобы класть самый эффективный путь
dist = [0 for i in range(len(g))]
# Чтобы развернуть путь от одной вершины до другой
parents = {start: -1}
# Поиск в ширину
def bfs(v: int, d: int):
    queue = []
    queue.append(v)
    while(len(queue) != 0):
        s = queue[0]
        queue.pop(0)
        used[s] = True
        for nv in g[s]:
            # Следующая вершина - последняя
            if nv == d and dist[nv] < dist[s] + 1:
                parents[nv] = s
                dist[nv] = dist[s] + 1
            # Следующая вершина - непоследняя
            elif used[nv] == False and dist[nv] < dist[s] + 1: 
                parents[nv] = s
                dist[nv] = dist[s] + 1
                queue.append(nv)


bfs(start, end)
way = [end]
daught = end
# Разворачиваем путь между данными вершинами
while(parents[daught] != -1):
    way.append(parents[daught])
    daught = parents[daught]
way.reverse()
way = [str(i+1) for i in way]
s = str(dist[end]) + '\n'
for i in way:
        s += i + " "
open('output.txt', 'w').write(s)