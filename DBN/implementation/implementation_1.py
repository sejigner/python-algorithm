coordinate = input()
row = int(coordinate[1])
column = int(ord(coordinate[0])) - int(ord('a')) + 1
count = 0

steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

for step in steps:
    x= row + step[0]
    y= column + step[1]

    if 0 < x < 9 and 0 < y < 9 :
        count += 1

print(count)