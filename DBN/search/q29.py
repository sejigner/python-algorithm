n, c = list(map(int,input().split(' ')))

array = []
for _ in range(n):
    array.append(int(input()))
array.sort() # 이진 탐색을 위해 정렬

start = 1 # 가능한 최소 거리
end = array[-1] - array[0] # 가능한 최대 거리
result = 0

while(start <= end):
    mid = (start + end) // 2 # 설치 간격 (gap) 설정
    value = array[0] # 첫 번째 집부터 설치
    count = 1

    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c: # C 개 이상 설치 가능하면 간격 늘이기
        start = mid + 1 # 가장 큰 gap과 이전에 설정한 mid 값의 중간을 gap으로 설정 -> gap이 커짐
        result = mid
    else: # C 개 이상 설치가 불가능하면 간격 줄이기
        end = mid - 1  # 가장 작은 gap과 이전에 설정한 mid 값의 중간을 gap으로 설정 -> gap이 작아짐
            
print(result)
