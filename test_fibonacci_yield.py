def fibonacci(a, b):
    # a = b = 1

    while True:
        a, b = b, a + b
        yield b


for num in fibonacci(a=1, b=1):
    if num > 200:
        break
    print(num)
