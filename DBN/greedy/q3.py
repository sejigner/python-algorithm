s = input()

zero = 0
one = 0
result = 0

for i in range(0, len(s) - 1):
    if s[i] != s[i + 1]:
        if int(s[i]) == 0:
            zero += 1
        else:
            one += 1
if s[-1] != s[-2]:
    if s[-1] == '0':
        zero += 1
    else:
        one += 1

print(min(zero, one))