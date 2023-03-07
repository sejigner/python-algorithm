x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    # + 1: 1을 뺀 것에 대한 횟수 증가
    d[i] = d[i - 1] + 1
    # i를 나누는 수가 클 수록 횟수가 적으므로 나누는 수를 오름차순으로 판별
    # + 1: 나누기를 수행한 것에 대한 횟수 증가

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])