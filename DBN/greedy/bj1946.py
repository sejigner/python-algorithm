import sys
input = sys.stdin.readline

for _ in range(int(input())):
    array = []
    for _ in range(int(input())):
        a, b = map(int, input().split())
        array.append((a, b))
    
    array.sort()
    prev = array[0][1]
    result = 1

    for i in range(1, len(array)):
        if array[i][1] < prev:
            prev = array[i][1]
            result += 1
    
    print(result)
