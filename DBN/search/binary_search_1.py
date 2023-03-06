# 이진 탐색 예제 1

def search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif target > array[mid]:
        return search(array, target, mid + 1, end)
    else:
        return search(array, target, start, mid - 1)
    


n = int(input())
stock = list(map(int, input().split()))
stock.sort()

m = int(input())
order = list(map(int, input().split()))


for i in order:
    result = search(stock, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
