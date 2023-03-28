v = int(input())
planets = []
edges = []
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(v):
    x, y, z = map(int, input().split())
    planets.append((x, y, z))

for i in range(v - 1):
    for j in range(i + 1, v):
        cost = min(abs(planets[i][0]-planets[j][0]),
                   abs(planets[i][1]-planets[j][1]),
                   abs(planets[i][2]-planets[j][2]))
        edges.append((cost, i, j))

edges.sort()
result = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


