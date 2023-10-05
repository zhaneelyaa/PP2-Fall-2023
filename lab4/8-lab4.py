total = set(range(1, (int(input()) + 1)))
while True:
    beatriss = input()
    if beatriss == 'HELP':
        break
    numbers = set(map(int, beatriss.split()))
    if len(total - numbers) < len(total & numbers):
        print('YES')
        total &= numbers
    else:
        print('NO')
        total -= numbers
print(*sorted(map(int, total)))


