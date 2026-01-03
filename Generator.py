def fibonacci_sequence():
    first,last = 0,1
    while True:
        yield first
        sum = first + last
        first,last = last,sum
    return sum

fib_gen = fibonacci_sequence()
for i in range(5):
    print(next(fib_gen))
