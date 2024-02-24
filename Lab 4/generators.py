def generate_squares(n):
    for i in range(1, n+1):
        yield i**2

n = 5
for square in generate_squares(n):
    print(square)


def generate_even_numbers(n):
    for i in range(0, n+1, 2):
        yield i

n = int(input())

even_numbers = generate_even_numbers(n)
print(', '.join(map(str, even_numbers)))


def generate_numbers_divisible_by_3_and_4(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in generate_numbers_divisible_by_3_and_4(n):
    print(num)


def squares(a, b):
    for i in range(a, b+1):
        yield i**2

for square in squares(1, 5):
    print(square)


def count_down(n):
    while n >= 0:
        yield n
        n -= 1
n = 5
for num in count_down(n):
    print(num)