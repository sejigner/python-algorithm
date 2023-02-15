import sys

class FixedStack:
    
    class Full(Exception):
        pass
    
    class Empty(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def push(self, value) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def size(self) -> int:
        return self.ptr
    
    def empty(self) -> int:
        if self.is_empty():
            return 1
        else : return 0

    def top(self) -> int:
        if self.is_empty():
            return -1
        return self.stk[self.ptr - 1]
    

n = int(sys.stdin.readline())
stk = FixedStack(n)
for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        stk.push(order[1])
    else:
        if order[0] == 'top':
            print(stk.top())
        elif order[0] == 'size':
            print(stk.size())
        elif order[0] == 'empty':
            print(stk.empty())
        else:
            try:
                print(stk.pop())
            except FixedStack.Empty:
                print(-1)
       

