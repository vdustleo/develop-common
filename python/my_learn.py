class MyTest:
    def __init__(self):
        dir()

    def print(self):
        print("hello, world", str(self))

    @staticmethod
    def help():
        print("help methods")

    def __lt__(self, y):
        return super().__lt__(y)


MyTest().print()
MyTest.help()


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + n


print(fib(100))
