n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        # 현재 보고 있는 금액에서 현재 금액 단위 만큼 뺐을 때 가능했는지 확인
        if d[j - array[i]] != 10001:
            # 이전 화폐 단위로 만들었을 때와 현재 화폐 단위로 해당 금액을 만들었을 때 중 더 작은 값을 취함
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])