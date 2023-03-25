n = int(input())
t = []
p = []
dp = [0] * (n + 1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
# 뒤에서부터 해당 인덱스에서 얻을 수 있는 최대 이익을 구함
for i in range(n -1, -1, -1):
    time = t[i] + i # 해당 인덱스의 소요 시간 계산
    if time <= n: # 정해진 기간 내에 수행이 가능할 경우
        dp[i] = max(p[i] + dp[time], max_value) # 최대 이익 업데이트
        max_value = dp[i]
    else:
        dp[i] = max_value 
        # 정해진 기간 내에 수행이 불가능하면 이후 인덱스에서의 최대 이익을 해당 인덱스의 최대 이익으로 설정.
        # 해당 인덱스를 건너뛰고 최대 이익을 얻을 수 있는 인덱스로 이동할 수 있기 때문


print(max_value)
