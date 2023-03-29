# 17:50 - 18:00
value = input()
result = int(value[0])
for i in range(1, len(value)):
    if result != 0 and int(value[i]) != 0 and int(value[i]) != 1:
        result *=  int(value[i])
    else:
        result += int(value[i])

print(result)
        