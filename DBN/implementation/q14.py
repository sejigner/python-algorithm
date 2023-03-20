from itertools import permutations
# n: 외벽의 길이, weak: 취약 지점의 위치, dist: 친구가 이동할 수 있는 거리
def solution(n, weak, dist):
    length = len(weak)
    # 원형의 리스트를 2배 길이의 배열로 변환
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
        if answer > len(dist):
            return -1
    return answer