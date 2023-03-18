n = input()
half = len(n)//2
front, rear = n[:half], n[half: len(n)]

if int(front) == int(rear):
    print('LUCKY')
else:
    print('READY')