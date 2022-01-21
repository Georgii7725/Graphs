# Задача:
# Найти наименьший путь между двумя данными вершинами в данном неориентированном взевешенном графе

# Список смежности
g = [{1: 1, 2: 9},
    {0: 1, 2: 2, 3: 4},
    {0: 9, 1: 2, 4: 3},
    {1: 4, 4: 6},
    {2: 3, 3: 6}
    ]
# Поюзанные вершины
used = [False for i in range(len(g))]
# Поиск минимального пути от start до end
start, end = 1, 4
# Дефолтное расстояние между вершинами, чтобы класть самый эффективный путь
dist = [100 for i in range(len(g))]
dist[start] = 0
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
            if nv == d and dist[nv] > dist[s] + g[s][nv]:
                parents[nv] = s
                dist[nv] = dist[s] + g[s][nv]
            # Следующая вершина - непоследняя
            elif used[nv] == False and dist[nv] > dist[s] + g[s][nv]: 
                parents[nv] = s
                dist[nv] = dist[s] + g[s][nv]
                queue.append(nv)


bfs(start, end)
way = [end]
daught = end
# Разворачиваем путь между данными вершинами
while(parents[daught] != -1):
    way.append(parents[daught])
    daught = parents[daught]
way.reverse()
print(dist[end], '\n', way)
