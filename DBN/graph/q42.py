def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

g = int(input())
p = int(input())
gates = [0] * (g + 1)
destinations = []
for i in range(1, g + 1):
    gates[i] = i 

result = 0

for _ in range(p):
    destinations.append(int(input()))
for destination in destinations:
    if gates[destination] == destination:
        union_parent(gates, destination, destination - 1)
        result += 1
    else:
        parent = find_parent(gates, destination)
        if parent != 0:
            union_parent(gates, parent, parent - 1)
            result += 1
        else:
            print(result)
            break
            
        
