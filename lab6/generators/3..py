def divisible_by_3_and_4_generator(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

n = int(input("Enter a number (n): "))
divisible_gen = divisible_by_3_and_4_generator(n)

print("Numbers between 0 and", n, "divisible by both 3 and 4:")
for number in divisible_gen:
    print(number)

