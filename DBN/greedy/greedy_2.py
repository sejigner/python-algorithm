def greedy():
    n, m = map(int, input().split())
    # 첫 풀이
    # nums_row = []
    # for i in range(n):
    #   nums = map(int, input().split())
    #   nums_row.append(min(nums))
    # print(max(nums_row))

    # 다른 풀이
    result = 0
    for i in range(n):
        nums = map(int, input().split())
        min_value = min(nums)
        result = max(result, min_value)
    
    print(result)


greedy()
