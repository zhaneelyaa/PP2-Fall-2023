def even_numbers_generator(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num

n = int(input("Enter a number (n): "))
even_gen = even_numbers_generator(n)

even_numbers = list(even_gen)  
even_numbers_str = ', '.join(map(str, even_numbers))
print("Even numbers between 0 and", n, "in comma-separated form:", even_numbers_str)
