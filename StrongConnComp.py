g = [[1], [2], [0], [1, 4], [2]]
gt = [[2], [0, 3], [1, 4], [], [3]]

used = [False for i in range(len(g))]

orders = []
component = []

def first_dfs(v: str):
    used[v] = True
    for nv in g[v]:
        if used[nv] == False:
            first_dfs(nv)
    orders.append(v)

def second_dfs(v):
    component.append(v)
    used[v] = True
    for nv in gt[v]:
        if used[nv] == False:
            second_dfs(nv)
    
for v in range(len(g)):
    if used[v] == False:
        first_dfs(v)
used = [False for i in range(len(g))]
for i in range(len(g)):
    v = orders[len(g)-i-1]
    if used[v] == False:
        second_dfs(v)
        print(component)
        component.clear()