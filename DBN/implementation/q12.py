def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 설치된 것이 '기둥'인 경우
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif stuff == 1:  # 설치된 것이 '보'인 경우
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):    
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)
# [x, y, a, b] - (x, y) : 좌표 / a = 구조물의 종류 (0 기둥 1 보) / b = 구조물 설치 0 / 삭제 1
# 보는 오른쪽으로 설치
# return 하는 배열의 원소 형식: [x, y, a]