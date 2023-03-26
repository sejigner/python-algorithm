from typing import List, ListNode

# 숫자 -> 숫자 형태로 입력
array = input().split('->')
print('true') if array == array[::-1] else print('false')

# 리스트를 이용한 풀이
def isPalindrome(self, head: ListNode) -> bool:
    q: List = []

    if not head:
        return True
    
    node = head
    # 리스트로 변환
    while node is not None:
      q.append(node.val)
      node = node.next
    
    while len(q) > 1:
       if q.pop(0) != q.pop():
          return False
       
    return True