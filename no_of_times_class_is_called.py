class A:
    count = 0
    def __init__(self):
        A.count += 1
        print(f"The class A is called {A.count} times")

A1 = A()

A1