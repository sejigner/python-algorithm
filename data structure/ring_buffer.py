n = int(input('정수를 몇 개 저장할까요?: '))
a = [None] * n

cnt = 0
while True:
    # n 이상의 수는 n 주기로 a 배열의 0부터 채움
    a[cnt % n] = int(input((f'{cnt+1}번째 정수를 입력하세요.: ')))
    cnt += 1

    retry = input(f'계속 할까요?(Y ... Yes / N ... No): ')
    if retry in {'N', 'n'}:
        break

# 배열의 크기 만큼 마지막 값부터 취함    
i = cnt - n
if i < 0: i = 0 # 배열의 크기보다 입력 값이 적을 경우 인덱스를 0으로 한다.

while i < cnt:
    print(f'{i + 1}번째 = {a[i % n]}')
    i += 1