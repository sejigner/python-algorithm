index = 0
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    result = 0
    index += 1
    result += (v // p) * l
    if v % p >= l:
        result += l
    else:
        result += v % p
    print("Case %d: %d" % (index, result))
