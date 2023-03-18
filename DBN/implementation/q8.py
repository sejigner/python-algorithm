data = input()
letter = []
num = 0

for x in data:
    if x >= 'A' and x <= 'Z':
        letter.append(x)
    else:
        num += int(x)

letter.sort()
letter.append(str(num))
letter = ''.join(letter)
rotated = [[0, 0, 0]]*3

print(letter)
print(rotated)
