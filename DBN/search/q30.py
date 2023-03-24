from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index


array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word)

    for q in queries:
        if q[0] == '?':
            q = q[::-1]
            answer.append(count_by_range(reversed_array,
                          q.replace('?', 'a'), q.replace('?', 'z')))
        else:
            answer.append(count_by_range(
                array, q.replace('?', 'a'), q.replace('?', 'z')))

    return answer
