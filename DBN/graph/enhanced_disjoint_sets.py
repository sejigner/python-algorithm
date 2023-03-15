'''
기존 방식
def find_parent(parent, x):
    # 부모 노드일 경우 값과 인덱스가 동일
    # 부모 노드가 아니라면 부모 노드 탐색
    if parent[x] != x:
        return find_parent(parent, parent[x])
    # 부모 노드의 인덱스 반환
    return x
'''

# 경로 압축 기법 활용
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


v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모 테이블 초기화
for i in range(1, v + 1):
    parent[i] = i

# 두 노드를 입력 받고 union 연산 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
