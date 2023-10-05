N, M = (int(i) for i in input().split())
Anya = [int(input()) for i in range(N)]
Borya = [int(input()) for i in range(M)]
A, B = set(Anya), set(Borya)
print(len(A & B))
print(' '.join([str(i) for i in A & B]))
print(len(A - B))
print(*sorted(A - B, key=int))
print(len(B - A))
print(' '.join([str(i) for i in B - A]))
