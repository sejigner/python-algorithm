from heapq import heappush, heappop

class Element:
    def __init__(self, key, string):
        self.key = key
        self.data = string

class MinPriorityQueue:
    def __init__(self) -> None:
        self.heap = []

    def is_empty(self):
        if not self.heap:
            return True
        return False
    
    def push(self, item):
        heappush(self.heap, (item.key, item.data))

    def pop(self):
        return heappop(self.heap)
    
    def min(self):
        return self.heap[0]
    
if __name__ =="__main__":
    pq = MinPriorityQueue()

    pq.push(Element(2, "Germany"))
    pq.push(Element(3, "USA"))
    pq.push(Element(4, "Italy"))
    pq.push(Element(5, "Spain"))
    pq.push(Element(1, "Korea"))

    while not pq.is_empty():
        elem = pq.pop()
        print(f"key[{elem[0]}] : data[{elem[1]}]")