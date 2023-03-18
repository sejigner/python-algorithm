def solution(s):
    answer = len(s)
    for unit in range(1, len(s)//2 + 1):
        compressed = ''
        previous = s[0:unit]
        count = 1
        for c in range(unit, len(s), unit):
            if s[c:c+unit] == previous:
                count += 1
            else:
                compressed += str(count)+previous if count > 1 else previous
                previous = s[c:c+unit]
                count = 1
        compressed += str(count)+previous if count > 1 else previous
        answer = min(answer, len(compressed))
    return answer
