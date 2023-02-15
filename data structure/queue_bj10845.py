import sys

class FixedQueue:
    
    class Empty(Exception):
        pass
    
    class Full(Exception):
        pass
    
    def __init__(self, capacity: int) -> None:
        self.no = 0
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.que = [None] * capacity

    def is_full(self) -> bool:
        return self.no >= self.capacity
    
    def is_empty(self) -> bool:
        return self.no <= 0

    def push(self, value) -> None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = value
        self.no += 1
        self.rear += 1
        if self.rear == self.capacity:
            self.rear = 0
        
    def pop(self):
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.no -= 1
        self.front += 1
        if(self.front == self.capacity):
            self.front = 0
        
        return x

    def size(self) -> int:
        return self.no
    
    def empty(self) -> int:
        if self.is_empty():
            return 1
        else: return 0
    
    def get_front(self) -> int:
        if self.is_empty():
            return -1
        else: return self.que[self.front]
    
    def get_rear(self) -> int:
        if self.is_empty():
            return -1
        else: return self.que[self.rear - 1]


n = int(sys.stdin.readline())
que = FixedQueue(n)
for i in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push' :
        que.push(command[1])
    else:
        if command[0] == 'front' :
            print(que.get_front())
        elif command[0] == 'back' :
            print(que.get_rear())
        elif command[0] == 'size':
            print(que.size())
        elif command[0] == 'empty':
            print(que.empty())
        else:
            try:
                print(que.pop())
            except FixedQueue.Empty:
                print(-1)
        
