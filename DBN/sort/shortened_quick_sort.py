arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]

    # 리스트 컴프리헨션을 이용해 피봇 좌우 분할
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    # 분할 후 각각 정렬 수행 및 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))