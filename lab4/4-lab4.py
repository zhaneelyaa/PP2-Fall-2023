numbers = input().split()
seen_numbers = {}

for num in numbers:
    if num in seen_numbers:
        print("YES")
    else:
        print("NO")
        seen_numbers[num] = True
