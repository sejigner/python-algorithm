import sys

class Element:
    def __init__(self, key):
        self.key = key


class MaxHeap:
    class Empty(Exception):
        pass
    
    def __init__(self, max):
        self.arr = [None] * max
        self.max = max
        self.heap_size = 0

    def is_empty(self):
        return self.heap_size <= 0

    def is_full(self):
        return self.heap_size >= self.max

    def parent(self, idx):
        return idx >> 1

    def left(self, idx):
        return idx << 1

    def right(self, idx):
        return (idx << 1) + 1

    def push(self, n):
        if self.is_full():
            raise IndexError('heap is full')
        item = Element(n)
        self.heap_size += 1
        cur_idx = self.heap_size

        while cur_idx != 1 and item.key > self.arr[self.parent(cur_idx)].key:
            self.arr[cur_idx] = self.arr[self.parent(cur_idx)]
            cur_idx = self.parent(cur_idx)
        self.arr[cur_idx] = item


    def pop(self):
        if self.is_empty():
            raise MaxHeap.Empty
        
        result = self.arr[1]
        
        tmp = self.arr[self.heap_size]
        self.heap_size -= 1

        cur_idx = 1
        child = self.left(cur_idx)

        while child <= self.heap_size:
            if child < self.heap_size and self.arr[self.left(cur_idx)].key < self.arr[self.right(cur_idx)].key:
                child = self.right(cur_idx)

            if tmp.key >= self.arr[child].key:
                break
            
            self.arr[cur_idx] = self.arr[child]
            cur_idx = child
            child = self.left(cur_idx)


        self.arr[cur_idx] = tmp

        return result



n = int(sys.stdin.readline())
heap = MaxHeap(n)
for i in range(n):
        num = int(sys.stdin.readline())
        if num == 0 :
            if heap.is_empty():
                print(0)
            else:
                print(heap.pop().key)
        else:
            heap.push(num)
