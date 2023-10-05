n = int(input())
ans = set(range(1, n + 1))
q = 0
while True:
    q = input()
    if q == "HELP":
        break
    else:
        a = set(list(map(int, q.split())))
        q = input()
        if q == "YES":
            ans = ans & a
        else:
            ans = ans - a
ans = sorted(ans)
print(*ans)

