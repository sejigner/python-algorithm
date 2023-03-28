n, m = map(int, input().split())
parent = [0] * (n + 1)
total = 0

for i in range(1, n + 1):
    parent[i] = i

edges = []
for _ in range(m):
    x, y, cost = map(int, input().split())
    edges.append((cost, x, y))
    total += cost

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

edges.sort()
result = 0

for edge in edges:
    cost, x, y = edge
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(total - result)